---
tags:
  - csrf
  - shopify
  - customer-tagging
  - wholesale
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:50.036Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: be52f769-d169-4299-b322-ead75e159976
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Tag Customer for Wholesale Access

## Summary

This procedure prepares a target customer in Shopify by applying the 'wholesale' tag, making them eligible for the CSRF-exploitable invitation process in the Wholesale app.

## Description

As part of the attack on Shopify's Wholesale CSRF vulnerability, this step involves selecting or creating a customer record and tagging it 'wholesale' in the Shopify customers section. The price list is then adjusted to include this tag. This positions the customer for unauthorized invitation via forged requests. Target environment is the Shopify admin web interface. Outcomes: Customer ready for invitation, visible in Wholesale app without 'invited' status yet.

## Requirements

1. Configured Wholesale app with price list from prior setup
2. Access to Shopify customers management
3. Target customer details (e.g., email, name)

## Defense

Defensive measures and detection strategies:

- Implement tag approval workflows to prevent unauthorized tagging
- Audit customer tags regularly via Shopify reports for suspicious patterns

## Objectives

1. Apply 'wholesale' tag to target customer
2. Associate with price list for eligibility
3. Confirm visibility in Wholesale section

## Instructions

### Step 1: Select or Create Customer

**Context**: Identify the target customer to make vulnerable to the CSRF invitation.

Go to Shopify admin > Customers. Search for an existing customer or click 'Add customer' to create one with basic details like name and email.

> Expected: Customer record saved and listed.

### Step 2: Apply Wholesale Tag

**Context**: Tag the customer to trigger price list association and invitation eligibility.

Edit the customer record, scroll to 'Tags' section, and add 'wholesale'. Save changes.

> Expected: Tag applied; customer searchable by tag.

### Step 3: Adjust Price List and Verify

**Context**: Link the tag to the price list and check Wholesale app visibility.

In Wholesale app > Price Lists, edit the list to include 'wholesale' tagged customers. Then navigate to Wholesale > Customers to confirm the target appears.

> Expected: Customer listed in Wholesale section, status not 'invited'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[shopify]]
- [[tagging]]
