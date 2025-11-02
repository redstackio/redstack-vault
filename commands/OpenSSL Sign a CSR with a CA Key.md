---
id: cc872159-0cbc-48b5-a8fa-cf25a359f0e2
name: OpenSSL Sign a CSR with a CA Key
type: command
executor: ''
data: openssl x509 -req -in $_PRIVATE_CSR -CA $_ROOT_CA_CRT -CAkey $_ROOT_CA -CAcreateserial
  -out $_PRIVATE_CRT -days 365 -sha256
output: 'openssl x509 -req -in priv.csr -CA rootca.crt -CAkey id_rsa -CAcreateserial
  -out signed.crt -days 365 -sha256

  Signature ok

  subject=C = AU, ST = Some-State, O = Internet Widgits Pty Ltd

  Getting CA Private Key'
created_at: '2019-09-30T19:48:33.637991+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[openssl]]'
---

# OpenSSL Sign a CSR with a CA Key

```bash
openssl x509 -req -in $_PRIVATE_CSR -CA $_ROOT_CA_CRT -CAkey $_ROOT_CA -CAcreateserial -out $_PRIVATE_CRT -days 365 -sha256
```

## Expected Output

```
openssl x509 -req -in priv.csr -CA rootca.crt -CAkey id_rsa -CAcreateserial -out signed.crt -days 365 -sha256
Signature ok
subject=C = AU, ST = Some-State, O = Internet Widgits Pty Ltd
Getting CA Private Key
```


