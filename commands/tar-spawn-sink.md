---
id: uuid-tar-spawn
data: >-
  spawn('tar', ['zxf', module_filepath, '-C', install_path, '--strip-components
  1'], {stdio:'inherit', env: process.env, shell:true})
tags:
  - sink
  - vulnerability
  - spawn
type: command
output: >-
  Tar extraction or error, but injected commands execute if present in
  module_filepath
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.538Z'
verified: false
validated: true
submitted: true
---
# tar-spawn-sink

## Command

```bash
spawn('tar', ['zxf', module_filepath, '-C', install_path, '--strip-components 1'], {stdio:'inherit', env: process.env, shell:true})
```

## Description

Node.js child_process.spawn call in TAR.js for extracting local tar.gz, vulnerable to injection due to shell:true and unsanitized module_filepath.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `zxf` | Gzip extract flags | Yes |
| `module_filepath` | Unsanitized user input path | Yes |
| `-C` | Change to install_path | Yes |
| `install_path` | Target extraction directory | Yes |
| `--strip-components 1` | Strip leading directories | Yes |
| `shell: true` | Enables Bash metacharacter interpretation | Yes |

## Examples

### Basic Usage

```javascript
child_process.spawn('tar', ['zxf', 'file.tar.gz', '-C', '/tmp'], {shell: true});
```

### Advanced Usage

```javascript
spawn('tar', ['zxf', 'malicious;rm -rf /', '-C', '/tmp'], {shell: true});
```

## Expected Output

Tar extracts files if valid; errors on invalid path, but any injected commands after ; in filepath execute via Bash.

## Related

- [[procedures/Exploit-PM2-CLI-Command-Injection]]
- [[commands/pm2-install-cli-injection]]
