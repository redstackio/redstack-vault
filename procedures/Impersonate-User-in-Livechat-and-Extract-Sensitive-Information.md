---
tags:
  - impersonation
  - data-exfiltration
  - pii-disclosure
type: procedure
tactics:
  - '[[Credential Access]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Application Access Token]]'
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:25:17.792Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 1a5b47a5-975a-47ad-88d9-3adccb575b39
validated: true
mitre_tactics:
  - '[[Credential Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
  - '[[Data from Local System]]'
---
# Impersonate-User-in-Livechat-and-Extract-Sensitive-Information

## Summary

This procedure uses the stolen access token to authenticate to Shopify's livechat as the victim, enabling impersonation in support chats and extraction of sensitive user data from the page source.

## Description

With the auth_code, the attacker navigates to the livechat endpoint, logging in without further credentials. The interface loads user details in JavaScript objects within the page source, allowing scraping of email, name, and metadata. This leads to full impersonation for chatting with support agents.

## Requirements

1. Stolen access token from previous step
2. Browser access to https://livechat.shopify.com
3. Ability to inspect page source

## Defense

Defensive measures and detection strategies:

- Short-lived tokens with revocation on misuse
- Encrypt or obfuscate PII in client-side JS
- Monitor for unusual chat sessions and token reuse

## Objectives

1. Authenticate to livechat using stolen token
2. Access victim-specific chat interface
3. Extract and disclose sensitive PII

## Instructions

### Step 1: Authenticate to Livechat with Token

**Context**: Use the token to gain access as the victim.

Navigate to:

```url
https://livechat.shopify.com/customer/chats/new?auth_code=<access_token>&auth_type=chat
```

> Replace <access_token> with the stolen value; successful load indicates impersonation.

### Step 2: Inspect Page Source for User Data

**Context**: View source to find embedded JS with user details.

Look for: var chat = new TC.CustomerChat({ chat:{"id":"<id>","token":"<chat_token>","name":"<user_first_and_last_name>","email":"<user_email>","metadata":"<other_meta_data>"}, ... });

> Parse the object to extract name, email, and other metadata.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access
- [[Collection]] Collection

### Techniques

- [[Steal Application Access Token]] Steal Application Access Token
- [[Data from Local System]] Data from Local System

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[impersonation]]
- [[data-exfiltration]]
