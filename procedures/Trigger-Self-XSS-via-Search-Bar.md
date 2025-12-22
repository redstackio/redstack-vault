---
id: proc-trigger-search-xss-001
tags:
  - xss
  - self-xss
  - search-trigger
type: procedure
tools:
  - '[[tools/Web-Browser-Chrome]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:30.969Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-Self-XSS-via-Search-Bar

## Summary

This alternative procedure uses Yelp's search functionality by clearing the 'From' field during a restaurant search, triggering the same /location_suggest/json endpoint to reflect and execute the tampered 'city' payload as self-XSS.

## Description

While performing a search (e.g., for restaurants), removing text from the 'From' location bar invokes the location suggestion API, pulling from the cookie's unsanitized 'city' field. The JSON response mirrors the profile page behavior, rendering the script when processed by the client-side JavaScript. Self-contained impact only.

## Requirements

1. Tampered cookie from prior steps
2. Access to Yelp search interface
3. Authenticated user

## Defense

Defensive measures and detection strategies:

- Sanitize location inputs in all client-server interactions
- Use parameterized queries or escaping in JSON generation
- Client-side CSP enforcement against eval or innerHTML

## Objectives

1. Trigger reflection via search UI
2. Achieve script execution
3. Validate consistency with primary trigger

## Instructions

### Step 1: Initiate Search

**Context**: Start a search to access the location input fields.

In [[tools/Web-Browser-Chrome]], go to yelp.com and search for 'restaurants'.

### Step 2: Clear From Field

**Context**: Interact with the 'From' field to invoke the API with cookie data.

Clear any text in the 'From' location bar, prompting the suggestion request.

**Expected Output**: API response reflects payload similarly to profile trigger, executing <script>debugger</script> in the browser.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser-Chrome]]

## Tags

- xss
- self-xss
- search-trigger
