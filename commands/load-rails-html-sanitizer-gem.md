---
id: cmd-load-rails-sanitizer
data: require 'rails-html-sanitizer'
tags:
  - setup
  - gem
type: command
output: 'false'
executor: ruby
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:25.752Z'
verified: false
validated: true
submitted: true
---
# load-rails-html-sanitizer-gem

## Command

```ruby
require 'rails-html-sanitizer'
```

## Description

Loads the rails-html-sanitizer gem into the current Ruby session, making classes like SafeListSanitizer available for testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | No parameters; standard require | Yes |

## Examples

### Basic Usage

```ruby
require 'rails-html-sanitizer'
```

### Advanced Usage

Typically used at start of IRB session; no advanced options.

## Expected Output

false (indicating the gem was already loaded or successfully required without output).

## Related

- [[commands/test-svg-style-xss-payload]]
- [[procedures/Verify-XSS-in-Rails-Sanitizer-Using-IRB]]
