---
id: acdf7c3c-ba5e-4115-b557-46e7567571e6
name: TLSSLed Command
type: command
executor: ''
data: tlssled  65.61.137.117 443
output: "------------------------------------------------------\n TLSSLed - (1.3)\
  \ based on sslscan and openssl\n                 by Raul Siles (www.taddong.com)\n\
  ------------------------------------------------------\n    openssl version: OpenSSL\
  \ 1.1.0h  27 Mar 2018\n    \n------------------------------------------------------\n\
  \    Date: 20200903-143811\n------------------------------------------------------\n\
  \n[*] Analyzing SSL/TLS on 65.61.137.117:443 ...\n    [.] Output directory: TLSSLed_1.3_65.61.137.117_443_20200903-143811\
  \ ...\n\n[*] Checking if the target service speaks SSL/TLS...\n    [.] The target\
  \ service 65.61.137.117:443 seems to speak SSL/TLS...\n\n    [.] Using SSL/TLS protocol\
  \ version: \n        (empty means I'm using the default openssl protocol version(s))\n\
  \n[*] Running sslscan on 65.61.137.117:443 ...\n\n    [-] Testing for SSLv2 ...\n\
  \n    [-] Testing for the NULL cipher ...\n\n    [-] Testing for weak ciphers (based\
  \ on key length - 40 or 56 bits) ...\n\n    [+] Testing for strong ciphers (based\
  \ on AES) ...\nAccepted  TLSv1.2  256 bits  ECDHE-RSA-AES256-SHA384       Curve\
  \ P-256 DHE 256\nAccepted  TLSv1.2  256 bits  ECDHE-RSA-AES256-SHA          Curve\
  \ P-256 DHE 256\nAccepted  TLSv1.2  256 bits  DHE-RSA-AES256-GCM-SHA384     DHE\
  \ 1024 bits\nAccepted  TLSv1.2  256 bits  DHE-RSA-AES256-SHA256         DHE 1024\
  \ bits\nAccepted  TLSv1.2  256 bits  DHE-RSA-AES256-SHA            DHE 1024 bits\n\
  Accepted  TLSv1.2  128 bits  ECDHE-RSA-AES128-GCM-SHA256   Curve P-256 DHE 256\n\
  Accepted  TLSv1.2  128 bits  ECDHE-RSA-AES128-SHA256       Curve P-256 DHE 256\n\
  Accepted  TLSv1.2  128 bits  ECDHE-RSA-AES128-SHA          Curve P-256 DHE 256\n\
  Accepted  TLSv1.2  128 bits  DHE-RSA-AES128-GCM-SHA256     DHE 1024 bits\nAccepted\
  \  TLSv1.2  128 bits  DHE-RSA-AES128-SHA256         DHE 1024 bits\nAccepted  TLSv1.2\
  \  128 bits  DHE-RSA-AES128-SHA            DHE 1024 bits\nAccepted  TLSv1.1  256\
  \ bits  DHE-RSA-AES256-SHA            DHE 1024 bits\nAccepted  TLSv1.1  128 bits\
  \  ECDHE-RSA-AES128-SHA          Curve P-256 DHE 256\nAccepted  TLSv1.1  128 bits\
  \  DHE-RSA-AES128-SHA            DHE 1024 bits\nAccepted  TLSv1.0  256 bits  DHE-RSA-AES256-SHA\
  \            DHE 1024 bits\nAccepted  TLSv1.0  128 bits  ECDHE-RSA-AES128-SHA  \
  \        Curve P-256 DHE 256\nAccepted  TLSv1.0  128 bits  DHE-RSA-AES128-SHA  \
  \          DHE 1024 bits\n\n    [-] Testing for MD5 signed certificate ...\n\n \
  \   [.] Testing for the certificate public key length ...\n\n    [.] Testing for\
  \ the certificate subject ...\nSubject:  demo.testfire.net\n\n    [.] Testing for\
  \ the certificate CA issuer ...\nIssuer:   Sectigo RSA Domain Validation Secure\
  \ Server CA\n\n    [.] Testing for the certificate validity period ...\n    Today:\
  \ Thu 03 Sep 2020 09:08:54 AM UTC\nNot valid before: May 22 00:00:00 2020 GMT\n\
  Not valid after:  May 22 23:59:59 2022 GMT\n\n    [.] Checking preferred server\
  \ ciphers ...\n\n\n[*] Testing for SSL/TLS renegotiation MitM vuln. (CVE-2009-3555)\
  \ ...\n\n    [+] Testing for secure renegotiation support (RFC 5746) ...\n    Secure\
  \ Renegotiation IS supported\n\n[*] Testing for SSL/TLS renegotiation DoS vuln.\
  \ (CVE-2011-1473) ...\n\n    [.] Testing for client initiated (CI) SSL/TLS renegotiation\
  \ (secure)...\n    UNKNOWN\n\n    [.] Testing for client initiated (CI) SSL/TLS\
  \ renegotiation (insecure)...\n    UNKNOWN\n\n[*] Testing for client authentication\
  \ using digital certificates ...\n\n    SSL/TLS client certificate authentication\
  \ IS NOT required\n\n[*] Testing for TLS v1.1 and v1.2 (CVE-2011-3389 vuln. aka\
  \ BEAST) ...\n\n    [-] Testing for SSLv3 and TLSv1 support ...\nAccepted  TLSv1.2\
  \  256 bits  ECDHE-RSA-AES256-SHA384       Curve P-256 DHE 256\nAccepted  TLSv1.2\
  \  256 bits  ECDHE-RSA-AES256-SHA          Curve P-256 DHE 256\nAccepted  TLSv1.2\
  \  256 bits  DHE-RSA-AES256-GCM-SHA384     DHE 1024 bits\nAccepted  TLSv1.2  256\
  \ bits  DHE-RSA-AES256-SHA256         DHE 1024 bits\nAccepted  TLSv1.2  256 bits\
  \  DHE-RSA-AES256-SHA            DHE 1024 bits\nAccepted  TLSv1.2  128 bits  ECDHE-RSA-AES128-GCM-SHA256\
  \   Curve P-256 DHE 256\nAccepted  TLSv1.2  128 bits  ECDHE-RSA-AES128-SHA256  \
  \     Curve P-256 DHE 256\nAccepted  TLSv1.2  128 bits  ECDHE-RSA-AES128-SHA   \
  \       Curve P-256 DHE 256\nAccepted  TLSv1.2  128 bits  DHE-RSA-AES128-GCM-SHA256\
  \     DHE 1024 bits\nAccepted  TLSv1.2  128 bits  DHE-RSA-AES128-SHA256        \
  \ DHE 1024 bits\nAccepted  TLSv1.2  128 bits  DHE-RSA-AES128-SHA            DHE\
  \ 1024 bits\nAccepted  TLSv1.1  256 bits  DHE-RSA-AES256-SHA            DHE 1024\
  \ bits\nAccepted  TLSv1.1  128 bits  ECDHE-RSA-AES128-SHA          Curve P-256 DHE\
  \ 256\nAccepted  TLSv1.1  128 bits  DHE-RSA-AES128-SHA            DHE 1024 bits\n\
  \n    [+] Testing for RC4 in the prefered cipher(s) list ...\n\n    [.] Testing\
  \ for TLS v1.1 support ...\n    TLS v1.1 IS supported\n\n    [.] Testing for TLS\
  \ v1.2 support ...\n    TLS v1.2 IS supported\n\n[*] Testing for HTTPS (SSL/TLS)\
  \ security headers using HTTP/1.0 ...\n\n    [+] Testing for HTTP Strict-Transport-Security\
  \ (HSTS) header ...\n\n    [+] Testing for cookies with the secure flag ...\nSet-Cookie:\
  \ JSESSIONID=1672C0C04E6B30C4B35BA958175305CD; Path=/; Secure; HttpOnly\n\n    [-]\
  \ Testing for cookies without the secure flag ...\n\n[*] Testing for HTTPS (SSL/TLS)\
  \ security headers using HTTP/1.1 & Host ...\n\n    [+] Testing for HTTP Strict-Transport-Security\
  \ (HSTS) header ...\n\n    [+] Testing for cookies with the secure flag ...\nSet-Cookie:\
  \ JSESSIONID=3FF6BE7CAF5ECD40447CC801F6D845BE; Path=/; Secure; HttpOnly\n\n    [-]\
  \ Testing for cookies without the secure flag ...\n\n[*] New files created:\n  \
  \  [.] Output directory: TLSSLed_1.3_65.61.137.117_443_20200903-143811 ...\n\nopenssl_HEAD_1.0_65.61.137.117_443_20200903-143811.err\t\
  openssl_RENEG_65.61.137.117_443_20200903-143811.log\nopenssl_HEAD_1.0_65.61.137.117_443_20200903-143811.log\t\
  openssl_RENEG_LEGACY_65.61.137.117_443_20200903-143811.err\nopenssl_HEAD_65.61.137.117_443_20200903-143811.err\t\
  openssl_RENEG_LEGACY_65.61.137.117_443_20200903-143811.log\nopenssl_HEAD_65.61.137.117_443_20200903-143811.log\t\
  sslscan_65.61.137.117_443_20200903-143811.log\nopenssl_RENEG_65.61.137.117_443_20200903-143811.err\n\
  \n[*] done\n"
