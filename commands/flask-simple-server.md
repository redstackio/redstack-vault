---
id: cmd-uuid-002
data: |-
  from flask import Flask
  app = Flask(__name__)
  @app.route('/')
  def index():
      return 'FindVuln'
  if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80, threaded=True)
tags:
  - server
  - testing
  - flask
type: command
output: null
executor: python
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.499Z'
verified: false
validated: true
submitted: true
---
# flask-simple-server

## Command

```python
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'FindVuln'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, threaded=True)
```

## Description

Starts a minimal Flask web server on port 80 to handle and respond to SSRF test requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `host='0.0.0.0'` | Binds to all interfaces | Yes |
| `port=80` | Listens on HTTP port | Yes |
| `threaded=True` | Enables threading for concurrent requests | Yes |

## Examples

### Basic Usage

Save to server.py and run `python server.py`.

### Advanced Usage

Add logging:

```python
app.logger.info('Request received')
return 'FindVuln'
```

## Expected Output

Server startup: '* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:80'. Logs requests as they arrive.

## Related

- [[commands/curl-gbk-ssrf-test]]
- [[procedures/Setup-Local-HTTP-Server-for-Testing]]
