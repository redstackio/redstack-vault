---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - api-key-leak
  - information-disclosure
  - google-maps
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Inspect-Web-Application-for-Exposed-API-Keys]]'
step_count: 1
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:32:10.880Z'
description: >-
  Attack chain demonstrating the discovery of an exposed Google Maps API key in
  Uber's client-side web application code, leading to potential unauthorized API
  usage.
skill_level: beginner
impact_level: low
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Google Maps API Key Exposure in Uber Web Application

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discovery of Exposed Key] --> B[Potential Unauthorized Access]

    style A fill:#e74c3c
    style B fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- Browser with developer tools (e.g., Chrome DevTools)

### Target Environment

- Web browser access to the Uber application
- No special services or ports required
- Public internet access to the application

### Initial Access Requirements

- No credentials required
- Public network position
- No prior access needed

## Detailed Attack Procedures

### Step 1: Discover Exposed API Key
procedure: [[procedures/Inspect-Web-Application-for-Exposed-API-Keys]]

**Objective**: Identify and extract the Google Maps API key from the client-side code or network requests of the Uber web application.

**Instructions**: Load the Uber web application in a browser. Open the developer tools (F12 or right-click > Inspect). Navigate to the Network tab and interact with map-related features to trigger API calls. Look for requests to Google Maps endpoints containing the API key in the URL or headers. Alternatively, inspect the source code (View Page Source or Elements tab) for hardcoded keys in JavaScript files.

**Expected Output**: A string resembling a Google Maps API key (e.g., AIzaSyD... format) visible in requests or code.

**Success Indicators**:
- API key identified in client-side JavaScript or network traffic
- Key confirmed as unrestricted by testing a simple API call (if applicable)

## Attack Chain Summary

### Key Achievements

1. Successful identification of the exposed Google Maps API key
2. Assessment of potential for unauthorized API usage
3. Reporting of the vulnerability for remediation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unsecured Credentials]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
