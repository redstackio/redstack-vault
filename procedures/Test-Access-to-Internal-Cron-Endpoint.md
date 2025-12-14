---
id: proc-who-cron-test-001
tags:
  - access-control
  - dos
  - endpoint-testing
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-test-internal-cron-access-verbose]]'
  - '[[commands/curl-verify-cron-access-restricted]]'
verified: false
platforms:
  - Web
  - GCP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:32:28.952Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
---
# Test-Access-to-Internal-Cron-Endpoint

## Summary

This procedure tests unauthorized access to an internal cron job endpoint, such as /internal/cron/refreshCaseStats in the WHO COVID-19 App, to confirm public accessibility and measure resource consumption. It exploits a misconfiguration where production environment checks failed after GCP migration, allowing DoS via repeated triggers.

## Description

The endpoint, handled by RefreshCaseStatsServlet.java, checks for Environment.isProduction() based on GCP project ID and the X-Appengine-Cron header. Post-migration, the project name change bypassed this, making it publicly callable. Testing with curl shows a 200 OK after ~20 seconds, indicating heavy backend load from stats refresh.

## Requirements

1. Internet access to the target domain (e.g., hack.whocoronavirus.org)
2. curl installed on a Linux/macOS terminal
3. Knowledge of the endpoint URL from prior reconnaissance

## Defense

Defensive measures and detection strategies:

- Implement proper access controls using GCP project IDs and cron headers
- Monitor for anomalous requests to internal endpoints without X-Appengine-Cron
- Rate-limit or block repeated calls to resource-intensive paths

## Objectives

1. Verify unauthorized access to the cron endpoint
2. Measure response time to assess DoS potential
3. Simulate impact by repeating requests

## Instructions

### Step 1: Send Test Request with Verbose Output

**Context**: Use curl to probe the endpoint, capturing headers and timing to confirm accessibility and load.

**Command** ([[commands/curl-test-internal-cron-access-verbose]]):
```bash
time curl -v https://hack.whocoronavirus.org/internal/cron/refreshCaseStats
```

> The -v flag shows verbose details including headers; time measures execution (~20 seconds for 200 OK), proving unauthorized trigger of refreshCaseStats.

### Step 2: Verify Post-Fix Restriction (Optional)

**Context**: After remediation, retest to confirm access denial.

**Command** ([[commands/curl-verify-cron-access-restricted]]):
```bash
time curl -i https://hack.whocoronavirus.org/internal/cron/refreshCaseStats
```

> Expect <1 second response with HTTP/2 401 Unauthorized and 'Cron access only' message.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/curl-test-internal-cron-access-verbose]]
- [[commands/curl-verify-cron-access-restricted]]

## Tools Used

- [[tools/curl]]

## Tags

- [[access-control]]
- [[dos]]
