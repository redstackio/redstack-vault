---
id: proc-stripo-create-template
tags:
  - web-access
  - template-creation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:33.501Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-New-HTML-Email-Template-in-Stripo

## Summary

This procedure outlines accessing the Stripo email template editor and creating a new HTML-based template, serving as the entry point for injecting malicious content like iframes.

## Description

In the context of exploiting CSP misconfigurations, this step provides access to the raw HTML editor in Stripo's platform (https://my.stripo.email). The editor allows direct HTML manipulation without strict sanitization, enabling subsequent iframe injections. Prerequisites include a valid Stripo account; the process targets the web-based interface and assumes no prior authentication bypass is needed.

## Requirements

1. Valid login credentials for Stripo (free account works)
2. Web browser with JavaScript enabled
3. Network access to https://my.stripo.email

## Defense

Defensive measures and detection strategies:

- Implement strict input validation in HTML editors to block iframe tags
- Monitor for unusual template creations or HTML injections via logging
- Use WAF rules to detect iframe src patterns matching public hosting wildcards

## Objectives

1. Gain editable access to HTML content in the template
2. Prepare the environment for payload insertion
3. Verify editor functionality without disruptions

## Instructions

### Step 1: Log In and Navigate to Editor

**Context**: Authenticate and access the cabinet to reach the template creation area.

No specific command; use browser to visit https://my.stripo.email/cabinet/#/template-editor/ and log in.

> Expected: Dashboard loads; click 'New Template' or similar to start HTML mode.

### Step 2: Select HTML Template Type

**Context**: Choose an HTML-based template to enable raw source editing.

Switch to HTML view in the editor.

> Expected: Blank HTML canvas opens, ready for content addition.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web-access
- template-creation
