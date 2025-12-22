---
tags:
  - idor
  - web
  - recon
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-capture-group-delete]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 679fa00a-5920-4dfd-bcf6-f82e7c29d09c
created_at: '2025-12-14T17:25:23.195Z'
updated_at: '2025-12-14T17:25:23.195Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Veris-Group-Deletion-Functionality

## Summary

This procedure involves logging into the Veris application and navigating to the groups section to initiate a legitimate group deletion, capturing the HTTP request structure for later modification in an IDOR exploit.

## Description

In the context of exploiting an IDOR vulnerability in Veris, this initial step establishes a baseline by accessing the group management interface and triggering a delete action on a group within the attacker's own organization. This allows interception of the request, revealing the group_id parameter that lacks proper authorization checks. Prerequisites include a valid user account with group permissions. Expected outcomes include a captured DELETE request ready for tampering, setting the stage for unauthorized deletions across organizations.

## Requirements

1. Authenticated access to Veris application with group management permissions
2. Proxy tool like Burp Suite for request interception
3. Knowledge of the target's group IDs (own organization)

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) to validate user permissions on group operations
- Log all group deletion attempts with user and organization context for anomaly detection
- Use web application firewalls (WAF) to monitor parameter tampering in DELETE requests

## Objectives

1. Capture the legitimate group deletion request structure
2. Identify the manipulable group_id parameter
3. Prepare for request modification without alerting defenses

## Instructions

### Step 1: Login and Navigate to Groups

**Context**: Authenticate and access the group management section to locate a deletable group.

**Command** ([[commands/curl-capture-group-delete]]):
```bash
# First, ensure login (manual via browser or API), then navigate to /groups in Veris UI
curl -X GET 'https://veris.example.com/api/groups' -H 'Authorization: Bearer {token}'
```

> This lists groups; select one from your organization and initiate deletion via UI to trigger the interceptable request.

### Step 2: Initiate and Intercept Deletion

**Context**: Trigger the delete action and capture the outgoing HTTP request.

**Command** ([[commands/curl-capture-group-delete]]):
```bash
curl -X DELETE 'https://veris.example.com/api/groups/{own-group-id}' -H 'Authorization: Bearer {token}' -H 'Content-Type: application/json'
```

> Intercept this in Burp Suite; expected output is the raw request with group_id visible for analysis.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-capture-group-delete]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[idor]]
- [[web]]
- [[recon]]
