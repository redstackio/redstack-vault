---
data: node ./node_modules/webpack-bundle-analyzer/lib/bin/analyzer.js poc.json
tags:
  - execution
  - node
  - analyzer
type: command
output: >-
  Webpack Bundle Analyzer is started at http://127.0.0.1:8888\nUse Ctrl+C to
  close it
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:36.947Z'
id: 7037c2b0-13f0-4fef-93a1-f86f1d91d4a3
verified: false
validated: true
submitted: true
---
# node-run-analyzer

## Command

```bash
node ./node_modules/webpack-bundle-analyzer/lib/bin/analyzer.js poc.json
```

## Description

Executes the webpack-bundle-analyzer binary using Node.js on a provided stats JSON file (e.g., poc.json), starting a local HTTP server to visualize the bundle and trigger XSS if malicious.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `./node_modules/webpack-bundle-analyzer/lib/bin/analyzer.js` | Path to analyzer script | Yes |
| `poc.json` | Path to webpack stats JSON file with payload | Yes |

## Examples

### Basic Usage

```bash
node ./node_modules/webpack-bundle-analyzer/lib/bin/analyzer.js poc.json
```

### Advanced Usage

```bash
node ./node_modules/webpack-bundle-analyzer/lib/bin/analyzer.js --port 8889 stats.json
```

## Expected Output

Webpack Bundle Analyzer is started at http://127.0.0.1:8888
Use Ctrl+C to close it

## Related

- [[commands/npm-run-build]]
- [[procedures/Run-Analyzer-on-Malicious-JSON]]
