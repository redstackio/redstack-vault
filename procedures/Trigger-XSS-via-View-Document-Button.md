---
id: proc-983077-trigger-xss
tags:
  - xss
  - execution-trigger
  - dca-generation
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:20.862Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-View-Document-Button

## Summary

This procedure clicks the 'View document' button on the advanced vetting page to generate an example Custom Digital Agreement (DCA), causing the unsanitized Program Name to be rendered in a Markdown React component and executing the stored XSS payload.

## Description

The button triggers DCA generation, passing the Program Name directly to the Markdown React component, which does not sanitize HTML inputs. This leads to arbitrary JS/HTML execution in the viewer's context, limited to sandbox program members. Discovered via PoC showing <blink> and <marquee> rendering.

## Requirements

1. Loaded advanced vetting page from prior step
2. 'View document' button visible
3. Browser with console for JS verification

## Defense

Defensive measures and detection strategies:

- Sanitize inputs before passing to Markdown components (e.g., use DOMPurify)
- Validate and escape Program Name on DCA generation
- Detect XSS attempts via browser security logs or WAF rules for HTML tags

## Objectives

1. Generate example DCA with payload
2. Achieve XSS execution
3. Confirm impact on viewer session

## Instructions

### Step 1: Locate and Click Button

**Context**: Interact with the page to initiate DCA rendering.

On the advanced vetting page, locate and click the 'View document' button.

> This fetches and renders the DCA, injecting the payload into the Markdown component.

### Step 2: Observe Execution

**Context**: Verify payload activation.

Watch for visual changes like blinking text or marquee scrolling; check browser console for JS events.

> Expected: Payload executes, e.g., <a> link activates, proving arbitrary code run.

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
- [[execution-trigger]]
