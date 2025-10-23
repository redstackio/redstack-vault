---
id: 45e56af6-807a-44a9-85bd-20b2bb3b3eb1
name: SSLyze Enumerate a Web Server's SSL/TLS Certificate
type: command
executor: bash
data: sslyze --regular $_TARGET_HOST
output: "root@kali:~# sslyze --regular reddit.com\n\nSCAN RESULTS FOR REDDIT.COM:443\
  \ - 151.101.193.140:443\n -----------------------------------------------------\n\
  \n  * Session Renegotiation:\n      Client-initiated Renegotiations:   OK - Rejected\n\
  \      Secure Renegotiation:              OK - Supported\n\n  * Deflate Compression:\n\
  \      OK - Compression disabled          \n\n  * Certificate - Content:\n     \
  \ SHA1 Fingerprint:                  e3c0f1cfcba46109021a74067183cda85928b40d\n\
  \      Common Name:                       *.reddit.com\n      Issuer:          \
  \                  DigiCert SHA2 Secure Server CA\n      Serial Number:        \
  \             075B02DF9DA416512F64CE7071FC8C07\n      Not Before:              \
  \          Aug 17 00:00:00 2018 GMT\n      Not After:                         Sep\
  \  2 12:00:00 2020 GMT\n      Signature Algorithm:               sha256WithRSAEncryption\n\
  \      Public Key Algorithm:              rsaEncryption\n      Key Size:       \
  \                   2048 bit\n      Exponent:                          65537 (0x10001)\n\
  \      X509v3 Subject Alternative Name:   {'DNS': ['*.reddit.com', 'reddit.com',\
  \ '*.redditmedia.com', 'redditmedia.com', '*.redd.it', 'redd.it', 'www.redditstatic.com',\
  \ 'i.reddituploads.com', '*.thumbs.redditmedia.com', 'www.redditinc.com', 'redditinc.com']}\n\
  \n\n SCAN COMPLETED IN 2.46 S\n ------------------------"
created_at: '2019-10-04T22:01:34.584142+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# SSLyze Enumerate a Web Server's SSL/TLS Certificate

```bash
sslyze --regular $_TARGET_HOST
```

## Expected Output

```
root@kali:~# sslyze --regular reddit.com

SCAN RESULTS FOR REDDIT.COM:443 - 151.101.193.140:443
 -----------------------------------------------------

  * Session Renegotiation:
      Client-initiated Renegotiations:   OK - Rejected
      Secure Renegotiation:              OK - Supported

  * Deflate Compression:
      OK - Compression disabled          

  * Certificate - Content:
      SHA1 Fingerprint:                  e3c0f1cfcba46109021a74067183cda85928b40d
      Common Name:                       *.reddit.com
      Issuer:                            DigiCert SHA2 Secure Server CA
      Serial Number:                     075B02DF9DA416512F64CE7071FC8C07
      Not Before:                        Aug 17 00:00:00 2018 GMT
      Not After:                         Sep  2 12:00:00 2020 GMT
      Signature Algorithm:               sha256WithRSAEncryption
      Public Key Algorithm:              rsaEncryption
      Key Size:                          2048 bit
      Exponent:                          65537 (0x10001)
      X509v3 Subject Alternative Name:   {'DNS': ['*.reddit.com', 'reddit.com', '*.redditmedia.com', 'redditmedia.com', '*.redd.it', 'redd.it', 'www.redditstatic.com', 'i.reddituploads.com', '*.thumbs.redditmedia.com', 'www.redditinc.com', 'redditinc.com']}


 SCAN COMPLETED IN 2.46 S
 ------------------------
```


