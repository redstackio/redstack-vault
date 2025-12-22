---
data: print(response.text)
tags:
  - debug
  - print
type: command
output: Response body as text
executor: python
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:38.399Z'
id: 38f784c2-b362-4b24-8175-3fefe2d31397
verified: false
validated: true
submitted: true
---
# print-response-text-python

## Command

```python
print(response.text)
```

## Description

Prints the raw text of the HTTP response for debugging purposes after API calls.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| response | Requests response object | Yes |

## Examples

### Basic Usage

```python
print(response.text)
```

## Expected Output

String representation of response body.

## Related

- [[commands/post-upload-metadata-python]]
