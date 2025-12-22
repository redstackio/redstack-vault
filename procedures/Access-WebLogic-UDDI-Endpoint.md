---
tags:
  - ssrf
  - weblogic
  - uddi
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-http-request]]'
verified: false
platforms:
  - Web
  - Oracle WebLogic
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:02.487Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: c5bcab03-679f-4080-89e4-d3f80c671da8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-WebLogic-UDDI-Endpoint

## Summary

This procedure accesses the publicly exposed UDDI SearchPublicRegistries.jsp page on Oracle WebLogic Server to confirm the presence of the vulnerable endpoint without requiring authentication.

## Description

The UDDI application in Oracle WebLogic Server exposes the /uddiexplorer/SearchPublicRegistries.jsp endpoint publicly, allowing unauthenticated users to interact with search functionalities. This step verifies accessibility, setting the stage for SSRF exploitation by confirming the endpoint processes user-supplied parameters like 'operator' without validation.

## Requirements

1. Network access to the target WebLogic server over HTTP/HTTPS
2. No credentials needed
3. Basic web request tool like curl or browser

## Defense

Defensive measures and detection strategies:

- Restrict UDDI endpoint access via firewall or authentication
- Monitor access logs for anomalous requests to /uddiexplorer/
- Disable unnecessary UDDI components in WebLogic

## Objectives

1. Confirm endpoint exposure
2. Verify unauthenticated access
3. Prepare for parameter manipulation

## Instructions

### Step 1: Send Initial Request to Endpoint

**Context**: Fetch the UDDI search page to ensure it's reachable and renders the form.

**Command** ([[commands/curl-http-request]]):
```bash
curl "http://target-server/uddiexplorer/SearchPublicRegistries.jsp"
```

> This command retrieves the HTML of the search page. Successful output includes form elements for parameters like 'operator', 'rdoSearch', and 'txtSearchname'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-http-request]]

## Tools Used


## Tags

- ssrf
- weblogic
- uddi
