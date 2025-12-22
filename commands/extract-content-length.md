---
data: 'content_length = re.search(''Content-Length: (\d+)'', attack).group(1)'
tags:
  - scripting
  - regex
type: command
executor: python
platforms:
  - Web
id: 58c5a3e9-a6ed-4955-afd2-5136c7a643c2
created_at: '2025-12-13T09:01:22.456Z'
updated_at: '2025-12-13T09:01:22.456Z'
verified: false
validated: true
submitted: true
---
# Extract Content Length

## Command

```python
content_length = re.search('Content-Length: (\d+)', attack).group(1)
```

## Description

Extracts the Content-Length value from the attack request using regex.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `re.search` | Searches for pattern | Yes |

## Examples

### Basic Usage

```python
content_length = re.search('Content-Length: (\d+)', attack).group(1)
```

## Expected Output

Numeric Content-Length value.

## Related

- [[procedures/Prepare-Turbo-Intruder-Desync-Script]]
