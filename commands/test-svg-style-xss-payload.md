---
id: cmd-test-svg-xss
data: >-
  Rails::Html::SafeListSanitizer.new.sanitize("<svg><style><script>alert(1)</script></style></svg>",
  tags: ["svg", "style"]).to_s
tags:
  - xss
  - test
type: command
output: '"<svg><style><script>alert(1)</script></style></svg>"'
executor: ruby
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:25.749Z'
verified: false
validated: true
submitted: true
---
# test-svg-style-xss-payload

## Command

```ruby
Rails::Html::SafeListSanitizer.new.sanitize("<svg><style><script>alert(1)</script></style></svg>", tags: ["svg", "style"]).to_s
```

## Description

Tests the sanitizer with an SVG+style payload containing a script tag; vulnerable versions fail to strip it.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| tags | Array of allowed tags, e.g., ["svg", "style"] | Yes |
| input | HTML string with payload | Yes |
| to_s | Converts SafeBuffer to string | No |

## Examples

### Basic Usage

```ruby
Rails::Html::SafeListSanitizer.new.sanitize("<svg><style><script>alert(1)</script></style></svg>", tags: ["svg", "style"]).to_s
```

### Advanced Usage

Vary payloads for different alerts.

## Expected Output

"<svg><style><script>alert(1)</script></style></svg>" (unsanitized if vulnerable).

## Related

- [[commands/test-math-style-xss-payload]]
- [[procedures/Verify-XSS-in-Rails-Sanitizer-Using-IRB]]
