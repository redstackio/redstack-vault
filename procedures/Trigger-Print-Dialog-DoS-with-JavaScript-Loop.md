---
tags:
  - dos
  - browser
  - javascript
  - brave
  - chromium
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
platforms:
  - Web
  - Browser (Brave/Chromium-based)
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 9880270a-1e57-4230-a30f-8426cb5df0d2
created_at: '2025-12-14T17:28:20.088Z'
updated_at: '2025-12-14T17:28:20.088Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Trigger-Print-Dialog-DoS-with-JavaScript-Loop

## Summary

This procedure creates and executes a proof-of-concept HTML file that uses a JavaScript infinite loop to repeatedly call window.print(), causing a flood of print dialogs in the Brave browser. This results in a denial-of-service attack by overwhelming the user interface, making the browser unusable until manually terminated. It targets the lack of invocation limits on the window.print() API in Chromium-based browsers like Brave.

## Description

The attack leverages client-side JavaScript execution in a web context to abuse the browser's print functionality. When the malicious HTML loads, the script enters an infinite loop calling window.print(), which triggers the native OS print dialog each time. This spams the UI, consumes resources, and prevents interaction with the browser tab or window. The vulnerability was reported via HackerOne (Report #176364) and classified as informative, as it requires user interaction to open the file and has no remote code execution or data exfiltration. It affects Brave on any platform supporting the browser (Windows, macOS, Linux). Prerequisites include a text editor for file creation and the ability to deliver the file to the victim (e.g., via email or web link). Expected outcomes: immediate DoS on the browser instance, with recovery possible by closing the tab or killing the process.

## Requirements

1. Brave browser installed on the target system
2. Ability to create and save an HTML file locally or host it online
3. Victim interaction to open the file in Brave (no automation required)

## Defense

Defensive measures and detection strategies:

- Educate users on avoiding suspicious HTML files or links from untrusted sources
- Browser extensions like uBlock Origin or NoScript to block or warn on suspicious JavaScript
- Monitor for anomalous browser behavior, such as high CPU from print dialogs, via endpoint detection tools (e.g., EDR alerts on process anomalies)
- Update Brave to the latest version, though this issue may persist in Chromium without specific patches

## Objectives

1. Overwhelm the browser UI with repeated print dialogs to deny service
2. Demonstrate API abuse for resource exhaustion
3. Highlight the need for rate limiting in browser JavaScript APIs

## Instructions

### Step 1: Create the Malicious HTML PoC File

**Context**: Prepare the attack payload by writing an HTML file with an infinite JavaScript loop invoking window.print(). This file serves as the vector for the DoS.

No command required; use a text editor to create `attack3.html` with the following content:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Print DoS PoC</title>
</head>
<body>
    <h1>Loading...</h1>
    <script>
        while(true) {
            window.print();
        }
    </script>
</body>
</html>
```

> This script starts the loop immediately upon page load, ensuring rapid onset of dialogs. Save the file in an accessible location.

### Step 2: Deliver and Execute the PoC in Brave

**Context**: Load the HTML file into the Brave browser to trigger the attack. Delivery can be direct (local open) or indirect (phishing).

Open the file by navigating to it in Brave (e.g., drag-and-drop or `file://` URL) or host it on a server and trick the victim into visiting the link.

> Upon loading, the print dialogs will spam continuously. The browser tab becomes unresponsive, achieving DoS. To stop, use Task Manager to end the Brave process or close the tab forcefully.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dos
- browser
- javascript
- brave
- chromium
