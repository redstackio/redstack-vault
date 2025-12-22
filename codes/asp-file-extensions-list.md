---
id: e2333ebe-3e8a-49a4-b904-435b4c618a8a
name: asp-file-extensions-list
type: code
language: text
verified: true
created_at: '2023-04-06T03:56:41.023926+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - file-upload
  - asp
  - iis
  - reference
validated: true
---

# asp-file-extensions-list

## Code

```text
.asp
.aspx
.config
.cer and .asa # (IIS <= 7.5)
shell.aspx;1.jpg # (IIS < 7.0)
shell.soap
```

## Description

This code snippet lists file extensions and formats usable for ASP/ASP.NET uploads on IIS servers, including version-specific bypasses. It helps in crafting uploads that evade restrictions and execute as server-side scripts.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Static list; no variables to substitute | N/A |

## Usage

Use these extensions to name ASP payloads (e.g., shell.aspx) or append to benign files (e.g., shell.aspx;1.jpg for old IIS). Test in the context of an insecure upload form to achieve RCE on Windows/IIS environments.

## Detection

- IIS logs with ASP extension uploads or double-extension patterns.
- Monitoring for .aspx or .config files in web-accessible directories.
- Anomalous HTTP requests to uploaded ASP files.

## Related

- [[procedures/Exploit-Insecure-File-Upload-with-Extension-Bypass]]
