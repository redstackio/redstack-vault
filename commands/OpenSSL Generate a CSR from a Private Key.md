---
id: 60e67cf9-6ea3-459f-b3e7-e365062870df
name: OpenSSL Generate a CSR from a Private Key
type: command
executor: ''
data: openssl req -new -key $_PRIVATE_KEY -out $_PRIVATE_CSR
output: 'oot@kali:~# openssl req -new -key private.key -out priv.csr

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

  Email Address []:

  Please enter the following ''extra'' attributes

  to be sent with your certificate request

  A challenge password []:

  An optional company name []:'
created_at: '2019-09-30T19:48:33.640028+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# OpenSSL Generate a CSR from a Private Key

```bash
openssl req -new -key $_PRIVATE_KEY -out $_PRIVATE_CSR
```

## Expected Output

```
oot@kali:~# openssl req -new -key private.key -out priv.csr
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

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:
```
