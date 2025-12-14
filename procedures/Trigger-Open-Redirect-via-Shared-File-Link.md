---
id: proc-uuid-2
tags:
  - open-redirect
  - phishing
  - drive-by
  - rocket-chat
type: procedure
tools: []
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
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:27.138Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[T1566.002]]'
---
# Trigger-Open-Redirect-via-Shared-File-Link

## Summary

This procedure shares the URL of an uploaded malicious SVG file from Rocket.Chat, tricking victims into accessing it and executing the embedded JavaScript for an open redirect to a phishing site or other malicious actions.

## Description

Once a malicious SVG is uploaded, its Rocket.Chat URL serves the content in a context that allows JavaScript execution, despite external storage. Sharing this link via phishing tactics leads to automatic redirection or exploits when victims visit. This relies on social engineering to get clicks and targets browser rendering of SVGs.

## Requirements

1. Uploaded malicious SVG with a valid Rocket.Chat URL
2. Means to communicate the link to victims (e.g., email, social media)
3. Control over a phishing or exploit hosting site
4. Browser for testing the redirect

## Defense

Defensive measures and detection strategies:

- Implement URL scanning for shared links in chats
- Use browser extensions or policies to block SVG JS execution
- Log and alert on file access patterns from uploads
- Train users to verify file sources before opening

## Objectives

1. Lure victim to access the weaponized URL
2. Execute client-side JavaScript for redirect or payload delivery
3. Achieve phishing success or further compromise

## Instructions

### Step 1: Obtain and Share the File URL

**Context**: Extract the shareable link from the chat and distribute it to the target.

1. In the Rocket.Chat chat, right-click or copy the file link (e.g., `https://open.rocket.chat/file-upload/{ID}/redirect.svg`).
2. Craft a phishing message, e.g., "Check out this diagram: [link]".
3. Send via email or other channels.

### Step 2: Verify Execution

**Context**: Test the URL to ensure JS executes as intended.

Open the URL in a browser. The SVG loads, and the script redirects to the target site.

Monitor your phishing site for incoming traffic from the victim's IP.

**Expected Output**: Immediate browser redirect to the malicious domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]
- [[T1566.002]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[open-redirect]]
- [[Phishing]]
- [[drive-by]]
- [[rocket-chat]]
