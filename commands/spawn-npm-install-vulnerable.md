---
data: >-
  spawn(cst.IS_WINDOWS ? 'npm.cmd' : 'npm', ['install', module_name,
  '--loglevel=error', '--prefix', '"' + install_path + '"'], {stdio: 'inherit',
  env: process.env, shell: true})
tags:
  - sink
  - vulnerable
type: command
output: Executes injected commands and installs the module if valid
executor: javascript
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.402Z'
id: e5fd26fc-f6bc-4e50-a9db-3ae73186aca0
verified: false
validated: true
submitted: true
---
# spawn-npm-install-vulnerable

## Command

```javascript
spawn(cst.IS_WINDOWS ? 'npm.cmd' : 'npm', ['install', module_name, '--loglevel=error', '--prefix', '"' + install_path + '"'], {stdio: 'inherit', env: process.env, shell: true})
```

## Description

The execution sink in PM2's continueInstall() function, spawning npm install with unsanitized module_name, enabling injection due to shell: true.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `install` | NPM install action | Yes |
| `--prefix` | Installation directory | Yes |
| `module_name` | Unsanitized payload (e.g., 'test;pwd;') | Yes |
| `--loglevel=error` | Suppresses NPM logs | Yes |

## Examples

### Basic Usage

```javascript
// Internal PM2 call
spawn('npm', ['install', 'test', '--loglevel=error'], {shell: true});
```

### Advanced Usage

```javascript
// With injection
spawn('npm', ['install', 'test;id;', '--loglevel=error', '--prefix', '/tmp'], {shell: true});
```

## Expected Output

Inherits stdio: NPM output, executed commands (e.g., id output), module install if valid, errors suppressed except critical.

## Related

- [[commands/pm2-install-payload]]
- [[procedures/Exploit-PM2-API-Command-Injection]]
