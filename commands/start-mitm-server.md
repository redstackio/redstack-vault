---
id: cmd-start-mitm-001
name: start-mitm-server
type: command
executor: bash
data: sudo node server.js
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.757Z'
platforms:
  - macOS
tags:
  - mitm
  - node-js
verified: false
validated: true
submitted: true
---

# start-mitm-server

## Command

```bash
sudo node server.js
```

## Description

This command starts a Node.js-based MITM proxy server script (server.js) with elevated privileges to intercept and modify traffic for domains like maps.googleapis.com, injecting malicious HTML for the Brave DnD exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `sudo` | Elevates privileges for port binding (e.g., 80/443) | Yes |
| `node` | Node.js runtime (v7.9.0) to execute the script | Yes |
| `server.js` | The MITM server script handling proxy and injection logic | Yes |

## Examples

### Basic Usage

```bash
sudo node server.js
```

### Advanced Usage

If script accepts args (e.g., port):
```bash
sudo node server.js --port 8080
```

## Expected Output

Server startup logs, e.g., "MITM server running, ready to proxy requests to maps.googleapis.com". No errors; confirm with curl to redirected domain showing injected content.

## Related

- [[procedures/Start-MITM-Server-for-Brave-DnD-Attack]]
