---
type: code
language: PHP
verified: true
tags:
  - vulnerable-code
  - php
  - wget
  - injection
platforms:
  - Linux
  - Web
validated: true
---

# Vulnerable-PHP-System-WGET-Call

## Code

```php
system(escapeshellcmd('wget '.$url));
```

## Description

This PHP code snippet demonstrates a vulnerable implementation of file download using wget invoked via system(). The $url variable is assumed to be user-controlled (e.g., from $_GET['url']). While escapeshellcmd prevents basic shell metacharacter injection (e.g., '; rm -rf /'), it does not block argument injection into wget, allowing options like --directory-prefix to be prepended when $url starts with '--option value '.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $url | User-supplied URL parameter, vulnerable to injection | '--directory-prefix=/var/www/html http://example.com/file.php' |

## Usage

Found in web applications with user-driven download features (e.g., /download.php?url=...). Attackers exploit by submitting crafted URLs via GET/POST requests. Use in red team scenarios to demonstrate OS command injection risks in legacy code. Deliver via tools like Burp Suite or curl to the endpoint.

## Detection

- Static analysis: Scan for system() or exec() calls with concatenated user input and wget/curl.
- Dynamic: Monitor process logs for wget invocations with unexpected options (e.g., via auditd or SELinux).
- WAF rules: Block requests where 'url' contains '--' followed by known wget flags.
- File integrity monitoring: Alert on new files in /var/www/html or /tmp from unknown sources.

## Related

- [[procedures/WGET-Argument-Injection]]
- [[tools/PHP]] (for language context)
