---
data: ./node_modules/statics-server/index.js
tags:
  - server
  - execution
type: command
output: '服务器已经启动 访问localhost:8080 (Server started, access localhost:8080)'
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:37.202Z'
id: 6c045370-a745-4419-8acc-166a66167af9
verified: false
validated: true
submitted: true
---
# run-statics-server

## Command

```bash
./node_modules/statics-server/index.js
```

## Description

Runs the statics-server script to start a static file server on the current directory, listening on port 8080, enabling the vulnerable directory listing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `./node_modules/statics-server/index.js` | Path to the executable script | Yes |

## Examples

### Basic Usage

```bash
./node_modules/statics-server/index.js
```

### Advanced Usage

```bash
node ./node_modules/statics-server/index.js --port 8080
```

## Expected Output

Server startup message indicating it's listening on localhost:8080.

## Related

- [[Related Procedure]]
