---
data: >-
  <?php while($f= @file("/proc/<pid of php server>/fd/<file descriptor
  associated with the tmp file>")){ var_dump($f); } ?>
tags:
  - race-condition
  - debug
type: command
output: null
executor: php
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.086Z'
id: c8f8ebc8-a735-4af6-b2e0-ee0085a521b1
verified: false
validated: true
submitted: true
---
---

# php-race-condition-demo-script

## Command

```php
<?php while($f= @file("/proc/<pid of php server>/fd/<file descriptor associated with the tmp file>")){ var_dump($f); } ?>
```

## Description

PHP script to repeatedly read a temporary file descriptor during race condition exploitation, dumping content to verify payload capture before deletion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /proc/<pid>/fd/<fd> | Path to process FD pointing to temp file | Yes |

## Examples

### Basic Usage

Replace <pid> and <fd> with actual values and run via php cli.

## Expected Output

Dumps array of file contents if read successfully.

## Related

- [[Related Procedure: Exploit-Race-Condition-for-XSS-Import]]
