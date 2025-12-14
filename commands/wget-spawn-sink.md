---
id: uuid-wget-spawn
data: >-
  spawn('wget', [url, '-O', dest, '-q'], {stdio:'inherit', env: process.env,
  shell:true})
tags:
  - sink
  - vulnerability
  - spawn
type: command
output: 'Download or error, but injected commands in URL execute'
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.535Z'
verified: false
validated: true
submitted: true
---
# wget-spawn-sink

## Command

```bash
spawn('wget', [url, '-O', dest, '-q'], {stdio:'inherit', env: process.env, shell:true})
```

## Description

Node.js child_process.spawn for downloading remote tar.gz in TAR.js, vulnerable to injection from unsanitized URL due to shell:true.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | Unsanitized user-provided URL | Yes |
| `-O` | Output to dest file | Yes |
| `dest` | Target download path | Yes |
| `-q` | Quiet mode | Yes |
| `shell: true` | Enables Bash interpretation of URL | Yes |

## Examples

### Basic Usage

```javascript
child_process.spawn('wget', ['http://example.com/file.tar.gz', '-O', '/tmp/file'], {shell: true});
```

### Advanced Usage

```javascript
spawn('wget', ['http://evil;whoami;', '-O', '/tmp/file'], {shell: true});
```

## Expected Output

Wget downloads file to dest quietly; if URL has ;commands, they execute post-download attempt, inheriting stdio.

## Related

- [[procedures/Exploit-PM2-Remote-URL-Command-Injection]]
- [[commands/remote-url-payload]]
