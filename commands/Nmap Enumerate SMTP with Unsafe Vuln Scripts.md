---
id: 648ba731-6fb4-4b56-99b8-cd97820fd54d
name: Nmap Enumerate SMTP with Unsafe Vuln Scripts
type: command
executor: bash
data: nmap --script vuln --script-args=unsafe -p $_TARGET_PORT $_TARGET_IP
output: "root@kali:~# nmap --script vuln --script-args=unsafe -p25 10.10.10.10\nStarting\
  \ Nmap 7.70 ( https://nmap.org ) at 2019-09-13 18:09 EDT\nNmap scan report for 10.10.10.10\n\
  Host is up (0.00097s latency).\n\nPORT   STATE SERVICE\n25/tcp open  smtp\n| smtp-vuln-cve2010-4344:\
  \ \n|_  The SMTP server is not Exim: NOT VULNERABLE\n| ssl-dh-params: \n|   VULNERABLE:\n\
  |   Anonymous Diffie-Hellman Key Exchange MitM Vulnerability\n|     State: VULNERABLE\n\
  |       Transport Layer Security (TLS) services that use anonymous\n|       Diffie-Hellman\
  \ key exchange only provide protection against passive\n|       eavesdropping, and\
  \ are vulnerable to active man-in-the-middle attacks\n|       which could completely\
  \ compromise the confidentiality and integrity\n|       of any data exchanged over\
  \ the resulting session.\n|     Check results:\n|       ANONYMOUS DH GROUP 1\n|\
  \             Cipher Suite: TLS_DH_anon_WITH_AES_256_CBC_SHA\n|             Modulus\
  \ Type: Safe prime\n|             Modulus Source: postfix builtin\n|           \
  \  Modulus Length: 1024\n|             Generator Length: 8\n|             Public\
  \ Key Length: 1024\n|     References:\n|       https://www.ietf.org/rfc/rfc2246.txt\n\
  ...\n..\nNmap done: 1 IP address (1 host up) scanned in 26.75 seconds"
created_at: '2019-09-13T22:29:10.938572+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Nmap Enumerate SMTP with Unsafe Vuln Scripts

```bash
nmap --script vuln --script-args=unsafe -p $_TARGET_PORT $_TARGET_IP
```

## Expected Output

```
root@kali:~# nmap --script vuln --script-args=unsafe -p25 10.10.10.10
Starting Nmap 7.70 ( https://nmap.org ) at 2019-09-13 18:09 EDT
Nmap scan report for 10.10.10.10
Host is up (0.00097s latency).

PORT   STATE SERVICE
25/tcp open  smtp
| smtp-vuln-cve2010-4344: 
|_  The SMTP server is not Exim: NOT VULNERABLE
| ssl-dh-params: 
|   VULNERABLE:
|   Anonymous Diffie-Hellman Key Exchange MitM Vulnerability
|     State: VULNERABLE
|       Transport Layer Security (TLS) services that use anonymous
|       Diffie-Hellman key exchange only provide protection against passive
|       eavesdropping, and are vulnerable to active man-in-the-middle attacks
|       which could completely compromise the confidentiality and integrity
|       of any data exchanged over the resulting session.
|     Check results:
|       ANONYMOUS DH GROUP 1
|             Cipher Suite: TLS_DH_anon_WITH_AES_256_CBC_SHA
|             Modulus Type: Safe prime
|             Modulus Source: postfix builtin
|             Modulus Length: 1024
|             Generator Length: 8
|             Public Key Length: 1024
|     References:
|       https://www.ietf.org/rfc/rfc2246.txt
...
..
Nmap done: 1 IP address (1 host up) scanned in 26.75 seconds
```
