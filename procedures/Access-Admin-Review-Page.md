---
tags:
  - xss
  - admin-access
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:30:07.333Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: b12e1074-723a-435e-a1bc-b01fbb21c3e5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Access-Admin-Review-Page

## Summary

This procedure navigates to the Zomato admin review page where the stored XSS payload is rendered, simulating admin access to trigger execution.

## Description

The vulnerability manifests when admins view reports at https://www.zomato.com/admin/reviews_new?review_id={ID}, rendering additional_text as unsafe HTML. In testing, this step assumes report triggering or direct access simulation. Prerequisites: Reported review_id. Expected outcome: Page load exposing the injected content.

## Requirements

1. Knowledge of the reported review_id
2. Browser or proxy access to admin endpoints (simulation)

## Defense

Defensive measures and detection strategies:

- Restrict admin panel access to authenticated sessions only
- Log all admin page views for anomaly detection
- Escape HTML in review details rendering

## Objectives

1. Load the admin page with stored report
2. Render the vulnerable additional_text field
3. Prepare for payload execution

## Instructions

### Step 1: Navigate to Admin Endpoint

**Context**: Use a browser to access the page, replacing {ID} with the reported review_id.

**Command**:
```bash
# Direct browser access or curl for source inspection
curl 'https://www.zomato.com/admin/reviews_new?review_id=32288944' > admin_page.html
```

> Fetches the page source. Expected output: HTML containing the additional_text with script tag.

### Step 2: Inspect Rendered Content

**Context**: Verify the field is rendered without escaping.

**Command**:
```bash
grep -i 'additional_text' admin_page.html
```

> Searches for the field. Expected output: Unescaped script in HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- admin-access
