---
tags:
  - template
  - jsreport
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 84588ebb-bfe0-4d22-b972-5741a9bd12bc
created_at: '2025-12-14T17:23:25.004Z'
updated_at: '2025-12-14T17:23:25.004Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create Initial Template in jsreport

## Summary

This procedure creates a basic HTML template in the jsreport web interface to prepare for SSRF testing and port scanning.

## Description

The jsreport interface allows unauthenticated creation of templates used for rendering reports. This initial template serves as a base for injecting SSRF payloads via HTML elements like img tags.

## Requirements

1. Access to jsreport web interface at http://localhost
2. Web browser (e.g., Chrome)

## Defense

Defensive measures and detection strategies:

- Implement authentication on jsreport admin interfaces
- Log and monitor template creation events
- Sanitize HTML inputs in templates

## Objectives

1. Create and save a simple template
2. Obtain the template's short ID for API usage
3. Verify rendering capability

## Instructions

### Step 1: Access Interface and Create Template

**Context**: Navigate to the dashboard and add a new template for testing.

**Command** (Browser Action):
No CLI command; use web interface.

> Go to http://localhost, click 'Templates' > 'New Template', name it 'test1', add HTML `<h1>hello world</h1>`, save. Note the shortid (e.g., BJe2Pi2AgB) from the URL or list.

### Step 2: Test Rendering

**Context**: Ensure the template renders correctly before exploitation.

**Command** (Browser Action):
No CLI; select chrome-pdf recipe and run.

> Produces a PDF with 'hello world' if successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- template
- jsreport
