---
id: 2a5473aa-f787-43f9-a6f8-92a72a05cc7d
name: start-oob-xxe-server-with-230-py
type: command
executor: bash
data: python3 230.py $_PORT
output: null
created_at: '2023-04-06T03:56:43.973161+00:00'
updated_at: '2023-04-10T20:24:45.357412+00:00'
platforms:
  - Linux
tags:
  - xxe
  - oob
  - exfiltration
verified: true
validated: true
---

# start-oob-xxe-server-with-230-py

## Command

```bash
python3 230.py $_PORT
```

## Description

Initiates an out-of-band XXE server using the 230.py script to receive exfiltrated data over FTP or HTTP.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PORT | Listening port for OOB callbacks (default: 2121) | Yes |

## Examples

### Basic Usage

```bash
python3 230.py 2121
```

## Expected Output

OOB server listening on port 2121, awaiting XXE data requests.

## Related

- [[procedures/Exploit-XXE-Vulnerability-Using-Multiple-Tools]]
- [[tools/230-OOB-XXE]]
