---
url: ''
tags:
  - api
  - indexing
  - search
type: tool
verified: false
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:35.912Z'
id: d657b4eb-7d47-4785-9d4b-13951dea5446
validated: true
submitted: true
---
---

# Elasticsearch-API

**Status**: Unverified

## Overview

The Elasticsearch REST API allows direct interaction with the search engine for indexing documents, querying data, and managing indices, used in security testing to insert malicious ML anomalies for exploiting Kibana vulnerabilities.

## Description

In Elastic Stack, the API (default port 9200) enables PUT operations to custom indices like .ml-anomalies-*, facilitating prototype pollution by storing unsanitized payloads. Supports JSON over HTTP, integrable with tools like curl for RCE setups in Kibana SIEM.

## Features

- Feature 1: Document indexing (PUT/POST) with refresh options
- Feature 2: Authentication via basic auth or API keys
- Feature 3: Index management for ML and SIEM data

## Installation

### Requirements

- Java 11+
- Sufficient RAM (4GB+)

### Install Commands

```bash
# Download and start
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.7.0-linux-x86_64.tar.gz
tar -xzf elasticsearch-7.7.0-linux-x86_64.tar.gz
cd elasticsearch-7.7.0
bin/elasticsearch &
```

## Basic Usage

```bash
# Health check
curl localhost:9200/_cluster/health
```

### Common Options

| Option | Description |
|--------|-------------|
| `-u user:pass` | Basic authentication |
| `?refresh` | Immediate index refresh |

## Examples

### Example 1: Basic Usage

```bash
curl -X GET "localhost:9200/_cat/indices"
```

### Example 2: Advanced Usage

```bash
curl -X PUT "localhost:9200/my-index/_doc/1" -H 'Content-Type: application/json' -d '{"field": "value"}'
```
For ML anomaly: See command examples in procedures.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Exploitation for Client Execution]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual PUT requests to .ml-anomalies-* indices
- Payloads with __proto__ keys in logs
- High-volume anomaly indexing

## Related Procedures


## Related Tools

- [[tools/Kibana]]

## References

- Official documentation: https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html
- Related resources: REST API docs

