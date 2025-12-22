---
tags:
  - shopify
  - endpoint-discovery
  - network-analysis
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
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:30:47.375Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 88c105ee-43b8-4fdd-a54d-22167ac25eb7
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Lead-Creation-Endpoint-as-Administrator

## Summary

This procedure involves using administrator access to interact with the referrals functionality in Shopify's Partner Portal, capturing the backend endpoint for POS lead creation via network inspection.

## Description

As an admin, navigate to the referrals page and trigger a lead submission to reveal the API endpoint. Use browser developer tools to monitor requests, identifying https://partners.shopify.com/[partner_id]/partner_leads/pos as the target for POST requests. This reconnaissance step uncovers the bypass vector.

## Requirements

1. Administrator credentials for full access.
2. Web browser with developer tools (e.g., Network tab in Chrome DevTools).
3. Partner ID for URL targeting.

## Defense

Defensive measures and detection strategies:

- Obfuscate or randomize API endpoints to hinder discovery.
- Log and alert on unusual network inspection patterns from admin sessions.
- Implement endpoint access logging for all admin actions.

## Objectives

1. Locate the exact backend URL for lead creation.
2. Understand the request format for later replication.
3. Confirm admin-level functionality works as expected.

## Instructions

### Step 1: Trigger Lead Submission and Capture Endpoint

**Context**: Perform an admin action to expose the backend API call.

Log in as admin, go to https://partners.shopify.com/[partner_id]/referrals/, click 'Submit a POS Lead', fill a test form, and submit while monitoring the Network tab in developer tools.

> Expected output: POST request to https://partners.shopify.com/[partner_id]/partner_leads/pos captured.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[endpoint-discovery]]
