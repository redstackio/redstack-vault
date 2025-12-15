---
id: cmd-uuid-009
data: 'curl -X POST https://███ -H "████"'
tags:
  - probe
  - header
type: command
output: <UnknownOperationException/>
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.847Z'
verified: false
validated: true
submitted: true
---
# curl-post-with-header

## Command

```bash
curl -X POST https://███ -H "████"
```

## Description

Sends a POST request to a redacted endpoint with a custom header to test operation exceptions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -X POST | HTTP method | Yes |
| -H | Custom header (████) | Yes |
| URL | Redacted endpoint (https://███) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://███ -H "████"
```

### Advanced Usage

```bash
curl -X POST https://███ -H "████" -d '{}'
```

## Expected Output

<UnknownOperationException/>.

## Related

- [[commands/curl-probe-invalid-endpoint]]
- [[procedures/Verify-Post-Mitigation-Endpoint-Validation]]
