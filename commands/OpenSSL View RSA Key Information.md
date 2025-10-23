---
id: b1c41ce1-a03e-4062-b278-ab73075e9aa2
name: OpenSSL View RSA Key Information
type: command
executor: ''
data: openssl rsa -in $_PRIVATE_KEY -text -noout
output: "root@kali:~# openssl rsa -in private.key -text -noout\nRSA Private-Key: (4096\
  \ bit, 2 primes)\nmodulus:\n    00:b0:d3:cd:28:26:72:c0:8e:52:ed:28:b4:53:ad:\n\
  \    13:ab:73:89:40:2e:35:cb:94:02:29:97:e3:0d:03:\n    d6:80:a2:31:f6:33:b8:c1:91:16:43:68:16:15:05:\n\
  ...\n...\ncoefficient:\n    00:80:19:36:55:a5:a6:67:5b:9b:73:f5:34:ba:ce:\n    0d:5b:59:d2:66:57:7d:3f:b6:ef:7e:a4:3a:a5:d0:\n\
  \    df:c9:20:a8:63:aa:8b:52:b9:f9:c3:85:3c:21:bb:\n    9c:fe:22:32:49:2d:93:99:45:72:50:36:67:15:4a:\n\
  \    60:50:fa:aa:0c:76:c2:c4:3c:2e:aa:ed:c4:2f:79:\n    de:1b:f3:d1:f5:de:b1:63:e8:d6:c6:82:95:4b:18:\n\
  \    6a:39:4d:bd:be:22:9e:c3:11:0b:00:34:ae:01:5e:\n    ee:62:bd:d8:7b:6a:46:11:9a:83:2f:19:d1:d3:c9:\n\
  \    03:5c:c7:af:69:cd:79:d1:02:a6:03:88:61:06:cd:\n    98:67:2a:aa:31:e9:0a:3e:53:22:79:ad:f9:39:d9:\n\
  \    f6:d4:fe:4c:93:ab:4f:b4:62:ad:95:ad:dd:02:4b:\n    cd:2c:e3:7f:55:4f:d9:71:14:6f:5d:6c:65:fb:1e:\n\
  \    79:64:e8:cf:09:94:63:df:b5:8e:f3:e3:28:b3:7e:\n    b6:62:ef:da:07:73:a5:8a:0b:39:bb:a3:2f:0b:fe:\n\
  \    54:38:28:ac:41:73:5d:ab:d4:72:7c:33:17:ff:0d:\n    e5:ec:cf:43:31:c8:0a:20:40:8c:6f:30:a5:71:b7:\n\
  \    98:94:ef:b6:7a:c9:37:c9:4f:dd:49:e7:1f:af:01:\n    6f:3a"
created_at: '2019-09-30T19:48:33.667256+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# OpenSSL View RSA Key Information

```bash
openssl rsa -in $_PRIVATE_KEY -text -noout
```

## Expected Output

```
root@kali:~# openssl rsa -in private.key -text -noout
RSA Private-Key: (4096 bit, 2 primes)
modulus:
    00:b0:d3:cd:28:26:72:c0:8e:52:ed:28:b4:53:ad:
    13:ab:73:89:40:2e:35:cb:94:02:29:97:e3:0d:03:
    d6:80:a2:31:f6:33:b8:c1:91:16:43:68:16:15:05:
...
...
coefficient:
    00:80:19:36:55:a5:a6:67:5b:9b:73:f5:34:ba:ce:
    0d:5b:59:d2:66:57:7d:3f:b6:ef:7e:a4:3a:a5:d0:
    df:c9:20:a8:63:aa:8b:52:b9:f9:c3:85:3c:21:bb:
    9c:fe:22:32:49:2d:93:99:45:72:50:36:67:15:4a:
    60:50:fa:aa:0c:76:c2:c4:3c:2e:aa:ed:c4:2f:79:
    de:1b:f3:d1:f5:de:b1:63:e8:d6:c6:82:95:4b:18:
    6a:39:4d:bd:be:22:9e:c3:11:0b:00:34:ae:01:5e:
    ee:62:bd:d8:7b:6a:46:11:9a:83:2f:19:d1:d3:c9:
    03:5c:c7:af:69:cd:79:d1:02:a6:03:88:61:06:cd:
    98:67:2a:aa:31:e9:0a:3e:53:22:79:ad:f9:39:d9:
    f6:d4:fe:4c:93:ab:4f:b4:62:ad:95:ad:dd:02:4b:
    cd:2c:e3:7f:55:4f:d9:71:14:6f:5d:6c:65:fb:1e:
    79:64:e8:cf:09:94:63:df:b5:8e:f3:e3:28:b3:7e:
    b6:62:ef:da:07:73:a5:8a:0b:39:bb:a3:2f:0b:fe:
    54:38:28:ac:41:73:5d:ab:d4:72:7c:33:17:ff:0d:
    e5:ec:cf:43:31:c8:0a:20:40:8c:6f:30:a5:71:b7:
    98:94:ef:b6:7a:c9:37:c9:4f:dd:49:e7:1f:af:01:
    6f:3a
```


