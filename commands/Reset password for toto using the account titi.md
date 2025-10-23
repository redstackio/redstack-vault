---
id: c491df2a-a440-49d5-ae88-d966131d4832
name: Reset password for toto using the account titi
type: command
executor: bash
data: Add-ObjectACL -TargetSamAccountName toto -PrincipalSamAccountName titi -Rights
  ResetPassword
output: null
created_at: '2023-04-06T03:56:06.430393+00:00'
updated_at: '2023-04-10T20:26:37.633229+00:00'
---

# Reset password for toto using the account titi

```bash
Add-ObjectACL -TargetSamAccountName toto -PrincipalSamAccountName titi -Rights ResetPassword
```


