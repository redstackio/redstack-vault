---
tags:
  - csrf
  - recon
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
updated_at: '2025-12-14T17:27:22.496Z'
sub_techniques: []
id: e5054b32-a056-4157-a1ba-3e1af8dc1901
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Comment Submission Endpoint

## Summary

This procedure involves inspecting a target blog's comment functionality to identify the submission endpoint and capture necessary form parameters, setting the stage for CSRF exploitation.

## Description

In a web application like blogs.starbucks.com, comment submission typically uses POST requests with form data. By using browser tools, attackers can uncover the exact endpoint URL and fields such as __VIEWSTATE (common in ASP.NET), tbComment, and submit coordinates. This reconnaissance is crucial for crafting accurate CSRF payloads. The target environment is a public-facing web app; prerequisites include access to the site and basic web inspection skills. Expected outcome: Full details for mimicking the request in a PoC.

## Requirements

1. Web browser with developer tools (e.g., Chrome)
2. Access to the target blog article
3. Basic knowledge of HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing forms
- Monitor for anomalous comment submissions from legitimate users
- Use web application firewalls to detect cross-origin POSTs

## Objectives

1. Locate the POST endpoint for comments
2. Capture form field values for replication
3. Validate request structure for exploitation

## Instructions

### Step 1: Navigate and Inspect Form

**Context**: Load the target blog page and prepare to capture the submission request.

Open the blog article in a browser, e.g., https://blogs.starbucks.com/blogs/customer/archive/2016/05/06/starbucks-doubleshot-174-energy-coffee-makes-a-flavorful-foray-into-the-realm-of-spiced-coffee.aspx. Open developer tools (F12), go to the Network tab, and attempt to submit a test comment.

**Expected Output**: Captured POST request in Network tab showing endpoint and form data.

### Step 2: Analyze Request Details

**Context**: Extract key parameters from the captured request.

Review the POST request: Note the URL, Content-Type: application/x-www-form-urlencoded, and body with fields like __VIEWSTATE=[value], tbComment=[text], and submit button coordinates.

**Expected Output**: List of required form fields and their sample values.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[recon]]
