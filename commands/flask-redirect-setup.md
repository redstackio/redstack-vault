---
data: |-
  cat > app.py << EOF
  from flask import Flask, redirect

  app = Flask(__name__)

  @app.route('/')
  def redirect_to_server2():
      return redirect('http://server2:8081/', code=302)

  if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8000)
  EOF

  python app.py
tags:
  - flask
  - setup
type: command
output: null
executor: bash
platforms:
  - macOS
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.555Z'
id: 3c1d12de-40a3-4127-951e-d04b19e75148
verified: false
validated: true
submitted: true
---
# flask-redirect-setup

## Command

```bash
cat > app.py << EOF
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def redirect_to_server2():
    return redirect('http://server2:8081/', code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
EOF

python app.py
```

## Description

Creates and runs a Flask application that sets up an HTTP redirect server on port 8000, used to simulate redirect scenarios for testing header leakage in tools like curl.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `app.py` | Output file for Flask script | Yes |
| `server2:8081` | Target redirect URL | Yes |
| `port=8000` | Listening port | Yes |

## Examples

### Basic Usage

```bash
cat > app.py << EOF ... EOF
python app.py
```

### Advanced Usage

```bash
# Customize port and target
sed 's/8000/9000/g; s/server2:8081/target:9090/g' app.py | python
```

## Expected Output

Flask output: '* Running on all addresses (0.0.0.0)\n* Running on http://127.0.0.1:8000\n* Running on http://[::]:8000'. Redirect confirmed via curl test showing 302.

## Related

- [[commands/curl-with-proxy-auth-redirect]]
- [[procedures/Set-Up-Redirect-Server-with-Flask]]
