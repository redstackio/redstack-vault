---
id: 232df366-d649-4335-8783-bff6d52967ae
name: Linux Privilege Escalation via Capabilities Edit
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:18.892896+00:00'
updated_at: '2023-04-10T20:34:33.039950+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Event Triggered Execution|T1546 - Event Triggered Execution]]'
sub_techniques:
- '[[Image File Execution Options Injection|T1546.012 - Image File Execution Options
  Injection]]'
tags:
- '[[Capabilities]]'
- '[[Edit capabilities]]'
- '[[Linux - Privilege Escalation]]'
commands:
- '[[Add cap_net_raw+p to ping binary]]'
- '[[Remove cap_net_raw from ping binary]]'
---

# Linux Privilege Escalation via Capabilities Edit

## Summary

Linux systems use capabilities to grant specific privileges to processes without requiring full root access. This procedure involves editing capabilities to escalate privileges. An attacker who has gained access to a low-privileged account can use this procedure to gain additional privileges and po

## Description

# Description

Linux systems use capabilities to grant specific privileges to processes without requiring full root access. This procedure involves editing capabilities to escalate privileges. An attacker who has gained access to a low-privileged account can use this procedure to gain additional privileges and potentially gain access to sensitive data. 

To perform this procedure, the attacker must identify a process with elevated capabilities and modify its capabilities to include additional privileges. This can be done through the use of the 'setcap' command. 

This procedure can be valuable for an attacker looking to gain access to sensitive data or systems. By escalating privileges, the attacker can bypass security measures and gain access to resources that would otherwise be restricted.

## Requirements

1. Access to a low-privileged account on a Linux system

1. Knowledge of Linux capabilities

1. Access to the 'setcap' command

## Defense

1. Limit the use of elevated capabilities to only necessary processes

1. Monitor for unusual activity, such as changes to capabilities

1. Regularly review and update access controls to prevent unauthorized access

## Objectives

1. Escalate privileges on a Linux system

1. Gain access to sensitive data or systems

# Instructions

1. To manage the capabilities of the ping command, use the following commands:

**Code**: [[/usr/bin/setcap -r /bin/ping            # remove
/]]

> The 'setcap' command is used to set or remove capabilities of a command. In this case, we are managing the capabilities of the 'ping' command. The first command removes the 'cap_net_raw' capability from the 'ping' command. The second command adds the 'cap_net_raw' capability to the 'ping' command. The 'cap_net_raw' capability allows the 'ping' command to send and receive raw network packets, which is necessary for its functionality.

**Command** ([[Add cap_net_raw+p to ping binary]]):

```bash
/usr/bin/setcap cap_net_raw+p /bin/ping
```

**Command** ([[Remove cap_net_raw from ping binary]]):

```bash
/usr/bin/setcap -r /bin/ping
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

- [[Add cap_net_raw+p to ping binary]]
- [[Remove cap_net_raw from ping binary]]

## Tags

- [[Capabilities]]
- [[Edit capabilities]]
- [[Linux - Privilege Escalation]]
