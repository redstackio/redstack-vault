---
id: dfb171e0-7b13-4ddb-a60d-875532f9f6a9
name: Set-LAPS-Password-Expiration-Time-for-Persistence
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:28.483883+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - '[[techniques/Account-Manipulation|T1098 - Account Manipulation]]'
sub_techniques:
  - '[[sub-techniques/Additional-Cloud-Roles|T1098.002 - Additional Cloud Roles]]'
tags:
  - '[[tags/Domain]]'
  - '[[tags/LAPS Persistence]]'
  - '[[tags/Windows - Persistence]]'
commands:
  - '[[commands/set-domain-object-laps-expiration]]'
platforms:
  - Windows
tools: []
validated: true
---

# Set-LAPS-Password-Expiration-Time-for-Persistence

## Summary

This procedure modifies the LAPS (Local Administrator Password Solution) password expiration time attribute on a domain-joined Windows computer to a distant future date, preventing the automatic randomization of the local administrator password. This allows an attacker with sufficient domain privileges to maintain persistent access to the target machine without the password changing periodically.

## Description

LAPS is a Microsoft solution that manages local administrator passwords on domain-joined systems by randomizing them at configurable intervals, typically 30 days, and storing the passwords securely in Active Directory. The expiration time is controlled by the ms-Mcs-AdmPwdExpirationTime attribute in the computer's AD object. By setting this attribute to a large future value (e.g., a 64-bit integer representing a date far in the future), the password rotation is delayed indefinitely, enabling persistence. This technique is effective post-compromise for red team operations or in scenarios where initial access credentials might be rotated. It requires domain-level permissions to modify AD attributes and assumes the attacker has executed on a domain-joined host with tools like PowerView loaded.

## Requirements

1. Domain credentials with permissions to modify computer object attributes in Active Directory (e.g., Domain Admin or delegated rights on the target computer object).
2. Access to a domain-joined Windows machine where the procedure will be executed.
3. PowerShell environment with Active Directory module or PowerView toolkit loaded for LDAP queries and modifications.
4. Network connectivity to a Domain Controller for AD interactions.

## Defense

- Monitor Active Directory for modifications to the ms-Mcs-AdmPwdExpirationTime attribute using tools like Event ID 5136 in Windows Security logs or Azure AD auditing.
- Implement least-privilege access to AD objects, restricting who can edit computer attributes.
- Regularly audit LAPS configurations and expiration times via scripts or monitoring tools like Microsoft Defender for Identity.
- Enforce short LAPS rotation intervals and alert on any extensions to expiration times.

## Objectives

1. Delay LAPS password randomization to preserve current local administrator credentials for ongoing access.
2. Establish persistence on the target system against password rotation mechanisms.
3. Maintain stealthy access in a domain environment without triggering immediate detection.

## Instructions

### Step 1: Verify Target Computer Object and Current Expiration Time

**Context**: Before modification, query the current ms-Mcs-AdmPwdExpirationTime attribute to confirm the LAPS setup and baseline the value. This helps verify permissions and understand the current state.

**Command** ([[commands/get-domain-object-laps-expiration]]):
```powershell
Get-DomainObject -Identity <target_machine> -Properties ms-Mcs-AdmPwdExpirationTime
```

> This command retrieves the AD object properties for the specified computer. Replace <target_machine> with the NetBIOS or distinguished name of the target (e.g., 'WORKSTATION01' or 'CN=WORKSTATION01,OU=Computers,DC=domain,DC=com'). Expected output includes the current expiration time as a large integer; if unset or low, proceed to modification.

### Step 2: Set the Expiration Time to a Future Date

**Context**: Use the Set-DomainObject cmdlet to update the ms-Mcs-AdmPwdExpirationTime attribute to a value representing a date far in the future, such as year 9999. The value is a FILETIME format (100-nanosecond intervals since January 1, 1601 UTC). This prevents LAPS from rotating the password until that date.

**Command** ([[commands/set-domain-object-laps-expiration]]):
```powershell
Set-DomainObject -Identity <target_machine> -Set @{"ms-Mcs-AdmPwdExpirationTime"="232609935231523081"}
```

> Execute this on a machine with domain credentials. The example value sets expiration to approximately year 9999. Confirm success by re-querying the attribute (Step 1). If errors occur (e.g., access denied), escalate privileges or check delegation.

### Step 3: Verify the Change and Test Persistence

**Context**: Re-query the attribute to confirm the update and optionally test by attempting to retrieve the LAPS password, ensuring it remains unchanged.

**Command** ([[commands/get-domain-computer-laps-password]]):
```powershell
Get-DomainComputer -Identity <target_machine> -Properties ms-Mcs-AdmPwd
```

> This retrieves the current LAPS password. Expected output shows the unchanged password hash or value. Monitor for any immediate rotation attempts via Task Scheduler on the target (LAPS tasks under Microsoft\Windows\LAPS).
