---
id: proc-discover-sharepoint-endpoint
tags:
  - recon
  - sharepoint
  - endpoint-discovery
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:23:54.291Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Discover Vulnerable SharePoint Endpoint

## Summary

This procedure involves identifying publicly accessible endpoints in Microsoft SharePoint installations, specifically the picker.aspx file under the _layouts/15/ directory, which can be tested for deserialization vulnerabilities like CVE-2019-0604.

## Description

In SharePoint environments, standard paths like /_layouts/15/picker.aspx are often exposed without authentication, allowing attackers to probe for unsafe deserialization of user-supplied data. This step focuses on reconnaissance to confirm endpoint accessibility and potential vulnerability without triggering alerts. The target environment is a web-facing SharePoint server, and success leads to the next exploitation phase.

## Requirements

1. Network access to the target domain (e.g., https://sdrc.starbucks.com)
2. Web browser or HTTP client for probing
3. Basic knowledge of SharePoint architecture

## Defense

Defensive measures and detection strategies:

- Restrict access to administrative paths like _layouts/15/ using IP whitelisting or authentication
- Monitor access logs for anomalous requests to picker.aspx
- Apply SharePoint security updates promptly to patch CVE-2019-0604

## Objectives

1. Confirm unauthenticated access to the picker.aspx endpoint
2. Identify if the endpoint processes serialized input
3. Gather evidence for vulnerability reporting or exploitation

## Instructions

### Step 1: Probe the Target URL

**Context**: Use a browser or HTTP client to access the suspected endpoint and verify it's publicly reachable without credentials.

No specific command needed; open https://target.com/_layouts/15/picker.aspx in a browser.

> If the page loads and shows a file picker interface without prompting for login, the endpoint is unauthenticated and potentially vulnerable.

### Step 2: Inspect for Input Vectors

**Context**: Examine the page for forms or parameters that accept user data, which could be serialized payloads.

Use browser developer tools to inspect POST requests or form fields on picker.aspx.

> Look for parameters like 'data' or serialized objects; successful inspection reveals opportunities for payload injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[Sharepoint]]
