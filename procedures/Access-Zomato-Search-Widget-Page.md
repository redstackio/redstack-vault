---
id: proc-uuid-456
tags:
  - web
  - recon
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:01.605Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Zomato-Search-Widget-Page

## Summary

This procedure involves navigating to the Zomato restaurant search widget page, which serves as the entry point for exploiting the reflected XSS vulnerability in the res_search_widget API.

## Description

The widget page at https://www.zomato.com/widgets/res_search_widget.php is a public-facing PHP-based endpoint that provides restaurant search functionality. Accessing this page exposes the vulnerable input field where user-supplied data is reflected without proper encoding, setting the stage for XSS injection. No prior access or credentials are needed, making it accessible for drive-by or social engineering attacks.

## Requirements

1. Standard web browser
2. Internet connectivity
3. No special permissions

## Defense

Defensive measures and detection strategies:

- Restrict access to widget embeds if not necessary for public use
- Log all accesses to API endpoints for anomaly detection
- Implement rate limiting on widget requests

## Objectives

1. Gain access to the vulnerable search interface
2. Identify the input field for payload injection
3. Prepare for subsequent exploitation steps

## Instructions

### Step 1: Open Browser and Navigate

**Context**: Use a web browser to directly access the target URL, loading the widget page.

Enter the URL https://www.zomato.com/widgets/res_search_widget.php in the address bar and press Enter.

> The page should load, displaying the restaurant search widget with an input field.

### Step 2: Inspect the Page

**Context**: Verify the presence of the search input to ensure it's exploitable.

Right-click on the search field and select "Inspect Element" to view the HTML structure.

**Expected Output**: Input field with attributes like name="search" or similar, confirming reflection point.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web
- recon
- php
