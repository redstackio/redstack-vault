---
id: 3c32c7d1-a36b-4263-88f4-d70c52b5ce47
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:09.318725+00:00'
updated_at: '2023-04-10T20:19:54.707071+00:00'
---

# Code Snippet 3c32c7d1

**Language**: Powershell

```powershell
$ aws iam create-policy-version –policy-arn target_policy_arn –policy-document file://path/to/administrator/policy.json –set-as-default
$ aws iam set-default-policy-version –policy-arn target_policy_arn –version-id v2
```
