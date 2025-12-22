---
tags:
  - xss
  - concrete-cms
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - PHP
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 01a4fbc6-9f31-4a64-bd57-23174191e4ef
created_at: '2025-12-14T00:11:09.651Z'
updated_at: '2025-12-14T00:11:09.651Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Malicious-Select-Attribute-in-Concrete-CMS

## Summary

This procedure outlines the creation of a new 'select' type attribute in Concrete CMS, setting the stage for injecting a stored XSS payload by exploiting the lack of sanitization in attribute options.

## Description

In Concrete CMS, attributes are customizable fields for pages, blocks, and forms. The 'select' attribute type allows predefined options, but user input for these options is not properly escaped when rendered back in the edit interface. This procedure creates such an attribute, requiring admin access to the dashboard. It is the first step in a stored XSS attack, enabling subsequent payload injection. Expected outcomes include a persistent attribute that can hold malicious content, potentially leading to JavaScript execution on admin pages or Express Forms.

## Requirements

1. Authenticated access to Concrete CMS admin dashboard
2. Web browser for navigation
3. Target Concrete CMS instance vulnerable to unsanitized attribute rendering

## Defense

Defensive measures and detection strategies:

- Implement input validation and HTML escaping for all user-supplied attribute values
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor admin dashboard logs for unusual attribute creations

## Objectives

1. Establish a vector for stored XSS by creating a configurable select attribute
2. Prepare for payload injection without triggering immediate alerts
3. Enable persistence across sessions for later exploitation

## Instructions

### Step 1: Access Attribute Management

**Context**: Log in and navigate to the attribute creation interface to select the vulnerable type.

Access the Concrete CMS dashboard at /index.php/dashboard/system/attributes. Click 'Add Attribute Type' and select 'Select' from the dropdown.

> This opens the configuration form for basic attribute details.

### Step 2: Configure Basic Attribute Details

**Context**: Provide necessary metadata to save the attribute skeleton.

Enter a name (e.g., 'Vulnerable Select') and handle (e.g., 'vulnerable_select'). Optionally, set a description. Do not add options yet. Click 'Add' to save.

> The attribute is now listed and ready for option configuration in the next procedure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[concrete-cms]]
