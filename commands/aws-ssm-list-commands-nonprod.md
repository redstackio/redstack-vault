---
id: cmd-uuid-007
data: 'aws ssm list-commands --endpoint-url https://███████'
tags:
  - aws
  - ssm
  - mitigated
type: command
output: ValidationException for both privileged and unprivileged
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.852Z'
verified: false
validated: true
submitted: true
---
# aws-ssm-list-commands-nonprod

## Command

```bash
aws ssm list-commands --endpoint-url https://███████
```

## Description

Lists SSM commands on non-production endpoint, post-mitigation showing ValidationException.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --endpoint-url | Non-production URL (https://███████) | Yes |

## Examples

### Basic Usage

```bash
aws ssm list-commands --endpoint-url https://███████
```

### Advanced Usage

```bash
aws ssm list-commands --endpoint-url https://███████ --filters Key=InvokedAfter,Values=2023-01-01T00:00:00Z
```

## Expected Output

ValidationException: 400 ERROR: Invalid Endpoint.

## Related

- [[procedures/Test-Additional-SSM-Actions-for-Silent-Enumeration]]
