---
tags:
  - shopify
  - admin
  - customer-profile
  - email
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.538Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: af4fe345-d1bf-4d76-8d7d-2aa08b1eaa42
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# View Customer Email Details

## Summary

This procedure opens a specific customer's profile in the Shopify admin to access their email and message history, positioning the attacker to interact with stored content like malicious messages.

## Description

As part of exploiting stored XSS in Shopify's Timeline feature, this step involves selecting a customer whose messages contain injected payloads. From the customers list, clicking the email address loads the profile page, revealing sections for orders, notes, and communications. The technical approach relies on standard admin UI navigation, with prerequisites including prior access to the customers page. Outcomes include exposure of the Timeline, where messages are previewed.

## Requirements

1. Access to the customers list page from previous procedure
2. Identification of a target customer with pre-injected malicious message
3. Browser session maintaining admin authentication

## Defense

Defensive measures and detection strategies:

- Log and alert on frequent customer profile views by staff
- Sanitize and validate all customer data displays
- Enable audit logs for admin actions on customer records

## Objectives

1. Load customer profile to access communication history
2. Identify messages in the Timeline feature
3. Prepare for payload triggering without alerting

## Instructions

### Step 1: Select Customer

**Context**: Target a customer with stored XSS payload in their messages.

From the customers page at https://store.myshopify.com/admin/customers, locate the target customer using search or scrolling, then click on their email address link.

> This redirects to the profile page (e.g., /admin/customers/{id}), loading details including email and activity feed.

### Step 2: Inspect Profile Sections

**Context**: Confirm availability of message and Timeline views.

Review the profile tabs or sections for 'Orders', 'Notes', and 'Timeline'. Ensure the email address is highlighted and messages are listed.

> Profile loads if successful; look for communication logs to proceed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[admin]]
- [[customer-profile]]
- [[email]]
