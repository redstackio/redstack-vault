---
data: python .\poc.py
tags:
  - exploit
  - server
type: command
output: Malicious server starts listening on port 1337
executor: cmd
platforms:
  - Windows
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.568Z'
id: 3a84f011-7a47-4d69-8e36-63d6f3ebc3c5
verified: false
validated: true
submitted: true
---
# run-poc-script

## Command

```cmd
python .\poc.py
```

## Description

Executes the Python-based PoC script to launch the malicious CS:GO server, handling protobuf messages and HTTP exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| poc.py | Path to the main exploit script | Yes |

## Examples

### Basic Usage

```cmd
python .\poc.py
```

### Advanced Usage

With arguments for custom port:
```cmd
python .\poc.py --port 1337
```

## Expected Output

Server startup message: 'Malicious server starts listening on port 1337' followed by logs of connections.

## Related

- [[commands/activate-poc-env]]
