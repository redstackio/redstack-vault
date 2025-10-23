---
id: d2b911dd-951d-447b-b7e3-49b3faaf7b3f
name: Create new policy version and set as default
type: command
executor: bash
data: '$ aws iam create-policy-version –policy-arn target_policy_arn –policy-document
  file://path/to/administrator/policy.json –set-as-default

  $ aws iam set-default-policy-version –policy-arn target_policy_arn –version-id v2'
output: null
created_at: '2023-04-06T03:56:09.318776+00:00'
updated_at: '2023-04-10T20:19:54.703524+00:00'
---

# Create new policy version and set as default

```bash
$ aws iam create-policy-version –policy-arn target_policy_arn –policy-document file://path/to/administrator/policy.json –set-as-default
$ aws iam set-default-policy-version –policy-arn target_policy_arn –version-id v2
```


