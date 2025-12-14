---
id: ac-uuid-001
tags:
  - xss
  - dom-xss
  - path-traversal
  - jsonp
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Analyze-Tags-Parameter-Behavior]]'
  - '[[procedures/Identify-JavaScript-Execution-from-Responses]]'
  - '[[procedures/Discover-JSONP-Endpoint]]'
  - '[[procedures/Craft-Path-Traversal-Payload-for-XSS]]'
step_count: 4
techniques:
  - '[[JavaScript]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-13T23:52:24.335Z'
description: >-
  A multi-stage attack exploiting a DOM-based reflected XSS vulnerability in the
  rockstargames.com/newswire/tags page by using path traversal to access an
  internal JSONP endpoint, leading to arbitrary JavaScript execution in the
  victim's browser.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[File and Directory Discovery]]'
---
# DOM-based Reflected XSS via Path Traversal and JSONP in Rockstar Games Newswire Tags

Multi-stage attack chain demonstrating a complete DOM-based reflected XSS workflow on the rockstargames.com/newswire/tags page, leveraging path traversal to access internal endpoints and JSONP for JavaScript execution.

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
    A[Analyze Tags Parameter] --> B[Identify JS Execution]
    B --> C[Discover JSONP Endpoint]
    C --> D[Craft Traversal Payload]
    D --> E[Arbitrary JS Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser Developer Tools (e.g., Chrome DevTools)
- Optional: Proxy tool like Burp Suite for intercepting requests

### Target Environment

- Web platform
- Access to http://www.rockstargames.com/newswire/tags
- Victim's browser session on the domain

### Initial Access Requirements

- No credentials required
- Direct URL access via link or bookmark
- Network access to rockstargames.com

## Detailed Attack Procedures

### Step 1: Analyze Tags Parameter Behavior
procedure: [[procedures/Analyze-Tags-Parameter-Behavior]]

**Objective**: Understand how the 'tags' URL fragment triggers AJAX requests and inserts responses into the DOM.

**Instructions**: Navigate to http://www.rockstargames.com/newswire/tags and append #/?tags= to the URL. Use browser developer tools to monitor network requests and observe the XHR to /newswire/tagContent/[decoded_tags]/1.

**Expected Output**: XHR request sent with the decoded tags value, response inserted into the page DOM.

**Success Indicators**:
- Network tab shows AJAX request to constructed endpoint
- Response content loaded into page elements

### Step 2: Identify JavaScript Execution from Responses
procedure: [[procedures/Identify-JavaScript-Execution-from-Responses]]

**Objective**: Confirm that responses with content-type application/javascript are automatically executed as script.

**Instructions**: Modify the tags parameter to fetch a known JavaScript resource (e.g., a public JS file) and inspect the content-type in the network response. Observe if the script executes by adding a console.log or alert in a test JS file.

**Expected Output**: Browser executes the JavaScript from the response, visible in console or via alert.

**Success Indicators**:
- Content-type application/javascript in response headers
- Script code runs without explicit eval or script tag

### Step 3: Discover JSONP Endpoint
procedure: [[procedures/Discover-JSONP-Endpoint]]

**Objective**: Identify internal endpoints that support JSONP callbacks via XHR, enabling script injection.

**Instructions**: Experiment with path traversal in the tags parameter (e.g., #/?tags=../../../) to probe internal paths. Look for endpoints like /comments_dal/users/getGlobalLoginSettings.json that wrap responses in callbacks when ?callback= is present.

**Expected Output**: Response from internal endpoint with JSONP wrapping, e.g., callbackName({...}).

**Success Indicators**:
- Access to non-public paths via traversal
- Endpoint responds with executable JavaScript format

### Step 4: Craft Path Traversal Payload for XSS
procedure: [[procedures/Craft-Path-Traversal-Payload-for-XSS]]

**Objective**: Combine path traversal with JSONP to inject and execute arbitrary JavaScript, such as an alert.

**Instructions**: Set the tags parameter to a URL-encoded path traversal payload targeting the JSONP endpoint with a malicious callback, e.g., #/?tags=%2e%2e%2e%2e%2e%2e%5ccomments_dal%5cusers%5cgetGlobalLoginSettings%2ejson?callback=alert(%2fxss%2f);%2f%2f. Load the URL and observe the execution.

**Expected Output**: Alert box pops up with 'xss', confirming arbitrary JS execution.

**Success Indicators**:
- XHR fetches the traversed endpoint
- Callback executes user-supplied JavaScript

## Attack Chain Summary

### Key Achievements

1. Bypassed URL fragment sanitization via direct decoding in AJAX construction
2. Exploited path traversal to access internal JSONP services
3. Achieved DOM-based XSS without server-side reflection, purely client-side execution

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
