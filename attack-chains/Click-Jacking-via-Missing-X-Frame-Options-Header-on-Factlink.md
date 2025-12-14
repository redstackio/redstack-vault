---
id: ac-clickjacking-factlink-missing-xframe
name: Click-Jacking via Missing X-Frame-Options Header on Factlink
tags:
  - clickjacking
  - x-frame-options
  - web-security
  - http-headers
type: attack_chain
tools:
  - '[[tools/urivalet]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Inspect-HTTP-Headers-for-X-Frame-Options]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:05.118Z'
description: >-
  Attack chain demonstrating the discovery and exploitation potential of a
  Click-Jacking vulnerability due to absent X-Frame-Options headers on Factlink
  website pages.
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Click-Jacking via Missing X-Frame-Options Header on Factlink

Multi-stage attack chain demonstrating a complete attack workflow.

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
    A[Header Inspection] --> B[Click-Jacking Exploitation Potential]

    style A fill:#e74c3c
    style B fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- [[tools/urivalet]]
- Alternatively, [[commands/curl-check-headers]]

### Target Environment

- Web platform
- HTTP/HTTPS accessible website (e.g., factlink.com)
- No specific ports required beyond standard 80/443

### Initial Access Requirements

- Public internet access to the target website
- No credentials needed for header inspection
- Browser or command-line tool for verification

## Detailed Attack Procedures

### Step 1: Inspect HTTP Response Headers
procedure: [[procedures/Inspect-HTTP-Headers-for-X-Frame-Options]]

**Objective**: Identify the absence of X-Frame-Options header to confirm Click-Jacking vulnerability exposure.

**Instructions**: Use [[tools/urivalet]] or [[commands/curl-check-headers]] to probe the target website's HTTP responses for the X-Frame-Options header.

First, inspect the homepage:

```bash
curl -I https://factlink.com
```

Look for the absence of `X-Frame-Options` in the output headers. If missing, the page is vulnerable to iframe embedding.

To verify framing capability, attempt to embed in a test HTML file:

```html
<iframe src="https://factlink.com"></iframe>
```

Load this in a browser; if it loads without restrictions, confirm vulnerability.

**Expected Output**: HTTP headers without `X-Frame-Options: DENY` or `SAMEORIGIN`, allowing iframe embedding.

**Success Indicators**:
- No X-Frame-Options header present
- Page embeds successfully in an iframe on a test page

## Attack Chain Summary

### Key Achievements

1. Discovered missing security header enabling UI redressing attacks
2. Validated potential for Click-Jacking by confirming iframe embeddability
3. Assessed impact as informative due to intentional framing on some pages

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
