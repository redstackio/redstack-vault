---
data: 'data.gsub(/("[^ ]+":) "[^ ]+"/, ''\1 "redacted"'')'
tags:
  - redaction
  - ruby
type: command
executor: ruby
platforms:
  - Web
id: b5e85e7a-1061-4d21-9102-13b56e44a644
created_at: '2025-12-11T06:10:15.671Z'
updated_at: '2025-12-11T06:10:15.671Z'
verified: false
validated: true
submitted: true
---
# ruby-redact-pii

## Command

```ruby
data.gsub(/("[^ ]+":) "[^ ]+"/, '\1 "redacted"')
```

## Description

This Ruby command redacts sensitive information in data strings by replacing quoted values in key-value pairs with 'redacted'. It is used by HackerOne staff to sanitize PII in report comments before disclosure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `gsub` | Ruby method for string substitution | Yes |
| `/("[^ ]+":) "[^ ]+"/` | Regex pattern to match key-value pairs | Yes |
| `'\1 "redacted"'` | Replacement string keeping the key and replacing value | Yes |

## Examples

### Basic Usage

```ruby
data = '{"email": "user@example.com"}'
data.gsub(/("[^ ]+":) "[^ ]+"/, '\1 "redacted"')
```

### Advanced Usage

Apply to larger JSON structures for batch redaction.

## Expected Output

Data with all quoted values replaced by 'redacted', e.g., '{"email": "redacted"}'.

## Related

- [[procedures/Create-Dummy-Report-on-HackerOne]]
