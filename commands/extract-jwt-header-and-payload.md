---
type: command
executor: bash
data: >-
  echo "Header: $(echo $_JWT | cut -d. -f1 | base64 -d 2>/dev/null)" && echo
  "Payload: $(echo $_JWT | cut -d. -f2 | base64 -d 2>/dev/null)"
output: null
platforms:
  - Linux
tags:
  - jwt
  - decoding
verified: true
validated: true
---

# extract-jwt-header-and-payload

## Command

```bash
echo "Header: $(echo $_JWT | cut -d. -f1 | base64 -d 2>/dev/null)" && echo "Payload: $(echo $_JWT | cut -d. -f2 | base64 -d 2>/dev/null)"
```

## Description

This command decodes and displays the header and payload sections of a JWT token in readable JSON format, excluding the signature. Use it during reconnaissance to inspect token structure before forging.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_JWT | The full JWT token string (e.g., eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...) | Yes |

## Examples

### Basic Usage

```bash
echo "Header: $(echo 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ' | cut -d. -f1 | base64 -d 2>/dev/null)" && echo "Payload: $(echo 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ' | cut -d. -f2 | base64 -d 2>/dev/null)"
```

## Expected Output

Header: {"alg":"HS256","typ":"JWT"}
Payload: {"sub":"1234567890","name":"John Doe","iat":1516239022}

This shows the decoded JSON; use jq for prettier formatting if available.
