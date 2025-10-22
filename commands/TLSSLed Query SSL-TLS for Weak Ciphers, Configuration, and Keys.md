---
id: 4ba14af9-d268-4757-89d7-659536fb720c
name: TLSSLed Query SSL/TLS for Weak Ciphers, Configuration, and Keys
type: command
executor: bash
data: tlssled $_TARGET_IP $_TARGET_PORT
output: "root@kali:~/Documents# tlssled 10.10.10.10 443                          \
  \   \n------------------------------------------------------\n TLSSLed - (1.3) based\
  \ on sslscan and openssl                              \n                 by Raul\
  \ Siles (www.taddong.com)\n------------------------------------------------------\
  \              \n    openssl version: OpenSSL 1.1.1a  20 Nov 2018 (Library: OpenSSL\
  \ 1.1.1c  28 May 2019)\n                                                       \
  \                    \n------------------------------------------------------\n\
  \    Date: 20191031-145453            \n------------------------------------------------------\
  \                   \n\n[*] Analyzing SSL/TLS on 10.10.10.10:443 ...           \
  \                                                                              \
  \                 \n    [.] Output directory: TLSSLed_1.3_10.10.10.10_443_20191031-145453\
  \ ...                                                                          \
  \   \n                                                                         \
  \                                                                             \n\
  [*] Checking if the target service speaks SSL/TLS...                           \
  \                                                                       \n    [.]\
  \ The target service 10.10.10.10:443 seems to speak SSL/TLS...       \n\n    [.]\
  \ Using SSL/TLS protocol version:                             \n        (empty means\
  \ I'm using the default openssl protocol version(s))\n                         \
  \                                                  \n[*] Running sslscan on 10.10.10.10:443\
  \ ...\n                                                                        \
  \   \n    [-] Testing for SSLv2 ...        \n\n    [-] Testing for the NULL cipher\
  \ ...\n\n    [-] Testing for weak ciphers (based on key length - 40 or 56 bits)\
  \ ...\n\n    [+] Testing for strong ciphers (based on AES) ...\nAccepted  TLSv1.2\
  \  256 bits  ECDHE-RSA-AES256-SHA384       Curve P-256 DHE 256\nAccepted  TLSv1.2\
  \  256 bits  ECDHE-RSA-AES256-SHA          Curve P-256 DHE 256\nAccepted  TLSv1.2\
  \  256 bits  DHE-RSA-AES256-GCM-SHA384     DHE 2048 bits\nAccepted  TLSv1.2  256\
  \ bits  DHE-RSA-AES256-SHA256         DHE 2048 bits\nAccepted  TLSv1.2  256 bits\
  \  DHE-RSA-AES256-SHA            DHE 2048 bits\n...\n..."
created_at: '2019-10-31T19:29:43.906247+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# TLSSLed Query SSL/TLS for Weak Ciphers, Configuration, and Keys

```bash
tlssled $_TARGET_IP $_TARGET_PORT
```

## Expected Output

```
root@kali:~/Documents# tlssled 10.10.10.10 443                             
------------------------------------------------------
 TLSSLed - (1.3) based on sslscan and openssl                              
                 by Raul Siles (www.taddong.com)
------------------------------------------------------              
    openssl version: OpenSSL 1.1.1a  20 Nov 2018 (Library: OpenSSL 1.1.1c  28 May 2019)

------------------------------------------------------
    Date: 20191031-145453            
------------------------------------------------------                   

[*] Analyzing SSL/TLS on 10.10.10.10:443 ...                                                                                                          
    [.] Output directory: TLSSLed_1.3_10.10.10.10_443_20191031-145453 ...                                                                             

[*] Checking if the target service speaks SSL/TLS...                                                                                                  
    [.] The target service 10.10.10.10:443 seems to speak SSL/TLS...       

    [.] Using SSL/TLS protocol version:                             
        (empty means I'm using the default openssl protocol version(s))

[*] Running sslscan on 10.10.10.10:443 ...

    [-] Testing for SSLv2 ...        

    [-] Testing for the NULL cipher ...

    [-] Testing for weak ciphers (based on key length - 40 or 56 bits) ...

    [+] Testing for strong ciphers (based on AES) ...
Accepted  TLSv1.2  256 bits  ECDHE-RSA-AES256-SHA384       Curve P-256 DHE 256
Accepted  TLSv1.2  256 bits  ECDHE-RSA-AES256-SHA          Curve P-256 DHE 256
Accepted  TLSv1.2  256 bits  DHE-RSA-AES256-GCM-SHA384     DHE 2048 bits
Accepted  TLSv1.2  256 bits  DHE-RSA-AES256-SHA256         DHE 2048 bits
Accepted  TLSv1.2  256 bits  DHE-RSA-AES256-SHA            DHE 2048 bits
...
...
```
