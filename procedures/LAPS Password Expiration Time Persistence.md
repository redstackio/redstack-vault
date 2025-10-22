---
id: dfb171e0-7b13-4ddb-a60d-875532f9f6a9
name: LAPS Password Expiration Time Persistence
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:28.483883+00:00'
updated_at: '2023-04-10T20:37:26.107447+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Event Triggered Execution|T1546 - Event Triggered Execution]]'
sub_techniques:
- '[[Image File Execution Options Injection|T1546.012 - Image File Execution Options
  Injection]]'
tags:
- '[[Domain]]'
- '[[LAPS Persistence]]'
- '[[Windows - Persistence]]'
commands:
- '[[Set Domain Object ms-mcs-admpwdexpirationtime]]'
---

# LAPS Password Expiration Time Persistence

## Summary

LAPS (Local Administrator Password Solution) is a Microsoft tool that periodically randomizes the local administrator password on domain-joined computers. By default, the LAPS password expiration time is set to 30 days. An attacker who gains access to a domain-joined computer can change the LAPS pa

## Description

# Description

LAPS (Local Administrator Password Solution) is a Microsoft tool that periodically randomizes the local administrator password on domain-joined computers. By default, the LAPS password expiration time is set to 30 days. An attacker who gains access to a domain-joined computer can change the LAPS password expiration time to maintain persistence on the system. This technique is useful for maintaining access to a network even if the attacker's original method of access is discovered and remediated. To accomplish this technique, the attacker can use the 'Set LAPS Password Expiration Time' command.

## Requirements

1. Access to a domain-joined computer

## Defense

1. Ensure that LAPS password expiration time is set to a reasonable value

1. Monitor for changes to LAPS password expiration time

1. Limit access to domain-joined computers to authorized personnel only

## Objectives

1. Maintain persistence on a compromised domain-joined computer

1. Maintain access to a network even if the attacker's original method of access is discovered and remediated

# Instructions

1. Use the Set-DomainObject command to set the ms-mcs-admpwdexpirationtime attribute to a future date on the target machine.

**Code**: [[Set-DomainObject -Identity <target_machine> -Set @]]

> This command sets the expiration time for the LAPS password of the target machine to a future date. This will prevent the machine from updating its password until the expiration time is reached. The -Identity parameter specifies the target machine and the -Set parameter sets the value of the ms-mcs-admpwdexpirationtime attribute to the specified date. The date should be in the format of a 64-bit integer representing the number of 100-nanosecond intervals since January 1, 1601 (UTC).

**Command** ([[Set Domain Object ms-mcs-admpwdexpirationtime]]):

```bash
Set-DomainObject -Identity <target_machine> -Set @{\"ms-mcs-admpwdexpirationtime\"=\"232609935231523081\"}
```

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Event Triggered Execution|T1546 - Event Triggered Execution]]

### Sub-Techniques

- [[Image File Execution Options Injection|T1546.012 - Image File Execution Options Injection]]

## Commands Used

- [[Set Domain Object ms-mcs-admpwdexpirationtime]]

## Tags

- [[Domain]]
- [[LAPS Persistence]]
- [[Windows - Persistence]]
