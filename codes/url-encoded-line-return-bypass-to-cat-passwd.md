---
id: 68f7d44a-69ba-4def-8d59-a3ec20f3c699
name: url-encoded-line-return-bypass-to-cat-passwd
type: code
language: bash
verified: true
created_at: '2023-04-06T03:55:57.128273+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Web
tags:
  - command-injection
  - bypass
  - payload
validated: true
---

# url-encoded-line-return-bypass-to-cat-passwd

## Code

```bash
something%0Acat%20/etc/passwd
```

## Description

This URL-encoded payload uses a line return (%0A) to bypass input filters in web applications, injecting a command to read the /etc/passwd file after a benign 'something' input. When decoded and executed in a shell, it splits into two lines, evading single-line scanners.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| something | Benign input to prepend (customize to match expected format) | ping, whoami |
| %0A | URL-encoded newline to split commands | Fixed |
| cat%20/etc/passwd | Encoded command to view password file | Fixed (use [[commands/cat-view-etc-passwd]]) |

## Usage

Inject into vulnerable HTTP parameters (e.g., via Burp Suite repeater) targeting endpoints that execute shell commands. Suitable for initial reconnaissance in command injection scenarios to enumerate users.

## Detection

- Web logs showing %0A or decoded newlines in inputs.
- File access monitoring for /etc/passwd reads from web processes (e.g., Apache).
- WAF rules blocking encoded control characters or anomalous command patterns.

## Related

- [[procedures/Command-Injection-with-Line-Return-Bypass]]
