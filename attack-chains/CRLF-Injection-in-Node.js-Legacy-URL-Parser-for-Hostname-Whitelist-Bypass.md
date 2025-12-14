---
tags:
  - crlf-injection
  - node-js
  - url-parse
  - whitelist-bypass
  - parsing-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Node.js
  - JavaScript
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Craft-CRLF-Injection-URL-for-Node.js]]'
  - '[[procedures/Parse-URL-with-Legacy-url.parse-to-Extract-Hostname]]'
  - '[[procedures/Compare-with-Modern-URL-Constructor-Parsing]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:01.501Z'
description: >-
  Demonstrates a CRLF injection vulnerability in Node.js legacy
  url.parse().hostname API to bypass hostname whitelists, enabling access to
  unauthorized hosts and potential website compromise.
skill_level: intermediate
impact_level: high
id: f367a6c3-f7b5-4bc8-949f-e8f9af825b18
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# CRLF Injection in Node.js Legacy URL Parser for Hostname Whitelist Bypass

Multi-stage attack chain demonstrating exploitation of a CRLF injection in Node.js's legacy url.parse().hostname API to manipulate hostname parsing and bypass whitelist validations.

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
    A[Craft Malicious URL] --> B[Parse with Legacy API]
    B --> C[Compare Parsing and Bypass Whitelist]
    C --> D[Exploit Unauthorized Host]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Node.js environment (version with legacy url module)

### Target Environment

- Node.js application using legacy url.parse() for hostname validation
- Whitelist-based access controls on hostnames

### Initial Access Requirements

- Access to input URL field or parameter in the Node.js application
- No special credentials needed; exploitable via user-supplied input

## Detailed Attack Procedures

### Step 1: Craft Malicious URL
procedure: [[procedures/Craft-CRLF-Injection-URL-for-Node.js]]

**Objective**: Create a proof-of-concept URL string that injects CRLF characters to split the hostname, allowing manipulation of parsing results.

**Instructions**: Define the POC URL in a Node.js script using newline escapes to inject after the whitelisted hostname.

Execute [[commands/define-poc-url]] to set the malicious URL:

```javascript
const poc_url = 'http://test1.com\r\ntest2.com';
```

**Expected Output**: A string variable holding the injected URL, ready for parsing.

**Success Indicators**:
- URL string contains CRLF after 'test1.com'
- No syntax errors in definition

### Step 2: Parse with Legacy API
procedure: [[procedures/Parse-URL-with-Legacy-url.parse-to-Extract-Hostname]]

**Objective**: Use the vulnerable legacy url.parse() to extract only the hostname before the CRLF, bypassing full validation.

**Instructions**: Require the url module and parse the POC URL, extracting .hostname which stops at the CRLF.

Execute [[commands/parse-legacy-url]] to perform the parsing:

```javascript
const url = require('url');
const parsed = url.parse(poc_url);
console.log(parsed.hostname); // Outputs: 'test1.com'
```

**Expected Output**: Hostname extracted as 'test1.com', ignoring the injected 'test2.com'.

**Success Indicators**:
- Parsed hostname matches only the pre-CRLF part
- Whitelist check would pass for 'test1.com' despite full URL targeting 'test2.com'

### Step 3: Compare with Modern Parsing
procedure: [[procedures/Compare-with-Modern-URL-Constructor-Parsing]]

**Objective**: Demonstrate the difference in parsing to confirm the vulnerability and its exploitability.

**Instructions**: Use the modern URL constructor to parse the same URL, showing it handles the full string without splitting.

Execute [[commands/parse-modern-url]] for comparison:

```javascript
const modernUrl = new URL(poc_url);
console.log(modernUrl.hostname); // Outputs: 'test1.com\r\ntest2.com'
```

**Expected Output**: Full hostname including injection, highlighting the legacy parser's flaw.

**Success Indicators**:
- Modern parser shows injected content in hostname
- Confirms legacy bypass potential for exploitation

## Attack Chain Summary

### Key Achievements

1. Successfully crafted a CRLF-injected URL to split hostname parsing.
2. Bypassed whitelist validation using legacy url.parse().hostname.
3. Validated the vulnerability by comparing with secure modern parsing, enabling potential access to unauthorized hosts and compromise of medium to high severity issues.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
