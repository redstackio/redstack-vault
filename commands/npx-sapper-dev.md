---
id: cmd-004
data: npx sapper dev
tags:
  - server
  - dev
type: command
output: 'Sapper app running at http://localhost:3000'
executor: bash
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.531Z'
verified: false
validated: true
submitted: true
---
---

# npx-sapper-dev

## Command

```bash
npx sapper dev
```

## Description

Starts the Sapper development server on port 3000, exposing the vulnerable /client/ endpoint for path traversal testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `dev` | Development mode | Yes |
| `sapper` | Sapper CLI | Yes |

## Examples

### Basic Usage

```bash
npx sapper dev
```

### Advanced Usage

```bash
npx sapper dev --port 4000
```

## Expected Output

Server startup message with URL.

## Related

- [[Related Procedure: Exploit-Path-Traversal-in-Development-Mode]]

---
