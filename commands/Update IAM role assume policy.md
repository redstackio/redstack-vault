---
id: 37322e9a-67a0-4989-a72b-116b6ad3baf2
name: Update IAM role assume policy
type: command
executor: bash
data: $ aws iam update-assume-role-policy –role-name role_i_can_assume –policy-document
  file://path/to/assume/role/policy.json
output: null
created_at: '2023-04-06T03:56:09.318650+00:00'
updated_at: '2023-04-10T20:19:54.703524+00:00'
---

# Update IAM role assume policy

```bash
$ aws iam update-assume-role-policy –role-name role_i_can_assume –policy-document file://path/to/assume/role/policy.json
```


