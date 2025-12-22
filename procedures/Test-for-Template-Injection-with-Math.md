---
id: proc-uuid-2
name: Test-for-Template-Injection-with-Math
tags:
  - csti
  - template-test
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/test-template-injection-math]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:08.265Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-for-Template-Injection-with-Math

## Summary

This procedure tests for Client Side Template Injection (CSTI) by injecting a harmless mathematical expression into the Search parameter, which the frontend engine evaluates, confirming vulnerability without triggering alerts.

## Description

Targeting web applications with template engines like Handlebars, this procedure exploits unsanitized user input in search fields. By using {{7*7}}, the engine evaluates it server-side or client-side, rendering 49 if vulnerable. This is a low-risk probe in an offensive security assessment, prerequisite for escalating to JS execution. Outcomes include vulnerability confirmation, enabling further bypass techniques.

## Requirements

1. Access to the /News/Speeches endpoint
2. Web browser for URL manipulation
3. Basic understanding of template syntax ({{}})

## Defense

Defensive measures and detection strategies:

- Sanitize or escape user input before template rendering
- Disable unsafe expression evaluation in template engines
- Log and alert on unusual rendered content in search results

## Objectives

1. Detect template evaluation capability
2. Confirm lack of input sanitization
3. Validate injection point without execution risk

## Instructions

### Step 1: Construct Test Payload

**Context**: Prepare a simple expression that evaluates to a number, avoiding JS to stay under radar.

**Command** ([[commands/test-template-injection-math]]):
```bash
# Browser URL: www.███/News/Speeches?Search={{7*7}}
```

> The template engine processes {{7*7}}, embedding "49" in the page if vulnerable.

### Step 2: Load and Inspect

**Context**: Observe the rendered output to confirm evaluation.

**Command** (Browser Load):

Load the URL and check page source or DOM.

```bash
# Inspect for '49' in rendered search results
```

> Expected output: "49" appears in the page content, indicating successful injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/test-template-injection-math]]

## Tools Used


## Tags

- csti
- template-test
