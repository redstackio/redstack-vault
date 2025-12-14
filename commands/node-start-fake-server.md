---
id: cmd-node-fake-server
name: node-start-fake-server
type: command
executor: bash
data: node ./index.js YOUR_IP YOUR_PORT
output: Server listening on port YOUR_PORT
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.353Z'
platforms:
  - Linux
tags:
  - server
  - node.js
verified: false
validated: true
submitted: true
---

# node-start-fake-server

## Command

```bash
node ./index.js YOUR_IP YOUR_PORT
```

## Description

Starts the Node.js dummy GitHub API server, serving malicious responses from the prepared index.js file. Replace YOUR_IP with attacker's public IP and YOUR_PORT with the listening port (e.g., 80).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| YOUR_IP | Attacker's public IP address | Yes |
| YOUR_PORT | Port to listen on (e.g., 80) | Yes |

## Examples

### Basic Usage

```bash
node ./index.js 51.75.74.52 80
```

### Advanced Usage

Run in background: `node ./index.js 51.75.74.52 80 &`.

## Expected Output

Console message indicating the server is listening, ready to handle GitLab's API requests.

## Related

- [[procedures/Run-Dummy-GitHub-Server]]
