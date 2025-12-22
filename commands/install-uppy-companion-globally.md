---
data: sudo npm install -g @uppy/companion
tags:
  - installation
  - npm
type: command
output: null
executor: bash
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.559Z'
id: 647335ba-5173-4352-82bb-a718b02f90dc
verified: false
validated: true
submitted: true
---
# install-uppy-companion-globally

## Command

```bash
sudo npm install -g @uppy/companion
```

## Description

This command installs the Uppy Companion server package globally using npm, making the 'companion' executable available for running the SSRF-vulnerable proxy server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `sudo` | Runs with elevated privileges for global install | Yes (on Linux/macOS) |
| `-g` | Installs package globally | Yes |
| `@uppy/companion` | The npm package name for Uppy Companion | Yes |

## Examples

### Basic Usage

```bash
sudo npm install -g @uppy/companion
```

### Advanced Usage

```bash
sudo npm install -g @uppy/companion@1.8.0
```

## Expected Output

Installation success message, e.g., "+ @uppy/companion@1.8.0\nadded 50 packages from 30 contributors and audited 100 packages in 5s". No errors indicate readiness to run.

## Related

- [[commands/start-uppy-companion-server]]
- [[procedures/Deploy-Uppy-Companion-Server]]
