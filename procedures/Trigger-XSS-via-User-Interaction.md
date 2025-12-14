---
id: proc-reddit-xss-trigger-001
tags:
  - xss-execution
  - event-handler
  - client-side
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:19.891Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-User-Interaction

## Summary

This procedure triggers the execution of an injected JavaScript payload in a reflected XSS attack by performing a user interaction that activates the embedded HTML event handler on Reddit's sh.reddit.com page.

## Description

After the malicious URL is loaded, the onmouseover event handler is present in the DOM, typically on comment elements like 'see more' links. Scrolling to the bottom of the page and hovering over such an element executes the payload (e.g., alert(document.domain)), running arbitrary JavaScript in the victim's browser. This can lead to stealing cookies, keystrokes, or redirecting to phishing sites. The technique relies on social engineering to induce the hover action and is effective against unsanitized web APIs.

## Requirements

1. The page must have loaded the injected payload from the previous step
2. Victim must scroll to the relevant page section
3. Standard mouse input capability in the browser

## Defense

Defensive measures and detection strategies:

- Strip or encode HTML attributes in API responses
- Implement client-side validation to prevent event handler execution
- Log and alert on unexpected JavaScript errors or popups in browser consoles
- Educate users on avoiding suspicious links and hovering over unknown elements

## Objectives

1. Activate the onmouseover event to execute JavaScript
2. Demonstrate arbitrary code execution in the browser context
3. Enable further attacks like data exfiltration

## Instructions

### Step 1: Load the Injected Page

**Context**: Ensure the page with the reflected payload is fully rendered.

Navigate to the crafted URL from the injection procedure.

Wait for the comments to load.

### Step 2: Scroll to Trigger Element

**Context**: Position the cursor over the vulnerable element.

Scroll down to the end of the comments section where 'see more' options appear.

### Step 3: Perform Hover Interaction

**Context**: Trigger the event handler to execute the payload.

Move the mouse cursor over the 'see more' link.

> This activates onmouseover=alert(document.domain), popping an alert with the domain name.

**Expected Output**: Alert dialog displays 'sh.reddit.com' or similar.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
- [[browser]]
