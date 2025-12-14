---
data: >-
  curl "https://api.hackerone.com/v1/hackers/programs" -X GET -u
  "mrtst:XXXXXXXXXXXXXXXXXXXX=" -H 'Accept: application/json'
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
updated_at: '2025-12-14T17:32:48.450Z'
id: 6b6d3a0b-2fcb-41e7-86dc-71b206259992
verified: false
validated: true
submitted: true
---
# curl-hackerone-fetch-programs

## Command

```bash
curl "https://api.hackerone.com/v1/hackers/programs" -X GET -u "mrtst:XXXXXXXXXXXXXXXXXXXX=" -H 'Accept: application/json'
```

## Description

Lists programs associated with the HackerOne user, accessible via banned account token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Username:token auth | Yes |
| URL | Programs endpoint | Yes |
| `-H` | JSON format | Yes |

## Examples

### Basic Usage

```bash
curl "https://api.hackerone.com/v1/hackers/programs" -X GET -u "mrtst:XXXXXXXXXXXXXXXXXXXX=" -H 'Accept: application/json'
```

## Expected Output

JSON array of programs with handles and details.

## Related

- [[commands/curl-hackerone-fetch-program-weaknesses]]
- [[procedures/Exploit-HackerOne-API-with-Old-Token]]
