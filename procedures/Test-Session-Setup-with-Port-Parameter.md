---
id: proc-test-port-001
tags:
  - testing
  - shopify
  - input-validation
type: procedure
tools:
  - '[[tools/pry]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/load-shopify-api-gem]]'
  - '[[commands/setup-session-benign-port]]'
  - '[[commands/create-session-instance]]'
verified: false
platforms:
  - Ruby
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:28.687Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Test-Session-Setup-with-Port-Parameter

## Summary

This procedure tests the benign behavior of the Session.setup method with a valid port parameter to observe URL construction, confirming lack of validation before proceeding to exploitation.

## Description

Using pry in a Ruby REPL, load the Shopify API SDK and configure a session with a simple port like '80'. Initialize a session object and inspect the resulting URL, which demonstrates direct appending without sanitization. This sets the stage for malicious injections in real scenarios where parameters derive from untrusted input.

## Requirements

1. Installed shopify_api gem
2. Pry REPL environment
3. No network access needed for this test

## Defense

Defensive measures and detection strategies:

- Enforce type checking (integer for port) in application code wrapping SDK usage
- Log all Session.setup calls with parameter values for anomaly detection
- Avoid deriving setup params from user input

## Objectives

1. Verify port appending mechanism
2. Confirm no immediate validation failures
3. Baseline for exploitation comparison

## Instructions

### Step 1: Load the SDK

**Context**: Prepare the environment by requiring the gem.

**Command** ([[commands/load-shopify-api-gem]]):
```ruby
require 'shopify_api'
```

> Loads the gem; expected output: true.

### Step 2: Setup Session with Benign Port

**Context**: Configure global session params with port '80' and empty secret.

**Command** ([[commands/setup-session-benign-port]]):
```ruby
ShopifyAPI::Session.setup port: '80', secret: ''
```

> Sets configuration; expected output: {:port=>"80", :secret=>""}.

### Step 3: Create Session Instance

**Context**: Initialize session and inspect URL.

**Command** ([[commands/create-session-instance]]):
```ruby
session = ShopifyAPI::Session.new('test.myshopify.com')
puts session.url
```

> Creates session; expected output: #<ShopifyAPI::Session:... url="test.myshopify.com:80">.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/load-shopify-api-gem]]
- [[commands/setup-session-benign-port]]
- [[commands/create-session-instance]]

## Tools Used

- [[tools/pry]]

## Tags

- testing
- shopify
- input-validation

---
