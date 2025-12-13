---
tags:
  - data-leak
  - ticket-access
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Data from Cloud Storage]]'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: 3f10c599-948c-4e32-abbe-2295e6c7820e
created_at: '2025-12-13T09:01:26.361Z'
updated_at: '2025-12-13T09:01:26.361Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Cloud Storage]]'
---
# Access Internal Zendesk Tickets

## Summary

This procedure navigates the Zendesk interface post-login to view and leak internal organization ticket information.

## Description

Once logged in via the bypassed SSO, the attacker can access the organization's ticket requests, potentially exposing sensitive internal data.

## Requirements

1. Active Zendesk session from SSO bypass
2. Access to support.trint.com

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls in Zendesk
- Audit access logs for unauthorized views

## Objectives

1. Exfiltrate ticket data
2. Leak internal information
3. Achieve impact of the exploit

## Instructions

### Step 1: Navigate to Tickets

**Context**: Go to the organization requests page.

Browse to https://support.trint.com/hc/en-us/requests/organization.

> This lists all tickets.

### Step 2: Read Ticket Details

**Context**: Open and review individual tickets.

Click on tickets to view contents.

> Extract sensitive information as needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Cloud Storage]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[data-leak]]
- [[ticket-access]]
