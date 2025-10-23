---
id: 7e2ea09c-090f-4481-a1d7-eedfe67f6a47
name: Keytool Extract Owner Information from SSL Certificate
type: command
executor: bash
data: keytool -printcert -sslserver $_TARGET_IP:$_TARGET_PORT
output: "root@kali:~# keytool -printcert -sslserver 10.10.10.10:443\nCertificate #0\n\
  ====================================\nOwner: EMAILADDRESS=bob@host.local, CN=host.local,\
  \ OU=hq, O=Cyber, L=LA, ST=California, C=US\nIssuer: EMAILADDRESS=bob@host.local,\
  \ CN=host.local, OU=hq, O=Cyber, L=LA, ST=California, C=US\nSerial number: a6fa3cc554cf5a5b\n\
  Valid from: Fri Aug 24 07:35:14 EDT 2019 until: Sun Sep 24 06:35:14 EDT 2019\nCertificate\
  \ fingerprints:\n         SHA1: 6B:08:22:B5:18:38:1A:EA:0A:6F:B4:BF:A6:22:20:A9:93:81:E0:4A\n\
  \         SHA256: 37:B6:D5:0E:91:3E:A7:0F:B3:58:BC:C1:61:AF:16:B7:FF:A7:D0:02:AC:E1:0C:E6:D8:61:C4:CF:E9:30:E1:A6\n\
  Signature algorithm name: SHA256withRSA\nSubject Public Key Algorithm: 2048-bit\
  \ RSA key\nVersion: 3"
created_at: '2019-10-31T19:06:18.268163+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Keytool Extract Owner Information from SSL Certificate

```bash
keytool -printcert -sslserver $_TARGET_IP:$_TARGET_PORT
```

## Expected Output

```
root@kali:~# keytool -printcert -sslserver 10.10.10.10:443
Certificate #0
====================================
Owner: EMAILADDRESS=bob@host.local, CN=host.local, OU=hq, O=Cyber, L=LA, ST=California, C=US
Issuer: EMAILADDRESS=bob@host.local, CN=host.local, OU=hq, O=Cyber, L=LA, ST=California, C=US
Serial number: a6fa3cc554cf5a5b
Valid from: Fri Aug 24 07:35:14 EDT 2019 until: Sun Sep 24 06:35:14 EDT 2019
Certificate fingerprints:
         SHA1: 6B:08:22:B5:18:38:1A:EA:0A:6F:B4:BF:A6:22:20:A9:93:81:E0:4A
         SHA256: 37:B6:D5:0E:91:3E:A7:0F:B3:58:BC:C1:61:AF:16:B7:FF:A7:D0:02:AC:E1:0C:E6:D8:61:C4:CF:E9:30:E1:A6
Signature algorithm name: SHA256withRSA
Subject Public Key Algorithm: 2048-bit RSA key
Version: 3
```


