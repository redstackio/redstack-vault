---
id: 2f25dc3d-bdeb-443e-891a-211962b6d84f
name: LFI to RCE via /proc/self/environ
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.458173+00:00'
updated_at: '2023-04-10T20:22:18.705621+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
sub_techniques:
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[File Inclusion]]'
- '[[LFI to RCE via /proc/self/environ]]'
---

# LFI to RCE via /proc/self/environ

## Summary

LFI to RCE via /proc/self/environ is a technique used by attackers to exploit a vulnerability in a web application that allows for local file inclusion. This technique can be used to execute arbitrary code on the server. By injecting malicious code into the User-Agent field of an HTTP request, an a

## Description

# Description

LFI to RCE via /proc/self/environ is a technique used by attackers to exploit a vulnerability in a web application that allows for local file inclusion. This technique can be used to execute arbitrary code on the server. By injecting malicious code into the User-Agent field of an HTTP request, an attacker can cause the server to write the request to the /proc/self/environ file, which can then be read by the attacker to execute arbitrary code. This technique can be used to gain access to sensitive data, escalate privileges, and perform other malicious activities.

From a technical perspective, this technique works by exploiting a vulnerability in the way that the web application handles user input. By manipulating the input to the vulnerable.php file, an attacker can trick the server into writing the payload to the /proc/self/environ file. Once the payload is in the file, the attacker can execute it by reading the file.

From a business perspective, this technique can be used by attackers to gain access to sensitive data, escalate privileges, and perform other malicious activities that can compromise the integrity, confidentiality, and availability of the organization's systems and data.

## Requirements

1. Access to a vulnerable web application

## Defense

1. Ensure that all input to the web application is properly sanitized and validated.

1. Implement access controls to prevent unauthorized access to sensitive data and resources.

1. Use web application firewalls (WAFs) and intrusion detection/prevention systems (IDS/IPS) to monitor and block malicious traffic.

## Objectives

1. To gain access to sensitive data

1. To escalate privileges

1. To execute arbitrary code on the server

# Instructions

1. 1. Identify a vulnerable web application.
2. Send a GET request to the vulnerable.php file with the filename parameter set to ../../../proc/self/environ.
3. In the User-Agent field of the request, include the payload that you want to execute.
4. Read the /proc/self/environ file to execute the code.

**Code**: [[GET vulnerable.php?filename=../../../proc/self/env]]

> The command sends a GET request to the vulnerable.php file with the filename parameter set to ../../../proc/self/environ. In the User-Agent field of the request, the payload is included. The payload will be reflected in the /proc/self/environ file, which can then be read to execute the code.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

### Sub-Techniques

- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Tags

- [[File Inclusion]]
- [[LFI to RCE via /proc/self/environ]]
