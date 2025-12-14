---
tags:
  - recon
  - telerik
  - handler-verification
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-verify-telerik-handler]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:23:37.471Z'
sub_techniques: []
id: bfc3d267-e36b-4680-8b40-74c33f5cd9f9
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Verify Telerik Upload Handler Registration

## Summary

This procedure verifies the registration of the RadAsyncUpload handler in Telerik UI, a prerequisite for exploiting CVE-2019-18935 and CVE-2017-11317 by confirming the vulnerable endpoint is accessible.

## Description

In vulnerable Telerik UI installations, the RadAsyncUpload handler at Telerik.Web.UI.WebResource.axd?type=rau allows arbitrary file uploads due to insecure deserialization. This step issues a GET request to check if the handler is registered, indicating potential for exploitation without authentication. It targets ASP.NET web apps on Windows servers and helps filter non-vulnerable targets early.

## Requirements

1. Network access to the target web server over HTTPS
2. [[tools/curl]] installed
3. Target URL with Telerik UI integration

## Defense

Defensive measures and detection strategies:

- Patch Telerik UI to version 2017.3.1027 or later
- Disable or remove unused handlers in web.config
- Monitor access logs for requests to .axd endpoints
- Implement WAF rules to block suspicious .axd traffic

## Objectives

1. Confirm handler availability for upload exploitation
2. Validate target as potentially vulnerable
3. Establish baseline for version identification

## Instructions

### Step 1: Issue GET Request to Handler Endpoint

**Context**: Send a silent, insecure SSL request to probe the endpoint without alerting typical monitoring.

**Command** ([[commands/curl-verify-telerik-handler]]):
```bash
curl -sk https://target.com/app/Telerik.Web.UI.WebResource.axd?type=rau
```

> This command uses -s for silent mode and -k to ignore SSL certificate issues. Expected output is a JSON message confirming registration. If absent, the target may not be vulnerable or the handler is disabled.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- [[Vulnerability Scanning]] Vulnerability Scanning

## Commands Used

- [[commands/curl-verify-telerik-handler]]

## Tools Used

- [[tools/curl]]

## Tags

- [[recon]]
- [[telerik]]
- [[web]]
