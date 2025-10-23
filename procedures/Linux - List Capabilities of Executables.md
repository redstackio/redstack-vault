---
id: 1ef0f721-9848-4f45-b0c7-f732224a08b4
name: Linux - List Capabilities of Executables
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:18.865869+00:00'
updated_at: '2023-04-10T20:34:28.284951+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]'
- '[[Process Injection|T1055 - Process Injection]]'
tags:
- '[[Capabilities]]'
- '[[Linux - Privilege Escalation]]'
- '[[List capabilities of binaries]]'
commands:
- '[[Check Capabilities]]'
---

# Linux - List Capabilities of Executables

## Summary

Listing the capabilities of binaries is a useful technique for privilege escalation on Linux systems. Capabilities are a way to grant specific privileges to a process without granting it full root access. By listing the capabilities of a binary, an attacker can identify which capabilities are avail

## Description

# Description

Listing the capabilities of binaries is a useful technique for privilege escalation on Linux systems. Capabilities are a way to grant specific privileges to a process without granting it full root access. By listing the capabilities of a binary, an attacker can identify which capabilities are available and potentially abuse them to escalate privileges. This technique can be used in combination with other techniques, such as process injection or abusing elevation control mechanisms.

From a technical perspective, capabilities are stored in the file system's extended attributes. The 'getcap' command can be used to list the capabilities of a binary. The output will show which capabilities are enabled for the binary and which file it belongs to.

The business value of this technique is that it allows an attacker to gain higher privileges on a system, potentially leading to access to sensitive data or control over critical systems.

 

## Requirements

1. Access to a Linux system

1. Permission to execute the 'getcap' command

 

## Defense

1. Limit or remove unnecessary capabilities from binaries

1. Monitor for unusual or unexpected capabilities being used

1. Regularly review and update file system permissions and extended attributes

 

## Objectives

1. Identify which capabilities are available for a binary

1. Use the identified capabilities to escalate privileges

 

# Instructions

1. To list capabilities of executables, run the following command:

 



**Code**: [[╭─swissky@lab ~  
╰─$ /usr/bin/getcap -r  /usr/bin]]



> getcap -r /path/to/executables

This will list the capabilities of all executables in the specified path recursively. The output will show the executable file name followed by the capabilities associated with it. The capabilities are represented in the format of <capability_name>+<capability_flag>. For example, cap_net_raw+ep means that the executable has the capability to perform raw network I/O operations and can be executed with elevated privileges.



**Command** ([[Check Capabilities]]):

```bash
/usr/bin/getcap -r  /usr/bin
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]
- [[Process Injection|T1055 - Process Injection]]

## Commands Used

- [[Check Capabilities]]

## Tags

- [[Capabilities]]
- [[Linux - Privilege Escalation]]
- [[List capabilities of binaries]]


