---
tags:
  - open-redirect
  - phishing
  - uber
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
  - '[[procedures/Exploit-Open-Redirect-on-Uber-Subdomains]]'
step_count: 1
techniques:
  - '[[Phishing]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:30.519Z'
description: >-
  An attack chain exploiting open redirect vulnerabilities on Uber's
  rush.uber.com, business.uber.com, and help.uber.com subdomains to redirect
  users to arbitrary malicious sites, facilitating phishing without user
  interaction.
id: 1955f6ee-0396-46d8-b979-bd123e1579a8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
  - '[[Exploit Public-Facing Application]]'
---
---
id: 123e4567-e89b-12d3-a456-426614174000
name: Open Redirect on Uber Subdomains Enabling Phishing Attacks
type: attack_chain
description: "An attack chain exploiting open redirect vulnerabilities on Uber's rush.uber.com, business.uber.com, and help.uber.com subdomains to redirect users to arbitrary malicious sites, facilitating phishing without user interaction."
verified: false
submitted: false
step_count: 1
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
procedures: [[procedures/Exploit-Open-Redirect-on-Uber-Subdomains]]
techniques: [[Phishing]], [[Exploit Public-Facing Application]]
tactics: [[Initial Access]]
tags: open-redirect, phishing, uber, web-vulnerability
platforms: Web
tools: []
---

# Open Redirect on Uber Subdomains Enabling Phishing Attacks

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discovery and Exploitation] --> B[Phishing Enablement]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser or [[commands/curl-test-open-redirect]]

### Target Environment

- Web platform
- Access to Uber subdomains: rush.uber.com, business.uber.com, help.uber.com
- No specific ports required beyond standard HTTPS (443)

### Initial Access Requirements

- Public internet access
- No credentials needed for exploitation
- Ability to craft malicious URLs

## Detailed Attack Procedures

### Step 1: Exploit Open Redirect
procedure: [[procedures/Exploit-Open-Redirect-on-Uber-Subdomains]]

**Objective**: Redirect users from legitimate Uber subdomains to arbitrary malicious sites without interaction, enabling phishing attacks.

**Instructions**: Identify the vulnerable redirect endpoint on the target subdomains (e.g., /redirect?url=). Craft a URL with a malicious external site as the parameter value. Test using [[commands/curl-test-open-redirect]]:

```bash
curl -L "https://rush.uber.com/redirect?url=http://evil.com" -v
```

Share the crafted URL via email or social engineering to trick users into clicking, leading to automatic redirection.

**Expected Output**: HTTP response showing a 3xx redirect status to the malicious URL, confirming the vulnerability.

**Success Indicators**:
- Redirect occurs without user confirmation
- Victim browser navigates to evil.com
- Potential for phishing payload delivery

## Attack Chain Summary

### Key Achievements

1. Successful exploitation of open redirect on multiple Uber subdomains
2. Enablement of seamless phishing redirection
3. Demonstration of high-impact social engineering vector

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Phishing]] Phishing
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
