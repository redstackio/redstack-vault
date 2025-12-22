---
tags:
  - xxe
  - interception
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 6d19eb53-abe3-407b-9092-3ca50366d777
created_at: '2025-12-13T09:00:28.045Z'
updated_at: '2025-12-13T09:00:28.045Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture and Intercept API Request

## Summary

This procedure involves accessing the target website, initiating a search, and using Burp Suite to intercept the API request for further analysis and modification in vulnerability testing.

## Description

In web vulnerability assessments, intercepting requests is crucial for identifying endpoints like /api/search/GeneralSearch that may process user input insecurely. This step sets the foundation for testing XML-based vulnerabilities such as XXE by capturing legitimate traffic.

## Requirements

1. Access to the target website (ubermovement.com)
2. Burp Suite installed and configured as a proxy
3. Network connectivity to perform searches

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on API endpoints
- Monitor for unusual request patterns in proxy logs

## Objectives

1. Capture the initial search request
2. Prepare for request modification
3. Identify vulnerable endpoints

## Instructions

### Step 1: Access Website and Perform Search

**Context**: Trigger the API request by performing a search on the site.

Go to http://ubermovement.com/ and initiate a search.

> This generates a GET request to /api/search/GeneralSearch.

### Step 2: Intercept Request with Burp Suite

**Context**: Use Burp Suite to capture the request for analysis.

Enable interception in Burp Suite and capture the GET /api/search/GeneralSearch request.

> Expected: Request details appear in the Interceptor tab.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite]]

## Tags

- xxe
- interception
