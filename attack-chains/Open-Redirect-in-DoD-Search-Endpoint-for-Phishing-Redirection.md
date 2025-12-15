---
id: ac-open-redirect-dod-search
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
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Open-Redirect-via-Unvalidated-URL-Parameter]]'
step_count: 1
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Phishing]]'
updated_at: '2025-12-14T17:24:26.433Z'
description: >-
  A single-stage attack exploiting an open redirect vulnerability in a U.S.
  Department of Defense web application's search redirection endpoint to
  redirect users to malicious external sites for phishing or malware
  distribution.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Phishing]]'
---
# Open Redirect in DoD Search Endpoint for Phishing Redirection

Multi-stage attack chain demonstrating a complete attack workflow exploiting an open redirect in a DoD web application to enable phishing attacks.

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
    A[Identify Vulnerable Endpoint] --> B[Craft Malicious Redirect URL]
    B --> C[Redirect User to Phishing Site]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or [[tools/curl]]

### Target Environment

- Web application using Texis search engine
- Publicly accessible DoD domain
- No authentication required for the endpoint

### Initial Access Requirements

- Internet access to the target domain
- No prior credentials needed
- Ability to craft and share URLs

## Detailed Attack Procedures

### Step 1: Exploit Open Redirect
procedure: [[procedures/Exploit-Open-Redirect-via-Unvalidated-URL-Parameter]]

**Objective**: Redirect users from the legitimate DoD search endpoint to a malicious external site to facilitate phishing or drive-by downloads.

**Instructions**: Identify the vulnerable endpoint /texis/search/redir.html and craft a URL with the 'u' parameter set to a malicious domain. Test the redirect using [[commands/curl-test-open-redirect]] to verify it follows to the external site without validation.

```bash
curl -L "https://[redacted-domain]/texis/search/redir.html?query=1234&pr=External+Meta&prox=page&rorder=500&rprox=500&rdfreq=500&rwfreq=250&rlead=500&rdepth=62&sufs=3&order=r&u=http://evil.com&m=0&p=2/" -o /dev/null -w "%{url_effective}\n"
```

Share the crafted URL via email, social engineering, or embedding in links to trick users into clicking it.

**Expected Output**: The curl command outputs the final redirected URL (http://evil.com), confirming the open redirect works.

**Success Indicators**:
- HTTP 302 redirect status to external domain
- Users visiting the link are seamlessly redirected to the malicious site
- Potential for credential theft if phishing page is hosted on evil.com

## Attack Chain Summary

### Key Achievements

1. Successful redirection from trusted DoD domain to attacker-controlled site
2. Enabled phishing campaigns targeting DoD users
3. Demonstrated lack of URL validation in search redirect functionality

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Drive-by Compromise]]
- [[Phishing]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
