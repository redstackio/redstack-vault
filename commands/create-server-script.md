---
data: >-
  echo "const tianma = require('tianma-static');\ntianma.serve(__dirname,
  3000);" > server.js
tags:
  - script-creation
  - node-js
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:13.965Z'
id: 486503e8-aa0e-41e6-b497-cbf57033a216
verified: false
validated: true
submitted: true
---
# create-server-script

## Command

```bash
echo "const tianma = require('tianma-static');\ntianma.serve(__dirname, 3000);" > server.js
```

## Description

Generates a Node.js script to start the tianma-static server on port 3000.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo ... > server.js` | Script content and output file | Yes |

## Examples

### Basic Usage

```bash
echo "const tianma = require('tianma-static');\ntianma.serve(__dirname, 3000);" > server.js
```

### Advanced Usage

```bash
cat > server.js << EOF\nconst tianma = require('tianma-static');\ntianma.serve(__dirname, 8080);\nEOF
```

## Expected Output

server.js file created; cat server.js shows the code.

## Related

- [[commands/node-start-server]]
