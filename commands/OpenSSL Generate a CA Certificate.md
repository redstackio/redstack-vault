---
id: b67d66cb-9544-4fce-8dc3-f11ccd360cbf
name: OpenSSL Generate a CA Certificate
type: command
executor: ''
data: openssl req -x509 -new -nodes -key $_ROOT_CA -sha256 -days 365 -out $_ROOT_CA_CRT
output: 'root@kali:~# openssl req -x509 -new -nodes -key id_rsa -sha256 -days 365
  -out rootca.crt

  You are about to be asked to enter information that will be incorporated

  into your certificate request.

  What you are about to enter is what is called a Distinguished Name or a DN.

  There are quite a few fields but you can leave some blank

  For some fields there will be a default value,

  If you enter ''.'', the field will be left blank.

  -----

  Country Name (2 letter code) [AU]:

  State or Province Name (full name) [Some-State]:

  Locality Name (eg, city) []:

  Organization Name (eg, company) [Internet Widgits Pty Ltd]:

  Organizational Unit Name (eg, section) []:

  Common Name (e.g. server FQDN or YOUR name) []:

  Email Address []:'
created_at: '2019-09-30T19:48:33.637582+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# OpenSSL Generate a CA Certificate

```bash
openssl req -x509 -new -nodes -key $_ROOT_CA -sha256 -days 365 -out $_ROOT_CA_CRT
```

## Expected Output

```
root@kali:~# openssl req -x509 -new -nodes -key id_rsa -sha256 -days 365 -out rootca.crt
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:
State or Province Name (full name) [Some-State]:
Locality Name (eg, city) []:
Organization Name (eg, company) [Internet Widgits Pty Ltd]:
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:
Email Address []:
```


