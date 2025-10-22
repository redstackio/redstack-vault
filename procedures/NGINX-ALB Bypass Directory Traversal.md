---
id: a1c02ec2-8475-4cd5-b88c-275f83bbeb49
name: NGINX/ALB Bypass Directory Traversal
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:57.940709+00:00'
updated_at: '2023-04-10T20:22:10.022411+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Remote Services|T1021 - Remote Services]]'
tags:
- '[[Basic exploitation]]'
- '[[Directory Traversal]]'
- '[[NGINX/ALB Bypass]]'
---

# NGINX/ALB Bypass Directory Traversal

## Summary

NGINX and Amazon Load Balancer (ALB) can block directory traversal attacks in the route. However, it is possible to bypass these security measures by adding forward slashes in front of the URL. This allows an attacker to access files and directories outside of the web root directory. A successful d

## Description

# Description

NGINX and Amazon Load Balancer (ALB) can block directory traversal attacks in the route. However, it is possible to bypass these security measures by adding forward slashes in front of the URL. This allows an attacker to access files and directories outside of the web root directory. A successful directory traversal attack can result in unauthorized access to sensitive files, data exfiltration, and even full system compromise.

## Requirements

1. Access to the target system

1. Knowledge of the target web application's file structure

## Defense

1. Implement input validation and sanitization to prevent directory traversal attacks

1. Configure NGINX and ALB to block directory traversal attacks

1. Regularly update and patch NGINX and ALB to prevent known vulnerabilities

## Objectives

1. Gain unauthorized access to sensitive files and directories

1. Exfiltrate sensitive data

1. Compromise the target system

# Instructions

1. Use the following command to perform a directory traversal attack against an NGINX server:

```
curl http://nginx-server/../../
```

**Code**: [[http://nginx-server/../../]]

> This command sends a GET request to the target server with the "../" characters added to the URL. If the server is vulnerable to directory traversal attacks, it will return the contents of the requested file or directory.

2. Use the following command to bypass NGINX and ALB security measures and perform a directory traversal attack:

```
curl http://nginx-server////////../../
```

**Code**: [[http://nginx-server////////../../]]

> This command sends a GET request to the target server with multiple forward slashes added to the URL before the "../" characters. This bypasses the security measures put in place by NGINX and ALB and allows an attacker to access files and directories outside of the web root directory.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Remote Services|T1021 - Remote Services]]

## Tags

- [[Basic exploitation]]
- [[Directory Traversal]]
- [[NGINX/ALB Bypass]]
