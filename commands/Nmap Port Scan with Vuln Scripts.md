---
id: 64372947-61ec-44f6-995f-7a455dc7b7fe
name: Nmap Port Scan with Vuln Scripts
type: command
executor: bash
data: nmap -script vuln $_TARGET_IP
output: "root@kali:~# nmap -script vuln 10.10.10.10\nNmap scan report for 10.10.10.10\n\
  Host is up (0.078s latency).\nNot shown: 65532 closed ports\nPORT    STATE SERVICE\n\
  22/tcp  open  ssh\n443/tcp open  https\n|_http-csrf: Couldn't find any CSRF vulnerabilities.\n\
  |_http-dombased-xss: Couldn't find any DOM based XSS.\n| http-enum: \n|   /dev/:\
  \ Potentially interesting directory w/ listing on 'apache/2.2.22 (ubuntu)'\n|_ \
  \ /index/: Potentially interesting folder\n|_http-stored-xss: Couldn't find any\
  \ stored XSS vulnerabilities.\n|_http-vuln-cve2014-3704: ERROR: Script execution\
  \ failed (use -d to debug)\n|_http-vuln-cve2017-1001000: ERROR: Script execution\
  \ failed (use -d to debug)\n| ssl-ccs-injection: \n|   VULNERABLE:\n|   SSL/TLS\
  \ MITM vulnerability (CCS Injection)\n|     State: VULNERABLE\n|     Risk factor:\
  \ High\n|       OpenSSL before 0.9.8za, 1.0.0 before 1.0.0m, and 1.0.1 before 1.0.1h\n\
  |       does not properly restrict processing of ChangeCipherSpec messages,\n| \
  \      which allows man-in-the-middle attackers to trigger use of a zero\n|    \
  \   length master key in certain OpenSSL-to-OpenSSL communications, and\n|     \
  \  consequently hijack sessions or obtain sensitive information, via\n|       a\
  \ crafted TLS handshake, aka the \"CCS Injection\" vulnerability.\n|           \n\
  |     References:\n|       http://www.cvedetails.com/cve/2014-0224\n|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0224\n\
  |_      http://www.openssl.org/news/secadv_20140605.txt\n| ssl-heartbleed: \n| \
  \  VULNERABLE:\n|   The Heartbleed Bug is a serious vulnerability in the popular\
  \ OpenSSL cryptographic software library. It allows for stealing information intended\
  \ to be protected by SSL/TLS encryption.\n|     State: VULNERABLE\n|     Risk factor:\
  \ High\n|       OpenSSL versions 1.0.1 and 1.0.2-beta releases (including 1.0.1f\
  \ and 1.0.2-beta1) of OpenSSL are affected by the Heartbleed bug. The bug allows\
  \ for reading memory of systems protected by the vulnerable OpenSSL versions and\
  \ could allow for disclosure of otherwise encrypted confidential information as\
  \ well as the encryption keys themselves.\n|           \n|     References:\n|  \
  \     https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0160\n|       http://cvedetails.com/cve/2014-0160/\n\
  |_      http://www.openssl.org/news/secadv_20140407.txt \n| ssl-poodle: \n|   VULNERABLE:\n\
  |   SSL POODLE information leak\n|     State: VULNERABLE\n|     IDs:  OSVDB:113251\
  \  CVE:CVE-2014-3566\n|           The SSL protocol 3.0, as used in OpenSSL through\
  \ 1.0.1i and other\n|           products, uses nondeterministic CBC padding, which\
  \ makes it easier\n|           for man-in-the-middle attackers to obtain cleartext\
  \ data via a\n|           padding-oracle attack, aka the \"POODLE\" issue.\n|  \
  \   Disclosure date: 2014-10-14\n|     Check results:\n|       TLS_RSA_WITH_AES_128_CBC_SHA\n\
  |     References:\n|       http://osvdb.org/113251\n|       https://www.openssl.org/~bodo/ssl-poodle.pdf\n\
  |       https://www.imperialviolet.org/2014/10/14/poodle.html\n|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-3566\n\
  |_sslv2-drown: \n\n# Nmap done at Mon Nov 25 12:28:55 2019 -- 1 IP address (1 host\
  \ up) scanned in 694.61 seconds"
created_at: '2019-11-25T18:08:22.068973+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Nmap Port Scan with Vuln Scripts

```bash
nmap -script vuln $_TARGET_IP
```

## Expected Output

```
root@kali:~# nmap -script vuln 10.10.10.10
Nmap scan report for 10.10.10.10
Host is up (0.078s latency).
Not shown: 65532 closed ports
PORT    STATE SERVICE
22/tcp  open  ssh
443/tcp open  https
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-enum: 
|   /dev/: Potentially interesting directory w/ listing on 'apache/2.2.22 (ubuntu)'
|_  /index/: Potentially interesting folder
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-vuln-cve2014-3704: ERROR: Script execution failed (use -d to debug)
|_http-vuln-cve2017-1001000: ERROR: Script execution failed (use -d to debug)
| ssl-ccs-injection: 
|   VULNERABLE:
|   SSL/TLS MITM vulnerability (CCS Injection)
|     State: VULNERABLE
|     Risk factor: High
|       OpenSSL before 0.9.8za, 1.0.0 before 1.0.0m, and 1.0.1 before 1.0.1h
|       does not properly restrict processing of ChangeCipherSpec messages,
|       which allows man-in-the-middle attackers to trigger use of a zero
|       length master key in certain OpenSSL-to-OpenSSL communications, and
|       consequently hijack sessions or obtain sensitive information, via
|       a crafted TLS handshake, aka the "CCS Injection" vulnerability.
|           
|     References:
|       http://www.cvedetails.com/cve/2014-0224
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0224
|_      http://www.openssl.org/news/secadv_20140605.txt
| ssl-heartbleed: 
|   VULNERABLE:
|   The Heartbleed Bug is a serious vulnerability in the popular OpenSSL cryptographic software library. It allows for stealing information intended to be protected by SSL/TLS encryption.
|     State: VULNERABLE
|     Risk factor: High
|       OpenSSL versions 1.0.1 and 1.0.2-beta releases (including 1.0.1f and 1.0.2-beta1) of OpenSSL are affected by the Heartbleed bug. The bug allows for reading memory of systems protected by the vulnerable OpenSSL versions and could allow for disclosure of otherwise encrypted confidential information as well as the encryption keys themselves.
|           
|     References:
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0160
|       http://cvedetails.com/cve/2014-0160/
|_      http://www.openssl.org/news/secadv_20140407.txt 
| ssl-poodle: 
|   VULNERABLE:
|   SSL POODLE information leak
|     State: VULNERABLE
|     IDs:  OSVDB:113251  CVE:CVE-2014-3566
|           The SSL protocol 3.0, as used in OpenSSL through 1.0.1i and other
|           products, uses nondeterministic CBC padding, which makes it easier
|           for man-in-the-middle attackers to obtain cleartext data via a
|           padding-oracle attack, aka the "POODLE" issue.
|     Disclosure date: 2014-10-14
|     Check results:
|       TLS_RSA_WITH_AES_128_CBC_SHA
|     References:
|       http://osvdb.org/113251
|       https://www.openssl.org/~bodo/ssl-poodle.pdf
|       https://www.imperialviolet.org/2014/10/14/poodle.html
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-3566
|_sslv2-drown: 

# Nmap done at Mon Nov 25 12:28:55 2019 -- 1 IP address (1 host up) scanned in 694.61 seconds
```


