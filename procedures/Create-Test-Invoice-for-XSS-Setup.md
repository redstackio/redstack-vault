---
tags:
  - xss
  - setup
  - invoice
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:31.431Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: a151de1a-aac4-4288-ab3d-8e1a62ff97e9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Test-Invoice-for-XSS-Setup

## Summary

This procedure sets up a test invoice in Moneybird containing a searchable string ('test') to enable triggering the reflected XSS in the backend search functionality. It prepares the environment for payload injection without alerting defenses.

## Description

In the context of exploiting the reflected XSS in Moneybird's search, an invoice with specific content is needed to appear in search results. This involves logging in, creating an invoice, adding the 'test' string to details, filling other fields, and sending it to an email for link extraction. The target is the Moneybird web app, requiring authenticated access. Expected outcome is a sent invoice with a public link containing the account ID.

## Requirements

1. Valid Moneybird credentials for login
2. Access to a web browser and email inbox
3. No additional tools needed; all via UI

## Defense

Defensive measures and detection strategies:

- Monitor for unusual invoice creation patterns (e.g., minimal details)
- Rate-limit invoice sending to prevent abuse
- Log search queries for anomalous strings

## Objectives

1. Create a searchable invoice artifact
2. Obtain email delivery for link extraction
3. Maintain low detection risk during setup

## Instructions

### Step 1: Login and Navigate to Invoice Creation

**Context**: Authenticate and access the feature to build the invoice.

No command; use browser to login at https://moneybird.com and navigate to 'New Invoice'.

> Successful login redirects to dashboard; click 'Sales > Invoices > New Invoice'.

### Step 2: Input Test String and Fill Fields

**Context**: Add the searchable 'test' and complete required data.

No command; in the invoice form, enter 'test' in the 'Description' or 'Details' field, add amount (e.g., $10), date (current), and a customer email.

> Form validates; preview shows 'test' in details.

### Step 3: Send Invoice to Email

**Context**: Trigger email to get the public link.

No command; enter a controlled email (e.g., attacker@example.com) in the recipient field and click 'Send'.

> Email confirmation appears; check inbox for link.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[setup]]
- [[invoice]]
