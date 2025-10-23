---
id: 8684d029-cb38-4a4b-8b26-ebbbc6a0a2d7
name: OpenSSL Compare the Modulus of a CRT and Private Key
type: command
executor: ''
data: "openssl x509 -noout -modulus -in $SIGNED_CRT | md5sum; \nopenssl rsa -noout\
  \ -modulus -in $_PRIVATE_KEY | md5sum"
output: 'root@kali:~# openssl rsa -noout -modulus -in id_rsa | md5sum;\

  openssl x509 -noout -modulus -in rootca.crt | md5sum

  03538d32cbfb61d7bc37085db3863d14  -

  03538d32cbfb61d7bc37085db3863d14  -'
created_at: '2019-09-30T19:48:33.638855+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# OpenSSL Compare the Modulus of a CRT and Private Key

```bash
openssl x509 -noout -modulus -in $SIGNED_CRT | md5sum; 
openssl rsa -noout -modulus -in $_PRIVATE_KEY | md5sum
```

## Expected Output

```
root@kali:~# openssl rsa -noout -modulus -in id_rsa | md5sum;\
openssl x509 -noout -modulus -in rootca.crt | md5sum
03538d32cbfb61d7bc37085db3863d14  -
03538d32cbfb61d7bc37085db3863d14  -
```


