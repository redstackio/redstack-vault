---
id: b86a343f-f52f-4e47-b379-ace33e5ac611
name: php-extensions-list
type: code
language: text
verified: true
created_at: '2023-04-06T03:56:41.023724+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - file-upload
  - php
  - reference
validated: true
---

# php-extensions-list

## Code

```text
.php
.php3
.php4
.php5
.php7

# Less known PHP extensions
.pht
.phps
.phar
.phpt
.pgif
.phtml
.phtm
.inc
```

## Description

This code snippet provides a comprehensive list of PHP file extensions, including common and obscure ones, for use in naming malicious files during insecure file upload exploitation. It serves as a quick reference to test various extensions that may be executable on PHP-enabled web servers.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Static list; no variables to substitute | N/A |

## Usage

Copy the relevant extensions from this list to rename your webshell or payload file before uploading. Start with common ones (.php) and escalate to obscure (.phtml) if filters block them. Embed in scripts or use manually during pentesting.

## Detection

- Web application logs showing uploads with these extensions.
- File integrity monitoring alerting on executable files in upload directories.
- WAF rules matching PHP extension patterns in upload requests.

## Related

- [[procedures/Exploit-Insecure-File-Upload-with-Extension-Bypass]]
