---
tags:
  - intercept
  - proxy
  - burp
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:08.183Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: f6c0dbb8-afaa-4113-bc36-bdaf89104a9c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Report-Export-with-Burp-Suite

## Summary

This procedure configures Burp Suite to intercept HTTP traffic from the DoD LMS, capturing the report export POST request for subsequent modification to exploit the RCE vulnerability.

## Description

Burp Suite acts as a proxy to inspect and alter requests. In the context of the LMS, this captures the POST to /RServer/rdPage.aspx triggered by the 'Export to Excel' action, allowing manipulation of parameters like rdExportFilename and rdReportName.

## Requirements

1. Burp Suite installed and running
2. Browser configured to use Burp as proxy (e.g., 127.0.0.1:8080)
3. Authenticated LMS session from prior procedure

## Defense

Defensive measures and detection strategies:

- Deploy client-side certificate pinning to block proxy interception
- Log and alert on unusual proxy-like traffic patterns
- Use HTTPS with HSTS to complicate interception

## Objectives

1. Successfully proxy LMS traffic through Burp Suite
2. Capture the exact export POST request
3. Pause the request for editing without forwarding prematurely

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up Burp Suite to intercept browser traffic.

Launch Burp Suite and ensure the Proxy tab is active. Configure your browser (e.g., Firefox) to use HTTP proxy 127.0.0.1 on port 8080. Install Burp's CA certificate if using HTTPS.

> Traffic now routes through Burp; verify by browsing a test site.

### Step 2: Trigger and Intercept Export

**Context**: Initiate the export in LMS to capture the request.

With proxy active, click 'Export to Excel' in the LMS reports page. In Burp Proxy > HTTP history or Intercept tab, catch the POST request to /RServer/rdPage.aspx.

> Request body includes parameters like rdExportFilename=report.xls&rdReportName=Sample Report.

### Step 3: Send to Repeater for Modification

**Context**: Prepare the request for parameter tampering.

Right-click the intercepted request in Burp and select 'Send to Repeater'. Drop the intercept to forward if needed, but use Repeater for safe editing.

> Repeater window opens with the full request editable.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- intercept
- proxy
- burp
