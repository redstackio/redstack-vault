---
tags:
  - clickjacking
  - ui-redressing
  - x-frame-options
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/User-Agent-Switcher]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Test-and-Exploit-Clickjacking-on-Mobile-Site]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:04.923Z'
description: >-
  A multi-step attack exploiting the absence of X-FRAME-OPTIONS on Mavenlink's
  mobile site to enable UI redressing, tricking users into unauthorized actions
  like workspace creation.
skill_level: intermediate
impact_level: high
id: b5d37b49-7359-469c-8f45-5680f6c3e86c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Clickjacking on Mavenlink Mobile Site to Trick Authenticated Users into Creating Workspaces

Multi-stage attack chain demonstrating a complete attack workflow exploiting Clickjacking on the mobile version of Mavenlink.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Mobile Site] --> B[Test and Exploit Clickjacking]
    B --> C[Trick User into Action]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/User-Agent-Switcher]]

### Target Environment

- Web platform
- Mobile version of the target site (e.g., m.mavenlink.com)
- No specific ports or services required beyond standard HTTPS

### Initial Access Requirements

- Ability to access the target website
- No credentials needed for discovery, but authenticated session required for impact demonstration
- Network access to the internet

## Detailed Attack Procedures

### Step 1: Access Mobile Version of the Site
procedure: [[procedures/Test-and-Exploit-Clickjacking-on-Mobile-Site]]

**Objective**: Simulate a mobile browser to access the vulnerable mobile site and identify the target page for iframing.

**Instructions**: Use [[tools/User-Agent-Switcher]] to change your browser's user agent to a mobile one (e.g., iPhone) and navigate to https://m.mavenlink.com/. This reveals the mobile interface, such as the workspaces/new page, which lacks frame protection.

**Expected Output**: The mobile site loads, allowing navigation to sensitive pages like /#/workspaces/new.

**Success Indicators**:
- Mobile site interface appears without desktop fallback
- Page loads successfully in the browser

### Step 2: Test and Exploit Clickjacking
procedure: [[procedures/Test-and-Exploit-Clickjacking-on-Mobile-Site]]

**Objective**: Embed the target page in an iframe on a malicious site to demonstrate UI redressing, overlaying invisible elements to trick users into actions like creating a workspace.

**Instructions**: Create a simple HTML PoC file with an iframe pointing to https://m.mavenlink.com/#/workspaces/new. Host this on a local server or external domain. For an authenticated user, the iframe loads the page, allowing overlay attacks where clicks on seemingly benign elements trigger workspace creation.

**Expected Output**: The iframe successfully loads the Mavenlink page without blocking, confirming the vulnerability.

**Success Indicators**:
- Iframe content renders without errors or restrictions
- Authenticated actions (e.g., form submission) can be induced via overlays

## Attack Chain Summary

### Key Achievements

1. Identified lack of X-FRAME-OPTIONS on mobile site while main site is protected
2. Demonstrated PoC for embedding sensitive pages in iframes
3. Highlighted potential for social engineering attacks on authenticated users

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
