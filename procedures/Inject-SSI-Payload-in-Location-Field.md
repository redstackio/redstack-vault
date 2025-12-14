---
id: proc-inject-ssi-location
tags:
  - ssi
  - injection
  - dos
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:30.691Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
---
# Inject-SSI-Payload-in-Location-Field

## Summary

This procedure involves modifying the 'location' parameter in a intercepted profile update request to include an SSI directive, aiming to exploit server-side processing flaws and cause a 500 error or DoS.

## Description

Server-Side Includes (SSI) directives, if unsanitized, can be processed by the server, potentially leading to errors or execution. Here, the payload <!--#config timefmt="A %B %d %Y %r"--> is injected into the form data. The target endpoint is POST /internal_api/v0.2/savePublicInformation on Semmle. Expected outcome is a 500 error due to improper handling (possibly from '%' decoding). Prerequisites: intercepted request and understanding of form encoding.

## Requirements

1. Intercepted POST request in Burp Suite
2. Knowledge of SSI syntax and URL encoding
3. Valid session to avoid auth errors

## Defense

Defensive measures and detection strategies:

- Sanitize and encode all user inputs, stripping SSI directives
- Disable SSI processing on the web server (e.g., via Apache/IIS config)
- Monitor server logs for 500 errors correlated with form submissions containing special characters

## Objectives

1. Insert SSI payload to test for directive processing
2. Trigger server error to assess impact on availability
3. Validate if error leads to DoS on settings page

## Instructions

### Step 1: Inspect Intercepted Request

**Context**: Review the request body to locate the 'location' parameter.

No command; Burp GUI:

- In Burp Proxy or Repeater, view the POST body.

> Body shows form data like location=original_value&other=params.

### Step 2: Modify the Location Parameter

**Context**: Replace the value with the SSI payload.

No command; edit in Burp:

- Change to location=<!--#config timefmt="A %B %d %Y %r"-->
- Ensure encoding is application/x-www-form-urlencoded.

> Payload inserted; note '%' characters may cause decoding issues.

### Step 3: Forward and Observe Response

**Context**: Send the modified request and check for errors.

No command; Burp action:

- Click 'Forward' in Intercept or 'Send' in Repeater.

> Server returns 500 error. Test settings page reload for DoS.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- ssi
- injection
