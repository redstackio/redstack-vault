---
id: d791bef5-5142-4379-8d5d-87049ecf9e94
name: Nmap Command to Identify SSL Certificate Details
type: command
executor: ''
data: nmap --script ssl-cert demo.testfire.net -p443
output: 'Starting Nmap 7.70 ( https://nmap.org ) at 2020-09-03 13:04 IST

  Nmap scan report for demo.testfire.net (65.61.137.117)

  Host is up (0.39s latency).


  PORT    STATE SERVICE

  443/tcp open  https

  | ssl-cert: Subject: commonName=demo.testfire.net

  | Subject Alternative Name: DNS:demo.testfire.net, DNS:altoromutual.com

  | Issuer: commonName=Sectigo RSA Domain Validation Secure Server CA/organizationName=Sectigo
  Limited/stateOrProvinceName=Greater Manchester/countryName=GB

  | Public Key type: rsa

  | Public Key bits: 2048

  | Signature Algorithm: sha256WithRSAEncryption

  | Not valid before: 2020-05-22T00:00:00

  | Not valid after:  2022-05-22T23:59:59

  | MD5:   c5a6 d33d 92a1 6089 26a0 4d42 1f57 cd1d

  |_SHA-1: b300 b380 6bb4 ac20 3236 5cc0 8051 fa5f a97e 1342

  '
created_at: '2020-09-03T14:48:30.690046+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Nmap]]'
- '[[host]]'
- '[[type]]'
---

# Nmap Command to Identify SSL Certificate Details

```bash
nmap --script ssl-cert demo.testfire.net -p443
```

## Expected Output

```
Starting Nmap 7.70 ( https://nmap.org ) at 2020-09-03 13:04 IST
Nmap scan report for demo.testfire.net (65.61.137.117)
Host is up (0.39s latency).

PORT    STATE SERVICE
443/tcp open  https
| ssl-cert: Subject: commonName=demo.testfire.net
| Subject Alternative Name: DNS:demo.testfire.net, DNS:altoromutual.com
| Issuer: commonName=Sectigo RSA Domain Validation Secure Server CA/organizationName=Sectigo Limited/stateOrProvinceName=Greater Manchester/countryName=GB
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2020-05-22T00:00:00
| Not valid after:  2022-05-22T23:59:59
| MD5:   c5a6 d33d 92a1 6089 26a0 4d42 1f57 cd1d
|_SHA-1: b300 b380 6bb4 ac20 3236 5cc0 8051 fa5f a97e 1342

```


