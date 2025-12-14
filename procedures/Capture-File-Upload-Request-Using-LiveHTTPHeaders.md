---
tags:
  - recon
  - http-intercept
  - xss-prep
type: procedure
tools:
  - '[[tools/LiveHTTPHeaders]]'
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
updated_at: '2025-12-14T03:15:41.578Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 29511ed0-af6b-483e-a9ab-77276df6f680
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Capture File Upload Request Using LiveHTTPHeaders

## Summary

This procedure intercepts an HTTP file upload request using the LiveHTTPHeaders browser extension to analyze the request structure, particularly the filename parameter, as a preparatory step for vulnerability testing like XSS injection.

## Description

In the context of testing web applications like Udemy's file upload feature, capturing the request allows identification of user-controlled parameters such as the filename. This is essential for crafting payloads in reflected XSS attacks where the filename is echoed back in error responses. The procedure assumes access to the target site and uses a benign file to avoid unintended actions. Expected outcome: A frozen request that can be inspected and modified.

## Requirements

1. Firefox browser with LiveHTTPHeaders extension installed and enabled
2. Valid user session on the target web application (e.g., logged-in Udemy account)
3. A test file ready for upload (e.g., a PNG image)

## Defense

Defensive measures and detection strategies:

- Monitor for unusual browser extension usage in corporate environments
- Implement request logging on file upload endpoints to detect interception patterns

## Objectives

1. Obtain the exact HTTP request format for file uploads
2. Identify the filename parameter location
3. Prepare for payload injection without alerting defenses

## Instructions

### Step 1: Enable Monitoring and Initiate Upload

**Context**: Activate the tool to capture traffic and perform a standard upload to freeze the request.

**Instructions**: Open Firefox, ensure LiveHTTPHeaders is active, navigate to the file upload page on Udemy, select a file named '2015-08-24_162829.png', and start the upload. The tool will intercept the POST request.

> The request will appear in the LiveHTTPHeaders interface, showing headers, method (POST), and body with multipart/form-data including the filename.

### Step 2: Inspect Request Details

**Context**: Examine the captured request to confirm the filename parameter.

**Instructions**: In the tool's view, expand the request body to locate the 'filename' field within the Content-Disposition header of the form data.

> Expected: Filename value visible and editable, confirming it's user-supplied.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/LiveHTTPHeaders]]

## Tags

- [[recon]]
- [[http-intercept]]
