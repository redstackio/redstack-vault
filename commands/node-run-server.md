---
data: node index.js
tags:
  - run
  - server
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: e376963f-ccb2-4dd6-a96e-74112e4808fd
created_at: '2025-12-13T23:56:19.641Z'
updated_at: '2025-12-13T23:56:19.641Z'
verified: false
validated: true
submitted: true
---
# node-run-server

## Command

```bash
node index.js
```

## Description

Executes a Node.js script (index.js) to start an Express server, hosting the malicious iframe page and payload for XSS exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `index.js` | Entry point script file | Yes |

## Examples

### Basic Usage

```bash
node index.js
```

### Advanced Usage

```bash
node index.js --port=3000
```

## Expected Output

Starts server and logs "Server running on port 5000". Listens for incoming requests.

## Related

- [[commands/npm-install-express]]
- [[procedures/Set-Up-Malicious-Express-Server-for-XSS]]
