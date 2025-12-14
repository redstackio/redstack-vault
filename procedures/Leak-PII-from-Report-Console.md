---
id: proc-bmc-pii-leak-2024
tags:
  - data-exfiltration
  - pii-leakage
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:28:58.711Z'
skill_level: intermediate
impact_level: critical
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Leak PII from Report Console

## Summary

This final procedure uses admin access to query and extract PII from the AR System Report Console, compromising DoD user data including IDs, emails, and names from the ticket database.

## Description

Within the bypassed admin session, the Report Console allows running queries on the ITSM database without restrictions, leaking sensitive info. This enables mass compromise; requires admin privileges from prior steps, with outcomes including downloadable or viewable PII for further exploitation.

## Requirements

1. Full admin session established.
2. Access to Applications menu.
3. Basic knowledge of report querying in BMC Remedy.

## Defense

Defensive measures and detection strategies:

- Encrypt PII at rest and enforce query logging with DLP (Data Loss Prevention) scans.
- Alert on bulk data exports or unusual report runs from admin accounts (e.g., via database audit trails).

## Objectives

1. Extract ticket database contents.
2. Capture PII for compromise.
3. Demonstrate impact of auth bypass.

## Instructions

### Step 1: Navigate to Report Console

**Context**: Access the console from admin quick links.

**Action** (UI Navigation):

Go to Applications > Quick Links > AR System Report Console.

> Console interface loads with report options.

### Step 2: Run PII Query

**Context**: Execute a report to dump ticket data.

**Action** (Report Execution):

Select a ticket database report and click 'Run' in the bottom left.

> Expected: Results table shows PII like DoD IDs, emails, names.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- data-exfiltration
- pii-leakage
