---
id: 150b2fd7-4d96-4b71-933f-52722dbb5c6d
name: SSLyze Command to Scan a Website
type: command
executor: ''
data: sslyze --regular demo.testfire.net:443
output: " AVAILABLE PLUGINS\n -----------------\n\n  PluginHeartbleed\n  PluginCompression\n\
  \  PluginOpenSSLCipherSuites\n  PluginCertInfo\n  PluginHSTS\n  PluginChromeSha1Deprecation\n\
  \  PluginSessionResumption\n  PluginSessionRenegotiation\n\n\n\n CHECKING HOST(S)\
  \ AVAILABILITY\n -----------------------------\n\n   demo.testfire.net:443     \
  \          => 65.61.137.117:443\n\n\n\n SCAN RESULTS FOR DEMO.TESTFIRE.NET:443 -\
  \ 65.61.137.117:443\n ----------------------------------------------------------\n\
  \n  * Deflate Compression:\n      OK - Compression disabled          \n\n  * Certificate\
  \ - Content:\n      SHA1 Fingerprint:                  b300b3806bb4ac2032365cc08051fa5fa97e1342\n\
  \      Common Name:                       demo.testfire.net\n      Issuer:     \
  \                       Sectigo RSA Domain Validation Secure Server CA\n      Serial\
  \ Number:                     6F1E3106C2F1A86613B7257D75DFED44\n      Not Before:\
  \                        May 22 00:00:00 2020 GMT\n      Not After:            \
  \             May 22 23:59:59 2022 GMT\n      Signature Algorithm:             \
  \  sha256WithRSAEncryption\n      Public Key Algorithm:              rsaEncryption\n\
  \      Key Size:                          2048 bit\n      Exponent:            \
  \              65537 (0x10001)\n      X509v3 Subject Alternative Name:   {'DNS':\
  \ ['demo.testfire.net', 'altoromutual.com']}\n\n  * Certificate - Trust:\n     \
  \ Hostname Validation:               OK - Subject Alternative Name matches\n   \
  \   Google CA Store (09/2015):         FAILED - Certificate is NOT Trusted: unable\
  \ to get local issuer certificate\n      Java 6 CA Store (Update 65):       FAILED\
  \ - Certificate is NOT Trusted: unable to get local issuer certificate\n      Microsoft\
  \ CA Store (09/2015):      FAILED - Certificate is NOT Trusted: unable to get local\
  \ issuer certificate\n      Mozilla NSS CA Store (09/2015):    FAILED - Certificate\
  \ is NOT Trusted: unable to get local issuer certificate\n      Apple CA Store (OS\
  \ X 10.10.5):     FAILED - Certificate is NOT Trusted: unable to get local issuer\
  \ certificate\n      Certificate Chain Received:        ['demo.testfire.net', 'USERTrust\
  \ RSA Certification Authority', 'AAA Certificate Services']\n\n  * Certificate -\
  \ OCSP Stapling:\n      NOT SUPPORTED - Server did not send back an OCSP response.\n\
  \n  * OpenSSL Heartbleed:\n      OK - Not vulnerable to Heartbleed  \n\n  * Session\
  \ Resumption:\n      With Session IDs:                  NOT SUPPORTED (0 successful,\
  \ 5 failed, 0 errors, 5 total attempts).\n      With TLS Session Tickets:      \
  \    NOT SUPPORTED - TLS ticket not assigned.\n\n  * SSLV2 Cipher Suites:\n    \
  \  Server rejected all cipher suites.\n\nUnhandled exception when processing --reneg:\
  \ \nsocket.timeout - timed out\n\n  * TLSV1_2 Cipher Suites:\n      Preferred: \
  \                      \n                 ECDHE-RSA-AES256-GCM-SHA384   ECDH-256\
  \ bits  256 bits      HTTP 200 OK                        \n      Accepted:     \
  \                   \n                 ECDHE-RSA-AES256-SHA384       ECDH-256 bits\
  \  256 bits      HTTP 200 OK                        \n                 ECDHE-RSA-AES256-SHA\
  \          ECDH-256 bits  256 bits      HTTP 200 OK                        \n  \
  \               ECDHE-RSA-AES256-GCM-SHA384   ECDH-256 bits  256 bits      HTTP\
  \ 200 OK                        \n                 DHE-RSA-AES256-SHA256       \
  \  DH-1024 bits   256 bits      HTTP 200 OK                        \n          \
  \       DHE-RSA-AES256-SHA            DH-1024 bits   256 bits      HTTP 200 OK \
  \                       \n                 DHE-RSA-AES256-GCM-SHA384     DH-1024\
  \ bits   256 bits      HTTP 200 OK                        \n                 ECDHE-RSA-AES128-SHA256\
  \       ECDH-256 bits  128 bits      HTTP 200 OK                        \n     \
  \            ECDHE-RSA-AES128-SHA          ECDH-256 bits  128 bits      HTTP 200\
  \ OK                        \n                 ECDHE-RSA-AES128-GCM-SHA256   ECDH-256\
  \ bits  128 bits      HTTP 200 OK                        \n                 DHE-RSA-AES128-SHA256\
  \         DH-1024 bits   128 bits      HTTP 200 OK                        \n   \
  \              DHE-RSA-AES128-SHA            DH-1024 bits   128 bits      HTTP 200\
  \ OK                        \n                 DHE-RSA-AES128-GCM-SHA256     DH-1024\
  \ bits   128 bits      HTTP 200 OK                        \n\n  * TLSV1_1 Cipher\
  \ Suites:\n      Preferred:                       \n                 ECDHE-RSA-AES256-SHA\
  \          ECDH-256 bits  256 bits      HTTP 200 OK                        \n  \
  \    Accepted:                        \n                 ECDHE-RSA-AES256-SHA  \
  \        ECDH-256 bits  256 bits      HTTP 200 OK                        \n    \
  \             DHE-RSA-AES256-SHA            DH-1024 bits   256 bits      HTTP 200\
  \ OK                        \n                 ECDHE-RSA-AES128-SHA          ECDH-256\
  \ bits  128 bits      HTTP 200 OK                        \n                 DHE-RSA-AES128-SHA\
  \            DH-1024 bits   128 bits      HTTP 200 OK                        \n\n\
  \  * TLSV1 Cipher Suites:\n      Preferred:                       \n           \
  \      ECDHE-RSA-AES256-SHA          ECDH-256 bits  256 bits      HTTP 200 OK  \
  \                      \n      Accepted:                        \n             \
  \    ECDHE-RSA-AES256-SHA          ECDH-256 bits  256 bits      HTTP 200 OK    \
  \                    \n                 DHE-RSA-AES256-SHA            DH-1024 bits\
  \   256 bits      HTTP 200 OK                        \n                 ECDHE-RSA-AES128-SHA\
  \          ECDH-256 bits  128 bits      HTTP 200 OK                        \n  \
  \               DHE-RSA-AES128-SHA            DH-1024 bits   128 bits      HTTP\
  \ 200 OK                        \n\n  * SSLV3 Cipher Suites:\n      Server rejected\
  \ all cipher suites.\n"
