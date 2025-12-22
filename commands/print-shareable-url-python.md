---
data: >-
  print(f'[*] URL TO
  SHARE:\n{response.json()["file"]["downloadUrl"]}?action=view')
tags:
  - output
  - url
type: command
output: URL to share with victim
executor: python
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:38.388Z'
id: 00bb6c76-8adc-459b-80c5-a64196284bde
verified: false
validated: true
submitted: true
---
# print-shareable-url-python

## Command

```python
print(f'[*] URL TO SHARE:\n{response.json()["file"]["downloadUrl"]}?action=view')
```

## Description

Prints the download URL with ?action=view parameter for sharing with the victim.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| response | Upload response | Yes |

## Examples

### Basic Usage

```python
print(f'[*] URL TO SHARE:\n{response.json()["file"]["downloadUrl"]}?action=view')
```

## Expected Output

Formatted string with the shareable URL.

## Related

- [[commands/post-file-upload-python]]
