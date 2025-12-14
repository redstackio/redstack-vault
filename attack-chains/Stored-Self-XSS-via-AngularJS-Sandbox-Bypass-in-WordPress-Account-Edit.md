---
id: ac-222224-stored-self-xss-angularjs-bypass
tags:
  - xss
  - stored-xss
  - self-xss
  - angularjs
  - sandbox-bypass
  - wordpress
type: attack_chain
tools:
  - '[[tools/Chrome]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Register-Account-on-WordPress-Swag-Store]]'
  - '[[procedures/Navigate-to-Account-Edit-Page]]'
  - '[[procedures/Inject-AngularJS-Sandbox-Bypass-Payload]]'
  - '[[procedures/Trigger-Self-XSS-by-Page-Refresh]]'
step_count: 4
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:30.755Z'
description: >-
  A multi-step attack exploiting a stored self-XSS vulnerability in the
  mercantile.wordpress.org swag store by bypassing AngularJS sandbox
  restrictions in the account edit form, allowing JavaScript execution limited
  to the authenticated user.
skill_level: intermediate
impact_level: low
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored Self-XSS via AngularJS Sandbox Bypass in WordPress Account Edit

Multi-stage attack chain demonstrating a complete self-XSS workflow in the mercantile.wordpress.org swag store, exploiting lax input validation in the account edit form to inject and execute malicious AngularJS expressions.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Register Account] --> B[Navigate to Edit Page]
    B --> C[Inject Payload]
    C --> D[Trigger XSS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Chrome]]

### Target Environment

- Web platform
- WordPress with AngularJS integration
- Access to mercantile.wordpress.org swag store

### Initial Access Requirements

- No prior credentials needed; registration is open
- Direct network access to the site
- No elevated privileges required

## Detailed Attack Procedures

### Step 1: Register Account
procedure: [[procedures/Register-Account-on-WordPress-Swag-Store]]

**Objective**: Create an authenticated user account to access the edit form, where input restrictions are bypassed compared to registration.

**Instructions**: Open [[tools/Chrome]] and navigate to the mercantile.wordpress.org signup page. Fill in the required fields with valid data, ensuring name fields comply with symbol restrictions during registration.

**Expected Output**: Successful account creation with confirmation email or redirect to dashboard.

**Success Indicators**:
- Account registered and login successful
- Access to /my-account/ endpoint granted

### Step 2: Navigate to Account Edit Page
procedure: [[procedures/Navigate-to-Account-Edit-Page]]

**Objective**: Reach the vulnerable edit form where First Name and Last Name fields allow unrestricted input.

**Instructions**: After logging in, browse to the /my-account/edit-account/ endpoint using the site's navigation or direct URL entry in [[tools/Chrome]].

**Expected Output**: Account edit form loaded, displaying current user details.

**Success Indicators**:
- Edit form accessible
- Input fields for First Name and Last Name visible

### Step 3: Inject Payload
procedure: [[procedures/Inject-AngularJS-Sandbox-Bypass-Payload]]

**Objective**: Inject a malicious AngularJS expression into the name fields to bypass sandbox protections and prepare for JavaScript execution.

**Instructions**: In the First Name and Last Name fields, paste the payload: `{{ c=''.sub.call;b=''.sub.bind;a=''.sub.apply; c.$apply=$apply;c.$eval=b;op=$root.$$phase; $root.$$phase=null;od=$root.$digest;$root.$digest=({}).toString; C=c.$apply(c);$root.$$phase=op;$root.$digest=od; B=C(b,c,b);$evalAsync(" astNode=pop();astNode.type='UnaryExpression'; astNode.operator='(window.X?void0:(window.X=true,prompt(document.domain)))+'; astNode.argument={type:'Identifier',name:'foo'}; "); m1=B($$asyncQueue.pop().expression,null,$root); m2=B(C,null,m1);[].push.apply=m2;a=''.sub; $eval('a(b.c)');[].push.apply=a; }}`. Submit the form to save the changes.

**Expected Output**: Form submission successful without errors; payload stored in user profile.

**Success Indicators**:
- No validation errors on submission
- Profile updates confirmed

### Step 4: Trigger XSS
procedure: [[procedures/Trigger-Self-XSS-by-Page-Refresh]]

**Objective**: Execute the stored payload by reloading the page, resulting in JavaScript alert displaying the document domain.

**Instructions**: Refresh the account edit page in [[tools/Chrome]] to re-render the form with the injected payload.

**Expected Output**: JavaScript alert pops up showing the domain (e.g., mercantile.wordpress.org).

**Success Indicators**:
- Alert box appears with domain
- JavaScript execution confirmed (self-XSS only affects the user's session)

## Attack Chain Summary

### Key Achievements

1. Bypassed AngularJS sandbox via AST manipulation and function rebinding
2. Stored malicious payload in user profile fields
3. Achieved JavaScript execution in authenticated context
4. Demonstrated low-impact self-XSS due to user-specific limitation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
