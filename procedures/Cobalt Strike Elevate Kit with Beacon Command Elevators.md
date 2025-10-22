---
id: 35f45ae4-7ad2-46d4-bc12-e58be7f64fb1
name: Cobalt Strike Elevate Kit with Beacon Command Elevators
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:16.627590+00:00'
updated_at: '2023-04-10T20:36:21.079529+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Event Triggered Execution|T1546 - Event Triggered Execution]]'
- '[[Process Injection|T1055 - Process Injection]]'
sub_techniques:
- '[[Component Object Model Hijacking|T1546.015 - Component Object Model Hijacking]]'
tags:
- '[[Cobalt Strike]]'
- '[[Elevate Kit]]'
- '[[Kits]]'
commands:
- '[[Beacon Command Elevators Exploit List]]'
---

# Cobalt Strike Elevate Kit with Beacon Command Elevators

## Summary

The Cobalt Strike Elevate Kit with Beacon Command Elevators is a tool used by attackers to escalate their privileges on a target system. This kit allows attackers to inject malicious code into a legitimate process, thereby bypassing security measures and gaining access to sensitive information. The

## Description

# Description

The Cobalt Strike Elevate Kit with Beacon Command Elevators is a tool used by attackers to escalate their privileges on a target system. This kit allows attackers to inject malicious code into a legitimate process, thereby bypassing security measures and gaining access to sensitive information. The Beacon Command Elevators command is used to elevate privileges to SYSTEM level by exploiting the Windows Management Instrumentation (WMI) Event Subscription feature. This technique is particularly effective as it allows the attacker to execute code without being detected by traditional anti-virus software.

From a technical perspective, the Cobalt Strike Elevate Kit uses a combination of process injection and WMI event subscriptions to gain SYSTEM level access on a target system. This allows the attacker to execute code with elevated privileges, providing access to sensitive data and the ability to move laterally within the network. The business value of this attack lies in the ability to gain access to valuable information, such as intellectual property, financial data or customer information, which can be used for financial gain or competitive advantage.

## Requirements

1. Access to a vulnerable system with a legitimate process to inject malicious code into

1. Cobalt Strike Elevate Kit

1. Beacon Command Elevators

## Defense

1. Regularly update and patch software to prevent vulnerabilities that attackers can exploit

1. Use anti-virus software and firewalls to detect and block malicious activity

1. Implement the principle of least privilege to limit the impact of any successful privilege escalation attacks

## Objectives

1. Gain SYSTEM level access on a target system

1. Execute code with elevated privileges

1. Access sensitive data

1. Move laterally within the network

# Instructions

1. To use the Beacon Command Elevators, run the command 'runasadmin' in the Beacon console. This command will display a list of exploits that can be used to escalate privileges. Choose the appropriate exploit based on the target system and run it using the 'execute' command.

For example, to use the 'uac-token-duplication' exploit, run the following commands:

beacon> runasadmin
beacon> execute uac-token-duplication

This will bypass User Account Control (UAC) and escalate privileges to SYSTEM level.

**Code**: [[beacon> runasadmin

Beacon Command Elevators
=====]]

> The Beacon Command Elevators is a collection of exploits that can be used to escalate privileges on a target system. These exploits take advantage of vulnerabilities in Windows operating systems to bypass User Account Control (UAC) and gain elevated privileges.

The list of exploits includes:

- ms14-058: TrackPopupMenu Win32k NULL Pointer Dereference (CVE-2014-4113)
- ms15-051: Windows ClientCopyImage Win32k Exploit (CVE 2015-1701)
- ms16-016: mrxdav.sys WebDav Local Privilege Escalation (CVE 2016-0051)
- svc-exe: Get SYSTEM via an executable run as a service
- uac-schtasks: Bypass UAC with schtasks.exe (via SilentCleanup)
- uac-token-duplication: Bypass UAC with Token Duplication

To use these exploits, first run the 'runasadmin' command in the Beacon console. This will run the Beacon payload with elevated privileges. Then, choose the appropriate exploit based on the target system and run it using the 'execute' command.

Note that the 'uac-token-duplication' exploit is fixed in Windows 10 Red Stone 5 (October 2018) and may not work on newer systems.

**Command** ([[Beacon Command Elevators Exploit List]]):

```bash
beacon> runasadmin

Beacon Command Elevators
========================

    Exploit                         Description
    -------                         -----------
    ms14-058                        TrackPopupMenu Win32k NULL Pointer Dereference (CVE-2014-4113)
    ms15-051                        Windows ClientCopyImage Win32k Exploit (CVE 2015-1701)
    ms16-016                        mrxdav.sys WebDav Local Privilege Escalation (CVE-2016-0051)
    svc-exe                         Get SYSTEM via an executable run as a service
    uac-schtasks                    Bypass UAC with schtasks.exe (via SilentCleanup)
    uac-token-duplication           Bypass UAC with Token Duplication
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Event Triggered Execution|T1546 - Event Triggered Execution]]
- [[Process Injection|T1055 - Process Injection]]

### Sub-Techniques

- [[Component Object Model Hijacking|T1546.015 - Component Object Model Hijacking]]

## Commands Used

- [[Beacon Command Elevators Exploit List]]

## Tags

- [[Cobalt Strike]]
- [[Elevate Kit]]
- [[Kits]]
