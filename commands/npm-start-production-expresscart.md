---
id: cmd-005
data: npm start --production
tags:
  - npm
  - start
  - server
type: command
output: null
executor: bash
platforms:
  - Node.js
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:27:23.105Z'
verified: false
validated: true
submitted: true
---
# npm-start-production-expresscart

## Command

```bash
npm start --production
```

## Description

Starts the express-cart server in production mode, binding to port 1111 and requiring a running MongoDB instance for database operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --production | Runs in production environment | Yes |

## Examples

### Basic Usage

```bash
npm start --production
```

### Advanced Usage

```bash
npm start --production --port 8080
```

## Expected Output

Server running on http://localhost:1111. MongoDB connection established.

## Related

- [[commands/npm-install-expresscart]]
- [[procedures/Local-Setup-of-Express-Cart-Application]]
