---
data: node scrap.js
tags:
  - execution
  - nodejs
type: command
output: null
executor: bash
platforms:
  - Node.js
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:02.683Z'
id: 5045d040-3b59-42c8-af13-65f9d41a4abe
verified: false
validated: true
submitted: true
---
# node-run-scrap-js

## Command

```bash
node scrap.js
```

## Description

Executes the scrap.js Node.js script to start an Express server for scraping and rendering metadata, enabling XSS trigger.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| scrap.js | Script file path | Yes |

## Examples

### Basic Usage

```bash
node scrap.js
```

### Advanced Usage

```bash
node --inspect scrap.js
```

## Expected Output

"Server running on port 8080" in terminal, server listening.

## Related

- [[Related Procedure|procedures/Run-the-Vulnerable-Node-js-Application]]
