---
tags:
  - misconfiguration
  - information-disclosure
  - cortex
  - golang
  - pprof
  - dos
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Cortex-Home-Endpoint]]'
  - '[[procedures/Retrieve-Cortex-Configuration]]'
  - '[[procedures/Access-Golang-Pprof-Debugger-Home]]'
  - '[[procedures/Expose-Golang-Pprof-Commandline-Arguments]]'
  - '[[procedures/Explore-Cortex-API-Endpoints]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:32:48.369Z'
description: >-
  Multi-stage attack exploiting a misconfigured Cortex metrics server exposed
  publicly without authentication, leading to information disclosure of server
  configuration, command-line arguments, API access, and potential
  denial-of-service via Golang pprof debugger.
skill_level: beginner
impact_level: high
id: 7d760f22-df2e-4c21-ad47-230c9277be3a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
---
# Unauthorized Access to Exposed Cortex Metrics Server for Configuration Disclosure and DoS

Multi-stage attack chain demonstrating exploitation of a publicly exposed Cortex metrics server without authentication, allowing unauthorized access to sensitive configuration, debugging interfaces, and APIs, with potential for denial-of-service attacks.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access to Home] --> B[Configuration Retrieval]
    B --> C[Pprof Debugger Access]
    C --> D[Commandline Exposure]
    D --> E[API Exploration and DoS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Web-based Cortex metrics server
- Cloud-hosted (e.g., Shopify Cloud)
- No authentication required on exposed endpoints
- Network access to public URL: https://cortex-ingest.shopifycloud.com/

### Initial Access Requirements

- Public internet access
- No credentials needed due to misconfiguration
- Basic HTTP client (browser or curl)

## Detailed Attack Procedures

### Step 1: Initial Access to Home Endpoint
procedure: [[procedures/Access-Cortex-Home-Endpoint]]

**Objective**: Gain unauthorized entry to the Cortex metrics server interface to confirm exposure.

**Instructions**: Use [[commands/curl-access-url]] to navigate to the home endpoint:

```bash
curl -i https://cortex-ingest.shopifycloud.com/
```

**Expected Output**: HTTP response displaying the Cortex metrics server interface without authentication prompts.

**Success Indicators**:
- 200 OK status code
- Cortex UI or API response visible

### Step 2: Retrieve Server Configuration
procedure: [[procedures/Retrieve-Cortex-Configuration]]

**Objective**: Extract sensitive server configuration details for reconnaissance.

**Instructions**: Execute [[commands/curl-access-config]] to request the configuration endpoint:

```bash
curl https://cortex-ingest.shopifycloud.com/config
```

**Expected Output**: JSON or text response containing server configuration, including internal settings and arguments.

**Success Indicators**:
- Configuration data returned
- No authentication error

### Step 3: Access Golang Pprof Debugger Home
procedure: [[procedures/Access-Golang-Pprof-Debugger-Home]]

**Objective**: Access the debugging interface to identify potential attack vectors like DoS.

**Instructions**: Use [[commands/curl-access-pprof-home]] to view the pprof interface:

```bash
curl https://cortex-ingest.shopifycloud.com/debug/pprof/
```

**Expected Output**: Listing of pprof debugging options and heap/profile data.

**Success Indicators**:
- Pprof index page loaded
- Available profiles (e.g., heap, goroutine) listed

### Step 4: Expose Commandline Arguments
procedure: [[procedures/Expose-Golang-Pprof-Commandline-Arguments]]

**Objective**: Disclose command-line arguments used to start the server, revealing operational secrets.

**Instructions**: Request the cmdline endpoint with debug flag using [[commands/curl-access-pprof-cmdline]]:

```bash
curl https://cortex-ingest.shopifycloud.com/debug/pprof/cmdline?debug=1
```

**Expected Output**: Text output of command-line flags and arguments passed to the Golang binary.

**Success Indicators**:
- Arguments like storage paths or API keys exposed
- No access denied

### Step 5: Explore Cortex API Endpoints
procedure: [[procedures/Explore-Cortex-API-Endpoints]]

**Objective**: Query metrics data and test for further exploitation, including potential DoS via heavy API calls.

**Instructions**: Test API endpoints documented at Cortex docs using [[commands/curl-api-query]]:

```bash
curl 'https://cortex-ingest.shopifycloud.com/api/v1/query?query=up'
```

For DoS, repeatedly query resource-intensive endpoints like pprof heap:

```bash
curl https://cortex-ingest.shopifycloud.com/debug/pprof/heap
```

**Expected Output**: Metrics query results or profile data; for DoS, server slowdown or errors on repeated calls.

**Success Indicators**:
- API responses with data
- Server resource exhaustion on DoS attempts

## Attack Chain Summary

### Key Achievements

1. Confirmed public exposure of Cortex server without auth
2. Disclosed server config and command-line args for internal insights
3. Accessed debugging tools enabling DoS
4. Queried sensitive metrics data via APIs

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Active Scanning]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---

*Last updated: 2023-10-01T00:00:00Z*
