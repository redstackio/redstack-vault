---
id: cmd-curl-get-trigger
data: >-
  curl -X GET
  "https://api.mapbox.com/styles/v1/{username}/{style_id}?access_token={your_token}"
  -H "User-Agent: Mozilla/5.0 (compatible; MSIE 11.0; Windows NT 10.0;
  Trident/7.0)"
tags:
  - http
  - api
  - xss
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:55.312Z'
verified: false
validated: true
submitted: true
---
# curl-get-styles-trigger

## Command

```bash
curl -X GET "https://api.mapbox.com/styles/v1/{username}/{style_id}?access_token={your_token}" -H "User-Agent: Mozilla/5.0 (compatible; MSIE 11.0; Windows NT 10.0; Trident/7.0)"
```

## Description

This command retrieves a Mapbox style via GET, simulating an IE11 request to trigger MIME confusion and XSS execution in that browser.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `URL` | API endpoint with placeholders | Yes |
| `-H "User-Agent: ..."` | Mimics IE11 user agent for sniffing simulation | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.mapbox.com/styles/v1/user/style1?access_token=pk.ey..." -H "User-Agent: Mozilla/5.0 (compatible; MSIE 11.0; Windows NT 10.0)"
```

### Advanced Usage

```bash
curl -X GET "https://api.mapbox.com/styles/v1/user/style1?access_token=pk.ey..." -H "User-Agent: Mozilla/5.0 (compatible; MSIE 11.0; Windows NT 10.0)" -v
```

## Expected Output

JSON response with the style data, including the injected script; in IE11 browser, this would execute the script.

## Related

- [[Related Procedure]]
