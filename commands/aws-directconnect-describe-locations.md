---
type: command
executor: bash
data: aws directconnect describe-locations
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - aws
  - directconnect
  - discovery
verified: true
validated: true
---

# aws-directconnect-describe-locations

## Command

```bash
aws directconnect describe-locations
```

## Description

Queries AWS Direct Connect to list available locations for connection endpoints. Use this to verify permissions for Direct Connect service discovery, often tested in IAM enumeration to check network infrastructure access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | No additional parameters; uses default AWS credentials | No |

## Examples

### Basic Usage

```bash
aws directconnect describe-locations
```

### With Output Format

```bash
aws directconnect describe-locations --output table
```

## Expected Output

JSON with locations array, e.g., {"locations": [{"locationCode": "EQ5", "locationName": "Equinix Ashburn"}]}. AccessDenied error if permissions lacking.

## Related

- [[procedures/AWS-IAM-Permissions-Enumeration]]
