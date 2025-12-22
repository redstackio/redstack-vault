---
data: python dos.py
tags:
  - dos
  - automation
type: command
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
id: 37939ded-f2b4-4bc6-84d1-63915c91f681
created_at: '2025-12-14T17:32:01.645Z'
updated_at: '2025-12-14T17:32:01.645Z'
verified: false
validated: true
submitted: true
---
# run-dos-python-script

## Command

```bash
python dos.py
```

## Description

This command executes the custom dos.py Python script to automate endless requests to Semmle API endpoints using captured session details, inducing DoS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `dos.py` | The script file with inserted cookie and nonce | Yes |

## Examples

### Basic Usage

```bash
python dos.py
```

### Advanced Usage

Run in background: ```bash
nohup python dos.py > dos.log 2>&1 &
```

## Expected Output

Console output showing request counts, response times, and any errors from the server, e.g., "Sent 100 requests in 10s" or HTTP 500 errors indicating overload.

## Related

- [[procedures/Automate-Excessive-API-Requests-with-Python-Script]]
