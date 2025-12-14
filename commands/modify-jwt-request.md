---
id: cmd-3371448-modify-jwt
data: >-
  sed 's/Bearer <ADMIN_JWT>/Bearer <EDITOR_JWT>/g' captured_request.txt >
  modified_request.txt
tags:
  - request-modification
  - sed
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.411Z'
verified: false
validated: true
submitted: true
---
# modify-jwt-request

## Command

```bash
sed 's/Bearer <ADMIN_JWT>/Bearer <EDITOR_JWT>/g' captured_request.txt > modified_request.txt
```

## Description

Uses sed to replace the admin JWT token in a captured request file with an Editor token, preparing it for replay.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `captured_request.txt` | Input file with original request | Yes |
| `<ADMIN_JWT>` / `<EDITOR_JWT>` | Tokens to swap | Yes |

## Examples

### Basic Usage

```bash
sed 's/Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.../Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.../g' request.txt > new.txt
```

### Advanced Usage

Multiple replacements if needed:

```bash
sed -e 's/old_token/new_token/g' -e 's/other/old/g' input.txt > output.txt
```

## Expected Output

Modified file with updated Authorization header.

## Related

- [[commands/analyze-api-request]]
- [[procedures/Capture-and-Replay-API-Request]]
