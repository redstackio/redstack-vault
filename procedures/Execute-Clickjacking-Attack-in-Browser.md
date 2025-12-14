---
id: proc-execute-clickjacking-browser
tags:
  - clickjacking
  - account-takeover
  - deactivation
type: procedure
tools:
  - '[[tools/SimpleScreenRecorder]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:05.030Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
# Execute-Clickjacking-Attack-in-Browser

## Summary

This procedure involves loading the malicious clickjacking HTML in a browser while authenticated to UPchieve, using overlaid instructions to trick the user into completing a multi-step account deactivation process, demonstrating the vulnerability's impact.

## Description

With the user authenticated to UPchieve, the malicious page loads the profile in an iframe. Overlaid divs guide clicks on hidden elements: first to the edit profile button, then to toggle account status, and finally to confirm deactivation. This UI redressing attack exploits the absence of frame protections, potentially leading to unauthorized account control or phishing escalation. A screen recording captures the PoC for verification.

## Requirements

1. Authenticated browser session to UPchieve
2. The malicious HTML file from prior procedure
3. Screen recording tool for PoC documentation

## Defense

Defensive measures and detection strategies:

- Educate users on suspicious overlays or unexpected prompts
- Browser extensions to detect clickjacking (e.g., frame-busting detectors)
- Server-side logging of unusual session actions like sudden deactivations

## Objectives

1. Trick the user into initiating account edit via iframe clicks
2. Force completion of deactivation sequence
3. Validate impact through account status change

## Instructions

### Step 1: Prepare and Load the Malicious Page

**Context**: Save the HTML and open it in a browser with active authentication.

No command required; save as 'clickjack.html' and open via file:// or host on a local server.

> Ensure the browser has a valid UPchieve session cookie; the iframe will load the authenticated profile.

### Step 2: Record and Execute the Tricked Clicks

**Context**: Use screen recording to capture the user following overlay instructions.

Launch [[tools/SimpleScreenRecorder]] and start recording while interacting:

- Click overlay 1 to hit edit button
- Click overlay 2 to toggle status
- Click overlay 3 to confirm deactivation

> The user perceives clicking instructions but actually interacts with the framed page.

### Step 3: Verify Deactivation

**Context**: Check the profile page directly for status change.

Navigate to https://app.upchieve.org/profile in the browser to confirm account is deactivated.

**Expected Output**: Profile shows deactivated status; no further access possible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/SimpleScreenRecorder]]

## Tags

- [[clickjacking]]
- [[web-exploit]]
