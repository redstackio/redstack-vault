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
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:35.419Z'
sub_techniques: []
id: 68dd1a52-1c2b-4018-9a12-c10647cf88f2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Testimonials-Feature-in-Concrete-CMS

## Summary

This procedure outlines how to navigate to the testimonials feature in Concrete CMS to locate the vulnerable Company URL input field, setting the stage for XSS payload injection.

## Description

In Concrete CMS, the testimonials feature allows users to add company endorsements with details like URL. The Company URL field lacks proper input validation, making it susceptible to stored XSS. This procedure assumes authenticated access and focuses on identifying the target input for exploitation. Expected outcomes include access to the form, enabling subsequent injection steps.

## Requirements

1. Authenticated session in Concrete CMS (admin or editor privileges)
2. Web browser with developer tools for inspection
3. Network access to the CMS instance

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls to limit testimonial editing
- Enable web application firewall (WAF) rules to monitor form submissions for suspicious patterns
- Regularly audit CMS plugins and core code for input validation gaps

## Objectives

1. Gain access to the testimonials management interface
2. Identify the unsanitized Company URL field
3. Prepare for payload injection without triggering errors

## Instructions

### Step 1: Log In to Dashboard

**Context**: Authenticate to reach the administrative interface where features like testimonials are managed.

No specific command; use the login form at `/login` or equivalent endpoint.

> Enter credentials and submit to access the dashboard.

### Step 2: Navigate to Testimonials

**Context**: Locate the testimonials section to access the input form.

No specific command; click on 'Testimonials' or 'Add Testimonial' in the dashboard menu.

> The page loads the form; inspect the Company URL field to confirm it's a simple text input without escaping.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[concrete-cms]]
