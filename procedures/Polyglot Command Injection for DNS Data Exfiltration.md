---
id: ee1463fa-689c-4887-a4d0-867d576bec29
name: Polyglot Command Injection for DNS Data Exfiltration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:57.539400+00:00'
updated_at: '2023-04-06T03:55:57.551800+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Data Encoding|T1132 - Data Encoding]]'
sub_techniques:
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[Command Injection]]'
- '[[Polyglot command injection]]'
---

# Polyglot Command Injection for DNS Data Exfiltration

## Summary

Polyglot command injection is a technique used by attackers to inject malicious commands into a vulnerable application. This technique involves using multiple comment types to evade detection and achieve successful injection. In this specific case, the attacker is using polyglot command injection t

## Description

# Description

Polyglot command injection is a technique used by attackers to inject malicious commands into a vulnerable application. This technique involves using multiple comment types to evade detection and achieve successful injection. In this specific case, the attacker is using polyglot command injection to exfiltrate data using DNS queries. The attacker is injecting malicious commands into the application, which are then executed on the server, allowing the attacker to exfiltrate data through DNS queries. This technique is highly effective because DNS requests are often allowed through firewalls and other security measures, making it difficult to detect and block this type of attack.

 

## Requirements

1. Access to a vulnerable application with command injection vulnerability

 

## Defense

1. Input validation and sanitization should be implemented to prevent command injection attacks.

1. Regularly monitor and analyze DNS traffic for suspicious activity.

1. Implement network segmentation to prevent lateral movement in case of a successful attack.

 

## Objectives

1. Inject malicious commands into the vulnerable application

1. Exfiltrate data through DNS queries

 

# Instructions

1. The attacker injects the payload into the vulnerable application to execute the malicious command.

 



**Code**: [[1;sleep${IFS}9;#${IFS}';sleep${IFS}9;#${IFS}";slee]]



> This command injects a malicious payload into the vulnerable application, which is then executed on the server. The payload is designed to sleep for 9 seconds and then send a DNS query to the attacker-controlled DNS server, thereby exfiltrating the data. The payload uses multiple comment types to evade detection and achieve successful injection.

2. The attacker injects the payload into the vulnerable application to execute the malicious command.

 



**Code**: [[/*$(sleep 5)`sleep 5``*/-sleep(5)-'/*$(sleep 5)`sl]]



> This command injects a malicious payload into the vulnerable application, which is then executed on the server. The payload is designed to sleep for 5 seconds and then send a DNS query to the attacker-controlled DNS server, thereby exfiltrating the data. The payload uses multiple comment types to evade detection and achieve successful injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Data Encoding|T1132 - Data Encoding]]

### Sub-Techniques

- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Tags

- [[Command Injection]]
- [[Polyglot command injection]]