created_at: '2020-09-03T15:26:43.785851+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# TLSSLed Command

```bash
tlssled  65.61.137.117 443
```

## Expected Output

```
------------------------------------------------------
 TLSSLed - (1.3) based on sslscan and openssl
                 by Raul Siles (www.taddong.com)
------------------------------------------------------
    openssl version: OpenSSL 1.1.0h  27 Mar 2018
    
------------------------------------------------------
    Date: 20200903-143811
------------------------------------------------------

[*] Analyzing SSL/TLS on 65.61.137.117:443 ...
    [.] Output directory: TLSSLed_1.3_65.61.137.117_443_20200903-143811 ...

[*] Checking if the target service speaks SSL/TLS...
    [.] The target service 65.61.137.117:443 seems to speak SSL/TLS...

    [.] Using SSL/TLS protocol version: 
        (empty means I'm using the default openssl protocol version(s))

[*] Running sslscan on 65.61.137.117:443 ...

    [-] Testing for SSLv2 ...

    [-] Testing for the NULL cipher ...

    [-] Testing for weak ciphers (based on key length - 40 or 56 bits) ...

    [+] Testing for strong ciphers (based on AES) ...
Accepted  TLSv1.2  256 bits  ECDHE-RSA-AES256-SHA384       Curve P-256 DHE 256
Accepted  TLSv1.2  256 bits  ECDHE-RSA-AES256-SHA          Curve P-256 DHE 256
Accepted  TLSv1.2  256 bits  DHE-RSA-AES256-GCM-SHA384     DHE 1024 bits
Accepted  TLSv1.2  256 bits  DHE-RSA-AES256-SHA256         DHE 1024 bits
Accepted  TLSv1.2  256 bits  DHE-RSA-AES256-SHA            DHE 1024 bits
Accepted  TLSv1.2  128 bits  ECDHE-RSA-AES128-GCM-SHA256   Curve P-256 DHE 256
Accepted  TLSv1.2  128 bits  ECDHE-RSA-AES128-SHA256       Curve P-256 DHE 256
Accepted  TLSv1.2  128 bits  ECDHE-RSA-AES128-SHA          Curve P-256 DHE 256
Accepted  TLSv1.2  128 bits  DHE-RSA-AES128-GCM-SHA256     DHE 1024 bits
Accepted  TLSv1.2  128 bits  DHE-RSA-AES128-SHA256         DHE 1024 bits
Accepted  TLSv1.2  128 bits  DHE-RSA-AES128-SHA            DHE 1024 bits
Accepted  TLSv1.1  256 bits  DHE-RSA-AES256-SHA            DHE 1024 bits
Accepted  TLSv1.1  128 bits  ECDHE-RSA-AES128-SHA          Curve P-256 DHE 256
Accepted  TLSv1.1  128 bits  DHE-RSA-AES128-SHA            DHE 1024 bits
Accepted  TLSv1.0  256 bits  DHE-RSA-AES256-SHA            DHE 1024 bits
Accepted  TLSv1.0  128 bits  ECDHE-RSA-AES128-SHA          Curve P-256 DHE 256
Accepted  TLSv1.0  128 bits  DHE-RSA-AES128-SHA            DHE 1024 bits

    [-] Testing for MD5 signed certificate ...

    [.] Testing for the certificate public key length ...

    [.] Testing for the certificate subject ...
Subject:  demo.testfire.net

    [.] Testing for the certificate CA issuer ...
Issuer:   Sectigo RSA Domain Validation Secure Server CA

    [.] Testing for the certificate validity period ...
    Today: Thu 03 Sep 2020 09:08:54 AM UTC
Not valid before: May 22 00:00:00 2020 GMT
Not valid after:  May 22 23:59:59 2022 GMT

    [.] Checking preferred server ciphers ...


[*] Testing for SSL/TLS renegotiation MitM vuln. (CVE-2009-3555) ...

    [+] Testing for secure renegotiation support (RFC 5746) ...
    Secure Renegotiation IS supported

[*] Testing for SSL/TLS renegotiation DoS vuln. (CVE-2011-1473) ...

    [.] Testing for client initiated (CI) SSL/TLS renegotiation (secure)...
    UNKNOWN

    [.] Testing for client initiated (CI) SSL/TLS renegotiation (insecure)...
    UNKNOWN

[*] Testing for client authentication using digital certificates ...

    SSL/TLS client certificate authentication IS NOT required

[*] Testing for TLS v1.1 and v1.2 (CVE-2011-3389 vuln. aka BEAST) ...

    [-] Testing for SSLv3 and TLSv1 support ...
Accepted  TLSv1.2  256 bits  ECDHE-RSA-AES256-SHA384       Curve P-256 DHE 256
Accepted  TLSv1.2  256 bits  ECDHE-RSA-AES256-SHA          Curve P-256 DHE 256
Accepted  TLSv1.2  256 bits  DHE-RSA-AES256-GCM-SHA384     DHE 1024 bits
Accepted  TLSv1.2  256 bits  DHE-RSA-AES256-SHA256         DHE 1024 bits
Accepted  TLSv1.2  256 bits  DHE-RSA-AES256-SHA            DHE 1024 bits
Accepted  TLSv1.2  128 bits  ECDHE-RSA-AES128-GCM-SHA256   Curve P-256 DHE 256
Accepted  TLSv1.2  128 bits  ECDHE-RSA-AES128-SHA256       Curve P-256 DHE 256
Accepted  TLSv1.2  128 bits  ECDHE-RSA-AES128-SHA          Curve P-256 DHE 256
Accepted  TLSv1.2  128 bits  DHE-RSA-AES128-GCM-SHA256     DHE 1024 bits
Accepted  TLSv1.2  128 bits  DHE-RSA-AES128-SHA256         DHE 1024 bits
Accepted  TLSv1.2  128 bits  DHE-RSA-AES128-SHA            DHE 1024 bits
Accepted  TLSv1.1  256 bits  DHE-RSA-AES256-SHA            DHE 1024 bits
Accepted  TLSv1.1  128 bits  ECDHE-RSA-AES128-SHA          Curve P-256 DHE 256
Accepted  TLSv1.1  128 bits  DHE-RSA-AES128-SHA            DHE 1024 bits

    [+] Testing for RC4 in the prefered cipher(s) list ...

    [.] Testing for TLS v1.1 support ...
    TLS v1.1 IS supported

    [.] Testing for TLS v1.2 support ...
    TLS v1.2 IS supported

[*] Testing for HTTPS (SSL/TLS) security headers using HTTP/1.0 ...

    [+] Testing for HTTP Strict-Transport-Security (HSTS) header ...

    [+] Testing for cookies with the secure flag ...
Set-Cookie: JSESSIONID=1672C0C04E6B30C4B35BA958175305CD; Path=/; Secure; HttpOnly

    [-] Testing for cookies without the secure flag ...

[*] Testing for HTTPS (SSL/TLS) security headers using HTTP/1.1 & Host ...

    [+] Testing for HTTP Strict-Transport-Security (HSTS) header ...

    [+] Testing for cookies with the secure flag ...
Set-Cookie: JSESSIONID=3FF6BE7CAF5ECD40447CC801F6D845BE; Path=/; Secure; HttpOnly

    [-] Testing for cookies without the secure flag ...

[*] New files created:
    [.] Output directory: TLSSLed_1.3_65.61.137.117_443_20200903-143811 ...

openssl_HEAD_1.0_65.61.137.117_443_20200903-143811.err	openssl_RENEG_65.61.137.117_443_20200903-143811.log
openssl_HEAD_1.0_65.61.137.117_443_20200903-143811.log	openssl_RENEG_LEGACY_65.61.137.117_443_20200903-143811.err
openssl_HEAD_65.61.137.117_443_20200903-143811.err	openssl_RENEG_LEGACY_65.61.137.117_443_20200903-143811.log
openssl_HEAD_65.61.137.117_443_20200903-143811.log	sslscan_65.61.137.117_443_20200903-143811.log
openssl_RENEG_65.61.137.117_443_20200903-143811.err

[*] done

```


