---
id: c626341a-dace-4537-ace1-bacbaedd94e4
name: Directory-Traversal-Bypass-Payloads
type: code
language: plaintext
verified: true
created_at: '2023-04-06T03:55:57.854455+00:00'
updated_at: '2023-04-10T20:22:08.607507+00:00'
platforms:
  - Web
tags:
  - directory-traversal
  - waf-bypass
  - payload
validated: true
---

# Directory-Traversal-Bypass-Payloads

## Code

```plaintext
..././
...\.
```

## Description

These are example string payloads for bypassing WAF filters that remove '../' in directory traversal attacks. '..././' is used for Unix-like path traversal (equivalent to multiple '../' after partial filtering), and '...\.\/' for Windows paths using backslashes. They are inserted into URL parameters to chain traversals and access restricted files.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | These are static strings; repeat as needed (e.g., '..././..././' for deeper traversal) | '..././..././../../../etc/passwd' |

## Usage

Embed these in HTTP requests, e.g., via curl: ?file=..././..././etc/passwd. Use in scenarios where standard '../' is filtered, such as testing file download endpoints. Start with minimal repetitions and increase to evade the specific WAF rule.

## Detection

- WAF logs showing requests with repeated dot-slash patterns (e.g., regex for \.{3,}/ or \.\.\/\.\/).
- Application logs with anomalous path resolutions or access to system files.
- Network monitoring for GET/POST parameters containing traversal sequences.

## Related

- [[procedures/Directory-Traversal-Bypass-Using-Duplication]]
