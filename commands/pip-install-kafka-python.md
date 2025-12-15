---
id: uuid-command-3
data: pip install kafka-python
tags:
  - setup
  - python
type: command
output: Successful installation of the library
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.046Z'
verified: false
validated: true
submitted: true
---
# pip-install-kafka-python

## Command

```bash
pip install kafka-python
```

## Description

Installs the kafka-python library prerequisite for running the exploit script that interacts with Kafka Connect APIs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| kafka-python | Package name for Kafka client in Python | Yes |

## Examples

### Basic Usage

```bash
pip install kafka-python
```

### Advanced Usage

```bash
pip install kafka-python==2.0.2
```

## Expected Output

"Collecting kafka-python" followed by "Successfully installed kafka-python-2.0.2".

## Related

- [[commands/python-run-poc]]
