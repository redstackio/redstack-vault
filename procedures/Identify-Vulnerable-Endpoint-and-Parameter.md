---
tags:
  - sqli
  - recon
  - aspnet
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/post-sqli-boolean-payload-initial]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:26.112Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 0f4eedb8-ce84-4e5c-b44b-d84e841beb94
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Vulnerable-Endpoint-and-Parameter

## Summary

This procedure involves reconnaissance to pinpoint the vulnerable endpoint in an ASP.NET application, specifically the resource manager in /DocCenter.aspx, and identify the sDirID parameter as the SQL injection entry point.

## Description

In ASP.NET applications using components like Ext.NET, the resource manager handles directory operations via POST requests. The sDirID parameter, passed in submitDirectEventConfig.extraParams, is directly concatenated into SQL queries without sanitization, allowing injection. This step requires intercepting legitimate requests to understand the structure, including ASP.NET-specific fields like VIEWSTATE and EVENTVALIDATION, before proceeding to payload testing.

## Requirements

1. Access to the web application (e.g., via browser or proxy)
2. Ability to capture and replay HTTP requests
3. Basic knowledge of ASP.NET form handling

## Defense

Defensive measures and detection strategies:

- Implement Web Application Firewall (WAF) rules to detect anomalous POST payloads
- Use parameterized queries or ORMs to prevent direct SQL concatenation
- Log and monitor sDirID parameter values for injection patterns like 'OR' or mathematical expressions

## Objectives

1. Confirm the endpoint and parameter location
2. Gather necessary tokens for request forging
3. Establish baseline response for comparison

## Instructions

### Step 1: Intercept Legitimate Request

**Context**: Navigate to the resource manager section and trigger a directory listing to capture the base request.

**Command** ([[commands/post-sqli-boolean-payload-initial]]):
```bash
curl -X POST https://target/DocCenter.aspx \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "X-Requested-With: XMLHttpRequest" \
  -d "EVENTTARGET=ResourceManager1&EVENTARGUMENT=-|public|GetDirs&VIEWSTATE=...&EVENTVALIDATION=...&submitDirectEventConfig={\"config\":{\"extraParams\":{\"sDirID\":\"51\"}}}" \
  -b "ASP.NET_SessionId=..."
```

> This sends a legitimate request with sDirID='51'. Expected output: JSON or HTML with directory list (e.g., ID 51 contents). Note the structure for modification.

### Step 2: Analyze Parameter Placement

**Context**: Examine the request body to locate sDirID within submitDirectEventConfig JSON.

**Instructions**: Use a proxy like Burp to decode and confirm sDirID is in extraParams. Verify Content-Length and encoding match.

**Expected Output**: Identification of sDirID as the injectable field.

**Success Indicators**:
- Request succeeds with expected directory data
- Parameter confirmed in JSON payload

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/post-sqli-boolean-payload-initial]]

## Tools Used


## Tags

- [[sqli]]
- [[recon]]
