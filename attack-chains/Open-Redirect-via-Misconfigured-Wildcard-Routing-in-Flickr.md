---
id: flickr-open-redirect-1581258
tags:
  - open-redirect
  - phishing
  - web-vuln
  - routing-misconfig
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
  - '[[procedures/Exploit-Flickr-Open-Redirect-via-Wildcard-Misconfig]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:31.233Z'
description: >-
  Demonstrates exploitation of an open redirect vulnerability in Flickr's
  routing system due to a misconfigured wildcard pattern, allowing redirection
  to arbitrary external sites for potential phishing.
skill_level: beginner
impact_level: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Open Redirect via Misconfigured Wildcard Routing in Flickr

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Redirect] --> B[Phishing Setup]

    style A fill:#e74c3c
    style B fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- Browser or [[curl]] for testing redirects

### Target Environment

- Web platform (Flickr application)
- Accessible via public internet
- No specific ports required beyond standard HTTPS (443)

### Initial Access Requirements

- No credentials needed
- Public network access to Flickr URLs
- No prior access required

## Detailed Attack Procedures

### Step 1: Exploit Open Redirect
procedure: [[procedures/Exploit-Flickr-Open-Redirect-via-Wildcard-Misconfig]]

**Objective**: Craft and test a URL that bypasses the wildcard routing misconfiguration to redirect users to an arbitrary external site, enabling phishing.

**Instructions**: Identify the vulnerable endpoint in Flickr's routing system, typically involving a wildcard pattern like `/*` that should route to a 404 but fails to do so reliably. Construct a URL with a redirect parameter pointing to an attacker-controlled site. Use a browser or [[commands/curl-test-redirect]] to verify the redirect occurs instead of a 404.

For example, if the vulnerable pattern is at `https://www.flickr.com/*`, append a redirect query like `?redirect_url=http://attacker.com/phish`:

```bash
curl -L -I "https://www.flickr.com/malicious?redirect_url=http://attacker.com/phish"
```

Follow the Location header to confirm redirection to the external site.

**Expected Output**: HTTP 302 redirect response with Location header pointing to the arbitrary external URL, rather than a 404 page.

**Success Indicators**:
- Redirect to external site confirmed via curl or browser
- No 404 error page served
- Potential for user to be phished if shared via social engineering

## Attack Chain Summary

### Key Achievements

1. Successful bypass of wildcard routing to achieve open redirect
2. Demonstration of low-severity phishing vector without account compromise
3. Identification of misconfiguration for reporting and remediation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
