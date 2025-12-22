---
id: proc-uuid-2
tags:
  - ssrf
  - testing
  - shopify
type: procedure
tools:
  - '[[tools/pry]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/require-shopify-api]]'
  - '[[commands/setup-session-with-port]]'
  - '[[commands/create-test-session]]'
verified: false
platforms:
  - Ruby
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:18.773Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Session-Setup-with-Valid-Port

## Summary

This procedure tests the Session.setup method with a valid port value to observe how it modifies URL construction, confirming the lack of validation that enables later exploitation.

## Description

Using pry in a Ruby environment, configure the session with port '80' and an empty secret, then create a new session instance. This demonstrates the direct appending of the port to the shop domain, setting the stage for malicious injection by showing the unsanitized behavior.

## Requirements

1. Ruby with Shopify API SDK installed
2. Pry gem (gem install pry)
3. Valid shop domain for testing

## Defense

Defensive measures and detection strategies:

- Enforce port validation to numeric values only
- Log session setup configurations for anomalies
- Use allowlists for permitted ports/protocols

## Objectives

1. Verify port appending in URL construction
2. Confirm no errors on valid inputs
3. Baseline for comparing malicious setups

## Instructions

### Step 1: Require SDK

**Context**: Load the Shopify API into the Ruby session.

**Command** ([[commands/require-shopify-api]]):
```ruby
require 'shopify_api'
```

> Expected output: true.

### Step 2: Setup Session with Port

**Context**: Configure global session parameters with a valid port.

**Command** ([[commands/setup-session-with-port]]):
```ruby
ShopifyAPI::Session.setup port: '80', secret: ''
```

> Sets port to '80' and empty secret. Expected output: {:port=>"80", :secret=>""}.

### Step 3: Create Session Instance

**Context**: Instantiate a session to see URL modification.

**Command** ([[commands/create-test-session]]):
```ruby
session = ShopifyAPI::Session.new('test.myshopify.com')
```

> Creates session with appended port. Expected output: #<ShopifyAPI::Session:0x... url="test.myshopify.com:80">.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/require-shopify-api]]
- [[commands/setup-session-with-port]]
- [[commands/create-test-session]]

## Tools Used

- [[tools/pry]]

## Tags

- ssrf
- testing
- shopify
