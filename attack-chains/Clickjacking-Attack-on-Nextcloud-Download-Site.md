---
tags:
  - clickjacking
  - ui-redressing
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
procedures:
  - '[[procedures/Demonstrate-Clickjacking-with-Iframe-Embedding]]'
step_count: 2
techniques:
  - '[[Drive-by Compromise]]'
description: >-
  Demonstrates a clickjacking vulnerability on the Nextcloud download website by
  embedding it in an iframe, allowing potential click hijacking.
skill_level: beginner
impact_level: medium
id: d7648ae6-30bb-46f4-963f-f9d71e3f0d4f
created_at: '2025-12-14T17:28:04.522Z'
updated_at: '2025-12-14T17:28:04.522Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Clickjacking Attack on Nextcloud Download Site

Multi-stage attack chain demonstrating a complete attack workflow.

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
    A[Create Malicious HTML] --> B[Embed and Demonstrate Clickjacking]
    B --> C[Hijack User Clicks]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)
- Text editor (e.g., Notepad, VS Code)

### Target Environment

- Target: Web platform
- Required services/ports: HTTP/HTTPS on port 443
- Network access requirements: Internet access to https://download.nextcloud.com/

### Initial Access Requirements

- No credentials required
- Public network access
- No prior access needed

## Detailed Attack Procedures

### Step 1: Create Malicious HTML File
procedure: [[procedures/Demonstrate-Clickjacking-with-Iframe-Embedding]]

**Objective**: Craft an HTML page that embeds the vulnerable Nextcloud download site in an iframe without frame-busting protections, setting up the clickjacking overlay.

**Instructions**: Use a text editor to create an HTML file with an iframe targeting the vulnerable site. The iframe should be sized to overlay the legitimate content transparently.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Clickjacking Demo</title>
</head>
<body>
    <p>This demonstrates a clickjacking vulnerability on Nextcloud download site.</p>
    <iframe src="https://download.nextcloud.com/" width="700" height="700"></iframe>
</body>
</html>
```

**Expected Output**: An HTML file that, when opened, loads the Nextcloud site in an iframe.

**Success Indicators**:
- HTML file created without errors
- Iframe embeds the site successfully when previewed

### Step 2: Execute and Verify Clickjacking
procedure: [[procedures/Demonstrate-Clickjacking-with-Iframe-Embedding]]

**Objective**: Load the HTML file in a browser to verify the site can be iframed, enabling potential click hijacking where user interactions are redirected to malicious actions.

**Instructions**: Save the HTML file (e.g., as clickjack.html) and open it in a web browser. Observe that the Nextcloud download page loads within the iframe, confirming lack of X-Frame-Options protection. An attacker could overlay invisible elements to hijack clicks, such as tricking users into downloading malware or authorizing actions.

**Expected Output**: The Nextcloud download site appears embedded in the iframe without restrictions, allowing transparent overlay for click manipulation.

**Success Indicators**:
- Site loads in iframe without blocking
- Clicks on the embedded content can be intercepted or redirected in a real attack scenario

## Attack Chain Summary

### Key Achievements

1. Successfully embedded the Nextcloud download site in an external iframe.
2. Demonstrated absence of frame-busting headers like X-Frame-Options.
3. Highlighted potential for click hijacking leading to unauthorized user actions or phishing.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Drive-by Compromise]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---

*Last updated: 2023-10-01T00:00:00Z*
