---
tags:
  - recon
  - rails
  - activestorage
type: procedure
tools:
  - '[[tools/ImageProcessing]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 36fe4271-06a8-4438-9a20-4d67ab162b7e
created_at: '2025-12-14T17:28:28.337Z'
updated_at: '2025-12-14T17:28:28.337Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Vulnerable ActiveStorage Variant Usage

## Summary

This procedure identifies code patterns in Ruby on Rails applications where user-supplied parameters are passed unsanitized to ActiveStorage's variant() or preview() methods, setting the stage for injection attacks.

## Description

In vulnerable Rails apps, ERB templates or controllers use user input directly in variant calls, such as resize: params[:new_size], allowing attackers to manipulate the ImageProcessing pipeline. This reconnaissance step involves code review or request interception to confirm the vulnerability, targeting apps with ActiveStorage 6.1.3.1 and related gems.

## Requirements

1. Access to application source code or ability to intercept HTTP requests (e.g., via proxy)
2. Authenticated session for image upload endpoints
3. Knowledge of Rails ActiveStorage usage

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all user parameters before passing to variant()
- Use whitelisting for allowed transformation keys
- Monitor for unusual ImageMagick command executions in logs

## Objectives

1. Confirm unsanitized parameter flow to ImageProcessing
2. Identify specific parameter names like :new_size or :t/:v
3. Establish baseline for exploitation

## Instructions

### Step 1: Review Application Code

**Context**: Examine ERB templates and controllers for vulnerable patterns.

Search for code like `<%= image_tag user.avatar.variant(resize: params[:new_size]) %>` or `variant(params[:t].to_s => params[:v].to_s)`.

> Use grep or IDE search: `grep -r "variant(" app/views/` to find matches.

### Step 2: Intercept and Test Requests

**Context**: Send test requests to verify parameter influence.

Use a proxy like Burp Suite to intercept a variant request and modify parameters with benign values, e.g., new_size=100x100, then observe if the image resizes accordingly.

> Expected: Image variant generated with the test size, confirming direct parameter usage.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/ImageProcessing]]

## Tags

- recon
- rails
