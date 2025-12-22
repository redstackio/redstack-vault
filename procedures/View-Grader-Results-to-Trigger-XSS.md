---
tags:
  - xss
  - execution-trigger
  - web
type: procedure
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:31.828Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 9e865341-3631-487e-b321-a4ab1422ec83
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# View-Grader-Results-to-Trigger-XSS

## Summary

This procedure involves viewing the results from the Shopify Ecommerce Store Grader Tool, which echoes the unsanitized src attribute from the submitted page, triggering the XSS payload execution in the browser.

## Description

Once the grader processes the URL, it displays error messages about missing ALT tags, directly inserting the user-controlled src value without escaping. This causes the browser to parse and execute the embedded onerror JavaScript, such as alert(123). The impact includes potential theft of session data for authenticated users viewing the results.

## Requirements

1. Successful completion of prior submission step
2. Web browser with JavaScript enabled
3. Access to the generated results page

## Defense

Defensive measures and detection strategies:

- Escape HTML attributes in all output (e.g., use textContent instead of innerHTML)
- Implement output encoding for reflected content
- Monitor for JavaScript errors or alerts in client-side logs

## Objectives

1. Cause reflection of the malicious src in error messages
2. Execute arbitrary JavaScript in the viewer's context
3. Demonstrate potential for data exfiltration or hijacking

## Instructions

### Step 1: Access Results Page

**Context**: Navigate to or refresh the grader results after processing.

No command; simply view the full report in the same browser tab.

> Look for sections highlighting image issues. The payload should be embedded in the displayed error text.

### Step 2: Observe Execution

**Context**: Confirm the XSS triggers by watching for the alert.

Interact with the results page (e.g., scroll to the error block).

> Expected: An alert('123') dialog appears, indicating successful execution. Check browser console for any additional errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-trigger
- js-execution
