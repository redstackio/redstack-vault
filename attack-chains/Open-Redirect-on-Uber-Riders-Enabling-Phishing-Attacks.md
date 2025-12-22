---
id: ac-open-redirect-uber-riders
tags:
  - open-redirect
  - phishing
  - web-vulnerability
  - uber
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
  - '[[procedures/Exploit-Open-Redirect-on-Uber-Riders]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:27.270Z'
description: >-
  An attack chain exploiting an open redirect vulnerability on riders.uber.com
  to redirect users to arbitrary malicious sites, facilitating phishing without
  user interaction.
skill_level: beginner
impact_level: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Open Redirect on Uber Riders Enabling Phishing Attacks

Multi-stage attack chain demonstrating a complete attack workflow exploiting an open redirect on riders.uber.com to trick users into visiting malicious sites for phishing.

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
    A[Discovery and Exploitation] --> B[Phishing Setup]
    B --> C[User Redirection]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Web platform
- Access to riders.uber.com
- No specific ports or services required beyond HTTP/HTTPS

### Initial Access Requirements

- Public internet access
- No credentials needed for discovery
- Ability to craft URLs with redirect parameters

## Detailed Attack Procedures

### Step 1: Discovery and Exploitation
procedure: [[procedures/Exploit-Open-Redirect-on-Uber-Riders]]

**Objective**: Identify and exploit the open redirect vulnerability to redirect users to a malicious phishing site without validation.

**Instructions**: Begin by identifying the vulnerable endpoint or parameter on riders.uber.com that accepts redirect URLs. Use [[commands/curl-test-open-redirect]] to send a request with an arbitrary external URL, such as a controlled phishing domain, to verify the redirect occurs without validation.

```bash
curl -L "https://riders.uber.com/redirect?url=https://malicious-phish-site.com" -v
```

Observe the response headers and final location to confirm the redirect. If successful, craft a link to share with victims, embedding the malicious URL in the parameter.

**Expected Output**: HTTP response showing a 3xx redirect status to the arbitrary URL, with Location header pointing to the malicious site.

**Success Indicators**:
- Redirect to external site without error or validation
- No user interaction required for redirection
- Potential for phishing confirmation via access logs on the malicious site

## Attack Chain Summary

### Key Achievements

1. Identified open redirect endpoint on riders.uber.com
2. Demonstrated redirection to arbitrary malicious sites
3. Enabled low-impact phishing attacks by tricking users

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
