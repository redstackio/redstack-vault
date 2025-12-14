---
id: uuid-command-5
data: python3 poc.py
tags:
  - exploit
  - rce
type: command
output: 'Triggers the exploitation, leading to reverse shell connection on port 4446'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.034Z'
verified: false
validated: true
submitted: true
---
# python-run-poc

## Command

```bash
python3 poc.py
```

## Description

Executes the proof-of-concept Python script to configure malicious Kafka Connect connectors for file upload and SSRF, leading to RCE via Jolokia agent load.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| poc.py | Script that configures Kafka Connect with malicious connectors | Yes |

## Examples

### Basic Usage

```bash
python3 poc.py
```

### Advanced Usage

```bash
python3 poc.py --host aiven-kafka-connect --topic exploit-topic
```

## Expected Output

Script logs connector creation (e.g., "Connector jdbc-sink created"), HTTP requests to Jolokia, and confirmation of agent load; reverse shell connects externally.

## Related

- [[commands/cd-exploit-dir]]
