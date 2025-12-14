---
data: >-
  curl "https://api.hackerone.com/v1/hackers/programs/{handle}/weaknesses" -X
  GET -u "mrtst:XXXXXXXXXXXXXXXXXXXX=" -H 'Accept: application/json'
tags:
  - api
  - hackerone
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.452Z'
id: 9faaa29d-0952-425d-b238-932cf23bbea4
verified: false
validated: true
submitted: true
---
# curl-hackerone-fetch-program-weaknesses

## Command

```bash
curl "https://api.hackerone.com/v1/hackers/programs/{handle}/weaknesses" -X GET -u "mrtst:XXXXXXXXXXXXXXXXXXXX=" -H 'Accept: application/json'
```

## Description

Retrieves weaknesses for a specific HackerOne program using the old token post-ban.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `{handle}` | Program handle (e.g., 'program-name') | Yes |
| `-u` | Basic auth | Yes |
| URL | Weaknesses endpoint | Yes |
| `-H` | JSON accept | Yes |

## Examples

### Basic Usage

```bash
curl "https://api.hackerone.com/v1/hackers/programs/example/weaknesses" -X GET -u "mrtst:XXXXXXXXXXXXXXXXXXXX=" -H 'Accept: application/json'
```

## Expected Output

JSON list of weaknesses associated with the program.

## Related

- [[commands/curl-hackerone-fetch-programs]]
- [[procedures/Exploit-HackerOne-API-with-Old-Token]]
