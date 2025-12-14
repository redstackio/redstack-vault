---
tags:
  - ssrf
  - leak
  - source-inspection
  - couchbase
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:48.525Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: f46cf4a4-909c-456f-b31b-c8e5ed4536d3
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inspect-Page-Source-for-Internal-Service-Leaks

## Summary

This procedure involves examining the HTML source of SSRF responses to uncover hidden details about internal services, such as Couchbase console elements, that are not visible in the rendered page.

## Description

After triggering SSRF with an internal URL like https://127.0.0.1:18091/ui/, the proxy may embed or leak internal content in the page source without rendering it fully. This reveals service indicators (e.g., Couchbase UI paths or scripts) for further targeting. The attack targets web browsers; expected outcomes include exposure of internal application details, aiding in deeper reconnaissance or exploitation.

## Requirements

1. Web browser with view-source capability
2. Successful prior SSRF test on an internal path
3. Basic HTML knowledge to identify leaks

## Defense

Defensive measures and detection strategies:

- Sanitize proxy responses to strip internal metadata
- Implement content security policies (CSP) on the proxy
- Audit source code emissions in proxy outputs

## Objectives

1. Extract non-rendered internal content from page source
2. Identify specific services like Couchbase consoles
3. Gather details for subsequent internal attacks

## Instructions

### Step 1: Trigger SSRF on Internal Path

**Context**: Access a specific internal UI endpoint via the proxy to generate a response with potential source leaks.

Navigate to:

```url
https://proxy.duckduckgo.com/iur/?f=1&image_host=https://127.0.0.1:18091/ui/
```

> The proxy attempts to fetch the Couchbase UI; the page may appear blank or erroneous, but source contains clues.

### Step 2: View and Analyze Source

**Context**: Inspect the raw HTML for embedded internal elements.

Right-click the page and select "View Page Source" (Ctrl+U in most browsers).

> Search for keywords like "Couchbase", UI paths, or internal scripts. Expected output includes leaked HTML snippets indicating console access.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- source-leak
- internal-ui
- reconnaissance
