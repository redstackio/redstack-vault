---
id: uuid-tool-3
url: 'https://kafka-python.readthedocs.io/'
tags:
  - kafka
  - library
type: tool
verified: false
platforms:
  - Linux
  - Python
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.027Z'
validated: true
submitted: true
---
# kafka-python

**Status**: Unverified

## Overview

kafka-python is a Python client library for Apache Kafka, used in exploit scripts to configure connectors and interact with Kafka services like Aiven's managed Connect.

## Description

This library enables programmatic creation and management of Kafka topics and connectors, crucial for exploits involving sink connectors to upload files or send SSRF requests in RCE chains.

## Features

- Feature 1: Producer/consumer APIs for Kafka
- Feature 2: Connector configuration support
- Feature 3: Admin client for cluster management

## Installation

### Requirements

- Python 3.x

### Install Commands

```bash
pip install kafka-python
```

## Basic Usage

```bash
python -c "from kafka import KafkaAdminClient"
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Library imported in scripts |

## Examples

### Example 1: Basic Usage

```python
from kafka.admin import KafkaAdminClient
admin_client = KafkaAdminClient(bootstrap_servers='localhost:9092')
```

### Example 2: Advanced Usage

```python
# Create connector config
config = {'connector.class': 'io.confluent.connect.jdbc.JdbcSinkConnector'}
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Python]] Python
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Python import logs for kafka modules
- Anomalous connector creations via API
- Traffic to Kafka endpoints from non-standard clients

## Related Procedures


## Related Tools

- [[tools/python3]]

## References

- Official documentation: https://kafka-python.readthedocs.io/
- Related resources: Kafka Connect API docs
