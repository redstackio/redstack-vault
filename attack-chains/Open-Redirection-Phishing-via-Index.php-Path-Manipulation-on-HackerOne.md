---
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
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Open-Redirect-via-Path-Manipulation]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:31.555Z'
description: >-
  Exploits an open redirection vulnerability in HackerOne's index.php by
  manipulating the URL path to redirect users to attacker-controlled domains,
  enabling phishing attacks.
skill_level: intermediate
impact_level: high
id: 2d74fd58-1182-4154-904e-570f4a6add36
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Open Redirection Phishing via Index.php Path Manipulation on HackerOne

Multi-stage attack chain demonstrating exploitation of an open redirection vulnerability in HackerOne's index.php page. By appending manipulated paths to the URL, attackers can bypass domain validation and redirect users to malicious sites, facilitating phishing for credentials or malware distribution.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Craft Malicious URL] --> B[Execution: Trigger Redirection]
    B --> C[Objective: Phishing via Redirect]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or [[commands/curl-test-redirect]]

### Target Environment

- Web platform
- PHP-based application (HackerOne site)
- No specific ports or services beyond HTTP/HTTPS

### Initial Access Requirements

- Public access to HackerOne website
- No credentials needed
- Ability to craft and share URLs (e.g., via email or social engineering)

## Detailed Attack Procedures

### Step 1: Initial Access
procedure: [[procedures/Exploit-Open-Redirect-via-Path-Manipulation]]

**Objective**: Craft a malicious URL that manipulates the index.php path to point to an attacker-controlled domain.

**Instructions**: Construct the URL by appending a manipulated path after index.php, such as 'index.php.hacker0ne.com' to create a subdomain-like redirect target. For testing, use [[commands/curl-test-redirect]] to verify the redirection without a browser:

```bash
curl -L -I "https://www.hackerone.com/index.php/index.php.hacker0ne.com"
```

This follows redirects (-L) and shows headers (-I) to confirm the Location header points to the manipulated domain.

**Expected Output**: HTTP response showing a 302 redirect to https://www.hackerone.com.hacker0ne.com/ or similar controlled domain.

**Success Indicators**:
- Redirect Location header indicates external or manipulated domain
- No validation error; redirect occurs

### Step 2: Execution
procedure: [[procedures/Exploit-Open-Redirect-via-Path-Manipulation]]

**Objective**: Trigger the redirection by visiting the crafted URL, tricking a victim into following it to reach the phishing site.

**Instructions**: Share the crafted URL with the target (e.g., via phishing email claiming a HackerOne reward). Upon access, the site interprets the path as a redirect target. Test locally with [[commands/curl-test-redirect]]:

```bash
curl -L "https://www.hackerone.com/index.php/index.php.hacker0ne.com" -o /dev/null -w "%{url_effective}\n"
```

This follows the redirect and prints the final URL.

**Expected Output**: Browser or curl lands on the attacker-controlled domain, disguised as a legitimate HackerOne redirect.

**Success Indicators**:
- User is redirected to malicious site
- Potential for credential theft or malware if site is controlled

## Attack Chain Summary

### Key Achievements

1. Bypassed domain validation in index.php redirection logic
2. Enabled phishing by mimicking legitimate HackerOne redirects
3. Demonstrated path manipulation for arbitrary domain targeting

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
