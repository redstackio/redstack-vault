---
id: 958e286d-e013-4823-a0e5-fcfa243fe353
name: Configure Kerberos only
type: command
executor: bash
data: Set-ADUser -Identity 'User1' -KerberosEncryptionType 'RC4-HMAC-NT', 'AES128-CTS-HMAC-SHA1-96'
output: null
created_at: '2023-04-06T03:56:07.951538+00:00'
updated_at: '2023-04-10T20:26:20.679788+00:00'
---

# Configure Kerberos only

```bash
Set-ADUser -Identity 'User1' -KerberosEncryptionType 'RC4-HMAC-NT', 'AES128-CTS-HMAC-SHA1-96'
```


