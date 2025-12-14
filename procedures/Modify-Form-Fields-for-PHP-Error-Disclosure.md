---
tags:
  - information-disclosure
  - path-disclosure
  - php
  - browser-devtools
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Inspect-Element]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:12.327Z'
sub_techniques: []
id: cb6e8f34-760d-44e1-89eb-23535d4a6a3d
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Modify-Form-Fields-for-PHP-Error-Disclosure

## Summary

This procedure uses browser developer tools to tamper with form inputs in the basic-google-maps-placemarks plugin, appending empty array syntax ([]) to values, which triggers PHP notices revealing file paths upon form submission.

## Description

The plugin's form fields process user input as arrays without validation, so modifying a field value to include '[]' (e.g., changing 'value' to 'value[]') causes PHP to treat it as an array offset, leading to an undefined index warning. The error message exposes the full path to the processing script. This is particularly effective in Firefox's Inspect Element tool for real-time HTML manipulation. Outcomes include path disclosure that can inform targeted attacks, though the vulnerability was noted as non-applicable in some reports due to low severity.

## Requirements

1. Firefox browser with developer tools enabled
2. Access to the plugin's form page (e.g., placemark configuration form)
3. No authentication; assumes public or low-privilege access

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all form inputs server-side (e.g., use filter_input() to enforce scalar types)
- Suppress error display with ini_set('display_errors', 0) and enable logging
- Implement Content Security Policy (CSP) to limit devtools interference, though not fully preventive
- Audit PHP error logs for patterns of undefined array accesses from form submissions

## Objectives

1. Alter form data to induce PHP array errors
2. Capture disclosed paths from error messages
3. Enhance reconnaissance for plugin-specific file locations

## Instructions

### Step 1: Load and Inspect the Form

**Context**: Navigate to the plugin's form and use devtools to locate editable input fields.

No specific command; browser interaction.

> In Firefox, go to the target form page (e.g., http://target.com/plugin-form). Right-click an input field and select 'Inspect Element' to open devtools.

### Step 2: Modify Input Value and Submit

**Context**: Append empty array syntax to the field's value attribute to trigger the error on submission.

No specific command; edit HTML.

> In the Elements panel, find the input tag (e.g., <input value="somevalue">), change it to <input value="somevalue[]">, then submit the form. Observe the PHP error in the response.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Inspect-Element]]

## Tags

- information-disclosure
- path-disclosure
- php
- browser-devtools
