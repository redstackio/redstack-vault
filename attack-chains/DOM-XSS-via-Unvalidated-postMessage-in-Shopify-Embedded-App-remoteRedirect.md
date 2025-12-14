---
tags:
  - xss
  - dom-xss
  - shopify
  - postmessage
  - javascript
  - embedded-app
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Review-Previous-Reports-for-Similar-Vulnerabilities]]'
  - '[[procedures/Identify-Vulnerable-postMessage-Handler]]'
  - '[[procedures/Craft-Malicious-XSS-Payload]]'
  - '[[procedures/Inject-Script-into-Store-Theme]]'
  - '[[procedures/Trigger-Payload-as-Authenticated-Admin]]'
step_count: 5
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:47:18.219Z'
description: >-
  Multi-stage attack exploiting a DOM-based XSS in Shopify's embedded app
  library by injecting a malicious script into a store theme to execute
  JavaScript in the authenticated admin context via crafted postMessage.
skill_level: intermediate
impact_level: high
id: e003c544-e196-45ac-9372-b1a262969816
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# DOM XSS via Unvalidated postMessage in Shopify Embedded App remoteRedirect

Multi-stage attack chain demonstrating exploitation of a DOM-based XSS vulnerability in Shopify's embedded app JavaScript library, allowing arbitrary JavaScript execution in the admin context.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Review Prior Reports] --> B[Identify Vulnerable Code]
    B --> C[Craft Payload]
    C --> D[Inject into Theme]
    D --> E[Trigger as Admin]
    E --> F[Execute XSS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools for code review
- Access to Shopify store admin for theme editing

### Target Environment

- Shopify store with admin access
- Web browser (e.g., Chrome)
- No specific ports or services beyond standard HTTPS

### Initial Access Requirements

- Authenticated access to a Shopify store as a user who can edit themes
- Ability to log in as an admin to trigger the exploit
- Network access to the store's frontend and admin pages

## Detailed Attack Procedures

### Step 1: Review Previous Reports
procedure: [[procedures/Review-Previous-Reports-for-Similar-Vulnerabilities]]

**Objective**: Identify patterns in prior vulnerabilities to discover similar issues in Shopify's embedded app code.

**Instructions**: Examine report #422043 on HackerOne, which details a postMessage vulnerability, and look for analogous handlers in the embedded app library.

**Expected Output**: Insight into unverified postMessage handlers, leading to the remoteRedirect function.

**Success Indicators**:
- Similar vulnerability patterns identified
- Target library file noted for further review

### Step 2: Identify Vulnerable Code
procedure: [[procedures/Identify-Vulnerable-postMessage-Handler]]

**Objective**: Locate the specific code flaw in the Shopify embedded app JavaScript that fails to validate protocols in postMessage data.

**Instructions**: Download and inspect the file at https://cdn.shopifycloud.com/web/assets/latest/embeddedApp-ab64a8a13eb3f06403cb2acf67e20576a144bf2d3625807923872e8adf469a14.js. Search for the 'de.RemoteRedirect' case, which calls this.handleRemoteRedirect(t.location) without checking if the location uses a javascript: protocol.

**Expected Output**: Confirmation of the vulnerability where window.location assignment executes javascript: URLs without validation.

**Success Indicators**:
- Vulnerable handler located
- Protocol bypass confirmed

### Step 3: Craft Malicious Payload
procedure: [[procedures/Craft-Malicious-XSS-Payload]]

**Objective**: Develop a JavaScript payload that opens the admin themes page and sends a crafted postMessage to exploit the remoteRedirect handler.

**Instructions**: Create the initial payload using [[commands/inject-shopify-xss-payload]] to open a new window to the admin/themes page and poll with postMessage until execution.

```javascript
function attack(){
  var ctx=window.open('https://cuxuri.myshopify.com/admin/themes');
  var interval;
  interval=setInterval(function(){
    if(window.attackSuccess){
      clearInterval(interval);
    }else{
      ctx.postMessage(`{"message":"Shopify.API.remoteRedirect","data":{"location":"javascript:alert(document.domain)"}}`);
    }
  },500);
}
</script>
<a href="javascript:attack()" style="display:block;text-align:center;width:100%;height:300px;line-height:300px;background:#000;color:#fff;">click me start attack</a>
```

Update to automatic version with [[commands/inject-auto-shopify-xss-payload]] for direct execution on load.

**Expected Output**: Payload ready for injection, testing alert in a local environment if possible.

**Success Indicators**:
- Payload script compiles without errors
- Simulated postMessage triggers javascript: execution

### Step 4: Inject into Store Theme
procedure: [[procedures/Inject-Script-into-Store-Theme]]

**Objective**: Embed the malicious script into the store's theme to enable delivery to authenticated users.

**Instructions**: Log in to the Shopify admin, navigate to Online Store > Themes, edit the current theme's liquid file (e.g., theme.liquid), and insert the payload script from Step 3.

**Expected Output**: Theme updated with injected <script> tag containing the attack function.

**Success Indicators**:
- Script visible in theme editor preview
- No syntax errors on save

### Step 5: Trigger Payload as Admin
procedure: [[procedures/Trigger-Payload-as-Authenticated-Admin]]

**Objective**: Execute the injected script in the context of an authenticated admin to achieve XSS in the admin session.

**Instructions**: Visit the store page with the modified theme while logged in as an admin. The script will open the admin/themes page in a new window and send the postMessage payload, triggering the remoteRedirect to execute the javascript:alert.

**Expected Output**: Alert box displaying the admin domain (e.g., alert('cuxuri.myshopify.com')) in the admin window context.

**Success Indicators**:
- New window opens to admin/themes
- postMessage sent successfully
- Arbitrary JS (alert) executes in admin context

## Attack Chain Summary

### Key Achievements

1. Discovered unvalidated protocol in postMessage handler
2. Injected persistent XSS payload via theme modification
3. Achieved admin-context JS execution for potential session compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Initial Access]]

---

*Last updated: 2023-10-01T00:00:00Z*
