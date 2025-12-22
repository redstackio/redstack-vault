---
id: 7acf1940-a5ba-4954-b741-41143b4ddc3d
name: AWS-IAM-Full-Access-Policy
type: code
language: json
verified: true
created_at: '2023-04-06T03:56:10.516391+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - iam
  - policy
  - escalation
validated: true
---

# AWS-IAM-Full-Access-Policy

## Code

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "*"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

## Description

This JSON defines a customer-managed IAM policy that grants unrestricted access to all AWS services and resources via wildcard (*) permissions. It is used in privilege escalation scenarios to create an administrative policy when partial IAM write permissions are available.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (None) | This is a static policy; customize Action or Resource arrays for narrower scope if needed | N/A |

## Usage

Save as a .json file and reference in AWS CLI commands like create-policy: aws iam create-policy --policy-name AdminPolicy --policy-document file://this-file.json. Attach to a user/role for immediate escalation. Used in procedures like [[procedures/AWS-Privilege-Escalation-via-Creating-Admin-Policy]] after discovering permissions.

## Detection

- CloudTrail logs for iam:CreatePolicy or iam:AttachUserPolicy events with wildcard policies.
- IAM Access Analyzer alerts on broad permissions.
- Anomalous API calls from compromised credentials creating *:* policies.

## Related

- [[procedures/AWS-Privilege-Escalation-via-Creating-Admin-Policy]]
- [[tools/AWS-CLI]]
