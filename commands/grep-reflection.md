---
id: cmd-uuid-5
data: >-
  curl "https://accounts.firefox.com/settings?flowId=test123" | grep -i
  "test123"
tags:
  - grep
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:23.616Z'
verified: false
validated: true
submitted: true
---
# grep-reflection

## Command

```bash
curl "https://accounts.firefox.com/settings?flowId=test123" | grep -i "test123"
```

## Description

Searches the response for the reflected parameter value to confirm injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i | Case-insensitive search | No |

## Examples

### Basic Usage

```bash
curl ... | grep -i "test123"
```

## Expected Output

Lines containing 'test123' from HTML, indicating reflection.

## Related

- [[commands/curl-fetch-settings]]
