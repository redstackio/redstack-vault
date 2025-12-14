---
tags:
  - xss
  - execution
  - cookie-theft
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:24.117Z'
sub_techniques: []
id: 5133fdc7-54e0-4894-8f5e-0b06da03c53d
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# View-Template-to-Execute-Stored-XSS

## Summary

This procedure triggers the execution of the stored XSS payload by rendering the tainted template in a browser, demonstrating arbitrary JavaScript execution that can lead to data theft or phishing attacks.

## Description

Following payload injection, this step involves previewing or sharing the template to cause its rendering, where the unsanitized description field executes the injected script in the viewer's context. For testing, the attacker can self-view; in exploitation, victims access via shared links or emails. The payload alerts the domain but can be modified for cookie exfiltration (e.g., via fetch to attacker server). This exploits the rendering pipeline's lack of output encoding, impacting any authenticated viewer.

## Requirements

1. Template saved with injected payload from prior procedure
2. Victim or test browser session
3. Optional: Attacker-controlled server for exfiltration

## Defense

Defensive measures and detection strategies:

- Apply output encoding when rendering user-controlled content
- Implement browser-based XSS auditors or extensions for detection
- Scan templates for known XSS patterns before rendering

## Objectives

1. Trigger JavaScript execution in the victim's browser
2. Validate XSS via alert or data exfiltration
3. Achieve impact like session hijacking

## Instructions

### Step 1: Preview or Share Template

**Context**: Initiate rendering of the template to load the banner block.

In the editor, click "Preview" to view in a new tab, or save and generate a shareable link to send to a victim.

> The template loads in a new window or browser, rendering all blocks including the banner.

### Step 2: Observe Payload Execution

**Context**: Confirm the script runs during rendering.

As the page loads, the description field's HTML parses, executing the onerror in the img tag, popping an alert with the domain.

> Alert box appears; in advanced payloads, network requests may exfiltrate cookies to an attacker endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
- [[cookie-theft]]
