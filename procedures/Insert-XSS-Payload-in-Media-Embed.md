---
id: proc-insert-xss-media-embed
tags:
  - xss
  - payload-injection
  - stored-xss
  - polldaddy
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
updated_at: '2025-12-14T03:46:31.442Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Insert-XSS-Payload-in-Media-Embed

## Summary

This procedure details injecting a stored XSS payload into the Media Embed section of a Polldaddy quiz by formatting it as a shortcode to bypass sanitization, enabling persistent script storage.

## Description

Polldaddy's Media Embed field in quiz creation lacks proper validation for shortcode-like inputs, allowing attackers to store HTML/JavaScript. The payload uses an img tag with an onerror handler that executes when the invalid src fails to load. This is tested during quiz editing and exploits the storage mechanism. Prerequisites include an existing quiz draft. Outcome: Malicious script stored and ready for execution on quiz views.

## Requirements

1. Existing Polldaddy quiz draft from prior procedure
2. Knowledge of XSS payload crafting
3. Web browser for testing (avoid executing in production sessions)

## Defense

Defensive measures and detection strategies:

- Sanitize Media Embed inputs by stripping or escaping JavaScript attributes (e.g., onerror)
- Validate shortcode formats strictly and reject malformed ones
- Scan stored quiz content for XSS patterns using tools like DOMPurify

## Objectives

1. Bypass input sanitization with shortcode mimicry
2. Store executable JavaScript in the quiz
3. Ensure payload persists without immediate detection

## Instructions

### Step 1: Locate Media Embed Section

**Context**: Open the quiz editor and find the embed field for a question.

In the quiz editor, select a question and scroll to the "Media Embed" or "Insert Media" option. This field accepts custom inputs intended for embeds like videos.

> Web UI navigation. Expected output: Text input field appears for embed code.

### Step 2: Craft and Insert Payload

**Context**: Input the XSS payload formatted to resemble a valid shortcode.

Enter the following payload: `[&lt;img src=&quot;http://url.to.file.which/not.exist&quot; onerror=alert(\&quot;Hello!\&quot;);&gt;]`. Replace the alert with more malicious code if needed (e.g., document.cookie exfiltration). Click "Save Quiz".

> Custom payload input. Expected output: Quiz saves; preview may show broken img but no execution yet.

### Step 3: Verify Storage

**Context**: Check that the payload is stored without errors.

Reload the quiz editor and confirm the Media Embed field retains the input. Avoid previewing in the same session to prevent self-execution.

> UI verification. Expected output: Payload visible in edit mode.

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
- [[payload-injection]]
