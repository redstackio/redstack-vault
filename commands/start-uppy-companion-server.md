---
data: companion --config conf.json
tags:
  - server-start
  - npm
type: command
output: null
executor: bash
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.556Z'
id: 85a72670-1320-4c48-8fc8-881313f657fe
verified: false
validated: true
submitted: true
---
# start-uppy-companion-server

## Command

```bash
companion --config conf.json
```

## Description

This command launches the Uppy Companion server using a specified JSON configuration file, binding to a host/port and enabling features like debug mode for SSRF exploitation testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--config` | Path to JSON config file (e.g., with server host/port, debug: true) | Yes |
| `conf.json` | Example config file name | Yes |

## Examples

### Basic Usage

```bash
companion --config conf.json
```

### Advanced Usage

```bash
companion --config conf.json --secret mysecret
```

## Expected Output

Server startup logs: "Debug mode enabled", "Companion is running on http://localhost:3020". Listens for requests until interrupted.

## Related

- [[commands/install-uppy-companion-globally]]
- [[procedures/Deploy-Uppy-Companion-Server]]
