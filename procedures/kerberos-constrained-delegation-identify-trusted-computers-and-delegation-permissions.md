---
id: 15ba2a49-99ff-4e31-a8a4-fe6091b8553a
name: >-
  kerberos-constrained-delegation-identify-trusted-computers-and-delegation-permissions
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:07.668987+00:00'
updated_at: '2023-04-10T20:26:18.830970+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account-Discovery|T1087 - Account Discovery]]'
  - >-
    [[techniques/Permission-Groups-Discovery|T1069 - Permission Groups
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Kerberos Constrained Delegation]]'
  - active-directory
  - kerberos
  - delegation
commands:
  - '[[commands/powerview-get-trusted-computers-for-delegation]]'
  - '[[commands/powerview-get-allowed-delegate-permissions-for-computers]]'
platforms:
  - Windows
tools:
  - '[[tools/PowerView]]'
validated: true
---

# kerberos-constrained-delegation-identify-trusted-computers-and-delegation-permissions

## Summary

This procedure uses the PowerView PowerShell module to enumerate computers in an Active Directory environment that are configured for Kerberos constrained delegation, identifying those trusted for authentication and their associated delegation permissions via the msDS-AllowedToDelegateTo attribute. This information reveals potential attack paths for impersonation, lateral movement, or privilege escalation by spotting services that can be delegated to sensitive resources.

## Description

Kerberos Constrained Delegation (KCD) allows a front-end service to impersonate a user to specific back-end services, controlled by the msDS-AllowedToDelegateTo attribute on computer or user accounts. While useful for legitimate multi-tier applications, attackers with domain access can abuse KCD by obtaining a service ticket for a trusted computer and using it to access delegated targets, such as domain controllers or file shares. This procedure focuses on discovery: first identifying computers where the current user is trusted for delegation (via -TrustedToAuth), then querying their allowed delegation targets. It assumes execution from a compromised domain-joined host with PowerView loaded. Outcomes include a list of exploitable delegation configurations, which can feed into attacks like resource-based constrained delegation abuse or printer bug exploits. The target environment is Windows Active Directory domains with Kerberos enabled.

## Requirements

1. Valid domain user credentials with read access to Active Directory objects (e.g., domain user or higher).
2. PowerShell execution policy set to allow script execution (e.g., Unrestricted or Bypass).
3. PowerView PowerShell module imported and active in the session.
4. Network connectivity to a domain controller for LDAP queries.

## Defense

- Monitor Active Directory LDAP queries for enumeration of msDS-AllowedToDelegateTo attributes using tools like Microsoft ATA or SIEM rules for anomalous AD access.
- Apply least privilege by auditing and removing unnecessary constrained delegation configurations; prefer resource-based constrained delegation with strict controls.
- Enable Protected Users group for sensitive accounts to prevent delegation abuse and implement Microsoft Defender for Identity for behavioral detection of delegation queries.

## Objectives

1. Enumerate computers trusted for Kerberos delegation involving the current user.
2. Identify specific services and resources that can be impersonated via constrained delegation.
3. Highlight potential abuse vectors for lateral movement or privilege escalation in the domain.

## Instructions

### Step 1: Identify Trusted Computers for Delegation

**Context**: This step queries Active Directory for computers where the current authenticated user is trusted to authenticate against, using the -TrustedToAuth filter in PowerView. This reveals hosts configured for delegation that could impersonate the user to other services, a key step in mapping KCD opportunities.

**Command** ([[commands/powerview-get-trusted-computers-for-delegation]]):

```powershell
Get-DomainComputer -TrustedToAuth | Select-Object -ExpandProperty dnshostname
```

> This command performs an LDAP query filtered for computers with the current user in their trustedToAuthForDelegation list. It extracts and displays the DNS hostnames of matching computers. Pipe the output to a file (e.g., | Out-File trusted_computers.txt) for use in the next step. If no output, the current user has no delegation trusts, indicating limited abuse potential.

### Step 2: Retrieve Delegation Permissions for Identified Computers

**Context**: Using the list of trusted computers from Step 1, query each for the msDS-AllowedToDelegateTo attribute, which specifies the services (SPNs) they can delegate to. This uncovers what resources an attacker could impersonate access to, such as CIFS on domain controllers for lateral movement.

**Command** ([[commands/powerview-get-allowed-delegate-permissions-for-computers]]):

```powershell
Get-Content trusted_computers.txt | ForEach-Object { Get-DomainComputer -Identity $_ | Select-Object -ExpandProperty 'msds-allowedtodelegateto' }
```

> Replace trusted_computers.txt with the file from Step 1, or pipe directly if in the same session (e.g., $computers = ...; $computers | ForEach { Get-DomainComputer -Identity $_... }). This iterates over each hostname, querying the delegation attribute and outputting arrays of allowed service principal names (SPNs). Look for high-value targets like HOST/DcName or CIFS/FileServer. Success is indicated by populated SPN lists; empty lists mean no constrained delegation is set.
