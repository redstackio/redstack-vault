---
tags:
  - laravel
  - debug-mode
  - information-disclosure
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/burp-intercept-password-reset]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:17.631Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: b3301905-fef2-4d6c-913d-eebf54036de5
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Hardware]]'
  - '[[Exploit Public-Facing Application]]'
---
# Discover-Laravel-Debug-Mode-via-Password-Reset

## Summary

This procedure triggers Laravel's debug mode by accessing a password reset endpoint, intercepting the response to extract stack traces, file paths, and configuration details like APP_DEBUG=true, enabling reconnaissance without authentication.

## Description

In Laravel applications with debug mode enabled (APP_DEBUG=true in .env), error pages expose detailed information. By requesting a non-existent or error-prone endpoint like password reset, attackers can observe the 'Whoops' debug output, revealing version, paths, and configs. This aids in chaining attacks like path traversal or targeted exploits. The target here is https://mpos.mtn.co.sz/srvgtw001/merchant/password/reset, using Burp Suite for interception.

## Requirements

1. Network access to the target web application (external)
2. Burp Suite installed and configured as proxy
3. Browser or tool to send HTTP requests

## Defense

Defensive measures and detection strategies:

- Disable APP_DEBUG in production (.env file)
- Use web application firewall (WAF) to block debug endpoint access
- Monitor logs for unusual requests to /password/reset or error pages
- Implement rate limiting on authentication endpoints

## Objectives

1. Confirm debug mode activation and extract sensitive info
2. Identify Laravel version for further exploit research
3. Gather paths for potential traversal attacks

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up Burp Suite to intercept traffic from your browser.

**Command** ([[commands/burp-intercept-password-reset]]):

No direct command; configure Burp listener on 127.0.0.1:8080 and set browser proxy.

> Launch Burp, enable intercept in Proxy tab. Expected: Traffic routed through Burp.

### Step 2: Request Password Reset Endpoint

**Context**: Send GET request to trigger error and debug output.

**Command** ([[commands/burp-intercept-password-reset]]):
```http
GET /srvgtw001/merchant/password/reset HTTP/1.1
Host: mpos.mtn.co.sz
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Connection: keep-alive
```

> Intercept in Burp, forward request, and inspect response for debug HTML. Expected: Stack trace with paths like /srvgtw001/ and Laravel 8.83.27.

### Step 3: Analyze Debug Output

**Context**: Examine response for sensitive details.

No command; manually review in Burp Repeater.

> Look for 'APP_DEBUG=true', file paths, and configs. Success: Info extracted for next steps.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Hardware]] Gather Victim Host Information: Software
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

- [[commands/burp-intercept-password-reset]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[laravel]]
- [[debug-mode]]
- [[information-disclosure]]
