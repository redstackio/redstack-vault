---
type: command
executor: bash
data: ./chisel server -p $_LISTEN_PORT --reverse
output: >-
  root@kali:~# ./chisel server -p 9001 --reverse

  2019/10/01 19:56:38 server: Reverse tunnelling enabled

  2019/10/01 19:56:38 server: Fingerprint
  85:91:1f:ed:c1:0b:f4:b5:01:e1:56:8d:d1:fb:d6:71

  2019/10/01 19:56:38 server: Listening on 0.0.0.0:9001...
created_at: '2019-10-02T01:17:50Z'
updated_at: '2023-05-29T16:48:52Z'
platforms:
  - Linux
  - Windows
tags:
  - tunneling
  - server
verified: true
validated: true
---

# chisel-server-reverse-tunnel

## Command

```bash
./chisel server -p $_LISTEN_PORT --reverse
```

## Description

This command launches the Chisel server in reverse tunneling mode, allowing clients (e.g., on compromised targets) to connect and forward ports back to the server. It is used on the attacker's machine to receive incoming tunnel requests over HTTP/WebSockets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p $_LISTEN_PORT | Port for the server to listen on (e.g., 9001) | Yes |
| --reverse | Enables reverse tunneling mode | Yes |

## Examples

### Basic Usage

```bash
./chisel server -p 9001 --reverse
```

### Advanced Usage

```bash
./chisel server -p 8080 --reverse --auth username:password
```

## Expected Output

Description of what output to expect when the command runs successfully.

```
root@kali:~# ./chisel server -p 9001 --reverse
2019/10/01 19:56:38 server: Reverse tunnelling enabled
2019/10/01 19:56:38 server: Fingerprint 85:91:1f:ed:c1:0b:f4:b5:01:e1:56:8d:d1:fb:d6:71
2019/10/01 19:56:38 server: Listening on 0.0.0.0:9001...
```

The server confirms reverse mode, shows its fingerprint for client verification, and begins listening.

## Related

- [[commands/chisel-client-reverse-port-forward]]
- [[procedures/Remote-Port-Forwarding-Using-Chisel]]
