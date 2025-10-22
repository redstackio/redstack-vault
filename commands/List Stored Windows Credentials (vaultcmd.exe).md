---
id: dedd471b-fa8e-44f8-a1ae-b3a0c4f4275a
name: List Stored Windows Credentials (vaultcmd.exe)
type: command
executor: command_prompt
data: vaultcmd.exe /list
output: "C:\\>vaultcmd.exe /list\nCurrently loaded vaults:\n        Vault: Web Credentials\n\
  \        Vault Guid:4BF4C442-9B8A-41A0-B380-DD4A704DDB28\n        Location: C:\\\
  Users\\Victim\\AppData\\Local\\Microsoft\\Vault\\4BF4C442-9B8A-41A0-B380-DD4A704DDB28\n\
  \n        Vault: Windows Credentials\n        Vault Guid:77BC582B-F0A6-4E15-4E80-61736B6F3B29\n\
  \        Location: C:\\Users\\Victim\\AppData\\Local\\Microsoft\\Vault"
created_at: '2019-12-12T18:42:23.953995+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# List Stored Windows Credentials (vaultcmd.exe)

```command_prompt
vaultcmd.exe /list
```

## Expected Output

```
C:\>vaultcmd.exe /list
Currently loaded vaults:
        Vault: Web Credentials
        Vault Guid:4BF4C442-9B8A-41A0-B380-DD4A704DDB28
        Location: C:\Users\Victim\AppData\Local\Microsoft\Vault\4BF4C442-9B8A-41A0-B380-DD4A704DDB28

        Vault: Windows Credentials
        Vault Guid:77BC582B-F0A6-4E15-4E80-61736B6F3B29
        Location: C:\Users\Victim\AppData\Local\Microsoft\Vault
```
