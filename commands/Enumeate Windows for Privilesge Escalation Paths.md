---
id: fa48b57a-9708-4e9f-91f9-30784dcec9e9
name: Enumeate Windows for Privilesge Escalation Paths
type: command
executor: command_prompt
data: winPEAS.exe
output: 'PS C:\Windows\Tasks> .\winPEAS.exe

  Creating Dynamic lists, this could take a while, please wait...[0m

  - Checking if domain...[0m

  - Getting Win32_UserAccount info...[0m

  - Creating current user groups list...[0m

  - Creating active users list...[0m

  - Creating disabled users list...[0m

  - Admin users list...[0m

  ...'
created_at: '2020-03-12T23:11:13.796632+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[ps]]'
- '[[winPEAS]]'
---

# Enumeate Windows for Privilesge Escalation Paths

```command_prompt
winPEAS.exe
```

## Expected Output

```
PS C:\Windows\Tasks> .\winPEAS.exe
Creating Dynamic lists, this could take a while, please wait...[0m
- Checking if domain...[0m
- Getting Win32_UserAccount info...[0m
- Creating current user groups list...[0m
- Creating active users list...[0m
- Creating disabled users list...[0m
- Admin users list...[0m
...
```


