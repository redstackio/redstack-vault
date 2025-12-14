---
tags:
  - xss
  - trigger
  - web
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
updated_at: '2025-12-14T03:16:37.416Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 82b2248c-51fc-4309-acc9-311940461121
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Review-Edit

## Summary

This procedure triggers the stored XSS payload by accessing the edit functionality of the injected review, exploiting poor output encoding during content rendering.

## Description

Once the payload is stored, Zomato's edit feature reloads the review content without proper escaping, allowing the JavaScript to parse and execute in the browser. This step demonstrates how standard user actions can activate the vulnerability, affecting the attacker's or victim's session. It requires the review to be visible and editable on the restaurant page.

## Requirements

1. Submitted review with payload from prior step
2. Access to the restaurant page where review is listed
3. Browser session with edit permissions

## Defense

Defensive measures and detection strategies:

- Encode output in edit forms using HTML entity encoding
- Implement client-side validation to flag suspicious content
- Log edit attempts and scan for script patterns

## Objectives

1. Load unsanitized review content into edit interface
2. Initiate payload evaluation during rendering
3. Confirm trigger without additional injection

## Instructions

### Step 1: Locate Submitted Review

**Context**: Find the injected review on the restaurant page to access its edit option.

Refresh the restaurant page (e.g., https://www.zomato.com/beirut/garcias-dbayeh-metn) and scroll to your review in the list.

### Step 2: Initiate Edit Action

**Context**: Click edit to render the stored payload, triggering execution if vulnerable.

Click the 'Edit' button next to the review.

> The edit form populates with the raw review text, parsing the img tag and attaching the onmouseover event.

**Expected Output**: Edit modal opens; hover over the injected img (if rendered) to see prompt.

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
- [[edit-trigger]]
