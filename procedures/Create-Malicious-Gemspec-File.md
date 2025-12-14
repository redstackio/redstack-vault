---
id: proc-uuid-1
tags:
  - xss
  - gemspec
  - payload-injection
type: procedure
tools:
  - '[[tools/gem]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Ruby
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.040Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Gemspec-File

## Summary

This procedure crafts a RubyGems specification (Gemspec) file with a malicious JavaScript URL injected into the homepage field, enabling stored XSS when the gem is served via the gem server UI.

## Description

In the context of exploiting the RubyGems gem server, create a Gemspec file for a dummy gem named 'securitytest'. Set the homepage attribute to a javascript: scheme URL, such as 'javascript:confirm(document.domain)', which will be rendered as a clickable WWW link in the server UI. When clicked, it executes the JavaScript in the viewer's browser. This stores the payload in the gem metadata, persisting across installations and views. Prerequisites include a Ruby environment; no tools beyond a text editor are needed initially.

## Requirements

1. RubyGems installed on the system
2. Text editor (e.g., vim, nano) for file creation
3. Basic knowledge of RubyGems metadata structure

## Defense

Defensive measures and detection strategies:

- Validate all URI schemes in Gemspec files during gem building or installation, rejecting javascript: protocols
- Sanitize hyperlinks in the gem server UI by stripping or escaping javascript: schemes
- Monitor for unusual Gemspec modifications or installations from untrusted sources

## Objectives

1. Inject arbitrary JavaScript payload into gem metadata
2. Ensure the payload is stored and retrievable via the gem server
3. Prepare for packaging into an installable gem

## Instructions

### Step 1: Initialize Gemspec Structure

**Context**: Start with a basic Gemspec template to define the gem's metadata.

Create the file 'securitytest.gemspec' with standard fields like name, version, and authors, then set the malicious homepage.

No command needed; use a text editor:

```ruby
Gem::Specification.new do |s|
  s.name = 'securitytest'
  s.version = '0.1.0'
  s.summary = 'Security Test Gem'
  s.description = 'A test gem for security demonstration'
  s.authors = ['Attacker']
  s.homepage = 'javascript:confirm(document.domain)'
  s.files = ['securitytest.rb']
end
```

> This creates the Gemspec with the injected payload. Expected output: Valid Ruby syntax, no errors when parsed.

### Step 2: Add Dummy Gem File

**Context**: Include a minimal Ruby file to make the gem buildable.

Create 'securitytest.rb' with empty content:

```ruby
# Empty file for gem structure
```

> Ensures the gem has files to package. Expected output: File exists in the directory.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/gem]]

## Tags

- xss
- gemspec
- payload-injection
