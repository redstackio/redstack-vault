---
tags:
  - recon
  - web
  - xss
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
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:16:08.324Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 0bf82cee-edad-455a-9774-567e1ff5e105
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Vulnerable ASPX Endpoints

## Summary

This procedure involves reconnaissance to identify ASPX pages under /GL/ on targets like videostore.mtnonline.com that use query parameters vulnerable to injection attacks, such as reflected XSS.

## Description

In ASP.NET applications, pages like MyAccount.aspx often accept parameters (e.g., PId, CID, OprId) that may reflect user input without proper sanitization. This step scans or manually explores the application to pinpoint these endpoints, setting the stage for vulnerability testing. Expected outcomes include a list of testable URLs where parameters are echoed back in the response.

## Requirements

1. Network access to the target web application
2. Web browser or HTTP client for probing
3. Basic knowledge of ASP.NET URL structures

## Defense

Defensive measures and detection strategies:

- Implement web application firewall (WAF) rules to monitor unusual parameter patterns
- Log and alert on access to admin or account pages with anomalous queries

## Objectives

1. Discover endpoints with reflected parameters
2. Confirm parameter names and default values
3. Prepare for injection testing

## Instructions

### Step 1: Enumerate ASPX Pages

**Context**: Browse the target site to find /GL/ directory and ASPX files.

Navigate to https://videostore.mtnonline.com/GL/ and identify pages like MyAccount.aspx. Note parameters in example URLs, such as ?PId=126&CID=5&OprId=11.

**Expected Output**: URL with parameters: https://videostore.mtnonline.com/GL/MyAccount.aspx?PId=126&CID=5&OprId=11.

### Step 2: Verify Parameter Reflection

**Context**: Check if parameters are outputted in the HTML response.

Load the URL in a browser and use Developer Tools (View Source) to search for parameter values like "126" or "5". Confirm they appear unencoded.

**Expected Output**: Parameters visible in HTML, e.g., <input value="126">.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[web]]
- [[xss]]
