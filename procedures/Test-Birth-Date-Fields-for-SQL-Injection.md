---
tags:
  - sqli-test
  - network-manipulation
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:04.924Z'
sub_techniques: []
id: 111223a6-70b0-4626-a698-5ab81798636d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Birth-Date-Fields-for-SQL-Injection

## Summary

This procedure uses the browser's network tab to intercept, modify, and resend requests, injecting payloads into birth date parameters to confirm SQL injection and observe server behavior.

## Description

After initial submission, capture the POST request and alter birth day, month, or year (e.g., to ''' for error or '''' for success). HTTP 500 indicates syntax errors from unsanitized inputs, while 200 suggests valid processing, enabling further exploitation like database errors or manipulation.

## Requirements

1. Initial form submission performed
2. Browser dev tools network tab open

## Defense

Defensive measures and detection strategies:

- Parameterized queries for all date inputs
- Error handling to avoid revealing backend details

## Objectives

1. Confirm SQLi in birth date fields
2. Induce server errors for info disclosure
3. Escalate to broader database control

## Instructions

### Step 1: Capture Request in Network Tab

**Context**: Monitor and intercept the form submission request.

Browser dev tools:

```plaintext
Open Network tab > Submit form > Locate POST request
```

> Right-click the request and select 'Edit and Resend'.

### Step 2: Modify and Resend with Payload

**Context**: Inject payloads into birth date parameters.

Edit request body:

```plaintext
Birth day: ''' (expect HTTP 500)
Birth month/year: '''' (expect HTTP 200)
```

> Resend; analyze responses for vulnerability confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[sqli-test]]
- [[network-manipulation]]
