---
id: e9d9221d-da65-41df-81f3-91835a3d1037
name: List Local Windows Users
type: command
executor: command_prompt
data: net user
output: 'PS C:\ > net user

  User accounts for \\DESKTOP-29CSGFA

  -------------------------------------------------------------------------------

  Administrator            Bob                      DefaultAccount

  Guest                    Alice                    WDAGUtilityAccount

  The command completed successfully.'
created_at: '2020-03-18T01:08:37.458677+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# List Local Windows Users

```command_prompt
net user
```

## Expected Output

```
PS C:\ > net user

User accounts for \\DESKTOP-29CSGFA

-------------------------------------------------------------------------------
Administrator            Bob                      DefaultAccount
Guest                    Alice                    WDAGUtilityAccount
The command completed successfully.
```
