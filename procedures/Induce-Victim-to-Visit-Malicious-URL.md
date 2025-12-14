---
id: proc-shopify-xss-induce-visit-001
tags:
  - user-interaction
  - xss-trigger
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
  - '[[User Execution]]'
updated_at: '2025-12-13T23:56:03.519Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[User Execution]]'
---
# Induce Victim to Visit Malicious URL

## Summary

This procedure focuses on getting the victim to access the malicious URL in an authenticated Shopify admin session, reflecting the XSS payload.

## Description

The victim must be logged in to trigger the admin context. Social engineering or timing ensures visitation. The page loads with the parameter reflected in an anchor, priming for the next step. Outcomes: Partial page load without immediate execution.

## Requirements

1. Victim has received and trusts the URL
2. Victim is authenticated in Shopify admin
3. No ad blockers interfering with load

## Defense

Defensive measures and detection strategies:

- Educate on verifying links before clicking in admin sessions
- Use browser extensions to warn on suspicious URLs
- Monitor admin session logs for unexpected page visits

## Objectives

1. Achieve authenticated access to the URL
2. Reflect the payload in the DOM
3. Avoid premature detection

## Instructions

### Step 1: Confirm Victim Readiness

**Context**: Ensure the victim is in the right context.

Follow up if needed: "Did you check the report yet?" to prompt action.

### Step 2: Victim Navigates to URL

**Context**: The victim clicks and loads the page.

The browser requests `https://[SHOP].myshopify.com/admin/marketing/reports/[ID]?return_page_pathname=javascript:...`, reflecting in the back link.

**Expected Output**: Page partially loads; anchor href shows injected payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[User Execution]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[user-interaction]]
