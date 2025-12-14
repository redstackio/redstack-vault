---
tags:
  - recon
  - web-endpoint
  - xss-prep
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T00:11:09.783Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: da26139b-4d91-4501-bf33-63ff4a7ac933
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Mouthoff-Feedback-Endpoint

## Summary

This procedure involves locating the feedback submission endpoint on the Rockstar Games website to identify vulnerable parameters for XSS injection. It focuses on the 'Mouthoff to Rockstar' form, revealing the POST endpoint /mouthoff/mouthoff/submit.json.

## Description

In a Blind XSS attack, the first step is reconnaissance to understand the target's feedback mechanism. The Rockstar Games website hosts a public form for user comments at https://www.rockstargames.com/mouthoff. By inspecting network requests during form submission (e.g., via browser dev tools), attackers discover the JSON endpoint that processes inputs like name, subject, body, email, age, and category_id. This endpoint lacks proper sanitization, allowing stored XSS payloads to persist until admin review.

## Requirements

1. Web browser with developer tools (e.g., Chrome DevTools)
2. Access to the public website https://www.rockstargames.com
3. Basic knowledge of HTTP requests and form inspection

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to restrict script sources
- Log and monitor anomalous form submissions
- Use WAF rules to detect common XSS payloads in inputs

## Objectives

1. Discover the exact submission endpoint and parameters
2. Verify form accessibility without authentication
3. Prepare for payload injection targeting vulnerable fields

## Instructions

### Step 1: Inspect the Feedback Form

**Context**: Navigate to the Mouthoff page and interact with the form to capture the submission request.

Open https://www.rockstargames.com/mouthoff in a browser, fill out the form with benign data, and submit while monitoring the Network tab in DevTools. Look for the POST request to /mouthoff/mouthoff/submit.json.

**Expected Output**: Request details showing endpoint URL, method (POST), headers (e.g., Content-Type: application/x-www-form-urlencoded), and parameters (name, subject, body, etc.).

### Step 2: Document Vulnerable Parameters

**Context**: Identify fields that accept user input for potential XSS injection.

From the captured request, note parameters like name, subject, and body as primary injection points due to their rendering in the admin panel.

**Expected Output**: List of parameters and sample request body.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- recon
- web-endpoint
