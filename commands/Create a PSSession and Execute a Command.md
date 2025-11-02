---
id: e4783fd1-fd34-4265-8a6b-746afdca0338
name: Create a PSSession and Execute a Command
type: command
executor: bash
data: '$Session = New-PSSession -ComputerName $_TARGET_IP -Credential $Cred

  Invoke-Command -Session $Session -ScriptBlock {Start-Process $_CMD}'
output: 'PS C:\ > $Session = New-PSSession -ComputerName 10.10.10.10 -Credential $Cred

  PS C:\ > Invoke-Command -Session $Session -ScriptBlock {Start-Process ping 10.10.10.100}'
created_at: '2020-03-21T02:22:47.090294+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[ps]]'
---

# Create a PSSession and Execute a Command

```bash
$Session = New-PSSession -ComputerName $_TARGET_IP -Credential $Cred
Invoke-Command -Session $Session -ScriptBlock {Start-Process $_CMD}
```

## Expected Output

```
PS C:\ > $Session = New-PSSession -ComputerName 10.10.10.10 -Credential $Cred
PS C:\ > Invoke-Command -Session $Session -ScriptBlock {Start-Process ping 10.10.10.100}
```


