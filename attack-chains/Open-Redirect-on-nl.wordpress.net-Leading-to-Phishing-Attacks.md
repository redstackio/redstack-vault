---
id: ac-open-redirect-wordpress-phishing
tags:
  - open-redirect
  - phishing
  - wordpress
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Open-Redirect-via-Malformed-Paths]]'
step_count: 3
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:31.169Z'
description: >-
  Multi-stage exploitation of an open redirect vulnerability on nl.wordpress.net
  to redirect users to malicious phishing sites mimicking legitimate WordPress
  domains.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
# Open Redirect on nl.wordpress.net Leading to Phishing Attacks

Multi-stage attack chain demonstrating the exploitation of an open redirect vulnerability on nl.wordpress.net, allowing attackers to redirect users to arbitrary malicious sites for phishing credential theft.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discovery of Malformed Path] --> B[Exploit Open Redirect] --> C[Verification and Phishing Setup]
    A --> D[Post-Fix Validation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Web platform
- Access to nl.wordpress.net
- No specific ports required beyond standard HTTP/HTTPS (80/443)

### Initial Access Requirements

- Public internet access to nl.wordpress.net
- No credentials needed for exploitation
- Ability to craft and send HTTP requests

## Detailed Attack Procedures

### Step 1: Discovery of Open Redirect via Malformed Path
procedure: [[procedures/Exploit-Open-Redirect-via-Malformed-Paths]]

**Objective**: Identify the open redirect vulnerability by testing malformed paths that bypass validation.

**Instructions**: Send a GET request to a malformed path like /@google.com on nl.wordpress.net to trigger an unvalidated redirect.

Use [[commands/curl-test-malformed-path]] to simulate:

```bash
curl -I http://nl.wordpress.net/@google.com
```

This appends the path to the hostname without a trailing slash, resulting in a redirect to http://nl.wordpress.org@google.com.

**Expected Output**: HTTP 301 response with Location header pointing to an arbitrary external domain.

**Success Indicators**:
- 301 redirect to external site like http://nl.wordpress.org@google.com
- No validation blocking the redirect

### Step 2: Exploit Alternative Vector with Subdomain Appending
procedure: [[procedures/Exploit-Open-Redirect-via-Malformed-Paths]]

**Objective**: Test and exploit an alternative vector using dot-prefixed paths to append subdomains to the legitimate redirect destination.

**Instructions**: Access a URL like http://nl.wordpress.net/.xpoc.pro, which redirects to nl.wordpress.org.xpoc.pro without validation.

Use [[commands/curl-test-subdomain-vector]] to verify:

```bash
curl -I http://nl.wordpress.net/.xpoc.pro
```

This allows crafting phishing links that appear to come from trusted WordPress subdomains.

**Expected Output**: 301 redirect to nl.wordpress.org.xpoc.pro or similar arbitrary subdomain.

**Success Indicators**:
- Redirect to attacker-controlled subdomain mimicking WordPress
- Potential for phishing site setup on that domain

### Step 3: Post-Fix Verification
procedure: [[procedures/Exploit-Open-Redirect-via-Malformed-Paths]]

**Objective**: Confirm the vulnerability's fix by testing that redirects now stay within the legitimate domain.

**Instructions**: After a potential fix, test with [[commands/curl-verify-post-fix-redirect]]:

```bash
curl -I http://nl.wordpress.net/.attacker.com | grep Location
```

The redirect should now point to https://nl.wordpress.org/.attacker.com, preventing open redirection.

**Expected Output**: Location: https://nl.wordpress.org/.attacker.com

**Success Indicators**:
- Redirect confined to wordpress.org domain
- No external arbitrary redirects possible

## Attack Chain Summary

### Key Achievements

1. Discovered open redirect via malformed paths like /@domain
2. Exploited subdomain appending for phishing-mimicking redirects
3. Validated fix to ensure domain confinement

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Drive-by Compromise]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---

*Last updated: 2023-10-01T00:00:00Z*
