---
id: a5199a28-d174-4c04-a408-e1789b6bd590
name: Change Domain User Password
type: command
executor: bash
data: '$NewPassword = ConvertTo-SecureString ''Password123!'' -AsPlainText -Force

  Set-DomainUserPassword -Identity ''TargetUser'' -AccountPassword $NewPassword'
output: null
created_at: '2023-04-06T03:56:06.985221+00:00'
updated_at: '2023-04-10T20:26:31.595504+00:00'
---

# Change Domain User Password

```bash
$NewPassword = ConvertTo-SecureString 'Password123!' -AsPlainText -Force
Set-DomainUserPassword -Identity 'TargetUser' -AccountPassword $NewPassword
```


