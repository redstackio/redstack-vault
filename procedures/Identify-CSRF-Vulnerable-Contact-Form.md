---
tags:
  - csrf
  - recon
  - web
type: procedure
tools:
  - '[[tools/Acunetix]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:22.902Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 74874e53-f064-42ff-acaa-9b6ed10fb067
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Identify CSRF Vulnerable Contact Form

## Summary

This procedure uses automated scanning to identify web forms, such as contact forms, that may be susceptible to CSRF attacks by enumerating endpoints and form structures without protection tokens.

## Description

In the context of the Automattic contact form at http://automattic.com/contact/, this step involves accessing the GET endpoint to retrieve the HTML form and analyzing its POST action and input fields (your_name, your_email, blog_url, subject, message, submit). The goal is to map the attack surface for potential forgery. Prerequisites include public access to the site and a web vulnerability scanner.

## Requirements

1. Network access to the target web application
2. Installed vulnerability scanner like Acunetix
3. Basic understanding of HTML forms and HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing forms
- Use Content-Security-Policy headers to restrict form submissions
- Monitor for anomalous POST requests to contact endpoints

## Objectives

1. Locate the contact form endpoint and document its fields
2. Confirm the form handles anonymous submissions
3. Prepare for further vulnerability verification

## Instructions

### Step 1: Scan Target Site

**Context**: Launch a scan to discover forms on the target.

Use [[tools/Acunetix]] to target http://automattic.com:

No specific command, as Acunetix is GUI-based; configure scan for http://automattic.com/contact/ and enable form analysis.

> The scanner crawls the site, identifies the GET /contact/ endpoint, and reports the form details including POST URL and inputs.

### Step 2: Analyze Form Structure

**Context**: Review the retrieved HTML to enumerate fields.

Manually inspect or export from Acunetix the form HTML.

> Expected: Form action="http://automattic.com/contact/" method="post" with fields for name, email, etc.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Acunetix]]

## Tags

- [[csrf]]
- [[recon]]
