---
data: aws datazone list-domains --endpoint-url ENDPOINT_URL
tags:
  - aws
  - datazone
  - api
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 67264b63-882c-49bb-b752-0cb8266bf790
created_at: '2025-12-14T17:32:39.215Z'
updated_at: '2025-12-14T17:32:39.215Z'
verified: false
validated: true
submitted: true
---
# AWS Datazone List Domains

## Command

```bash
aws datazone list-domains --endpoint-url ENDPOINT_URL
```

## Description

Uses AWS CLI to call the Datazone service's list-domains operation, overriding the endpoint to a custom (non-production) URL for permission testing and enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--endpoint-url` | Custom URL for the API endpoint (e.g., non-prod Datazone URL) | Yes |
| `datazone list-domains` | Built-in AWS CLI operation to retrieve domains | Yes |

## Examples

### Basic Usage with Non-Prod Endpoint

```bash
aws datazone list-domains --endpoint-url https://nonprod-datazone.example.amazonaws.com
```

### With Profile (Admin)

```bash
export AWS_PROFILE=admin\naws datazone list-domains --endpoint-url [redacted]
```

## Expected Output

For admin: 'An error occurred (AccessDeniedException) when calling the ListDomains operation: Invalid endpoint or operation type'. For noperm: Detailed denial with ARN and action. No CloudTrail log in both cases.

## Related

- [[commands/export-aws-profile]]
- [[procedures/Test-Non-Production-Endpoint-with-Limited-Credentials]]
