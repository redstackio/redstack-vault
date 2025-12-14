---
id: ac-nodejs-dns-dos-1033107
tags:
  - dos
  - node-js
  - dns
  - resource-consumption
type: attack_chain
tools:
  - '[[tools/Node.js]]'
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Node.js
  - Windows
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Trigger-Node.js-DNS-DoS-with-Large-Response-Domain]]'
step_count: 1
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:30.828Z'
description: >-
  A denial-of-service attack exploiting uncontrolled resource consumption in
  Node.js DNS module by resolving domains with over 1300 A records, causing
  application hang or freeze.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
---
# Node.js DNS DoS via Excessive A Records Resolution

Multi-stage attack chain demonstrating a complete attack workflow targeting Node.js applications vulnerable to DNS resolution DoS.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Trigger DNS Resolution] --> B[Resource Exhaustion and DoS]

    style A fill:#e74c3c
    style B fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Node.js]]

### Target Environment

- Node.js runtime (versions v12.18.4 and v14.15.0 affected)
- Windows platform
- DNS service access

### Initial Access Requirements

- Ability to execute Node.js code in the target application
- No authentication required for remote trigger if DNS resolution is exposed
- Network access to resolve external domains

## Detailed Attack Procedures

### Step 1: Trigger DNS Resolution DoS
procedure: [[procedures/Trigger-Node.js-DNS-DoS-with-Large-Response-Domain]]

**Objective**: Force the Node.js application to resolve a domain with excessive A records, leading to uncontrolled resource consumption and service disruption.

**Instructions**: Execute the Node.js DNS resolution command using the vulnerable domain 'ticbrasil.com.br' which returns over 1300 A records. This can be injected into the application's code or triggered remotely if the app performs DNS lookups on user-controlled input.

Use [[commands/node-dns-resolve4-ticbrasil]] to reproduce:

```javascript
var dns = require('dns');
dns.resolve4('ticbrasil.com.br', function (err, addresses, family) {
  console.log(err);
  console.log(addresses);
  console.log(family);
});
```

Run with Node.js: `node script.js`

**Expected Output**: No response or hang instead of the list of addresses; the process consumes excessive resources and freezes.

**Success Indicators**:
- Node.js process hangs or produces no output
- High CPU/memory usage observed during resolution
- Service disruption in the application

## Attack Chain Summary

### Key Achievements

1. Successful trigger of DNS resolution leading to resource exhaustion
2. Demonstration of remote DoS without authentication
3. Identification of vulnerable Node.js versions

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[OS Exhaustion Flood]] OS Exhaustion Floods

### MITRE ATT&CK Tactics

- [[Impact]] Impact

---
*Last updated: 2023-10-01T00:00:00Z*
