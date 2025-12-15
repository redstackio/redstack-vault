---
tags:
  - pii-exfiltration
  - data-leak
  - verification
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:33.946Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 50c4e14c-abcc-480e-a3d2-d133e7d8917f
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Verify-PII-Leak-via-Contact-Info

## Summary

This procedure confirms the IDOR exploitation by observing and documenting the unauthorized display of another user's biographical and contact details in the DoD JOINOnline Contact-Info section.

## Description

Following parameter manipulation, this step validates the vulnerability's impact by checking for exposed PII such as names, emails, phones, and demographics. The application's failure to verify user ownership results in full profile visibility. This is critical for assessing the leak's scope across endpoints, with outcomes including screenshots or copied data to prove unauthorized access in a controlled test environment.

## Requirements

1. Successful manipulation from prior procedure, with modified URL loaded.
2. Active session to prevent logout during verification.
3. Tools for capturing evidence (e.g., browser screenshots).

## Defense

Defensive measures and detection strategies:

- Implement data masking or role-based access controls for sensitive fields.
- Audit logs for cross-user access attempts and alert on mismatches.
- Encrypt PII in transit and enforce HTTPS to mitigate interception.

## Objectives

1. Confirm visibility of unauthorized PII.
2. Document the leak for reporting or remediation.
3. Assess potential for broader enumeration of user data.

## Instructions

### Step 1: Load Modified Endpoint

**Context**: Access the tampered URL to trigger data retrieval.

With User-A session, visit /JOINOnline/Board/QuestionCard/1327/1021/1614/false (User-B's ID).

**Expected Output**: Contact-Info page renders with User-B's details.

### Step 2: Review Exposed Data

**Context**: Inspect fields for PII leakage.

Scroll through the section, noting elements like contact details, demographics, and biographical info.

**Expected Output**: Full profile data visible, unrelated to the logged-in user.

### Step 3: Capture and Test Scope

**Context**: Document and probe additional endpoints.

Screenshot the page and test /JOINOnline/Board/QuestionCard/1327/1021/1611/false for consistency.

**Expected Output**: Repeated successful access, confirming systemic issue.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[pii-exfiltration]]
- [[data-leak]]
- [[verification]]
