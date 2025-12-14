---
id: cmd-uuid-008
data: curl █████
tags:
  - probe
  - mitigation
type: command
output: >-
  <ValidationException> <Message>400 ERROR: Invalid Endpoint</Message>
  </ValidationException>
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.849Z'
verified: false
validated: true
submitted: true
---
# curl-probe-invalid-endpoint

## Command

```bash
curl █████
```

## Description

Probes a redacted AWS SSM endpoint to check for validation errors post-mitigation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Redacted endpoint (█████) | Yes |

## Examples

### Basic Usage

```bash
curl █████
```

### Advanced Usage

```bash
curl -v █████
```

## Expected Output

XML ValidationException indicating invalid endpoint.

## Related

- [[commands/curl-post-with-header]]
- [[procedures/Verify-Post-Mitigation-Endpoint-Validation]]
