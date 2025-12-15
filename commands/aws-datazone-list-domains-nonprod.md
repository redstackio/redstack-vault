---
data: aws datazone list-domains --endpoint-url <redacted>
tags:
  - aws
  - datazone
  - bypass
type: command
executor: bash
platforms:
  - AWS
id: 41526a9f-6c84-41a1-8cef-7acadf51cd29
created_at: '2025-12-14T17:32:39.025Z'
updated_at: '2025-12-14T17:32:39.025Z'
verified: false
validated: true
submitted: true
---
# aws-datazone-list-domains-nonprod

## Command

```bash
aws datazone list-domains --endpoint-url <redacted>
```

## Description

Lists domains using a non-production endpoint, bypassing CloudTrail logging while enforcing IAM permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --endpoint-url | Non-production URL (redacted, e.g., test aliases) | Yes |

## Examples

### Basic Usage

```bash
aws datazone list-domains --endpoint-url https://datazone-test.example.amazonaws.com
```

### With Profile

```bash
AWS_PROFILE=admin aws datazone list-domains --endpoint-url <redacted>
```

## Expected Output

Success: Domain list JSON; Denial: AccessDeniedException. No CloudTrail log.

## Related

- [[commands/aws-datazone-list-domains]]
- [[procedures/Test-Non-Production-Datazone-Endpoint]]