created_at: '2020-09-03T13:49:07.555003+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# SSLyze Command to Scan a Website

```bash
sslyze --regular demo.testfire.net:443
```

## Expected Output

```
 AVAILABLE PLUGINS
 -----------------

  PluginHeartbleed
  PluginCompression
  PluginOpenSSLCipherSuites
  PluginCertInfo
  PluginHSTS
  PluginChromeSha1Deprecation
  PluginSessionResumption
  PluginSessionRenegotiation



 CHECKING HOST(S) AVAILABILITY
 -----------------------------

   demo.testfire.net:443               => 65.61.137.117:443



 SCAN RESULTS FOR DEMO.TESTFIRE.NET:443 - 65.61.137.117:443
 ----------------------------------------------------------

  * Deflate Compression:
      OK - Compression disabled          

  * Certificate - Content:
      SHA1 Fingerprint:                  b300b3806bb4ac2032365cc08051fa5fa97e1342
      Common Name:                       demo.testfire.net
      Issuer:                            Sectigo RSA Domain Validation Secure Server CA
      Serial Number:                     6F1E3106C2F1A86613B7257D75DFED44
      Not Before:                        May 22 00:00:00 2020 GMT
      Not After:                         May 22 23:59:59 2022 GMT
      Signature Algorithm:               sha256WithRSAEncryption
      Public Key Algorithm:              rsaEncryption
      Key Size:                          2048 bit
      Exponent:                          65537 (0x10001)
      X509v3 Subject Alternative Name:   {'DNS': ['demo.testfire.net', 'altoromutual.com']}

  * Certificate - Trust:
      Hostname Validation:               OK - Subject Alternative Name matches
      Google CA Store (09/2015):         FAILED - Certificate is NOT Trusted: unable to get local issuer certificate
      Java 6 CA Store (Update 65):       FAILED - Certificate is NOT Trusted: unable to get local issuer certificate
      Microsoft CA Store (09/2015):      FAILED - Certificate is NOT Trusted: unable to get local issuer certificate
      Mozilla NSS CA Store (09/2015):    FAILED - Certificate is NOT Trusted: unable to get local issuer certificate
      Apple CA Store (OS X 10.10.5):     FAILED - Certificate is NOT Trusted: unable to get local issuer certificate
      Certificate Chain Received:        ['demo.testfire.net', 'USERTrust RSA Certification Authority', 'AAA Certificate Services']

  * Certificate - OCSP Stapling:
      NOT SUPPORTED - Server did not send back an OCSP response.

  * OpenSSL Heartbleed:
      OK - Not vulnerable to Heartbleed  

  * Session Resumption:
      With Session IDs:                  NOT SUPPORTED (0 successful, 5 failed, 0 errors, 5 total attempts).
      With TLS Session Tickets:          NOT SUPPORTED - TLS ticket not assigned.

  * SSLV2 Cipher Suites:
      Server rejected all cipher suites.

Unhandled exception when processing --reneg: 
socket.timeout - timed out

  * TLSV1_2 Cipher Suites:
      Preferred:                       
                 ECDHE-RSA-AES256-GCM-SHA384   ECDH-256 bits  256 bits      HTTP 200 OK                        
      Accepted:                        
                 ECDHE-RSA-AES256-SHA384       ECDH-256 bits  256 bits      HTTP 200 OK                        
                 ECDHE-RSA-AES256-SHA          ECDH-256 bits  256 bits      HTTP 200 OK                        
                 ECDHE-RSA-AES256-GCM-SHA384   ECDH-256 bits  256 bits      HTTP 200 OK                        
                 DHE-RSA-AES256-SHA256         DH-1024 bits   256 bits      HTTP 200 OK                        
                 DHE-RSA-AES256-SHA            DH-1024 bits   256 bits      HTTP 200 OK                        
                 DHE-RSA-AES256-GCM-SHA384     DH-1024 bits   256 bits      HTTP 200 OK                        
                 ECDHE-RSA-AES128-SHA256       ECDH-256 bits  128 bits      HTTP 200 OK                        
                 ECDHE-RSA-AES128-SHA          ECDH-256 bits  128 bits      HTTP 200 OK                        
                 ECDHE-RSA-AES128-GCM-SHA256   ECDH-256 bits  128 bits      HTTP 200 OK                        
                 DHE-RSA-AES128-SHA256         DH-1024 bits   128 bits      HTTP 200 OK                        
                 DHE-RSA-AES128-SHA            DH-1024 bits   128 bits      HTTP 200 OK                        
                 DHE-RSA-AES128-GCM-SHA256     DH-1024 bits   128 bits      HTTP 200 OK                        

  * TLSV1_1 Cipher Suites:
      Preferred:                       
                 ECDHE-RSA-AES256-SHA          ECDH-256 bits  256 bits      HTTP 200 OK                        
      Accepted:                        
                 ECDHE-RSA-AES256-SHA          ECDH-256 bits  256 bits      HTTP 200 OK                        
                 DHE-RSA-AES256-SHA            DH-1024 bits   256 bits      HTTP 200 OK                        
                 ECDHE-RSA-AES128-SHA          ECDH-256 bits  128 bits      HTTP 200 OK                        
                 DHE-RSA-AES128-SHA            DH-1024 bits   128 bits      HTTP 200 OK                        

  * TLSV1 Cipher Suites:
      Preferred:                       
                 ECDHE-RSA-AES256-SHA          ECDH-256 bits  256 bits      HTTP 200 OK                        
      Accepted:                        
                 ECDHE-RSA-AES256-SHA          ECDH-256 bits  256 bits      HTTP 200 OK                        
                 DHE-RSA-AES256-SHA            DH-1024 bits   256 bits      HTTP 200 OK                        
                 ECDHE-RSA-AES128-SHA          ECDH-256 bits  128 bits      HTTP 200 OK                        
                 DHE-RSA-AES128-SHA            DH-1024 bits   128 bits      HTTP 200 OK                        

  * SSLV3 Cipher Suites:
      Server rejected all cipher suites.

```


