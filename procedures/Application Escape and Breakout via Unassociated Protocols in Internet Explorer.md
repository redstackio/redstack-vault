---
id: c25ae809-f867-40df-a215-1b289cba3048
name: Application Escape and Breakout via Unassociated Protocols in Internet Explorer
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:17.510672+00:00'
updated_at: '2023-04-06T03:56:17.525269+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]'
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
sub_techniques:
- '[[Bypass User Account Control|T1548.002 - Bypass User Account Control]]'
tags:
- '[[Application Escape and Breakout]]'
- '[[Internet Explorer]]'
- '[[Unassociated Protocols]]'
commands:
- '[[Open IRC channel in Firefox with Test profile]]'
---

# Application Escape and Breakout via Unassociated Protocols in Internet Explorer

## Summary

Application escape and breakout via unassociated protocols in Internet Explorer is a technique used by attackers to bypass security mechanisms and execute malicious code. This attack involves opening Internet Explorer and using an unassociated protocol to launch a payload. By doing so, the attacker

## Description

# Description

Application escape and breakout via unassociated protocols in Internet Explorer is a technique used by attackers to bypass security mechanisms and execute malicious code. This attack involves opening Internet Explorer and using an unassociated protocol to launch a payload. By doing so, the attacker can bypass security controls that are designed to prevent malicious code execution. This technique can be used to gain a foothold in a target network, escalate privileges, and ultimately achieve their objectives.

Technical Explanation: This technique involves the use of unassociated protocols in Internet Explorer to execute malicious code. The attacker can use a command such as 'Open Firefox with a specific profile and URL' to launch a payload using an unassociated protocol. This technique can be used to bypass security mechanisms such as User Account Control (UAC) and execute code with elevated privileges.

Business Value: This technique can be used by attackers to gain access to sensitive data, steal intellectual property, or cause disruption to business operations. By bypassing security mechanisms, attackers can achieve their objectives without being detected.

 

## Requirements

1. Access to a vulnerable system running Internet Explorer

1. Ability to execute commands on the target system

 

## Defense

1. Keep systems and software up-to-date with the latest security patches

1. Implement security controls such as firewalls and antivirus software

1. Educate users on how to identify and avoid phishing attacks

 

## Objectives

1. Gain access to the target network

1. Escalate privileges

1. Execute malicious code

 

# Instructions

1. To open Firefox with a specific profile and URL, use the following command:

firefox [URL] -P [profile name]

Replace [URL] with the desired URL and [profile name] with the name of the profile you want to use.

For example, to open Firefox with the URL irc://127.0.0.1 and the profile named "Test", use the following command:

firefox irc://127.0.0.1 -P "Test"

 

The "firefox" command opens the Firefox web browser. The "-P" option specifies the name of the profile to use. The "irc://127.0.0.1" argument specifies the URL to open. In this example, Firefox will open with the "Test" profile and the URL irc://127.0.0.1.



**Command** ([[Open IRC channel in Firefox with Test profile]]):

```bash
firefox irc://127.0.0.1 -P "Test"
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]
- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]

### Sub-Techniques

- [[Bypass User Account Control|T1548.002 - Bypass User Account Control]]

## Commands Used

- [[Open IRC channel in Firefox with Test profile]]

## Tags

- [[Application Escape and Breakout]]
- [[Internet Explorer]]
- [[Unassociated Protocols]]


