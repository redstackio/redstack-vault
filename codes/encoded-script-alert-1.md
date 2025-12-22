---
id: 5ed08373-bb4d-479d-be0c-91ab724b1e65
name: encoded-script-alert-1
type: code
language: html
verified: true
created_at: '2023-04-06T03:56:41.758946+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - xss
  - payload
  - encoded
  - bypass
validated: true
---

# encoded-script-alert-1

## Code

```html
&lt;script&gt;alert(1)&lt;/script&gt;
```

## Description

HTML entity-encoded version of a basic alert payload to bypass simple filters that strip unencoded <script> tags while still executing the alert on decode.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Encoded fixed payload | N/A |

## Usage

Paste directly into input fields where raw tags are filtered. The server decodes entities, allowing execution. Confirm with popup; use for filter evasion in testing.

## Detection

- Logs showing HTML entities in inputs.
- Output encoding checks failing on entities.
- Advanced WAFs decoding and blocking alert patterns.

## Related

- [[procedures/Identify-and-Exploit-XSS-Vulnerabilities]]
