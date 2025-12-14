---
tags:
  - cors
  - misconfiguration
  - information-disclosure
  - account-takeover
  - web
type: attack_chain
tools:
  - '[[tools/Browser-Firefox]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Test-CORS-Policy-with-Custom-Origin]]'
  - '[[procedures/Exploit-CORS-to-Fetch-User-Data]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:33:12.120Z'
description: >-
  A multi-stage attack exploiting a CORS misconfiguration on nordvpn.com to
  disclose sensitive user data and enable account takeover via credentialed
  cross-origin requests.
skill_level: intermediate
impact_level: high
id: 39a68460-b045-4743-9146-3ad9ff91df66
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
---
# CORS Misconfiguration on NordVPN Leading to Private Information Disclosure and Account Takeover

Multi-stage attack chain demonstrating a complete attack workflow exploiting a CORS vulnerability on nordvpn.com's WordPress REST API.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Test CORS Policy] --> B[Exploit for Data Theft]
    B --> C[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Browser-Firefox]]

### Target Environment

- Web platform with WordPress REST API
- Services: HTTPS on port 443
- Tech stack: WordPress, Cloudflare

### Initial Access Requirements

- No prior credentials needed for testing
- Victim must be authenticated on nordvpn.com
- Attacker needs to host a malicious HTML page

## Detailed Attack Procedures

### Step 1: Test CORS Policy
procedure: [[procedures/Test-CORS-Policy-with-Custom-Origin]]

**Objective**: Verify the CORS misconfiguration by sending a request with a custom Origin header to check if it's echoed without validation.

**Instructions**: Use a browser developer tools or curl to send a GET request to the /wp-json/ endpoint with a custom Origin header. Execute [[commands/test-cors-with-custom-origin]] via curl:

```bash
curl -X GET https://nordvpn.com/wp-json/ -H "Origin: http://iamsoevil.com/" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0" -v
```

Inspect the response headers for Access-Control-Allow-Origin reflecting the custom origin and Access-Control-Allow-Credentials: true.

**Expected Output**: HTTP 200 response with headers including Access-Control-Allow-Origin: http://iamsoevil.com/ and Access-Control-Allow-Credentials: true.

**Success Indicators**:
- Custom Origin is echoed in ACAO header
- Credentials are allowed for any origin

### Step 2: Exploit for Data Theft
procedure: [[procedures/Exploit-CORS-to-Fetch-User-Data]]

**Objective**: Trick an authenticated user into loading a malicious page that performs credentialed cross-origin requests to steal user data from the WordPress API.

**Instructions**: Host an HTML page on an attacker-controlled domain (e.g., http://iamsoevil.com) containing JavaScript. When the victim visits it while logged into nordvpn.com, execute [[commands/exploit-cors-fetch-user-data-js]] in the browser context:

```javascript
var req = new XMLHttpRequest(); req.onload = reqListener; req.open('get','https://nordvpn.com/wp-json/wp/v2/users/1',true); req.withCredentials = true; req.send('{}'); function reqListener() { alert(this.responseText); };
```

The script sends a credentialed request to /wp-json/wp/v2/users/1, displaying the JSON response with user details.

**Expected Output**: Alert showing JSON with user information, such as name, email, and potentially session data.

**Success Indicators**:
- Cross-origin request succeeds with victim's credentials
- Sensitive data (e.g., user profile) is disclosed
- Potential for session theft leading to account takeover

## Attack Chain Summary

### Key Achievements

1. Confirmed CORS misconfiguration allowing arbitrary origins with credentials
2. Demonstrated data exfiltration from authenticated WordPress API endpoints
3. Enabled potential account takeover via stolen sessions or private info

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]
- [[Steal Web Session Cookie]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---

*Last updated: 2023-10-01T00:00:00Z*
