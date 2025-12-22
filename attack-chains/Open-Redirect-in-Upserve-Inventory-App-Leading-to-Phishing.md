---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: Open Redirect in Upserve Inventory App Leading to Phishing
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
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Test-Open-Redirect-in-Upserve-Login]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:35.001Z'
description: >-
  Demonstrates exploitation of an open redirect vulnerability in the Upserve
  Inventory App login page to redirect users to arbitrary external sites,
  enabling phishing attacks.
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.002]]'
---
# Open Redirect in Upserve Inventory App Leading to Phishing

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Malicious Link] --> B[Redirection to Phishing Site]
    B --> C[Phishing Objective]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses browser or basic HTTP client)

### Target Environment

- Web platform
- Access to public-facing login page at https://inventory.upserve.com
- No specific ports or services required beyond HTTP/HTTPS

### Initial Access Requirements

- No credentials needed
- Public network access
- No prior access required

## Detailed Attack Procedures

### Step 1: Exploit Open Redirect
procedure: [[procedures/Test-Open-Redirect-in-Upserve-Login]]

**Objective**: Craft and test a malicious URL to redirect users from the Upserve Inventory App login page to an external attacker-controlled site, facilitating phishing.

**Instructions**: Construct a URL by appending an arbitrary external domain to the path of the login endpoint, such as https://inventory.upserve.com/http://evil-phish-site.com. Navigate to this URL in a browser or use [[commands/curl-test-redirect]] to verify the redirect behavior. Observe if the application processes the path as a redirect target without validation, leading to an HTTP 302 response or browser navigation to the external site. Similarly, inspect the 'Cancel' button link for the same vulnerability.

```bash
curl -I -L "https://inventory.upserve.com/http://google.com/"
```

**Expected Output**: HTTP response showing a 302 redirect to the specified external URL, or browser navigation away from the login page.

**Success Indicators**:
- Redirect occurs to the injected URL
- No validation errors or blocking of external domains

## Attack Chain Summary

### Key Achievements

1. Identified open redirect in URL path handling
2. Demonstrated potential for phishing by redirecting to arbitrary sites
3. Highlighted similar issue in UI elements like the Cancel button

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[T1566.002]] Phishing: Spearphishing Link

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T12:00:00Z*
