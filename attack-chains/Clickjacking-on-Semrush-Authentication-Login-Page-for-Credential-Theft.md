---
id: ac-clickjacking-semrush-auth
tags:
  - clickjacking
  - ui-redressing
  - credential-theft
  - semrush
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
  - '[[procedures/Demonstrate-Clickjacking-on-Semrush-Login]]'
step_count: 2
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:30:58.774Z'
description: >-
  A clickjacking attack exploiting the lack of frame-busting protections on
  Semrush's geo.semrush.com login page, allowing embedding in an iframe to trick
  users into entering credentials.
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Clickjacking on Semrush Authentication Login Page for Credential Theft

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
    A[Setup Malicious Page] --> B[Embed and Trick User]
    B --> C[Capture Credentials]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses basic HTML and browser)

### Target Environment

- Web platform
- Access to Semrush geo.semrush.com login page
- No specific ports or services beyond HTTP/HTTPS

### Initial Access Requirements

- Ability to host or open a local HTML file
- User interaction required (tricking victim to visit malicious page)
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Create Malicious HTML Page with Iframe
procedure: [[procedures/Demonstrate-Clickjacking-on-Semrush-Login]]

**Objective**: Embed the Semrush login page in an invisible or overlaid iframe to demonstrate vulnerability.

**Instructions**: Create a simple HTML file that loads the target login URL in an iframe without any frame restrictions.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Clickjacking PoC</title>
</head>
<body>
    <iframe src="https://geo.semrush.com/" width="100%" height="100%" style="opacity: 0.5;"></iframe>
    <!-- Overlay elements can be added here to trick clicks -->
</body>
</html>
```

Save this as `clickjacking-poc.html` and open it in a browser.

**Expected Output**: The Semrush Single Sign-On login page appears within the iframe, confirming it can be embedded.

**Success Indicators**:
- Login popup or page loads inside the iframe without errors
- No X-Frame-Options denial observed

### Step 2: Simulate User Interaction for Credential Capture
procedure: [[procedures/Demonstrate-Clickjacking-on-Semrush-Login]]

**Objective**: Trick a user into interacting with the overlaid login form, potentially capturing entered credentials.

**Instructions**: Enhance the HTML to include a transparent overlay that aligns invisible elements over the iframe's login fields. Host the page on a server or share it to lure victims.

For demonstration, open the HTML file locally and interact with the visible login elements through the frame.

**Expected Output**: User inputs (e.g., username/password) are processed by the Semrush page, but in a real attack, could be intercepted or observed via overlays.

**Success Indicators**:
- Successful embedding allows form submission from the iframe
- Potential for account takeover if credentials are entered unknowingly

## Attack Chain Summary

### Key Achievements

1. Confirmed lack of frame-busting headers on Semrush login page
2. Demonstrated iframe embedding for UI redressing
3. Highlighted risk of credential theft through user deception

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Drive-by Compromise]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---

*Last updated: 2023-10-01T00:00:00Z*
