---
url: 'https://www.elastic.co/kibana'
tags:
  - siem
  - visualization
  - elasticsearch
type: tool
verified: false
platforms:
  - Web
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:35.924Z'
id: 26186403-ea3e-4e03-a3b6-be8ed5217725
validated: true
submitted: true
---
---

# Kibana

**Status**: Unverified

## Overview

Kibana is a web-based visualization and management interface for Elasticsearch, including SIEM features for detection rules and ML anomaly processing, commonly used in security testing to import rules and trigger vulnerabilities like prototype pollution.

## Description

Kibana 7.7.0 provides UI for SIEM rule management, enabling imports and evaluations that expose the prototype pollution flaw in ML signals. It's typically deployed alongside Elasticsearch in Elastic Stack environments, allowing authenticated users to configure and enable rules leading to RCE.

## Features

- Feature 1: SIEM detection engine for importing and managing rules
- Feature 2: Integration with ML jobs for anomaly-based alerts
- Feature 3: API endpoints for programmatic rule operations

## Installation

### Requirements

- Elasticsearch 7.x cluster
- Node.js runtime
- Java 11+ for Elasticsearch

### Install Commands

```bash
# Download and start via Elastic package
wget https://artifacts.elastic.co/downloads/kibana/kibana-7.7.0-linux-x86_64.tar.gz
tar -xzf kibana-7.7.0-linux-x86_64.tar.gz
cd kibana-7.7.0
bin/kibana &
```

## Basic Usage

```bash
# Access UI
open http://localhost:5601
```

### Common Options

| Option | Description |
|--------|-------------|
| `-p 5601` | Port to bind (default 5601) |
| `--elasticsearch.hosts` | Elasticsearch connection |

## Examples

### Example 1: Basic Usage

```bash
# Launch Kibana
bin/kibana
```
Access SIEM at http://localhost:5601/app/siem.

### Example 2: Advanced Usage

```bash
bin/kibana --elasticsearch.hosts=http://localhost:9200 --server.port=5601
```
Import rule via API: curl -X POST localhost:5601/api/siem/detection_engine/rules -H 'kbn-xsrf: true' -d @rule.json

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Tactics

- [[Initial Access]]
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Traffic to port 5601 with rule import payloads
- Log entries for SIEM rule enables
- Anomalous ML signal creations

## Related Procedures


## Related Tools

- [[tools/Elasticsearch-API]]

## References

- Official documentation: https://www.elastic.co/guide/en/kibana/current/index.html
- Related resources: Elastic Security docs

