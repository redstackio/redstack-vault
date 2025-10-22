---
id: f42abda6-c23d-4648-84ec-b69a8d60da45
name: Disable Windows Firewall (Windows 7+)
type: command
executor: command_prompt
data: netsh advfirewall set allprofiles state off
output: 'C:\>netsh advfirewall set allprofiles state off

  Ok.'
created_at: '2019-11-15T01:22:12.204907+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Disable Windows Firewall (Windows 7+)

```command_prompt
netsh advfirewall set allprofiles state off
```

## Expected Output

```
C:\>netsh advfirewall set allprofiles state off
Ok.
```
