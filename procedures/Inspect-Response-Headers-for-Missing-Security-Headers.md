---
tags:
  - reconnaissance
  - headers
  - web-security
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:28:12.808Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 189ed1ed-9412-4941-be5c-0d39c6086fd9
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Inspect-Response-Headers-for-Missing-Security-Headers

## Summary

This procedure involves examining HTTP response headers of a target web page to identify missing security headers like X-Frame-Options, which can indicate vulnerabilities such as clickjacking.

## Description

In the context of web security testing, inspecting response headers helps discover misconfigurations that allow attacks like clickjacking. For Yelp's /reservations page, the absence of X-Frame-Options permits embedding the page in external iframes, enabling attackers to overlay invisible forms for unauthorized interactions. This step is reconnaissance-focused and requires only browser tools, with outcomes confirming exploitability.

## Requirements

1. Access to a web browser with developer tools (e.g., Chrome, Firefox)
2. Public URL of the target page (e.g., https://www.yelp.com/reservations)
3. Basic knowledge of HTTP headers

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN in all responses
- Use Content-Security-Policy (CSP) frame-ancestors directive to restrict framing
- Monitor server logs for unusual header requests or iframe attempts

## Objectives

1. Identify missing anti-framing headers to assess clickjacking risk
2. Gather evidence for proof-of-concept exploitation
3. Determine if the page can be embedded without restrictions

## Instructions

### Step 1: Load the Target Page

**Context**: Navigate to the vulnerable page to trigger the HTTP request.

Open your browser and visit https://www.yelp.com/reservations. Ensure you're on the page that handles reservation forms.

**Expected Output**: The page loads normally, displaying reservation interface.

### Step 2: Open Developer Tools and Inspect Headers

**Context**: Use built-in tools to view network traffic and response details.

Right-click on the page and select "Inspect" or press F12. Go to the Network tab, reload the page, and select the request for /reservations. In the Headers sub-tab, scroll through Response Headers.

**Expected Output**: List of headers; absence of X-Frame-Options confirms vulnerability.

### Step 3: Verify Exploitability

**Context**: Test if the page can be framed to validate the finding.

Create a simple HTML file with an iframe src="https://www.yelp.com/reservations" and open it locally. If it loads without errors, the vulnerability is confirmed.

**Expected Output**: Iframe loads the Yelp page successfully.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[web-security]]
- [[headers]]
