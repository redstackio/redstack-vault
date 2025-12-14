---
id: proc-uuid-1
tags:
  - code-review
  - rails
  - activestorage
type: procedure
tools:
  - '[[tools/aws-sdk-s3]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T05:32:10.053Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Review-ActiveStorage-S3-Service-Code

## Summary

This procedure involves static code analysis of Ruby on Rails ActiveStorage's S3 service to identify the vulnerability where presigned URLs do not enforce content-length headers, enabling file size bypasses.

## Description

In a Rails application using ActiveStorage for direct S3 uploads, the s3_service.rb file generates presigned URLs via the aws-sdk-s3 gem. The gem blacklists 'content-length' in presigner.rb, and Rails does not whitelist it, allowing clients to upload larger files than specified. This review confirms the root cause through code inspection, typically done via git clone or decompiling the app.

## Requirements

1. Access to Rails source code or deployed app binaries
2. Ruby environment for local testing
3. Knowledge of AWS SDK and Rails internals

## Defense

Defensive measures and detection strategies:

- Implement code reviews for third-party gem integrations
- Use S3 bucket policies to enforce max object sizes
- Monitor S3 PUT requests for anomalous sizes via CloudTrail

## Objectives

1. Confirm absence of whitelist_headers in presigned_url call
2. Understand impact on direct upload flow
3. Identify fix: add whitelist_headers: ['content-length']

## Instructions

### Step 1: Locate and Examine s3_service.rb

**Context**: Find the url_for_direct_upload method to check presigned_url parameters.

No command needed; use text editor to view:

```ruby
def url_for_direct_upload(key, expires_in:, content_type:, content_length:, checksum:)
  instrument :url, key: key do |payload|
    generated_url = object_for(key).presigned_url :put, expires_in: expires_in.to_i,
                                              content_type: content_type,
                                              content_length: content_length,
                                              content_md5: checksum
    payload[:url] = generated_url
    generated_url
  end
end
```

> This code lacks whitelist_headers, confirming vulnerability.

### Step 2: Cross-Reference aws-sdk-s3 Presigner

**Context**: Verify header blacklisting in the gem's source.

Clone and inspect:

```bash
git clone https://github.com/aws/aws-sdk-ruby.git
grep -r "blacklist" gems/aws-sdk-s3/lib/aws-sdk-s3/presigner.rb
```

> Expected: Line ~22 shows 'content-length' in blacklisted_headers array.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/aws-sdk-s3]]

## Tags

- code-review
- rails
