---
id: 80812520-8c17-4b35-b117-b9929d78d47f
name: Proxychains Redirect an Application's Network Traffic Through a SOCKS Proxy
type: command
executor: bash
data: proxychains $_PROGRAM
output: 'root@kali:~# proxychains firefox

  [proxychains] config file found: /etc/proxychains.conf

  [proxychains] preloading /usr/lib/x86_64-linux-gnu/libproxychains.so.4

  [proxychains] DLL init: proxychains-ng 4.14

  [proxychains] DLL init: proxychains-ng 4.14

  [proxychains] DLL init: proxychains-ng 4.14

  [proxychains] DLL init: proxychains-ng 4.14

  [proxychains] DLL init: proxychains-ng 4.14

  [proxychains] Strict chain  ...  127.0.0.1:9050  ...  google.com:80  ...  OK

  [proxychains] Strict chain  ...  127.0.0.1:9050  ...  detectportal.firefox.com:80  ...  OK

  [proxychains] Strict chain  ...  127.0.0.1:9050  ...  getpocket.cdn.mozilla.net:443  ...  OK

  [proxychains] Strict chain  ...  127.0.0.1:9050  ...  getpocket.cdn.mozilla.net:443  ...  OK

  [proxychains] Strict chain  ...  127.0.0.1:9050  ...  ocsp.digicert.com:80  ...  OK'
created_at: '2019-10-02T01:17:50.984250+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Proxychains]]'
---

# Proxychains Redirect an Application's Network Traffic Through a SOCKS Proxy

```bash
proxychains $_PROGRAM
```

## Expected Output

```
root@kali:~# proxychains firefox
[proxychains] config file found: /etc/proxychains.conf
[proxychains] preloading /usr/lib/x86_64-linux-gnu/libproxychains.so.4
[proxychains] DLL init: proxychains-ng 4.14
[proxychains] DLL init: proxychains-ng 4.14
[proxychains] DLL init: proxychains-ng 4.14
[proxychains] DLL init: proxychains-ng 4.14
[proxychains] DLL init: proxychains-ng 4.14
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  google.com:80  ...  OK
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  detectportal.firefox.com:80  ...  OK
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  getpocket.cdn.mozilla.net:443  ...  OK
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  getpocket.cdn.mozilla.net:443  ...  OK
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  ocsp.digicert.com:80  ...  OK
```


