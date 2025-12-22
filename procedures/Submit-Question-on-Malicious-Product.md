---
tags:
  - xss
  - persistence
  - judge-me
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - Shopify
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 429dd64f-62c6-49b2-8f2e-2966984fea7f
created_at: '2025-12-14T03:46:32.057Z'
updated_at: '2025-12-14T03:46:32.057Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Submit-Question-on-Malicious-Product

## Summary

This procedure submits a customer question linked to the malicious product, storing the XSS payload association in the Judge.me backend for later admin exposure.

## Description

Questions in Judge.me are tied to products, inheriting the product name metadata. By submitting a question on the product with the injected payload, the unsanitized name is persisted in the question record. This step requires only customer-level access and does not trigger the XSS immediately. Expected outcome: Question record created with payload reference.

## Requirements

1. Access to the storefront as a logged-in customer
2. Malicious product already created and visible
3. Judge.me app enabled for questions

## Defense

Defensive measures and detection strategies:

- Sanitize product references in question storage and display
- Rate-limit question submissions to prevent abuse
- Audit question logs for associations with suspicious products

## Objectives

1. Link payload to a persistent entity (question)
2. Maintain payload integrity through association
3. Prepare for admin-side trigger

## Instructions

### Step 1: Navigate to Product Page

**Context**: Locate the malicious product in the storefront.

Search for or directly access the product page with the XSS-named item.

### Step 2: Submit Question

**Context**: Use the Judge.me form to create the association.

In the questions section, enter any neutral question text (e.g., 'What is the size?') and submit. The product name payload is automatically stored with the question.

> No visible changes; confirm by checking if the question appears under the product.

### Step 3: Verify Association

**Context**: Ensure the link is established.

If possible, view recent questions; the association should be present.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Persistence]]
