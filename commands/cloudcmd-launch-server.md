---
id: cmd-uuid-2
data: ./node_modules/cloudcmd/bin/cloudcmd.js --root .
tags:
  - server-launch
  - web
type: command
output: 'Server startup message, listening on http://127.0.0.1:8080/'
executor: bash
platforms:
  - Node.js
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:31.030Z'
verified: false
validated: true
submitted: true
---
# cloudcmd-launch-server

## Command

```bash
./node_modules/cloudcmd/bin/cloudcmd.js --root .
```

## Description

Launches the CloudCMD web file manager server with the current directory as the root, exposing the vulnerable interface.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --root | Sets the root directory for file management | Yes |
| . | Current directory as root | Yes |

## Examples

### Basic Usage

```bash
./node_modules/cloudcmd/bin/cloudcmd.js --root .
```

### Advanced Usage

```bash
./node_modules/cloudcmd/bin/cloudcmd.js --root /path/to/dir --port 3000
```

## Expected Output

CloudCmd v9.1.5
http://127.0.0.1:8080

## Related

- [[commands/npm-i-cloudcmd]]
