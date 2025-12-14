---
id: p-navigate-glassdoor-job-page
tags:
  - web
  - reconnaissance
type: procedure
tools:
  - '[[tools/Chrome-Browser]]'
  - '[[tools/Firefox-Browser]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:47:12.981Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Navigate to Glassdoor Job Search Page

## Summary

This procedure involves accessing the vulnerable job search page on Glassdoor.co.in to set up the environment for XSS testing and exploitation.

## Description

In the context of exploiting reflected XSS, the attacker first navigates to a standard job search URL where the path segment reflects user input. This establishes the base for injecting payloads. The target environment is any modern web browser accessing the public-facing Glassdoor site. Expected outcomes include loading the page with reflected search terms, confirming the reflection point exists.

## Requirements

1. Internet access to https://www.glassdoor.co.in
2. A web browser like Chrome or Firefox
3. No authentication required

## Defense

Defensive measures and detection strategies:

- Implement URL parameter validation on the server side
- Monitor for unusual URL lengths or encoded characters in access logs

## Objectives

1. Establish access to the vulnerable endpoint
2. Verify page functionality
3. Prepare for payload injection

## Instructions

### Step 1: Open Browser and Navigate

**Context**: Launch the browser and directly access the job search URL to observe the initial reflection.

No specific command required; use the browser's address bar:

```url
https://www.glassdoor.co.in/Job/pratt-whitney-jobs-SRCH_KE0,13.htm?initiatedFromCountryPicker=true&countryRedirect=true
```

> This loads the page with the search term 'pratt-whitney-jobs' reflected in the HTML. Expected output: Job listings page displays normally.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-Browser]]
- [[tools/Firefox-Browser]]

## Tags

- [[web]]
- [[Reconnaissance]]
