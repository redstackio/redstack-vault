---
type: command
executor: bash
data: proxychains $_PROGRAM
output: >-
  root@kali:~# proxychains firefox

  [proxychains] config file found: /etc/proxychains.conf

  [proxychains] preloading /usr/lib/x86_64-linux-gnu/libproxychains.so.4

  [proxychains] DLL init: proxychains-ng 4.14

  [proxychains] DLL init: proxychains-ng 4.14

  [proxychains] DLL init: proxychains-ng 4.14

  [proxychains] DLL init: proxychains-ng 4.14

  [proxychains] DLL init: proxychains-ng 4.14

  [proxychains] Strict chain  ...  127.0.0.1:9050  ...  google.com:80  ...  OK

  [proxychains] Strict chain  ...  127.0.0.1:9050  ... 
  detectportal.firefox.com:80  ...  OK

  [proxychains] Strict chain  ...  127.0.0.1:9050  ... 
  getpocket.cdn.mozilla.net:443  ...  OK

  [proxychains] Strict chain  ...  127.0.0.1:9050  ... 
  getpocket.cdn.mozilla.net:443  ...  OK

  [proxychains] Strict chain  ...  127.0.0.1:9050  ...  ocsp.digicert.com:80 
  ...  OK
platforms:
  - Linux
tags:
  - proxy
  - tunnel
verified: true
validated: true
---

# Proxychains Redirect an Application's Network Traffic Through a SOCKS Proxy

## Command

```bash
proxychains $_PROGRAM
```

## Description

This command forces any TCP-based application to route its network traffic through a pre-configured proxy chain, typically a SOCKS proxy established via SSH. Use it to pivot traffic through a compromised host during reconnaissance or exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PROGRAM | The executable or command to proxy (e.g., firefox, nmap, curl) | Yes |

## Examples

### Basic Usage

```bash
proxychains firefox
```

Launches Firefox with all traffic routed through the SOCKS proxy.

### Advanced Usage

```bash
proxychains nmap -sV 10.0.0.0/24
```

Scans an internal network via the proxy.

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

The application launches normally, with proxy chain logs showing successful routing ("OK" status).

## Related

- [[procedures/dynamic-port-forwarding-with-ssh-socks-proxy]]
- [[tools/Proxychains]]
