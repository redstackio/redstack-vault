---
tags:
  - open-redirect
  - phishing
  - serendipity
  - php
  - web
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-open-redirect]]'
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Exploit-Serendipity-Open-Redirect-via-Base64-URL]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  A multi-stage attack chain exploiting an open redirect vulnerability in
  Serendipity's exit.php to redirect users to arbitrary external sites,
  facilitating phishing and social engineering.
skill_level: beginner
impact_level: medium
id: d1540041-fced-4d9b-88eb-6adb41d2cb80
created_at: '2025-12-14T17:24:23.312Z'
updated_at: '2025-12-14T17:24:23.312Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Open Redirect in Serendipity exit.php Enabling Phishing Attacks

Multi-stage attack chain demonstrating exploitation of an open redirect vulnerability in Serendipity's exit.php script to redirect users to malicious external sites, enabling phishing attacks.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Vulnerable Endpoint] --> B[Trigger Redirect to Malicious Site]
    B --> C[Phishing or Social Engineering]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[commands/curl-test-open-redirect]]

### Target Environment

- Web platform running Serendipity CMS
- PHP backend
- Accessible exit.php endpoint

### Initial Access Requirements

- Public access to the Serendipity blog instance
- No authentication required
- Ability to craft hyperlinks for victims

## Detailed Attack Procedures

### Step 1: Access Vulnerable Endpoint
procedure: [[procedures/Exploit-Serendipity-Open-Redirect-via-Base64-URL]]

**Objective**: Craft and access the exit.php endpoint with a base64-encoded arbitrary URL to test the redirect functionality.

**Instructions**: Encode the target malicious URL in base64 and append it to the url parameter. Use [[commands/curl-test-open-redirect]] to simulate the request:

```bash
curl -I "https://blog.fuzzing-project.org/exit.php?url=aHR0cHM6Ly9nb29nbGUuY29t"
```

Replace the base64 value with an encoded malicious URL for real attacks.

**Expected Output**: HTTP response with a 301 status code and Location header pointing to the decoded URL.

**Success Indicators**:
- 301 redirect status received
- Location header matches the decoded arbitrary URL

### Step 2: Trigger Redirect to Malicious Site
procedure: [[procedures/Exploit-Serendipity-Open-Redirect-via-Base64-URL]]

**Objective**: Embed the crafted redirect URL in hyperlinks to lure victims, leading them to phishing sites.

**Instructions**: Create a hyperlink like `<a href="https://targetblog.com/exit.php?url=[base64-encoded-phishing-url]">Click here</a>` and distribute it via email or social engineering. Verify the redirect using [[commands/curl-test-open-redirect]] with the malicious URL encoded:

```bash
curl -I "https://targetblog.com/exit.php?url=[base64-of-phishing-site]"
```

**Expected Output**: Victim's browser redirects to the phishing site upon clicking.

**Success Indicators**:
- Victim follows the link and lands on the external malicious site
- Potential credential harvest or malware delivery

## Attack Chain Summary

### Key Achievements

1. Successful exploitation of open redirect without hostname validation
2. Demonstration of arbitrary external redirection
3. Enablement of phishing attacks via crafted hyperlinks

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
