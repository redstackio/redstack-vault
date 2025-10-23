---
id: fa7646af-4b6d-4ebd-9d93-950483215b46
name: PHP Filter LFI/RFI
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.325412+00:00'
updated_at: '2023-04-10T20:22:19.763012+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[File Inclusion]]'
- '[[LFI / RFI using wrappers]]'
- '[[Wrapper php://filter]]'
---

# PHP Filter LFI/RFI

## Summary

PHP Filter LFI/RFI is a technique that allows an attacker to include a remote file by abusing the php://filter wrapper. This technique is commonly used to bypass input validation filters and execute arbitrary code on the target system. By encoding the payload in base64, the attacker can bypass any 

## Description

# Description

PHP Filter LFI/RFI is a technique that allows an attacker to include a remote file by abusing the php://filter wrapper. This technique is commonly used to bypass input validation filters and execute arbitrary code on the target system. By encoding the payload in base64, the attacker can bypass any input validation filters that may be in place. This technique can be used to obtain sensitive information, such as credentials, or to execute arbitrary code on the target system.

 

## Requirements

1. Access to a vulnerable web application.

1. Knowledge of the target system.

 

## Defense

1. Sanitize input to prevent injection attacks.

1. Implement access controls to prevent unauthorized access to sensitive files.

1. Monitor web application logs for suspicious activity.

 

## Objectives

1. To obtain sensitive information, such as credentials.

1. To execute arbitrary code on the target system.

 

# Instructions

1. Replace the URL with the vulnerable web application URL and the parameter with the vulnerable parameter.

 



**Code**: [[./kadimus -u "http://example.com/index.php?page=vu]]



> The command uses Kadimus to exploit the vulnerability and download the remote file to the local system. The -S option enables SSL, -f specifies the file name, -O specifies the output file, and --parameter specifies the parameter to inject the payload. The curl command is used to encode the payload in base64 and decode it on the local system.

2. 

 



**Code**: [[php://filter]]



> The PHP Filter wrapper is a built-in PHP wrapper that allows data to be filtered through a chain of filters. This can be used to encode and decode data, among other things.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[System Information Discovery|T1082 - System Information Discovery]]

## Tags

- [[File Inclusion]]
- [[LFI / RFI using wrappers]]
- [[Wrapper php://filter]]


