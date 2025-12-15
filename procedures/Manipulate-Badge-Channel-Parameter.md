---
id: proc-vimeo-manipulate-parameter
tags:
  - idor
  - parameter-tampering
  - web
type: procedure
tools:
  - '[[tools/Burp-Proxy]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:51.796Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Manipulate-Badge-Channel-Parameter

## Summary

This procedure involves editing the 'badge_channel' parameter in intercepted requests to a private channel ID, testing for IDOR by bypassing access validation tied to the user's membership.

## Description

In Burp Proxy, target the second request to https://vimeo.com/tools/widget/montage, which includes parameters like user_id=36807051 and badge_channel. Change badge_channel to a private ID (e.g., 870575) and forward. The lack of server-side checks allows the request to succeed. Requires prior interception. Outcome: Successful manipulation without errors.

## Requirements

1. Intercepted request from montage widget
2. Burp Proxy Repeater or Intruder tool
3. Valid private channel ID

## Defense

Defensive measures and detection strategies:

- Validate user membership against channel ID on every request
- Log and alert on parameter mismatches between user_id and badge_channel

## Objectives

1. Tamper with badge_channel to private ID
2. Confirm IDOR by successful response
3. Enable unauthorized content access

## Instructions

### Step 1: Edit and Forward Request

**Context**: Modify the parameter in the proxy tool.

In Burp, drop the request, change badge_channel=870575, and forward.

> Server processes without access denial, returning widget data.

**Expected Output**: 200 OK response with montage parameters intact.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Proxy]]

## Tags

- [[idor]]
- [[parameter-tampering]]
