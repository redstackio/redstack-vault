---
id: 45cc73fe-787e-4178-85b5-0659c0da8f38
name: Or this way sometimes gets around MFA restrictions
type: command
executor: bash
data: '$credential = Get-Credential

  Connect-MsolService -Credential $credential

  '
output: null
created_at: '2020-07-14T19:07:50.919941+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Or this way sometimes gets around MFA restrictions

```bash
$credential = Get-Credential
Connect-MsolService -Credential $credential

```
