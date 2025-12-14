---
id: proc-uuid-3
tags:
  - injection
  - proxy
  - http-intercept
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:32.060Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Payload-via-Picker-Endpoint

## Summary

This procedure uses an interception proxy to modify an HTTP request to SharePoint's picker.aspx, injecting the encoded XAML payload into the vulnerable parameter for deserialization-based RCE.

## Description

The picker.aspx endpoint in SharePoint deserializes user-supplied data in the ctl00$PlaceHolderDialogBodySection$ctl05$hiddenSpanDataValue parameter without validation, allowing gadget chains via ObjectDataProvider to execute commands. Burp Suite intercepts the request triggered by interacting with the picker dialog, enabling payload insertion.

## Requirements

1. Encoded payload from previous step
2. Burp Suite configured as proxy (e.g., browser proxy 127.0.0.1:8080)
3. Access to the target SharePoint URL (e.g., https://target/OrgStruct/StandingGroups/_layouts/15/picker.aspx?PickerDialogType=...)

## Defense

Defensive measures and detection strategies:

- Patch SharePoint to mitigate CVE-2019-0604
- Proxy all traffic through a WAF to inspect and block modified parameters with encoded content
- Log and alert on requests to picker.aspx with unusual data lengths

## Objectives

1. Intercept legitimate request to vulnerable endpoint
2. Inject encoded payload for deserialization
3. Trigger RCE on the SharePoint server

## Instructions

### Step 1: Configure Interception Proxy

**Context**: Set up Burp Suite to capture HTTP requests to the target site.

**Command** (Burp Configuration):
No CLI command; in Burp Suite, go to Proxy > Options and ensure intercept is on for the target scope.

> Browser traffic routes through Burp. Expected output: Intercepted requests visible in Proxy > Intercept tab.

### Step 2: Trigger and Modify Request

**Context**: Access the endpoint to generate the interceptable request, then replace the parameter with the payload.

**Command** (Manual Injection):
Browse to https://target/_layouts/15/picker.aspx?PickerDialogType=Microsoft.SharePoint.WebControls.ItemPickerDialog,... and click the hourglass icon; in the intercepted POST request, set 'ctl00$PlaceHolderDialogBodySection$ctl05$hiddenSpanDataValue=' to the encoded string (e.g., __bp4b7135...).

> Forward the request after modification. Expected output: Server response without errors; command executes silently.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- injection
- proxy
- http-intercept
