---
id: cmd-001
data: node calculate_authpw.js --email $EMAIL --password $PASSWORD
tags:
  - hash-computation
  - pbkdf2
type: command
output: Base64-encoded authPW string
executor: bash
platforms:
  - Linux
  - macOS
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.081Z'
verified: false
validated: true
submitted: true
---
# compute-authpw-script

## Command

```bash
node calculate_authpw.js --email $EMAIL --password $PASSWORD
```

## Description

Executes a Node.js/TypeScript script to compute the authPW using PBKDF2 based on Mozilla's fxa-auth-client logic, taking email and password as inputs to derive a base64-encoded hash for API authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--email` | Victim's email address (lowercased) | Yes |
| `--password` | Plaintext password from leak | Yes |

## Examples

### Basic Usage

```bash
node calculate_authpw.js --email victim@example.com --password password123
```

### Advanced Usage

```bash
node calculate_authpw.js --email victim@example.com --password 'complex$pass123' --iterations 1000
```

## Expected Output

A single line with the base64 authPW, e.g., "v0+authpw_hash==". Errors if inputs invalid.

## Related

- [[Related Procedure: Compute-AuthPW-from-Password]]
