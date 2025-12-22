---
type: command
executor: bash
data: 'nikto -host http://$_TARGET_URL'
output: Sample output showing vulnerabilities and server info
platforms:
  - Linux
tags:
  - web-scanning
  - enumeration
verified: true
validated: true
---

# nikto-scan-host

## Command

```bash
nikto -host http://$_TARGET_URL
```

## Description

This command performs a basic scan of a web server using Nikto, identifying potential vulnerabilities, misconfigurations, and outdated software by sending multiple requests and checking against a database of known issues.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | The URL of the target web server (e.g., http://example.com or https://example.com) | Yes |
| -host | Specifies the target host to scan | Built-in |

## Examples

### Basic Usage

```bash
nikto -host http://10.10.10.10
```

### HTTPS Scan

```bash
nikto -host https://example.com
```

## Expected Output

```
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.10.10
+ Target Hostname:    10.10.10.10
+ Target Port:        80
+ Start Time:         2019-09-13 22:39:46 (GMT-4)
---------------------------------------------------------------------------
+ Server: Apache/2.4.29 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /, fields: 0x2aa6 0x59277789d6649 
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: GET, POST, OPTIONS, HEAD 
+ OSVDB-3233: /icons/README: Apache default file found.
+ 7499 requests: 0 error(s) and 6 item(s) reported on remote host
+ End Time:           2019-09-13 22:40:01 (GMT-4) (15 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

## Related

- [[Related Procedure: Web Server Enumeration]]
- [[tools/Nikto]]
