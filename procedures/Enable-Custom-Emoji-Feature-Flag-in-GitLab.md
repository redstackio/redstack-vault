---
tags:
  - gitlab
  - feature-flag
  - setup
type: procedure
tools:
  - '[[tools/gitlab-rails-console]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/enable-custom-emoji-flag]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.677Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 7c8d3104-6b29-4e93-ab7d-98250779b5c3
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Enable Custom Emoji Feature Flag in GitLab

## Summary

This procedure activates the custom emoji feature in a self-managed GitLab installation using the Rails console, enabling the vulnerable functionality for subsequent XSS injection attacks.

## Description

In GitLab self-managed setups, the custom emoji feature is controlled by a feature flag. Enabling it via the Rails console allows creation of custom emojis through the GraphQL API, where the vulnerability lies in unescaped src attributes. This step is a prerequisite for exploiting the stored XSS in the emoji_image_tag function within lib/gitlab/emoji.rb. The target environment requires administrative access to the GitLab server.

## Requirements

1. Access to the GitLab server with sudo privileges to run gitlab-rails console
2. Ruby on Rails environment (GitLab's tech stack: Ruby 2.7.2, Rails 6.0.3.6)
3. No network restrictions on local console access

## Defense

Defensive measures and detection strategies:

- Monitor Rails console access logs for unauthorized feature flag changes
- Disable custom emoji feature by default or patch the emoji_image_tag function to escape src attributes
- Use GitLab's audit logs to track feature enablement

## Objectives

1. Activate the custom emoji feature to allow payload injection
2. Prepare the environment for GraphQL-based emoji creation
3. Ensure the vulnerability is exposed without triggering alerts

## Instructions

### Step 1: Access Rails Console

**Context**: Launch the interactive Ruby console for GitLab to execute administrative commands.

**Command** ([[commands/enable-custom-emoji-flag]]):
```bash
gitlab-rails console
```

> This opens the Rails console (irb session). Expected output: GitLab environment prompt like '>> '.

### Step 2: Enable Feature Flag

**Context**: Run the Ruby code to toggle the custom emoji flag on.

**Command** ([[commands/enable-custom-emoji-flag]]):
```ruby
Feature.enable(:custom_emoji)
```

> Executes within the console. Expected output: `true` if successful, indicating the flag is enabled.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/enable-custom-emoji-flag]]

## Tools Used

- [[tools/gitlab-rails-console]]

## Tags

- gitlab
- feature-flag
