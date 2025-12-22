---
id: ac-flickr-open-redirect-1217570
tags:
  - open-redirect
  - phishing
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Test-Flickr-Open-Redirect-via-Continue-Parameter]]'
step_count: 1
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:30.828Z'
description: >-
  Demonstrates exploitation of an open redirect vulnerability in Flickr's
  upgrade page to redirect users to arbitrary external domains, facilitating
  phishing attacks.
skill_level: beginner
impact_level: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
# Flickr Open Redirect via Upgrade Continue Parameter Enabling Phishing

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Vulnerable Endpoint] --> B[Test Redirect to External Domain]
    B --> C[Phishing Potential]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or [[commands/curl-test-redirect]]

### Target Environment

- Web platform
- Access to https://www.flickr.com
- No authentication required

### Initial Access Requirements

- Public internet access
- No credentials needed
- Direct URL access to the upgrade page

## Detailed Attack Procedures

### Step 1: Identify and Test Open Redirect
procedure: [[procedures/Test-Flickr-Open-Redirect-via-Continue-Parameter]]

**Objective**: Examine the Flickr upgrade endpoint to identify lack of validation in the 'continue' parameter, allowing redirects to external domains for phishing.

**Instructions**: Navigate to the upgrade page and append the 'continue' parameter with an external URL. Use [[commands/curl-test-redirect]] to simulate the request and follow the redirect:

```bash
curl -L "https://www.flickr.com/browser/upgrade/?continue=https://evil.com" -v
```

Observe the response headers and final location to confirm redirection without path or domain validation.

**Expected Output**: HTTP response showing a 302 redirect to the supplied external URL, such as Location: https://evil.com.

**Success Indicators**:
- Redirect occurs to arbitrary external domain
- No error or validation blocking the redirect

## Attack Chain Summary

### Key Achievements

1. Identified open redirect in upgrade page 'continue' parameter
2. Demonstrated redirection to external domains
3. Highlighted phishing potential by tricking users into malicious sites

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Drive-by Compromise]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
