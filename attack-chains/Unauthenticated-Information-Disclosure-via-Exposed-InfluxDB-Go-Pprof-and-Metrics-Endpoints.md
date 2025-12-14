---
tags:
  - information-disclosure
  - pprof
  - influxdb
  - go-runtime
  - unauthenticated-access
  - debug-endpoint
type: attack_chain
tools:
  - '[[tools/go-tool-pprof]]'
  - '[[tools/go-tool-trace]]'
tactics:
  - '[[Discovery]]'
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
  - Kubernetes
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Go-Pprof-Index]]'
  - '[[procedures/Retrieve-Goroutine-Stack-Traces]]'
  - '[[procedures/Download-Heap-Profile]]'
  - '[[procedures/Download-Execution-Trace]]'
  - '[[procedures/Access-Metrics-Endpoint]]'
  - '[[procedures/Access-Stats-Endpoint]]'
step_count: 6
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[System Information Discovery]]'
  - '[[Software]]'
updated_at: '2025-12-14T17:26:17.247Z'
description: >-
  This attack chain exploits unauthenticated access to debugging endpoints on an
  InfluxDB instance, disclosing runtime information such as stack traces, heap
  profiles, execution traces, metrics, and stats to aid reconnaissance.
skill_level: beginner
impact_level: low
id: d25066ea-37b7-49e8-b254-cad7cf701863
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[System Information Discovery]]'
  - '[[Software]]'
---
# Unauthenticated Information Disclosure via Exposed InfluxDB Go Pprof and Metrics Endpoints

Multi-stage attack chain demonstrating reconnaissance through unauthenticated access to sensitive debugging and monitoring endpoints on an InfluxDB instance running on Go, exposing runtime details like memory allocations, stack traces, and system metrics. This was reported in GitLab's quality environment and assessed as low severity due to limited sensitivity of the data, but it could aid attackers in understanding the target's internals for further exploitation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Pprof Index] --> B[Retrieve Goroutines]
    B --> C[Download Heap Profile]
    C --> D[Download Execution Trace]
    D --> E[Access Metrics]
    E --> F[Access Stats]
    F --> G[Analyze Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#f39c12
    style E fill:#3498db
    style F fill:#3498db
    style G fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]] (for HTTP requests)
- [[tools/go-tool-pprof]] (for heap/goroutine analysis)
- [[tools/go-tool-trace]] (for trace analysis)

### Target Environment

- Web-based InfluxDB instance on Kubernetes
- Exposed ports: 80/443 (HTTP/HTTPS for endpoints)
- Services: InfluxDB, Go runtime (v1.18.3)

### Initial Access Requirements

- Public network access to the target URL (https://influxdb.quality.gitlab.net)
- No credentials required (unauthenticated)
- Basic HTTP client like curl

## Detailed Attack Procedures

### Step 1: Access Pprof Index
procedure: [[procedures/Access-Go-Pprof-Index]]

**Objective**: Retrieve the index of available Go pprof profiles to identify exposable runtime data types.

**Instructions**: Use [[commands/curl-access-pprof-index]] to fetch the pprof debugging index:

```bash
curl https://influxdb.quality.gitlab.net/debug/pprof
```

**Expected Output**: HTML or plain text listing profiles such as /debug/pprof/allocs, /debug/pprof/heap, /debug/pprof/goroutine, etc.

**Success Indicators**:
- List of pprof endpoints returned without authentication prompt
- Profiles like heap and goroutine visible

### Step 2: Retrieve Goroutine Stack Traces
procedure: [[procedures/Retrieve-Goroutine-Stack-Traces]]

**Objective**: Obtain detailed stack traces of all running goroutines, revealing memory addresses, file paths, and runtime internals.

**Instructions**: Execute [[commands/curl-retrieve-goroutine-traces]] to get goroutine dumps:

```bash
curl "https://influxdb.quality.gitlab.net/debug/pprof/goroutine?debug=1"
```

**Expected Output**: Text output with stack traces, including paths like /usr/local/go-1.18.3/src/runtime/netpoll.go and memory addresses.

**Success Indicators**:
- Stack traces displayed with internal Go file references
- No access denied error

### Step 3: Download Heap Profile
procedure: [[procedures/Download-Heap-Profile]]

**Objective**: Capture a snapshot of live memory allocations to analyze object usage and potential leaks.

**Instructions**: Download the heap profile using [[commands/curl-download-heap-profile]]:

```bash
curl -o heap.pprof.gz https://influxdb.quality.gitlab.net/debug/pprof/heap
```

**Expected Output**: Gzip-compressed profile file (heap.pprof.gz) containing memory allocation samples.

**Success Indicators**:
- File downloaded successfully (check with ls -l heap.pprof.gz)
- File size indicates non-empty profile

### Step 4: Download Execution Trace
procedure: [[procedures/Download-Execution-Trace]]

**Objective**: Acquire an execution trace of the program's runtime to visualize goroutine scheduling and system calls.

**Instructions**: Fetch the trace file with [[commands/curl-download-execution-trace]]:

```bash
curl -o trace.out https://influxdb.quality.gitlab.net/debug/pprof/trace
```

**Expected Output**: Binary trace file (trace.out) in octet-stream format capturing runtime events.

**Success Indicators**:
- Trace file downloaded (verify with file trace.out)
- No errors in curl response

### Step 5: Access Metrics Endpoint
procedure: [[procedures/Access-Metrics-Endpoint]]

**Objective**: Expose system and application metrics to reveal resource usage and internal states.

**Instructions**: Request metrics using [[commands/curl-access-metrics]]:

```bash
curl https://influxdb.quality.gitlab.net/metrics/
```

**Expected Output**: Prometheus-format text with metrics like go_goroutines, process_cpu_seconds_total, etc.

**Success Indicators**:
- Metrics data returned in exposition format
- Indicators of Go runtime and InfluxDB performance

### Step 6: Access Stats Endpoint
procedure: [[procedures/Access-Stats-Endpoint]]

**Objective**: Retrieve JSON statistics about the InfluxDB instance, including configuration and time-series data details.

**Instructions**: Fetch stats with [[commands/curl-access-stats]]:

```bash
curl https://influxdb.quality.gitlab.net/stats.json
```

**Expected Output**: JSON object with InfluxDB stats like numDatabases, numSeries, etc.

**Success Indicators**:
- Valid JSON response with instance statistics
- Details on stored data volumes

## Attack Chain Summary

### Key Achievements

1. Unauthenticated access to Go pprof endpoints disclosing runtime internals
2. Retrieval of memory, trace, and metrics data for reconnaissance
3. Exposure of InfluxDB operational statistics without barriers

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[System Information Discovery]] System Information Discovery
- [[Software]] Gather Victim Host Information: Software

### MITRE ATT&CK Tactics

- [[Discovery]] Discovery
- [[Reconnaissance]] Reconnaissance

---
*Last updated: 2023-10-01T00:00:00Z*
