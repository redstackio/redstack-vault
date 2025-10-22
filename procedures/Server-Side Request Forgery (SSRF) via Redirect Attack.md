---
id: 3b9ed0b7-938a-4aaa-b7ad-6553a362804a
name: Server-Side Request Forgery (SSRF) via Redirect Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.661683+00:00'
updated_at: '2023-04-10T20:24:12.415827+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Bypassing filters]]'
- '[[Bypassing using a redirect]]'
- '[[Server-Side Request Forgery]]'
commands:
- '[[Launch SSRF pointing to vulnerable.com]]'
---

# Server-Side Request Forgery (SSRF) via Redirect Attack

## Summary

A Server-Side Request Forgery (SSRF) vulnerability allows an attacker to send crafted requests from a vulnerable server. This can be used to access services and resources that are not intended to be exposed to the attacker. In this particular attack, the attacker bypasses filters and uses a redirec

## Description

# Description

A Server-Side Request Forgery (SSRF) vulnerability allows an attacker to send crafted requests from a vulnerable server. This can be used to access services and resources that are not intended to be exposed to the attacker. In this particular attack, the attacker bypasses filters and uses a redirect to execute an SSRF attack. This allows the attacker to send requests to internal or external systems, pivot through the network, and potentially access sensitive data.

Technical Explanation: The attacker crafts a request to a vulnerable server that contains a redirect to a target URL. The server sends the request to the target URL, which can be an internal or external system. The response from the target URL is then sent back to the attacker. This allows the attacker to bypass filters that are in place to prevent SSRF attacks.

Business Value: An attacker can use this technique to access sensitive data, pivot through the network, and potentially gain access to critical systems. This can lead to data theft, data manipulation, and other malicious activities.

## Requirements

1. Access to a vulnerable server

1. Knowledge of the target URL

1. Ability to craft requests

## Defense

1. Implement input validation and sanitization to prevent crafted requests

1. Implement filters to prevent redirects to external systems

1. Monitor network traffic for suspicious activity

## Objectives

1. Send crafted requests to a vulnerable server

1. Access internal or external systems

1. Pivot through the network

1. Potentially access sensitive data

# Instructions

1. To perform an SSRF redirect attack, follow the below steps:

1. Choose a whitelisted host and create a page on it that can redirect requests to the target URL.
2. Launch the SSRF pointing to vulnerable.com/index.php?url=http://YOUR_SERVER_IP.
3. vulnerable.com will fetch YOUR_SERVER_IP which will redirect to the target URL.
4. Use response codes 307 and 308 to retain HTTP method and body after the redirection.

**Code**: [[1. Create a page on a whitelisted host that redire]]

> This command explains how to perform an SSRF redirect attack. It provides a step-by-step guide on how to create a page on a whitelisted host that can redirect requests to a target URL. It also explains how to launch the SSRF pointing to vulnerable.com/index.php?url=http://YOUR_SERVER_IP and use response codes 307 and 308 to retain HTTP method and body after the redirection.

**Command** ([[Launch SSRF pointing to vulnerable.com]]):

```bash
http://vulnerable.com/index.php?url=http://YOUR_SERVER_IP
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Launch SSRF pointing to vulnerable.com]]

## Tags

- [[Bypassing filters]]
- [[Bypassing using a redirect]]
- [[Server-Side Request Forgery]]
