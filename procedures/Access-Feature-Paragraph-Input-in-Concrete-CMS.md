---
id: proc-access-feature-paragraph-concrete-cms
tags:
  - xss
  - concrete-cms
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:35.546Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Feature-Paragraph-Input-in-Concrete-CMS

## Summary

This procedure outlines how to navigate to the content editing interface in Concrete CMS to access the Feature Paragraph input field, which is vulnerable to stored XSS due to lack of proper sanitization.

## Description

In Concrete CMS, the Feature Paragraph feature allows users to add text blocks to pages. The input field for this feature does not properly sanitize user input, enabling the injection of HTML and JavaScript. This procedure assumes authenticated access to the CMS and focuses on locating the vulnerable input as the first step in exploiting the stored XSS vulnerability. Expected outcomes include exposure of the editable field for payload injection, setting the stage for persistent client-side attacks affecting all page viewers.

## Requirements

1. Valid credentials for a Concrete CMS user with content editing permissions
2. Web browser with access to the CMS URL
3. Network connectivity to the Concrete CMS instance (typically over HTTP/HTTPS)

## Defense

Defensive measures and detection strategies:

- Implement role-based access control to limit editing privileges
- Enable content security policy (CSP) headers to restrict script execution
- Monitor admin logs for unusual content edits

## Objectives

1. Gain access to the vulnerable Feature Paragraph input field
2. Prepare for payload injection without triggering immediate validation
3. Establish initial foothold for stored XSS exploitation

## Instructions

### Step 1: Log In to Concrete CMS

**Context**: Authenticate to the CMS dashboard to reach editing interfaces.

Log in using valid credentials at the CMS login page. Navigate to the admin dashboard or page editor.

> Upon successful login, the dashboard loads, providing access to content management tools.

### Step 2: Locate Feature Paragraph Feature

**Context**: Identify and access the specific input field vulnerable to XSS.

In the page editor or block composer, add a new block or edit an existing one, selecting the 'Feature Paragraph' option. This exposes the text input field.

> The input field appears, ready for text entry, without any visible sanitization warnings.

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
- [[web]]
