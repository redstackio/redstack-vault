---
id: cmd-uuid-1
data: node ./index.js YOUR_IP YOUR_PORT
tags:
  - setup
  - server
type: command
output: Server listening on port YOUR_PORT
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:19.871Z'
verified: false
validated: true
submitted: true
---
# node-dummy-github-server

## Command

```bash
node ./index.js YOUR_IP YOUR_PORT
```

## Description

Runs a Node.js script to start a dummy GitHub server serving malicious labels for GitLab import exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| YOUR_IP | IP address to bind (public for access) | Yes |
| YOUR_PORT | Port to listen on (e.g., 80) | Yes |

## Examples

### Basic Usage

```bash
node ./index.js 192.168.1.100 3000
```

### Advanced Usage

```bash
node ./index.js 51.75.74.52 80
```

## Expected Output

Console output: "Server running and accessible at http://YOUR_IP:YOUR_PORT". Test with curl to /api/v3/repos/repo_id/labels.

## Related

- [[Related Procedure|procedures/Set-Up-Dummy-GitHub-Server-for-Malicious-Labels]]
