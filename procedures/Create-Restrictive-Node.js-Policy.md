---
tags:
  - node.js
  - policy
  - setup
type: procedure
tools:
  - '[[tools/Node.js]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Linux
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:58.911Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 14d5e0ea-0f41-4a8b-a66e-d9aaceb3123a
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Restrictive-Node.js-Policy

## Summary

This procedure sets up a restrictive experimental policy in Node.js v19.6.1 that allows loading only a single JavaScript file without any dependencies, preparing the environment for demonstrating a permission bypass.

## Description

The Node.js experimental permission system uses a policy manifest to control module loading and execution. By defining a policy that permits only './proc.js' with 'integrity: true', this procedure ensures no external or dependent modules can be loaded directly, creating a controlled scenario to test and exploit the vulnerability in the CommonJS loader where prototype chain access evades checks.

## Requirements

1. Node.js v19.6.1 installed on Linux
2. Write access to the current directory for creating policy.json
3. Basic knowledge of JSON for policy definition

## Defense

Defensive measures and detection strategies:

- Enable and monitor Node.js experimental policies in production to restrict untrusted code
- Audit script executions for prototype chain manipulations using code scanning tools
- Update to Node.js versions beyond v19.6.1 where this bypass is patched

## Objectives

1. Establish a baseline restrictive environment for module permissions
2. Verify policy enforcement prevents direct dependency loading
3. Prepare for privilege escalation testing

## Instructions

### Step 1: Define Policy Resources

**Context**: Create the policy.json file specifying allowed resources.

No command required; manually create the file with the following content:

```json
{
  "resources": {
    "./proc.js": {
      "integrity": true
    }
  }
}
```

> This JSON defines './proc.js' as the only allowed file with integrity checks, blocking any require() calls to dependencies.

### Step 2: Validate Policy Syntax

**Context**: Ensure the policy is syntactically correct before use.

Use a JSON validator or Node.js to check:

```bash
node -e "console.log(JSON.parse(require('fs').readFileSync('policy.json', 'utf8')));"
```

> Expected output: No errors, parsed object displayed. This confirms the policy is loadable.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Node.js]]

## Tags

- node.js
- policy
- setup
