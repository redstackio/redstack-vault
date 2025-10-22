---
id: 6f84fef7-b4f0-4920-ad0d-294071673c23
name: Test User Credentials
type: command
executor: bash
data: 'powerpick $password = ConvertTo-SecureString "PlainTextPassword" -AsPlainText
  -Force;$cred= New-Object System.Management.Automation.PSCredential ("domain\name",
  $password);

  '
output: null
created_at: '2020-07-14T18:21:10.826474+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Test User Credentials

```bash
powerpick $password = ConvertTo-SecureString "PlainTextPassword" -AsPlainText -Force;$cred= New-Object System.Management.Automation.PSCredential ("domain\name", $password);

```
