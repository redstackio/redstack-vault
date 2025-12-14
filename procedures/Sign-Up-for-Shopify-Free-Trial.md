---
id: proc-uuid-1
tags:
  - shopify
  - signup
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:58.674Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Sign-Up-for-Shopify-Free-Trial

## Summary

This procedure initiates a Shopify free trial account using an attacker-controlled email, establishing the foundation for subsequent email manipulation in the profile.

## Description

In the context of exploiting Shopify's email confirmation bypass, signing up for a free trial creates a new store account tied to the attacker's email. This allows quick access to the profile management without prior authentication barriers. The target environment is the public-facing Shopify signup page, and success enables immediate profile editing. Prerequisites include an email account under attacker control.

## Requirements

1. Web browser with internet access
2. Attacker-controlled email address (e.g., attacker@gmail.com)
3. No existing Shopify account needed

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on trial signups to prevent abuse
- Monitor for rapid profile changes post-signup
- Require CAPTCHA or additional verification during trial creation

## Objectives

1. Create a new Shopify trial store
2. Associate it with attacker email for email interception
3. Gain dashboard access for profile manipulation

## Instructions

### Step 1: Navigate to Signup Page

**Context**: Start the trial creation process on the official pricing page.

Visit https://www.shopify.com/pricing in your browser.

> This loads the pricing plans; select the free trial option.

### Step 2: Enter Signup Details

**Context**: Provide basic information to create the account.

Enter the store name, attacker email (e.g., attacker@gmail.com), and password. Click 'Start free trial' and complete any prompted store details like address.

> Upon submission, the system creates the store (e.g., you-shop.myshopify.com) and redirects to the dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[signup]]
- [[initial-access]]
