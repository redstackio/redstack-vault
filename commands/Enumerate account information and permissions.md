---
id: 8aa20aa2-a17f-4d65-b9f3-99c03b989469
name: Enumerate account information and permissions
type: command
executor: bash
data: 'run iam__enum_users_roles_policies_groups

  run iam__enum_permissions

  whoami

  '
output: null
created_at: '2020-07-14T19:06:15.108732+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Enumerate account information and permissions

```bash
run iam__enum_users_roles_policies_groups
run iam__enum_permissions
whoami

```
