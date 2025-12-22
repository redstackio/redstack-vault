---
data: sudo npm install -g --unsafe-perm node-red
tags:
  - installation
  - npm
type: command
output: Installation logs and success message for node-red v0.18.4
executor: bash
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.432Z'
id: 3c0230a8-cade-47d8-9a39-ae0aae628b95
verified: false
validated: true
submitted: true
---
# sudo-npm-install-node-red

## Command

```bash
sudo npm install -g --unsafe-perm node-red
```

## Description

This command installs the Node-RED package globally using npm as root, with the unsafe-perm flag to avoid permission restrictions, setting up the vulnerable version for XSS testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `sudo` | Elevates privileges for global install | Yes |
| `-g` | Installs package globally | Yes |
| `--unsafe-perm` | Bypasses npm's permission checks for root | Yes |
| `node-red` | Package name to install (defaults to latest, but context is v0.18.4) | Yes |

## Examples

### Basic Usage

```bash
sudo npm install -g --unsafe-perm node-red
```

### Advanced Usage

```bash
sudo npm install -g --unsafe-perm node-red@0.18.4
```

## Expected Output

Progress logs showing dependency downloads, followed by 'added X packages' and node-red@0.18.4 in global list. No errors indicate success.

## Related

- [[Related Procedure|procedures/Install-Node-RED-for-XSS-Exploitation]]
