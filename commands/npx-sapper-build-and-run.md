---
id: cmd-006
data: npx sapper build && node __sapper__build
tags:
  - build
  - prod
type: command
output: |-
  Build complete.
  Listening on http://localhost:3000
executor: bash
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.523Z'
verified: false
validated: true
submitted: true
---
---

# npx-sapper-build-and-run

## Command

```bash
npx sapper build && node __sapper__build
```

## Description

Builds the Sapper project for production and starts the server using the generated entry point, enabling Polka-based serving vulnerable to traversal.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `build` | Build mode | Yes |
| `&&` | Command chaining | Yes |
| `node` | Execute JS runtime | Yes |
| `__sapper__build` | Prod entry | Yes |

## Examples

### Basic Usage

```bash
npx sapper build && node __sapper__build
```

### Advanced Usage

```bash
npx sapper build --legacy && node __sapper__build
```

## Expected Output

Build logs followed by server startup.

## Related

- [[Related Procedure: Exploit-Path-Traversal-in-Production-Mode]]

---
