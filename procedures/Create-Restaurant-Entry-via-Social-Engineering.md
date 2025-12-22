---
id: proc-uuid-001
tags:
  - social-engineering
  - content-moderation-bypass
  - web
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
updated_at: '2025-12-14T03:15:30.795Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Restaurant-Entry-via-Social-Engineering

## Summary

This procedure involves submitting a new restaurant entry to Zomato's platform using social engineering techniques to craft legitimate-appearing details, ensuring it passes content moderation for later exploitation.

## Description

In the context of exploiting Zomato's XSS vulnerability, this initial step establishes a foothold by adding a controllable restaurant. The target environment is Zomato's public-facing web application. Expected outcomes include moderation approval, granting edit access. Prerequisites include a Zomato account and knowledge of plausible restaurant data.

## Requirements

1. Zomato user account with submission privileges
2. Internet access to https://www.zomato.com/addrestaurant
3. Social engineering skills to create convincing submissions (e.g., using real but obscure location data)

## Defense

Defensive measures and detection strategies:

- Implement stricter moderation with AI-assisted review for new submissions
- Rate-limit restaurant additions per account
- Log and monitor submission patterns for anomalies

## Objectives

1. Gain approved restaurant entry for modification
2. Bypass initial content filters
3. Set up for payload injection

## Instructions

### Step 1: Prepare Submission Data

**Context**: Gather details to make the restaurant appear legitimate, reducing rejection risk.

Use browser to research low-profile areas (e.g., Kingman, KS) and fabricate plausible name, address, and description.

### Step 2: Submit Restaurant Addition

**Context**: Access the addition form and submit.

Navigate to https://www.zomato.com/addrestaurant and fill in fields:

- Restaurant Name: "Test Cafe"
- Location: Valid address in target city
- Description: Neutral text

Submit and monitor for approval email or status.

> Expected output: Submission confirmation; approval within 1-24 hours if social engineering succeeds.

### Step 3: Verify Approval

**Context**: Check if the entry is live.

Search for the restaurant name on Zomato to confirm visibility.

> Expected output: Restaurant profile appears in search results.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[social-engineering]]
- [[web-exploitation]]
