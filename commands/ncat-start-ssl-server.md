---
type: command
executor: bash
data: ncat --ssl -vv -l -p $_PORT
output: null
platforms:
  - Linux
tags:
  - ncat
  - server
  - ssl
verified: true
validated: true
---

# ncat-start-ssl-server

## Command

```bash
ncat --ssl -vv -l -p $_PORT
```

## Description

Alternative to OpenSSL s_server: Starts an SSL-enabled Netcat listener for encrypted connections, useful for reverse shells when certificates are pre-configured or for simple TLS wrapping.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --ssl | Enable SSL/TLS | Yes |
| -vv | Very verbose output | No |
| -l | Listen mode | Yes |
| -p $_PORT | Listening port (e.g., 4242) | Yes |

## Examples

### Basic Usage

```bash
ncat --ssl -vv -l -p 4242
```

Listens with verbose logging.

### Advanced Usage

```bash
ncat --ssl -vv -l -p 4242 --ssl-cert cert.pem --ssl-key key.pem
```

Specifies custom cert/key if needed.

## Expected Output

```
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::4242
Ncat: Listening on 0.0.0.0:4242
Ncat: SSL connection from (unknown) [target_ip]:port.
(... shell I/O ...)
```

Forwards client data to stdout/stdin.

## Related

- [[commands/openssl-start-server-with-cert]]
- [[procedures/openssl-reverse-shell]]
