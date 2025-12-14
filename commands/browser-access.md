---
data: '# Manual browser access: Visit http://localhost:3000/ in a web browser'
tags:
  - access
  - trigger
  - xss
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:13.956Z'
id: 79eed344-7be6-4e53-94ae-b09660626972
verified: false
validated: true
submitted: true
---
# browser-access

## Command

```bash
# Manual: Open browser to http://localhost:3000/
# Verification with curl: curl http://localhost:3000/
```

## Description

Accesses the server endpoint in a browser to trigger XSS; curl for non-JS verification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http://localhost:3000/` | Server URL | Yes |

## Examples

### Basic Usage

```bash
# Browser: Navigate to http://localhost:3000/
```

### Advanced Usage

```bash
curl -v http://localhost:3000/'<img src=x onerror=alert(1)>.txt'
```

## Expected Output

Browser: Alert popup; curl: HTML response with unsanitized filename.

## Related

- [[commands/node-start-server]]
