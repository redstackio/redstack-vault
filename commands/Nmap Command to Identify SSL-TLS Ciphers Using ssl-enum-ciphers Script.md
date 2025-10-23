---
id: bf30d47f-741e-40da-8551-1eb6152f10a2
name: Nmap Command to Identify SSL/TLS Ciphers Using ssl-enum-ciphers Script
type: command
executor: ''
data: nmap --script ssl-enum-ciphers demo.testfire.net:443
output: "Starting Nmap 7.70 ( https://nmap.org ) at 2020-09-03 13:03 IST\nFailed to\
  \ resolve \"demo.testfire.net:443\".\nWARNING: No targets were specified, so 0 hosts\
  \ scanned.\nNmap done: 0 IP addresses (0 hosts up) scanned in 0.56 seconds\nroot@kali:~#\
  \ nmap --script ssl-enum-ciphers demo.testfire.net -p443\nStarting Nmap 7.70 ( https://nmap.org\
  \ ) at 2020-09-03 13:03 IST\nNmap scan report for demo.testfire.net (65.61.137.117)\n\
  Host is up (0.37s latency).\n\nPORT    STATE SERVICE\n443/tcp open  https\n| ssl-enum-ciphers:\
  \ \n|   TLSv1.0: \n|     ciphers: \n|       TLS_DHE_RSA_WITH_AES_128_CBC_SHA (dh\
  \ 1024) - A\n|       TLS_DHE_RSA_WITH_AES_256_CBC_SHA (dh 1024) - A\n|       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA\
  \ (secp256r1) - A\n|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (secp256r1) - A\n\
  |     compressors: \n|       NULL\n|     cipher preference: client\n|     warnings:\
  \ \n|       Key exchange (dh 1024) of lower strength than certificate key\n|   TLSv1.1:\
  \ \n|     ciphers: \n|       TLS_DHE_RSA_WITH_AES_128_CBC_SHA (dh 1024) - A\n| \
  \      TLS_DHE_RSA_WITH_AES_256_CBC_SHA (dh 1024) - A\n|       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA\
  \ (secp256r1) - A\n|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (secp256r1) - A\n\
  |     compressors: \n|       NULL\n|     cipher preference: client\n|     warnings:\
  \ \n|       Key exchange (dh 1024) of lower strength than certificate key\n|   TLSv1.2:\
  \ \n|     ciphers: \n|       TLS_DHE_RSA_WITH_AES_128_CBC_SHA (dh 1024) - A\n| \
  \      TLS_DHE_RSA_WITH_AES_128_CBC_SHA256 (dh 1024) - A\n|       TLS_DHE_RSA_WITH_AES_128_GCM_SHA256\
  \ (dh 1024) - A\n|       TLS_DHE_RSA_WITH_AES_256_CBC_SHA (dh 1024) - A\n|     \
  \  TLS_DHE_RSA_WITH_AES_256_CBC_SHA256 (dh 1024) - A\n|       TLS_DHE_RSA_WITH_AES_256_GCM_SHA384\
  \ (dh 1024) - A\n|       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA (secp256r1) - A\n| \
  \      TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 (secp256r1) - A\n|       TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256\
  \ (secp256r1) - A\n|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (secp256r1) - A\n\
  |       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 (secp256r1) - A\n|       TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384\
  \ (secp256r1) - A\n|     compressors: \n|       NULL\n|     cipher preference: client\n\
  |     warnings: \n|       Key exchange (dh 1024) of lower strength than certificate\
  \ key\n|_  least strength: A\n"
created_at: '2020-09-03T14:25:24.550802+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Nmap Command to Identify SSL/TLS Ciphers Using ssl-enum-ciphers Script

```bash
nmap --script ssl-enum-ciphers demo.testfire.net:443
```

## Expected Output

```
Starting Nmap 7.70 ( https://nmap.org ) at 2020-09-03 13:03 IST
Failed to resolve "demo.testfire.net:443".
WARNING: No targets were specified, so 0 hosts scanned.
Nmap done: 0 IP addresses (0 hosts up) scanned in 0.56 seconds
root@kali:~# nmap --script ssl-enum-ciphers demo.testfire.net -p443
Starting Nmap 7.70 ( https://nmap.org ) at 2020-09-03 13:03 IST
Nmap scan report for demo.testfire.net (65.61.137.117)
Host is up (0.37s latency).

PORT    STATE SERVICE
443/tcp open  https
| ssl-enum-ciphers: 
|   TLSv1.0: 
|     ciphers: 
|       TLS_DHE_RSA_WITH_AES_128_CBC_SHA (dh 1024) - A
|       TLS_DHE_RSA_WITH_AES_256_CBC_SHA (dh 1024) - A
|       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (secp256r1) - A
|     compressors: 
|       NULL
|     cipher preference: client
|     warnings: 
|       Key exchange (dh 1024) of lower strength than certificate key
|   TLSv1.1: 
|     ciphers: 
|       TLS_DHE_RSA_WITH_AES_128_CBC_SHA (dh 1024) - A
|       TLS_DHE_RSA_WITH_AES_256_CBC_SHA (dh 1024) - A
|       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (secp256r1) - A
|     compressors: 
|       NULL
|     cipher preference: client
|     warnings: 
|       Key exchange (dh 1024) of lower strength than certificate key
|   TLSv1.2: 
|     ciphers: 
|       TLS_DHE_RSA_WITH_AES_128_CBC_SHA (dh 1024) - A
|       TLS_DHE_RSA_WITH_AES_128_CBC_SHA256 (dh 1024) - A
|       TLS_DHE_RSA_WITH_AES_128_GCM_SHA256 (dh 1024) - A
|       TLS_DHE_RSA_WITH_AES_256_CBC_SHA (dh 1024) - A
|       TLS_DHE_RSA_WITH_AES_256_CBC_SHA256 (dh 1024) - A
|       TLS_DHE_RSA_WITH_AES_256_GCM_SHA384 (dh 1024) - A
|       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (secp256r1) - A
|     compressors: 
|       NULL
|     cipher preference: client
|     warnings: 
|       Key exchange (dh 1024) of lower strength than certificate key
|_  least strength: A

```


