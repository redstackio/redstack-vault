---
id: f3d7ceb0-63a8-4dd4-823e-dfd206e244f3
name: nikto-scan-web-application
type: command
executor: bash
data: nikto -h $_TARGET_URL
output: null
created_at: '2020-08-19T16:08:58.983461+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Web
tags:
  - vulnerability-scanning
  - web
verified: true
validated: true
---

# nikto-scan-web-application

## Command

```bash
nikto -h $_TARGET_URL
```

## Description

This command runs Nikto to perform a vulnerability scan on a specified web application URL, checking for common issues like server misconfigurations, outdated software, and potential attack vectors such as enabled HTTP methods or missing security headers. Use it during initial reconnaissance to quickly identify low-hanging fruit in web targets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -h | Specifies the target host/URL to scan (e.g., http://example.com/path) | Yes |
| $_TARGET_URL | The full URL of the web application or page to scan | Yes |
| -o | Optional: Output file for saving results (e.g., -o scan.txt) | No |
| -Format | Optional: Format for output file (txt, html, xml) | No |

## Examples

### Basic Usage

```bash
nikto -h http://192.168.1.100/vulnerable-app/login.php
```

### Advanced Usage

```bash
nikto -h http://example.com -o results.txt -Format html -Tuning 123
```

This tunes the scan to focus on injection, remote file retrieval, and software-specific checks.

## Expected Output

Nikto will display real-time findings, such as:

```
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          192.168.1.100
+ Target Hostname:    192.168.1.100
+ Target Port:        80
+ Start Time:         2023-10-01 12:00:00 (UTC)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Unix) OpenSSL/1.1.1 PHP/7.4.0
+ Retrieved x-powered-by header: PHP/7.4.0
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined.
+ OSVDB-877: HTTP TRACE method is active, suggesting the host is vulnerable to XST.
+ OSVDB-44056: /login.php/... : Potential vulnerable endpoint detected.
+ 7539 requests: 0 error(s) and 8 item(s) reported on remote host
+ End Time:           2023-10-01 12:00:30 (UTC) (30 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

Success is indicated by a list of vulnerabilities with OSVDB/CVE references; zero items may mean a secure or non-responsive target.

## Related

- [[procedures/using-nikto-to-scan-for-common-web-vulnerabilities]]
- [[tools/Nikto]]
