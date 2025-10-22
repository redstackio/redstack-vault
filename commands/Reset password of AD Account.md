---
id: f352d7c7-1c4f-407f-b1b0-c0095d9b2f48
name: Reset password of AD Account
type: command
executor: bash
data: 'Set-ADAccountPassword -Identity administrator -Reset -NewPassword (ConvertTo-SecureString
  -AsPlainText "Password1" -Force)

  '
output: null
created_at: '2020-07-15T19:05:44.363610+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Reset password of AD Account

```bash
Set-ADAccountPassword -Identity administrator -Reset -NewPassword (ConvertTo-SecureString -AsPlainText "Password1" -Force)

```
