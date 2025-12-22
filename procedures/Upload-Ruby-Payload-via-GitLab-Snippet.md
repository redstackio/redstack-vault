---
id: 57bc2224-d109-4836-9075-76e5a897f04b
name: Upload Ruby Payload via GitLab Snippet
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:13.215Z'
updated_at: '2025-12-11T06:10:13.215Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - gitlab
  - payload-upload
commands:
  - '[[commands/ruby-puts-hello]]'
  - '[[commands/ruby-echo-tmp-file]]'
  - '[[commands/git-clone-wiki-repo]]'
  - '[[commands/git-add-all]]'
  - '[[commands/git-commit-message]]'
  - '[[commands/git-push]]'
  - '[[commands/cat-tmp-vakzz]]'
  - '[[commands/ps-memory-injection]]'
  - '[[commands/ruby-echo-inject-tmp]]'
  - '[[commands/id]]'
  - '[[commands/hostname-a]]'
  - '[[commands/ps-auxww]]'
  - '[[commands/exit]]'
  - '[[commands/nc-reverse-shell]]'
platforms:
  - Web
tools:
  - '[[tools/git]]'
  - '[[tools/Kramdown]]'
  - '[[tools/Rouge]]'
  - '[[tools/Redis-rb]]'
  - '[[tools/GetProcessMem]]'
  - '[[tools/GitHub::Markup]]'
  - '[[tools/nc]]'
skill_level: beginner
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---

# Upload Ruby Payload via GitLab Snippet

## Summary

This procedure uploads a malicious Ruby payload to GitLab via a snippet, placing it in a predictable server path for later exploitation.

## Description

By creating a snippet and attaching a file, the payload is uploaded to /uploads/-/system/user/... allowing directory traversal in subsequent steps. This sets up for RCE via Kramdown rendering.

## Requirements

1. GitLab user account with snippet creation access
2. Ruby payload file ready (e.g., containing puts and echo commands)
3. Access to GitLab web interface

## Defense

Defensive measures and detection strategies:

- Monitor snippet uploads for suspicious file attachments
- Restrict wiki push access and validate rendering options

## Objectives

1. Upload payload to server
2. Obtain upload path
3. Prepare for wiki-based triggering

## Instructions

### Step 1: Create Snippet

**Context**: Create a new snippet in GitLab UI.

No specific command, use UI to create snippet with any title.

> Snippet created for file upload.

### Step 2: Attach Payload

**Context**: Attach the Ruby file to the snippet description.

The payload includes [[commands/ruby-puts-hello]] and [[commands/ruby-echo-tmp-file]]:

```ruby
puts "hello from ruby"
`echo vakzz was here > /tmp/vakzz`
```

> File uploaded to predictable path.

### Step 3: Note Path

**Context**: Record the upload path for use in .rmd file.

No command, manually note path like /uploads/-/system/user/1/.../payload.rb.

> Path recorded.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/ruby-puts-hello]]
- [[commands/ruby-echo-tmp-file]]

## Tools Used

- [[tools/git]]

## Tags

- [[gitlab]]
- [[payload-upload]]
