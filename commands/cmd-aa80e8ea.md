---
id: aa80e8ea-af4c-47bb-813a-7840c4590fac
name: cmd-aa80e8ea
type: command
executor: bash
data: '$Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force

  $Cred = New-Object -TypeName System.Management.Automation.PSCredential -Argument
  "$_USER", $Pass'
output: ''
created_at: '2023-03-13T19:52:35.078857+00:00'
updated_at: '2023-03-14T01:17:35.768642+00:00'
---

# Command aa80e8ea

```bash
$Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
$Cred = New-Object -TypeName System.Management.Automation.PSCredential -Argument "$_USER", $Pass
```
