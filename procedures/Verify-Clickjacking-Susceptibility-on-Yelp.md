---
tags:
  - clickjacking
  - testing
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: fe59f5b9-cade-4fa3-b9ec-1e1a36cf7324
created_at: '2025-12-14T17:28:05.222Z'
updated_at: '2025-12-14T17:28:05.222Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Verify-Clickjacking-Susceptibility-on-Yelp

## Summary

This procedure tests whether identified Yelp endpoints can be loaded into iframes from external sites, confirming the absence of frame protections and enabling clickjacking exploitation.

## Description

Clickjacking relies on embedding victim pages in iframes without detection. For Yelp, this involves creating a simple HTML test file to iframe endpoints like /flag_content and observing if they render. The target environment is any web-accessible Yelp page; prerequisites include the endpoint list from prior recon. Successful verification shows the page loads, allowing overlay tricks for user deception.

## Requirements

1. Local web server or file:// access for HTML testing
2. Web browser supporting iframes
3. Identified Yelp endpoint URLs

## Defense

Defensive measures and detection strategies:

- Enforce strict CSP frame-ancestors policies
- Log iframe embedding attempts via WAF rules
- Browser extensions or client-side checks for unusual framing

## Objectives

1. Confirm iframe embedding is possible
2. Identify any partial protections
3. Validate setup for POC creation

## Instructions

### Step 1: Create Test HTML

**Context**: Build a basic HTML file to embed the Yelp endpoint.

Create test_iframe.html with: <iframe src="https://www.yelp.com/flag_content?..." width="800" height="600" style="opacity:0.5;"></iframe> using a real vulnerable URL.

### Step 2: Load and Observe

**Context**: Open the HTML in a browser to check rendering.

Load the file; if the Yelp page appears in the iframe without errors (e.g., no "Refused to display" console message), susceptibility is confirmed.

### Step 3: Test Multiple Endpoints

**Context**: Repeat for other endpoints like /following_user/add and /thanx.

Embed each URL similarly and verify all load without frame denials.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[vulnerability-testing]]
