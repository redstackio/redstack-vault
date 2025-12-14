---
tags:
  - ssrf
  - line
  - pagepoker
  - opengraph
  - internal-access
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Exploit-SSRF-in-PagePoker-OpenGraph-Image-Tags]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  A single-stage attack exploiting SSRF in the website preview feature of LINE
  Official Account Manager to access internal network resources through
  unvalidated OpenGraph image tags in PagePoker.
skill_level: intermediate
impact_level: low
id: c81943ad-71d6-4109-bd8d-b2a7b2e73eab
created_at: '2025-12-14T04:08:47.837Z'
updated_at: '2025-12-14T04:08:47.837Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SSRF in LINE Official Account Manager Website Preview via OpenGraph Image Tags

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Preview Feature] --> B[SSRF Exploitation for Internal Access]

    style A fill:#e74c3c
    style B fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- Web browser or proxy tool like Burp Suite for intercepting requests

### Target Environment

- Web platform
- LINE Official Account Manager at https://manager.line.biz/
- Access to the website preview feature

### Initial Access Requirements

- Valid user account on LINE Official Account Manager
- No special credentials beyond standard login
- Direct network access to the public-facing application

## Detailed Attack Procedures

### Step 1: Exploit SSRF in Website Preview
procedure: [[procedures/Exploit-SSRF-in-PagePoker-OpenGraph-Image-Tags]]

**Objective**: Identify and exploit the SSRF vulnerability in the PagePoker service used for generating website previews, allowing requests to internal network resources via unvalidated OpenGraph image tags.

**Instructions**: Log in to the LINE Official Account Manager at https://manager.line.biz/. Navigate to the website preview feature, which relies on PagePoker for rendering OpenGraph metadata. Intercept or modify the request to the preview endpoint using a proxy tool. Alter the OpenGraph image tag URL to point to an internal resource, such as http://localhost/admin or http://169.254.169.254/latest/meta-data/ (for cloud metadata). Submit the preview request and observe if the internal resource is fetched, potentially leaking data in the response or logs.

**Expected Output**: The preview generation succeeds but includes data from the internal resource, or server-side errors indicate internal access was attempted.

**Success Indicators**:
- Response contains internal resource data (e.g., metadata or service responses)
- Server behavior changes, such as delayed response or error messages hinting at internal fetch

## Attack Chain Summary

### Key Achievements

1. Successful identification of SSRF in the preview feature
2. Demonstration of access to internal network resources
3. Low-severity impact highlighting potential for broader reconnaissance

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01*
