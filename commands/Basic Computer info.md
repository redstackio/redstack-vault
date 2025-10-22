---
id: 23ff215f-6e1c-433a-970c-6d6b8b49a6f6
name: Basic Computer info
type: command
executor: bash
data: 'Get-NetComputer | select samaccountname, operatingsystem, description

  '
output: null
created_at: '2020-07-15T19:06:26.863865+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Basic Computer info

```bash
Get-NetComputer | select samaccountname, operatingsystem, description

```
