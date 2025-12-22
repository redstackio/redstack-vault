---
id: 9e470e5b-7bc9-4121-ba3b-1632f7052640
type: code
name: aws-iam-admin-policy-json-snippet
language: json
verified: true
created_at: '2023-04-06T03:56:09.317515+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - policy
  - iam
validated: true
---

# aws-iam-admin-policy-json-snippet

## Code

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "*",
      "Resource": "*"
    }
  ]
}
```

## Description

This JSON snippet defines a full administrator policy allowing all actions on all resources, used for inline IAM policies to achieve shadow admin access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | Full wildcard policy; no variables | N/A |

## Usage

Save as policy.json and reference in put-user-policy or similar commands to grant unrestricted access. Embed in Lambda or role updates for escalation.

## Detection

- CloudTrail logs for PutUserPolicy or CreatePolicyVersion with wildcard statements.
- IAM Access Analyzer alerts on excessive permissions.

## Related

- [[procedures/AWS-Shadow-Admin-Access]]
