---
type: code
language: PHP
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - PHP
tags:
  - Argument-Injection
  - FIND
  - Safe-Example
validated: true
---

# PHP-Find-Command-Safe-Example

## Code

```php
$file = "some_file";
system("find /tmp -iname " . escapeshellcmd($file));
```

## Description

This PHP code snippet demonstrates a safe way to execute the 'find' command using user input for the filename, wrapped with escapeshellcmd() to prevent shell metacharacters from being interpreted. It searches for a specified file in the /tmp directory using the -iname option for case-insensitive matching. While this protects against shell injection, it does not guard against argument injection specific to the 'find' utility's option parsing.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $file | The filename to search for | "some_file" |

## Usage

Embed this in a PHP script or web application where user input populates $file, such as a file search feature. Execute via a vulnerable endpoint to test safe behavior. Used in red teaming to baseline normal 'find' output before attempting injections.

## Detection

- PHP execution logs showing system() calls with 'find /tmp'.
- File system access logs (e.g., via auditd) for reads in /tmp.
- No anomalous output beyond standard 'find' results; monitor for deviations in command arguments.

## Related

- [[procedures/Argument-Injection-via-Find-Command]]
