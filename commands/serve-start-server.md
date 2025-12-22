---
data: ./node_modules/serve/bin/serve.js
tags:
  - server
  - start
type: command
executor: bash
platforms:
  - Node.js
id: 3a1e3c90-2c8f-4ca4-842c-435fb130e14e
created_at: '2025-12-14T03:15:41.874Z'
updated_at: '2025-12-14T03:15:41.874Z'
verified: false
validated: true
submitted: true
---
# serve-start-server

## Command

```bash
./node_modules/serve/bin/serve.js
```

## Description

Executes the serve module's binary to start a static HTTP server on port 3000, serving the current directory and enabling vulnerable directory listings.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Runs with defaults (port 3000, localhost) | N/A |

## Examples

### Basic Usage

```bash
./node_modules/serve/bin/serve.js
```

### Advanced Usage

```bash
./node_modules/serve/bin/serve.js -p 5000
```

## Expected Output

"Serving!" and "http://127.0.0.1:3000" listening message.

## Related

- [[Related Procedure|procedures/Start-Serve-Server]]
