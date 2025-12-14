---
id: cmd-curl-tiktok-profile
data: >-
  curl -s "https://www.tiktok.com/@username" -H "User-Agent: Mozilla/5.0" | grep
  -o 'join_date:\"[^\"]*\"' || grep -o 'creation_time:\"[^\"]*\"'
tags:
  - recon
  - web
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:13.118Z'
verified: false
validated: true
submitted: true
---
# curl-profile-fetch

## Command

```bash
curl -s "https://www.tiktok.com/@username" -H "User-Agent: Mozilla/5.0" | grep -o 'join_date:\"[^\"]*\"' || grep -o 'creation_time:\"[^\"]*\"'
```

## Description

This command uses curl to fetch a TikTok user's profile page silently and grep to extract the account creation or join date from the response. It is used in reconnaissance to disclose user metadata without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, suppresses progress meter | Yes |
| `"https://www.tiktok.com/@username"` | Target profile URL, replace 'username' with actual handle | Yes |
| `-H "User-Agent: Mozilla/5.0"` | Mimics browser to avoid bot detection | No |
| `grep -o 'join_date:\"[^\"]*\"'` | Regex pattern to match creation date field | Yes |

## Examples

### Basic Usage

```bash
curl -s "https://www.tiktok.com/@exampleuser" | grep -o 'join_date:\"[^\"]*\"'
```

### Advanced Usage

```bash
curl -s "https://www.tiktok.com/@exampleuser" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)" | grep -o 'creation_time:\"[^\"]*\"' > date.txt
```

## Expected Output

A string like "join_date:\"2022-05-06\"" indicating the account creation date. If no match, the command outputs nothing, suggesting the field name varies or access is restricted.

## Related

- [[Related Procedure]]
