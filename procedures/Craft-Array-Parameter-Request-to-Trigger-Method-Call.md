---
tags:
  - rails
  - array-injection
  - method-invocation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-array-probe]]'
verified: false
platforms:
  - Web
  - Ruby on Rails
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:27.486Z'
sub_techniques: []
id: 470bf240-e204-4884-b15d-de09ff940eb3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Array-Parameter-Request-to-Trigger-Method-Call

## Summary

This procedure crafts HTTP requests with array-form parameters (e.g., ?user_input[]=something) to exploit Rails' redirect_to helper, causing the application to invoke a method named something_url and redirect to its value or error out.

## Description

The vulnerability arises when user input is passed unsanitized to redirect helpers, interpreting array inputs as method calls on URL helpers. Targets are Rails apps with such patterns on public routes. Prerequisites: Identified vulnerable endpoint from prior recon. Outcomes: Trigger method execution or errors revealing internal structure.

## Requirements

1. Vulnerable endpoint URL
2. HTTP client for parameter manipulation
3. Knowledge of potential _url method names to probe

## Defense

Defensive measures and detection strategies:

- Sanitize inputs with .to_s or allowlists (e.g., private def check(param); case param; when "valid"; "/"; else; "/"; end; end)
- Avoid dynamic method calls in redirects; use explicit paths
- Log and alert on array parameters in redirect contexts
- Patch Rails to versions fixing this (post-2019 CVE)

## Objectives

1. Inject array parameter to invoke dynamic _url method
2. Achieve unintended redirect or error
3. Set up for response analysis

## Instructions

### Step 1: Prepare Array Parameter

**Context**: Format the parameter as an array to trigger Rails' polymorphic behavior leading to method call.

**Command** ([[commands/curl-array-probe]]):
```bash
curl -v -X GET "http://target.com/vulnerable?user_input[]=test_url" -o response.html
```

> This sets params[:user_input] = ["test_url"], attempting to call test_url method. Expect 302 if exists, 500 if not.

### Step 2: Test with Known Method

**Context**: Use a guessed internal method name to verify exploitation.

**Command** ([[commands/curl-array-probe]]):
```bash
curl -v -X GET "http://target.com/vulnerable?user_input[]=admin_url" -o response.html
```

> If admin_url exists, redirects to admin path; otherwise, errors with method missing details.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-array-probe]]

## Tools Used


## Tags

- rails
- exploit
- parameter-injection
