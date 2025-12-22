---
id: proc-uuid-1137218
name: Bypass-Invoice-Download-Permissions-via-Open-Page-Manipulation
type: procedure
verified: false
submitted: true
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.954Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - access-control-bypass
  - authorization-bypass
  - web-vulnerability
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Bypass-Invoice-Download-Permissions-via-Open-Page-Manipulation

## Summary

This procedure exploits an improper access control vulnerability in the Moneybird invoice documents downloading feature, where the download action does not perform additional permission checks beyond the initial page load, allowing unauthorized downloads after permissions are modified mid-session.

## Description

In the Moneybird web application, the invoice documents downloading feature relies on frontend-loaded permissions without re-validating them on the backend during the export download. An attacker with initial access can open the relevant page, trigger a permission change (e.g., via admin downgrade or multi-session manipulation), and then proceed with the download from the unchanged page state. This bypasses authorization, leading to unauthorized access to sensitive invoice data. The vulnerability was resolved by implementing extra permission checks in the download endpoint. This technique is applicable in web environments with session-based permissions and weak backend validation.

## Requirements

1. Valid authenticated session to Moneybird with initial permissions to access the invoice page
2. Ability to modify user permissions (e.g., admin access or secondary account for testing)
3. Web browser to maintain an open session without refresh
4. Network access to the Moneybird application

## Defense

Defensive measures and detection strategies:

- Implement runtime permission re-verification on all sensitive actions like downloads
- Use short-lived session tokens that invalidate on permission changes
- Log and monitor permission modifications and subsequent actions for anomalies
- Enforce page refreshes or token renewals before critical operations

## Objectives

1. Gain unauthorized access to invoice export documents
2. Demonstrate the impact of missing authorization checks in web APIs
3. Exfiltrate sensitive financial data without triggering access denials

## Instructions

### Step 1: Establish Initial Authenticated Session

**Context**: Log in as a user with permissions to view and initiate downloads from the invoice page, loading the necessary frontend state.

Open a web browser and navigate to the Moneybird login page. Enter credentials for a user account that has access to the invoice documents feature.

**Expected Output**: Successful login and redirection to the dashboard.

### Step 2: Load the Vulnerable Page

**Context**: Navigate to the invoice documents downloading feature to cache the initial permission state in the browser session.

From the dashboard, go to the invoices section and open the page for downloading or exporting documents. Ensure the page fully loads without interacting further.

**Expected Output**: The download/export interface appears, ready for action.

### Step 3: Manipulate Permissions Mid-Session

**Context**: Change the user's permissions to revoke download access while keeping the original page open to exploit the lack of re-checks.

Using a separate browser tab, session, or administrative interface, modify the target user's permissions to deny access to invoice exports (e.g., downgrade role or revoke specific rights). Do not refresh or reload the original invoice page.

**Expected Output**: Permission change confirmed in the admin panel, but no immediate effect on the open page.

### Step 4: Initiate Unauthorized Download

**Context**: Trigger the download action from the still-open page, bypassing backend checks due to reliance on stale session state.

On the original open page, select the export option and initiate the download of invoice documents.

**Expected Output**: The download proceeds successfully, providing the export file with sensitive data.

### Step 5: Verify Bypass Success

**Context**: Confirm that the download succeeded despite the permission revocation.

Open the downloaded file and check for access to invoices that should be restricted. Attempt a legitimate refresh and re-download to verify denial.

**Expected Output**: File contains unauthorized documents; subsequent attempts after refresh fail with permission errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- access-control-bypass
- authorization-bypass
- web-vulnerability
