---
id: 92df115e-188b-4b01-921f-422a16e79de0
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:05.731601+00:00'
updated_at: '2023-04-10T20:25:45.492561+00:00'
---

# Code Snippet 92df115e

**Language**: ps1

```ps1
Certify.exe find /vulnerable
Certify.exe find /vulnerable /currentuser
# or
PS> Get-ADObject -LDAPFilter '(&(objectclass=pkicertificatetemplate)(!(mspki-enrollment-flag:1.2.840.113556.1.4.804:=2))(|(mspki-ra-signature=0)(!(mspki-ra-signature=*)))(|(pkiextendedkeyusage=1.3.6.1.4.1.311.20.2.2)(pkiextendedkeyusage=1.3.6.1.5.5.7.3.2) (pkiextendedkeyusage=1.3.6.1.5.2.3.4))(mspki-certificate-name-flag:1.2.840.113556.1.4.804:=1))' -SearchBase 'CN=Configuration,DC=lab,DC=local'
# or
certipy 'domain.local'/'user':'password'@'domaincontroller' find -bloodhound
```


