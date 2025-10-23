---
id: d72d4aca-493b-4a1f-bfc8-3dc3f69b1fb1
name: Check .Net version 2.0.50727 and run PowerShell v2
type: command
executor: bash
data: "if ($ShowOnly -eq $True)\n{\n        Write-Output \"If .Net version 2.0.50727\
  \ is installed, run powershell -v 2 and run scripts from the new PowerShell process.\"\
  \n}\nelse\n{\n        Write-Verbose \"Checking if .Net version 2.0.50727 is installed.\"\
  \n        $versions = Get-ChildItem 'HKLM:\\SOFTWARE\\Microsoft\\NET Framework Setup\\\
  NDP' -recurse | Get-ItemProperty -name Version -EA 0 | Where { $_.PSChildName -match\
  \ '^(?!S)\\p{L}'} | Select -ExpandProperty Version\n    if($versions -match \"2.0.50727\"\
  )\n    {\n            Write-Verbose \".Net version 2.0.50727 found.\"\n        \
  \    Write-Output \"Executing the bypass.\"\n            powershell.exe -version\
  \ 2\n    }\n    else\n    {\n            Write-Verbose \".Net version 2.0.50727\
  \ not found. Can't start PowerShell v2.\"\n    }\n}"
output: null
created_at: '2023-04-06T03:56:26.092263+00:00'
updated_at: '2023-04-10T20:36:19.395604+00:00'
---

# Check .Net version 2.0.50727 and run PowerShell v2

```bash
if ($ShowOnly -eq $True)
{
        Write-Output "If .Net version 2.0.50727 is installed, run powershell -v 2 and run scripts from the new PowerShell process."
}
else
{
        Write-Verbose "Checking if .Net version 2.0.50727 is installed."
        $versions = Get-ChildItem 'HKLM:\SOFTWARE\Microsoft\NET Framework Setup\NDP' -recurse | Get-ItemProperty -name Version -EA 0 | Where { $_.PSChildName -match '^(?!S)\p{L}'} | Select -ExpandProperty Version
    if($versions -match "2.0.50727")
    {
            Write-Verbose ".Net version 2.0.50727 found."
            Write-Output "Executing the bypass."
            powershell.exe -version 2
    }
    else
    {
            Write-Verbose ".Net version 2.0.50727 not found. Can't start PowerShell v2."
    }
}
```


