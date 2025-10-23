---
id: 709bc988-c220-4c0e-973d-d3f1733e6f65
name: PowerShell Check for Anti-Virus in Windows (SecurityCenter2)
type: command
executor: powershell
data: Get-WmiObject -Namespace root\SecurityCenter2 -Class AntiVirusProduct
output: "PS C:\\> Get-WmiObject -Namespace root\\SecurityCenter2 -Class AntiVirusProduct\n\
  \n\n__GENUS                  : 2\n__CLASS                  : AntiVirusProduct\n\
  __SUPERCLASS             :\n__DYNASTY                : AntiVirusProduct\n__RELPATH\
  \                : AntiVirusProduct.instanceGuid=\"{D68DDC3A-831F-4fae-9E44-DA\n\
  \                           132C1ACF46}\"\n__PROPERTY_COUNT         : 6\n__DERIVATION\
  \             : {}\n__SERVER                 : WS01\n__NAMESPACE              :\
  \ ROOT\\SecurityCenter2\n__PATH                   : \\\\WS01\\ROOT\\SecurityCenter2:AntiVirusProduct.instanceGuid=\n\
  \                           \"{D68DDC3A-831F-4fae-9E44-DA132C1ACF46}\"\ndisplayName\
  \              : Windows Defender\ninstanceGuid             : {D68DDC3A-831F-4fae-9E44-DA132C1ACF46}\n\
  pathToSignedProductExe   : windowsdefender://\npathToSignedReportingExe : %ProgramFiles%\\\
  Windows Defender\\MsMpeng.exe\nproductState             : 397568\ntimestamp    \
  \            : Wed, 08 Jul 2020 03:25:31 GMT\nPSComputerName           : WS01"
created_at: '2020-07-09T04:30:18.659248+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# PowerShell Check for Anti-Virus in Windows (SecurityCenter2)

```powershell
Get-WmiObject -Namespace root\SecurityCenter2 -Class AntiVirusProduct
```

## Expected Output

```
PS C:\> Get-WmiObject -Namespace root\SecurityCenter2 -Class AntiVirusProduct


__GENUS                  : 2
__CLASS                  : AntiVirusProduct
__SUPERCLASS             :
__DYNASTY                : AntiVirusProduct
__RELPATH                : AntiVirusProduct.instanceGuid="{D68DDC3A-831F-4fae-9E44-DA
                           132C1ACF46}"
__PROPERTY_COUNT         : 6
__DERIVATION             : {}
__SERVER                 : WS01
__NAMESPACE              : ROOT\SecurityCenter2
__PATH                   : \\WS01\ROOT\SecurityCenter2:AntiVirusProduct.instanceGuid=
                           "{D68DDC3A-831F-4fae-9E44-DA132C1ACF46}"
displayName              : Windows Defender
instanceGuid             : {D68DDC3A-831F-4fae-9E44-DA132C1ACF46}
pathToSignedProductExe   : windowsdefender://
pathToSignedReportingExe : %ProgramFiles%\Windows Defender\MsMpeng.exe
productState             : 397568
timestamp                : Wed, 08 Jul 2020 03:25:31 GMT
PSComputerName           : WS01
```


