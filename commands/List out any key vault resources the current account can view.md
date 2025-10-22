---
id: 292e7a82-4b4e-46a1-9d88-44d76d16cc38
name: List out any key vault resources the current account can view
type: command
executor: bash
data: 'az keyvault list –query ''[].name'' --output tsv

  '
output: null
created_at: '2020-07-14T19:07:50.923564+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# List out any key vault resources the current account can view

```bash
az keyvault list –query '[].name' --output tsv

```
