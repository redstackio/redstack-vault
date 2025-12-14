---
id: ac-phabricator-oauth-theft-3930
tags:
  - oauth
  - open-redirect
  - phabricator
  - token-theft
  - facebook
  - disqus
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
  - '[[procedures/Test-Phabricator-OAuth-for-Open-Redirect]]'
  - '[[procedures/Craft-Malicious-Phabricator-OAuth-URL]]'
  - '[[procedures/Chain-with-Facebook-OAuth]]'
  - '[[procedures/Trigger-User-Interaction-for-Token-Leak]]'
  - '[[procedures/Extend-to-Disqus-OAuth]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T17:24:35.429Z'
description: >-
  A multi-stage attack exploiting an open redirect vulnerability in
  Phabricator's OAuth dialog to chain with external providers like Facebook and
  Disqus, enabling one-click theft of OAuth tokens or codes without user login
  or additional interaction.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Application Access Token]]'
---
# OAuth Token Theft via Phabricator Open Redirect Chaining

Multi-stage attack chain demonstrating exploitation of an open redirect in Phabricator's OAuth dialog to steal OAuth tokens from external providers like Facebook and Disqus through chained redirects, requiring only one user click for authorization.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Observe Phabricator OAuth Behavior] --> B[Craft Malicious URL]
    B --> C[Chain with External Provider]
    C --> D[User Authorization Click]
    D --> E[Token Leak to Attacker Site]
    E --> F[Account Compromise on Provider]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#e67e22
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser for testing
- URL encoder tool (e.g., built-in browser dev tools)

### Target Environment

- Phabricator instance (e.g., secure.phabricator.com)
- External OAuth providers (Facebook, Disqus)
- Attacker-controlled site for receiving redirects

### Initial Access Requirements

- Public access to Phabricator OAuth endpoint
- No credentials needed due to bypass
- Network access to external providers

## Detailed Attack Procedures

### Step 1: Observe Phabricator OAuth Behavior
procedure: [[procedures/Test-Phabricator-OAuth-for-Open-Redirect]]

**Objective**: Identify the open redirect vulnerability by testing the OAuth endpoint with invalid parameters to confirm automatic redirection without user interaction.

**Instructions**: Access the Phabricator OAuth endpoint and supply malformed parameters to trigger the redirect.

**Expected Output**: Immediate browser redirect to the specified redirect_uri without prompts.

**Success Indicators**:
- Redirect occurs without login or confirmation
- No error for invalid scope

### Step 2: Craft Malicious Phabricator OAuth URL
procedure: [[procedures/Craft-Malicious-Phabricator-OAuth-URL]]

**Objective**: Construct a URL that exploits the open redirect by using an invalid scope to force redirection to the attacker's site.

**Instructions**: Build the URL with attacker-controlled redirect_uri and invalid scope parameter.

**Expected Output**: A valid-looking Phabricator URL that auto-redirects to attacker site.

**Success Indicators**:
- URL parses correctly
- Test redirect confirms bypass

### Step 3: Chain with External OAuth Provider
procedure: [[procedures/Chain-with-Facebook-OAuth]]

**Objective**: Integrate the malicious Phabricator URL as the redirect_uri in an external provider's OAuth flow to hijack the authorization redirect.

**Instructions**: URL-encode the Phabricator URL and set it as redirect_uri in Facebook's OAuth dialog.

**Expected Output**: Facebook authorization leads to Phabricator redirect, then to attacker site with leaked token.

**Success Indicators**:
- Chained URL authorizes without errors
- Token appears in attacker site query parameters

### Step 4: User Interacts with Chained OAuth Link
procedure: [[procedures/Trigger-User-Interaction-for-Token-Leak]]

**Objective**: Simulate or entice user to click the chained link, resulting in one-click token theft during authorization.

**Instructions**: Provide the chained OAuth link to the user; upon authorization, the flow redirects through Phabricator to leak the token.

**Expected Output**: OAuth code or token captured on attacker site.

**Success Indicators**:
- User sees only provider authorization prompt
- No additional Phabricator interaction required
- Token/code received

### Step 5: Repeat for Other Providers
procedure: [[procedures/Extend-to-Disqus-OAuth]]

**Objective**: Apply the same chaining technique to additional providers like Disqus to broaden the attack scope.

**Instructions**: Construct and use a similar chained URL for Disqus OAuth, encoding the malicious Phabricator URL.

**Expected Output**: Disqus token leaked via the redirect chain.

**Success Indicators**:
- Successful authorization on Disqus
- Token exfiltration to attacker site

## Attack Chain Summary

### Key Achievements

1. Bypassed Phabricator OAuth validation using invalid scope for open redirect.
2. Chained redirect to steal tokens from Facebook and Disqus with one-click user interaction.
3. Enabled account compromise on external providers without direct access to Phabricator credentials.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Steal Application Access Token]] Steal Application Access Token

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Credential Access]] Credential Access

---
*Last updated: 2023-10-01T00:00:00Z*
