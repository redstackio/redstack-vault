---
id: 6ea13953-8267-43cb-9df8-e8b60371b5be
name: Read-LAPS-Password-from-Domain-Using-Credentials
type: procedure
verified: true
submitted: false
created_at: '2023-01-12T19:27:21.428532+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Unsecured Credentials]]'
sub_techniques:
  - '[[Credentials in Files]]'
tags:
  - administrator
  - Permissions
  - Privilege Escalation
  - LAPS
  - Active Directory
commands:
  - '[[commands/get-domainobject-retrieve-laps-password]]'
platforms:
  - Windows
tools:
  - '[[tools/PowerView]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Read-LAPS-Password-from-Domain-Using-Credentials

## Summary

This procedure retrieves the plaintext Local Administrator Password Solution (LAPS) password for a domain-joined computer using domain credentials that have read access to the ms-Mcs-AdmPwd attribute in Active Directory. LAPS is a Microsoft feature that securely stores unique local admin passwords for workstations and servers, allowing authorized users to access them for administrative tasks or privilege escalation.

## Description

LAPS automates the management of local administrator account passwords by generating unique, randomized passwords for each computer and storing them in the ms-Mcs-AdmPwd attribute of the computer's Active Directory object. This procedure uses PowerView, a PowerShell toolkit for Active Directory enumeration, to query the domain for a specific computer's LAPS password. It requires domain credentials with at least read permissions on the ms-Mcs-AdmPwd extended right (ObjectAceType). This technique is useful in red team engagements for gaining local admin access on target machines after initial domain compromise, enabling lateral movement or persistence. Note that LAPS passwords rotate regularly (default 30 days), so retrieved passwords may have limited validity.

## Requirements

1. Domain user credentials with read access to the ms-Mcs-AdmPwd attribute on target computer objects (e.g., via delegated permissions or group membership like "LAPS Readers").
2. PowerShell execution policy allowing script execution (Bypass or Unrestricted).
3. Network access to a domain controller for LDAP queries.
4. PowerView module loaded in the current PowerShell session.
5. Target computer name or distinguished name in Active Directory.

## Defense

Defensive measures and detection strategies:

- Restrict read access to ms-Mcs-AdmPwd using granular ACLs; audit access via Event ID 4662 (Object Access Auditing) on domain controllers.
- Enable LAPS auditing and monitor for unauthorized queries to computer objects.
- Use advanced auditing policies for directory service changes and implement just-in-time privilege elevation to limit standing access.
- Deploy endpoint detection tools to monitor PowerShell execution of reconnaissance scripts like PowerView.

## Objectives

1. Query Active Directory for the LAPS password attribute of a target computer.
2. Extract the plaintext password for local admin access.
3. Verify the password's validity by testing it on the target machine.

## Instructions

### Step 1: Load PowerView and Authenticate

**Context**: Import the PowerView module and establish domain authentication using provided credentials to enable AD queries. This step ensures the session has the necessary context for domain operations.

If not already loaded, import PowerView:

```powershell
Import-Module PowerView.ps1
```

Then add credentials for authentication:

```powershell
$SecPassword = ConvertTo-SecureString 'password' -AsPlainText -Force
$Cred = New-Object System.Management.Automation.PSCredential('domain\user', $SecPassword)
Add-DomainCredential -Credential $Cred
```

Expected output: No errors; credentials added successfully.

### Step 2: Retrieve the LAPS Password

**Context**: Use the Get-DomainObject cmdlet to fetch the target computer's AD object and expand the ms-Mcs-AdmPwd property, which contains the plaintext LAPS password. Replace $TargetComputer with the actual computer name (e.g., 'WORKSTATION01'). This step directly accesses the stored credential.

**Command** ([[commands/get-domainobject-retrieve-laps-password]]):

```powershell
Get-DomainObject -Identity $TargetComputer | Select-Object -ExpandProperty ms-Mcs-AdmPwd
```

Expected output: The plaintext password, e.g., "P@ssw0rd123!". If access is denied, an error like "Access is denied" will appear; verify permissions and retry.

### Step 3: Verify the Password

**Context**: Test the retrieved password by attempting to connect to the target machine using tools like PsExec or WMI. This confirms the password's usability for local admin access.

Use PsExec to execute a command remotely:

```powershell
psexec \\$TargetComputer -u $TargetComputer\Administrator -p 'retrieved_password' cmd /c whoami
```

Expected output: Successful connection showing the administrator context, e.g., "nt authority\system" if elevated.
