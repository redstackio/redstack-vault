---
tags:
  - xss
  - shopify
  - configuration
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: a0213800-3729-4d8f-ae2b-a506d15dcbaa
created_at: '2025-12-14T00:11:16.778Z'
updated_at: '2025-12-14T00:11:16.778Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Enable Google Apps Login in Shopify Admin

## Summary

This procedure enables the Google Apps login option in Shopify admin settings, which is a prerequisite for exploiting the reflected XSS vulnerability in the login functionality.

## Description

By accessing the Shopify admin panel and toggling the Google login feature, the environment is prepared for parameter manipulation. This step is necessary to expose the vulnerable google_apps_uri parameter on the login page. The procedure targets web-based Shopify services and requires admin access.

## Requirements

1. Shopify account with admin privileges
2. Web browser access to Shopify admin URL
3. No prior Google integration enabled

## Defense

Defensive measures and detection strategies:

- Regularly audit admin settings for unnecessary integrations
- Monitor for unexpected changes in login configurations

## Objectives

1. Activate Google Apps login
2. Prepare the login page for exploitation
3. Confirm feature enablement

## Instructions

### Step 1: Access Admin Settings

**Context**: Navigate to the account settings page to enable the feature.

Access the URL:

```bash
https://YOURSHOP.myshopify.com/admin/settings/account
```

> This loads the settings page where login options are configured.

### Step 2: Enable Feature

**Context**: Toggle the Google Apps login option.

Enable 'Staff can use Google Apps to log in' and save changes.

> Expected confirmation of successful enablement.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- xss
- shopify
