---
id: 2553c253-0588-4190-a9f2-56c4547f0a85
name: Accesschk.exe - Check Permissions for Authenticated Users and upnphost Services
type: command
executor: bash
data: "$ accesschk.exe -uwcqv \"Authenticated Users\" * /accepteula\nRW SSDPSRV\n\
  \        SERVICE_ALL_ACCESS\nRW upnphost\n        SERVICE_ALL_ACCESS"
output: null
created_at: '2023-04-06T03:56:29.544808+00:00'
updated_at: '2023-04-10T20:37:52.272360+00:00'
---

# Accesschk.exe - Check Permissions for Authenticated Users and upnphost Services

```bash
$ accesschk.exe -uwcqv "Authenticated Users" * /accepteula
RW SSDPSRV
        SERVICE_ALL_ACCESS
RW upnphost
        SERVICE_ALL_ACCESS
```


