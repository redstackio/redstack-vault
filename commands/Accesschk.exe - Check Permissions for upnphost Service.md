---
id: 421f09bc-ff32-4613-8e62-9611d00c7091
name: Accesschk.exe - Check Permissions for upnphost Service
type: command
executor: bash
data: "$ accesschk.exe -ucqv upnphost\nupnphost\n  RW NT AUTHORITY\\SYSTEM\n     \
  \   SERVICE_ALL_ACCESS\n  RW BUILTIN\\Administrators\n        SERVICE_ALL_ACCESS\n\
  \  RW NT AUTHORITY\\Authenticated Users\n        SERVICE_ALL_ACCESS\n  RW BUILTIN\\\
  Power Users\n        SERVICE_ALL_ACCESS"
output: null
created_at: '2023-04-06T03:56:29.544864+00:00'
updated_at: '2023-04-10T20:37:52.272360+00:00'
---

# Accesschk.exe - Check Permissions for upnphost Service

```bash
$ accesschk.exe -ucqv upnphost
upnphost
  RW NT AUTHORITY\SYSTEM
        SERVICE_ALL_ACCESS
  RW BUILTIN\Administrators
        SERVICE_ALL_ACCESS
  RW NT AUTHORITY\Authenticated Users
        SERVICE_ALL_ACCESS
  RW BUILTIN\Power Users
        SERVICE_ALL_ACCESS
```
