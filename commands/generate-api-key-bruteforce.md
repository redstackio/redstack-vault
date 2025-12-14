---
data: |-
  import string
  import random
  def id_generator(size=32, char=string.ascii_lowercase + string.digits):
      return ''.join(random.choice(char) for _ in range(size))
  i=1
  while(i<=n):
      print(id_generator())
      i+=1
tags:
  - bruteforce
  - keygen
type: command
output: Printed 32-char alphanumeric strings
executor: python
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:11.254Z'
id: d4dd948d-efcd-4c84-a089-4ceed62161bf
verified: false
validated: true
submitted: true
---
# generate-api-key-bruteforce

## Command

```python
import string
import random
def id_generator(size=32, char=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(char) for _ in range(size))
i=1
while(i<=n):
    print(id_generator())
    i+=1
```

## Description

Generates random 32-character API key candidates using lowercase letters and digits for potential brute-force testing against Semrush API.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `size` | Length of generated key (default 32) | No |
| `char` | Character set (default lowercase + digits) | No |
| `n` | Number of keys to generate | Yes |

## Examples

### Basic Usage

```python
# Set n=100
n=100
# Run the script
```

### Advanced Usage

Modify char for uppercase inclusion.

## Expected Output

Series of lines like: a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6

## Related

- [[procedures/Cross-User-Project-Injection-via-API-Key-Reuse]]
