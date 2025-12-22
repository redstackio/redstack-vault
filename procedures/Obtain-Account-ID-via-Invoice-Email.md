---
tags:
  - recon
  - email
  - id-extraction
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T03:15:31.424Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 60b8f871-ab68-4f36-9faf-5513f5b65284
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Obtain-Account-ID-via-Invoice-Email

## Summary

This procedure involves receiving the invoice email and extracting the Moneybird account ID from the public viewing link, which is necessary for crafting the malicious search URL in the XSS attack.

## Description

After sending the test invoice, the email contains a link like https://moneybird.com/[id]/sales_invoices/[invoice_id]/[hash]. Parsing this URL reveals the account [id], a critical parameter for targeting the backend search endpoint. This step assumes email access and browser usage, with the outcome being the [id] for subsequent payload delivery.

## Requirements

1. Access to the email inbox used for invoice delivery
2. Web browser to open and inspect the link
3. Prior completion of invoice creation

## Defense

Defensive measures and detection strategies:

- Use short-lived or randomized hashes in email links
- Log link accesses for unusual patterns
- Educate users on phishing risks in invoice emails

## Objectives

1. Retrieve the account identifier from the email link
2. Enable targeted search URL construction
3. Avoid direct interaction that could trigger alerts

## Instructions

### Step 1: Receive and Open Email

**Context**: Access the sent invoice email.

No command; check the inbox for the Moneybird email and open it.

> Email body contains the 'View Invoice' link.

### Step 2: Click Link and Extract ID

**Context**: Load the link to inspect the URL structure.

No command; click the link in the browser, then copy the full URL from the address bar.

> URL format: https://moneybird.com/[id]/...; note the [id] segment (e.g., 123456).

### Step 3: Validate ID

**Context**: Confirm the ID by checking if the invoice loads.

No command; ensure the page displays the invoice with 'test' details.

> Page loads successfully, confirming valid [id].

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[email]]
- [[id-extraction]]
