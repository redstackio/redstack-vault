---
id: proc-brave-ios-spoof-poc-001
tags:
  - address-bar-spoofing
  - phishing
  - brave-browser
  - ios
  - javascript
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - iOS
  - Mobile Browser
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Phishing]]'
updated_at: '2025-12-14T17:24:42.184Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Phishing]]'
---
# Execute Brave iOS Address Bar Spoofing PoC

## Summary

This procedure exploits a UI spoofing vulnerability in Brave for iOS (v1.2.16) by loading and executing a JavaScript-based PoC that injects malicious content while spoofing the address bar to display a trusted URL, enabling effective phishing attacks.

## Description

The attack targets improper synchronization in Brave's address bar rendering during JavaScript content injection and rapid redirects. An attacker hosts or delivers an HTML page with embedded JavaScript that uses document.write() to overwrite page content and setInterval() for periodic location reloads to a port-modified trusted domain (e.g., google.com:1234). This causes the address bar to lag and display the spoofed URL while malicious phishing content loads, tricking users into entering credentials. The vulnerability was reported on HackerOne (#176929) and affects iOS mobile browsing, with high impact for social engineering in phishing scenarios. Prerequisites include victim access to the PoC page via link or file.

## Requirements

1. Brave for iOS version 1.2.16 (or vulnerable build) installed on an iOS device
2. Access to create/host a simple HTML file with JavaScript (no special tools needed)
3. Victim interaction to load and click within the browser

## Defense

Defensive measures and detection strategies:

- Update Brave to the latest version to patch address bar synchronization issues
- Enable browser warnings for non-standard ports and unexpected content changes
- User training on verifying URLs and avoiding suspicious links; monitor for anomalous JavaScript redirects in browser logs

## Objectives

1. Spoof the browser address bar to mimic a trusted site
2. Inject and display phishing content without detection
3. Facilitate credential theft or malware delivery via social engineering

## Instructions

### Step 1: Prepare and Load the PoC HTML Page

**Context**: Create the malicious HTML snippet containing the spoofing JavaScript and load it into Brave for iOS to set up the exploit.

The PoC HTML is as follows (host on a server or save locally):

```html
<!DOCTYPE html>
<html>
<head><title>Spoof Test</title></head>
<body>
<button onclick="spoof()">Spoof</button>
<script>
function spoof() {
  document.write('This is not Google');
  document.location = 'https://google.com:1234';
  setInterval(function() { document.location.reload(); }, 9800);
}
</script>
</body>
</html>
```

Open the file or URL in Brave for iOS. The page should display a 'Spoof' button.

> This step delivers the payload without triggering immediate alerts, as it's standard web content.

### Step 2: Execute the Spoofing Function

**Context**: Trigger the JavaScript to inject content and manipulate the location, desynchronizing the address bar update.

Click the 'Spoof' button in the loaded page.

> The function injects 'This is not Google' text, redirects to the spoofed URL, and reloads periodically. In vulnerable Brave versions, the address bar shows 'https://google.com:1234' while displaying the injected content, confirming the spoof.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Phishing]] Phishing

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- address-bar-spoofing
- phishing
- brave-browser
- ios
- javascript
