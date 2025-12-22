---
id: proc-confirm-handler
tags:
  - recon
  - telerik-ui
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
updated_at: '2025-12-14T17:23:36.077Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Confirm-RadAsyncUpload-Handler-Presence

## Summary

This procedure verifies the presence of the RadAsyncUpload handler in Telerik UI by accessing the WebResource.axd endpoint, confirming if the application is potentially vulnerable to file upload exploits.

## Description

In Telerik UI for ASP.NET AJAX, the RadAsyncUpload control uses a handler registered at WebResource.axd?type=rau. Accessing this endpoint directly returns a JSON message if the handler is registered, indicating the potential for CVE-2017-11317 exploitation. This is a non-intrusive reconnaissance step targeting public-facing web applications on Windows servers.

## Requirements

1. Network access to the target web application (HTTPS/HTTP)
2. Web browser or curl tool
3. Target URL with the endpoint (e.g., https://target/apps/XTRAHome/Telerik.Web.UI.WebResource.axd?type=rau)

## Defense

Defensive measures and detection strategies:

- Remove or disable unused Telerik handlers in web.config
- Implement web application firewall (WAF) rules to block direct access to .axd endpoints
- Monitor access logs for unusual requests to WebResource.axd

## Objectives

1. Confirm handler registration for vulnerability scoping
2. Identify potential entry point for file upload attacks
3. Establish baseline for further exploitation steps

## Instructions

### Step 1: Access the Endpoint

**Context**: Browse to the target endpoint to elicit the registration message, confirming the handler's availability without authentication.

**Command** (browser or curl):

Use a web browser to navigate to the URL or execute a simple GET request.

```bash
curl -X GET "https://target/apps/XTRAHome/Telerik.Web.UI.WebResource.axd?type=rau"
```

> This command sends a GET request to the rau handler. Expected output is a JSON response confirming registration, indicating the handler is present and potentially exploitable.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- recon
- telerik-ui
