---
id: ab2d27ed-ab27-417f-ae6c-e18d92e41edd
name: Read remote registry key
type: command
executor: bash
data: '$reg = [Microsoft.Win32.RegistryKey]::OpenRemoteBaseKey(''LocalMachine'', ''dc.htb.local'',[Microsoft.Win32.RegistryView]::Registry64)

  $winlogon = $reg.OpenSubKey(''SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon'')

  $winlogon.GetValueNames() | foreach {"$_ : $(($winlogon).GetValue($_))"}'
output: null
created_at: '2023-04-06T03:56:06.526142+00:00'
updated_at: '2023-04-10T20:26:17.815665+00:00'
---

# Read remote registry key

```bash
$reg = [Microsoft.Win32.RegistryKey]::OpenRemoteBaseKey('LocalMachine', 'dc.htb.local',[Microsoft.Win32.RegistryView]::Registry64)
$winlogon = $reg.OpenSubKey('SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon')
$winlogon.GetValueNames() | foreach {"$_ : $(($winlogon).GetValue($_))"}
```
