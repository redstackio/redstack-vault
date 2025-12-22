---
id: cmd-python-poc
data: python3 poc.py
tags:
  - poc
  - api
type: command
output: >-
  Connector configuration updated, leading to LDAP query to attacker server and
  subsequent RCE
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.571Z'
verified: false
validated: true
submitted: true
---
# python3-poc-execution

## Command

```bash
python3 poc.py
```

## Description

Executes a Python script to configure the Debezium connector with malicious JAAS via API.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| poc.py | Script file with API logic | Yes |

## Examples

### Basic Usage

```bash
python3 poc.py
```

### Advanced Usage

Pass args if script supports: `python3 poc.py --api-key token`.

## Expected Output

JSON response like {"config": {"database.history.producer.sasl.jaas.config": "..."}} with status 200.

## Related

- [[procedures/Execute-Debezium-Connector-PoC-Script]]
