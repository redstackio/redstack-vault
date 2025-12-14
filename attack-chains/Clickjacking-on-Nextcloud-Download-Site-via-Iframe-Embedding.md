---
id: ac-clickjacking-nextcloud-download
name: Clickjacking on Nextcloud Download Site via Iframe Embedding
tags:
  - clickjacking
  - web
  - iframe
  - nextcloud
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
  - '[[procedures/Demonstrate-Clickjacking-via-Iframe-Embedding]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:04.492Z'
description: >-
  Demonstrates a clickjacking vulnerability on the Nextcloud download website by
  embedding it in an iframe without frame-busting protections, allowing
  attackers to overlay invisible elements and trick users into unintended
  actions like file downloads.
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Clickjacking on Nextcloud Download Site via Iframe Embedding

Multi-stage attack chain demonstrating a complete attack workflow for exploiting clickjacking on the Nextcloud download site.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~2 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Iframe HTML] --> B[Embed and Test in Browser]
    B --> C[Trick User Actions]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)
- Text editor (e.g., Notepad, VS Code)

### Target Environment

- Target: https://download.nextcloud.com
- Required services/ports: HTTP/HTTPS on port 80/443
- Network access requirements: Internet access to the target site

### Initial Access Requirements

- No credentials required
- Direct internet access
- No prior access needed

## Detailed Attack Procedures

### Step 1: Create Iframe HTML File
procedure: [[procedures/Demonstrate-Clickjacking-via-Iframe-Embedding]]

**Objective**: Construct an HTML page that embeds the vulnerable Nextcloud download site in an iframe to test for clickjacking susceptibility.

**Instructions**: Use a text editor to create a file named `clickjacking.html` with the following content:

```html
<html>
<head>
<title>Clickjack test page</title>
</head>
<body>
<p>Website is vulnerable to clickjacking!</p>
<iframe src="https://download.nextcloud.com" width="500" height="500"></iframe>
</body>
</html>
```

Save the file locally.

**Expected Output**: An HTML file that, when opened, will load the target site in an iframe.

**Success Indicators**:
- HTML file created without errors
- File saved in accessible location

### Step 2: Test Embedding in Browser
procedure: [[procedures/Demonstrate-Clickjacking-via-Iframe-Embedding]]

**Objective**: Load the HTML file in a browser to confirm the site embeds without restrictions, verifying the clickjacking vulnerability.

**Instructions**: Open the `clickjacking.html` file in any modern web browser (e.g., double-click the file or use File > Open).

Observe the iframe loading the Nextcloud download site fully without any frame-busting errors or blocks.

**Expected Output**: The target site (https://download.nextcloud.com) renders inside the iframe, allowing potential overlay of invisible elements for user deception.

**Success Indicators**:
- Site loads in iframe without restrictions
- No X-Frame-Options header blocks the embedding

## Attack Chain Summary

### Key Achievements

1. Successfully embedded the Nextcloud download site in an external iframe
2. Confirmed absence of frame-busting protections like X-Frame-Options
3. Demonstrated potential for tricking users into unintended actions, such as downloading malicious files

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
