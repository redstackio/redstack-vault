---
tags:
  - idor
  - verification
  - data-tampering
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data Manipulation]]'
updated_at: '2025-12-14T17:25:30.101Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 7e5dca4c-aecf-4953-aad8-4ab0649af12a
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Data Manipulation]]'
---
# Verify-Unauthorized-Profile-Modifications

## Summary

This procedure confirms the success of IDOR exploitation by checking that modified profile details have been applied to the victim's account in the MTN MoBad application.

## Description

After tampering with profile data, verification involves re-accessing the dashboard or profile views to observe persisted changes. Using Burp Suite, an attacker can intercept subsequent requests to confirm updates without logging in as the victim, highlighting the vulnerability's impact on data integrity in the web application.

## Requirements

1. Successful completion of prior enumeration and exploitation steps
2. Burp Suite for optional re-interception
3. Access to the application (potentially as victim if credentials available)

## Defense

Defensive measures and detection strategies:

- Implement audit logs for all profile changes, alerting on mismatches between updater and owner
- Use integrity checks or versioning on user data to detect unauthorized modifications
- Conduct regular security audits on API endpoints for IDOR risks

## Objectives

1. Validate persistence of unauthorized changes
2. Assess the full scope of the vulnerability's impact
3. Provide evidence for reporting or further exploitation

## Instructions

### Step 1: Re-access Dashboard or Profile

**Context**: Load data that includes the victim's profile to check for changes.

Navigate back to the dashboard at https://mtnmobad.mtnbusiness.com.ng/#/dashboard/home and intercept the /app/dashboardData request again.

**Technical Details**: Inspect the response JSON for the victim's entry; altered fields (e.g., name, mobile) should now reflect the modifications.

### Step 2: Direct Profile Verification

**Context**: If possible, view the profile directly as the victim or via another method.

Log in as the victim (if credentials obtained) and access /userProfile, or use enumeration to confirm via API.

**Technical Details**: The profile displays the tampered data, confirming no rollback or validation occurred.

**Expected Output**: Updated details visible in the victim's profile or dashboard data.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Data Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[idor]]
- [[verification]]
- [[data-tampering]]
