---
data: 'Digest::SHA2.hexdigest("project_id")'
tags:
  - hashing
  - gitlab
type: command
executor: ruby
platforms:
  - Web
  - GitLab.com
id: ecd84b44-7cd1-440e-9510-9aa13d06c3f6
created_at: '2025-12-11T03:47:59.546Z'
updated_at: '2025-12-11T03:47:59.546Z'
verified: false
validated: true
submitted: true
---
# sha256-hash-project-id

## Command

```ruby
Digest::SHA2.hexdigest("project_id")
```

## Description

Computes the SHA256 hash of a GitLab project ID to determine its repository storage path.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `project_id` | Project ID as string | Yes |

## Examples

### Basic Usage

```ruby
Digest::SHA2.hexdigest("38006449")
```

### Advanced Usage

Use in a script to automate path calculation.

## Expected Output

A 64-character hexadecimal string, e.g., 'b174103b399555239923697fbe124faa61de4d441bd5c5678275eb0a5a27a562'.

## Related

- [[procedures/Calculate-GitLab-Repository-Path-from-Project-ID]]
- [[commands/git-fetch-local-path]]
