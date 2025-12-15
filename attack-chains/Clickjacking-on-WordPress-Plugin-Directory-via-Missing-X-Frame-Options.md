---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - clickjacking
  - ui-redressing
  - x-frame-options
  - wordpress
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
  - '[[procedures/Access-WordPress-Plugin-Directory-Site]]'
  - '[[procedures/Create-HTML-Page-with-Iframe-Embedding]]'
  - '[[procedures/Verify-Clickjacking-by-Loading-HTML]]'
step_count: 3
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:12.298Z'
description: >-
  Demonstrates clickjacking vulnerability on mercantile.wordpress.org by
  embedding the site in an iframe due to absent X-Frame-Options header, allowing
  UI redressing attacks.
skill_level: beginner
impact_level: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Clickjacking on WordPress Plugin Directory via Missing X-Frame-Options

Multi-stage attack chain demonstrating a complete attack workflow for exploiting clickjacking on mercantile.wordpress.org.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~2 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Target Site] --> B[Embed in Iframe]
    B --> C[Verify Framing]
    C --> D[UI Redressing Potential]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Web platform
- WordPress-based site without X-Frame-Options header
- No specific ports or services required beyond HTTP/HTTPS

### Initial Access Requirements

- Public internet access to https://mercantile.wordpress.org/
- Local file system access to create and open HTML files
- No credentials or prior access needed

## Detailed Attack Procedures

### Step 1: Access Target Website
procedure: [[procedures/Access-WordPress-Plugin-Directory-Site]]

**Objective**: Confirm accessibility of the target site and inspect for framing protections.

**Instructions**: Open the target URL in a browser to verify it loads without errors. Use browser developer tools to inspect HTTP response headers for the absence of X-Frame-Options.

**Expected Output**: Site loads successfully; response headers lack X-Frame-Options, indicating potential clickjacking risk.

**Success Indicators**:
- Site is accessible and interactive
- No X-Frame-Options header present in network tab

### Step 2: Embed Target URL in Iframe
procedure: [[procedures/Create-HTML-Page-with-Iframe-Embedding]]

**Objective**: Construct a malicious HTML page that embeds the target site in an iframe to bypass framing restrictions.

**Instructions**: Create a local HTML file with an iframe element sourcing the target URL. Set attributes for visibility and size to overlay or hide elements as needed for UI redressing.

**Expected Output**: HTML file saved locally, ready for testing.

**Success Indicators**:
- Iframe code is syntactically correct
- File can be opened without errors

### Step 3: Load HTML and Observe Iframe
procedure: [[procedures/Verify-Clickjacking-by-Loading-HTML]]

**Objective**: Demonstrate successful embedding by loading the HTML page and confirming the target site appears in the iframe without restrictions.

**Instructions**: Open the created HTML file in a browser and interact with the embedded site to verify full functionality, proving clickjacking is possible.

**Expected Output**: Target site loads fully within the iframe, allowing clicks and interactions as if on the original site.

**Success Indicators**:
- Iframe displays the target site without blocking
- User can perform actions like clicking links within the iframe

## Attack Chain Summary

### Key Achievements

1. Confirmed absence of X-Frame-Options on mercantile.wordpress.org
2. Successfully embedded the site in a cross-origin iframe
3. Demonstrated potential for UI redressing to trick users into unintended actions

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Drive-by Compromise]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
