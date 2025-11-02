---
id: b3f638e8-463c-4e23-b40a-1db897122c2f
name: PowerShell Generate Credentials Using a Secure String
type: command
executor: ''
data: $creds = New-Object System.Management.Automation.PSCredential('$_COMPUTER_NAME/$_USERNAME',
  $pass)
output: PS C:\> $creds = New-Object System.Management.Automation.PSCredential('BOB-PC/BOB',
  $pass)
created_at: '2019-09-30T19:48:33.639766+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Powershell]]'
- '[[ps]]'
---

# PowerShell Generate Credentials Using a Secure String

```bash
$creds = New-Object System.Management.Automation.PSCredential('$_COMPUTER_NAME/$_USERNAME', $pass)
```

## Expected Output

```
PS C:\> $creds = New-Object System.Management.Automation.PSCredential('BOB-PC/BOB', $pass)
```


