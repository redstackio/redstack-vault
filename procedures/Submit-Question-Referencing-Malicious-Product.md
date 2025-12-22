---
tags:
  - xss
  - stored-xss
  - shopify
  - judge.me
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
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 3aba5d32-bd66-4b30-acd0-3a57a4282c37
created_at: '2025-12-14T03:16:19.944Z'
updated_at: '2025-12-14T03:16:19.944Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Submit-Question-Referencing-Malicious-Product

## Summary

This procedure submits a question via the Judge.me interface on the frontend, linking it to the malicious product to enable the stored payload's reflection during admin moderation.

## Description

Once the product with the XSS payload is created, submitting a question about it in the Judge.me system ties the unsanitized product name to the question data. This step leverages the app's question feature, which pulls product details without sanitization, setting up the vector for admin-side execution. It assumes the attacker can act as a customer on the store frontend.

## Requirements

1. Access to the Shopify store frontend
2. Malicious product already created
3. Judge.me questions enabled on the product page

## Defense

Defensive measures and detection strategies:

- Sanitize product references in question submissions and displays
- Rate-limit question submissions to prevent abuse
- Log and review questions for suspicious content or patterns

## Objectives

1. Associate the malicious product with a trackable question
2. Ensure the product name is embedded in question metadata
3. Facilitate admin interaction for payload trigger

## Instructions

### Step 1: Locate Product Page

**Context**: Navigate to the store to find the product and access the question form.

Visit the Shopify store URL, search for or directly access the malicious product page where Judge.me questions are enabled.

### Step 2: Submit Question

**Context**: Use the question form to reference the product, relying on the stored payload in the name.

In the Judge.me question input, enter a benign question body but ensure it references the product. Optionally append a payload like '><img src=x onerror=prompt(document.domain)>' to the body for chaining. Submit the form.

> The submission stores the question with the product's unsanitized name attached.

### Step 3: Confirm Submission

**Context**: Verify the question is posted and queued for admin review.

Refresh the product page; the question should appear in the Judge.me section without executing the payload yet.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[xss]]
- [[stored-xss]]
- [[shopify]]
- [[judge.me]]
