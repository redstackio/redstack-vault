---
id: de456e79-1bac-43e5-b912-abe1fcd13391
name: Create IAM User Policy
type: command
executor: bash
data: $ aws iam put-user-policy –user-name my_username –policy-name my_inline_policy
  –policy-document file://path/to/administrator/policy.json
output: null
created_at: '2023-04-06T03:56:09.318405+00:00'
updated_at: '2023-04-10T20:19:54.703524+00:00'
---

# Create IAM User Policy

```bash
$ aws iam put-user-policy –user-name my_username –policy-name my_inline_policy –policy-document file://path/to/administrator/policy.json
```
