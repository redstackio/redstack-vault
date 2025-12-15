---
id: cmd-python-requests-get-001
data: |-
  import requests
  response = requests.get(url)
  len(response.text)
tags:
  - http
  - api
  - recon
type: command
output: Response length (0 or 36)
executor: python
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.091Z'
verified: false
validated: true
submitted: true
---
# python-requests-get

## Command

```python
import requests
response = requests.get('https://hackerone.com/reports/%s.json' % report_id)
```

## Description

Sends an HTTP GET request to the HackerOne report endpoint using the requests library and retrieves the response text for length analysis to detect report existence.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | Full URL with report ID placeholder | Yes |
| report_id | Integer ID to query (e.g., 159874) | Yes |

## Examples

### Basic Usage

```python
import requests
response = requests.get('https://hackerone.com/reports/159874.json')
print(len(response.text))  # 0 for submitted
```

### Advanced Usage

```python
import requests
for id in range(159874, 159880):
    response = requests.get(f'https://hackerone.com/reports/{id}.json')
    if len(response.text) == 0:
        print(f'Valid ID: {id}')
```

## Expected Output

Response object; text length 0 for private submitted reports, 36 for non-existent (404 JSON).

## Related

- [[Related Procedure: Poll-for-New-Report-Submissions]]
