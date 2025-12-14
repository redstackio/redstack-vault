---
id: cmd-pip-install-requests
data: pip3 install requests
tags:
  - setup
  - python
type: command
output: Successfully installed requests-2.x.x
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:19.922Z'
verified: false
validated: true
submitted: true
---
# pip3-install-requests

## Command

```bash
pip3 install requests
```

## Description

Installs the Python requests library, essential for making HTTP API calls in the exploit script targeting Rocket.Chat endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | Uses pip3 default | No |

## Examples

### Basic Usage

```bash
pip3 install requests
```

### Advanced Usage

```bash
pip3 install requests==2.28.0
```

## Expected Output

Requirement already satisfied or Successfully installed requests-2.x.x and dependencies.

## Related

- [[commands/python3-run-exploit]]
