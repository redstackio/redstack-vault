---
id: uuid-8
data: ruby InstagramBrandEnumerationExploit.rb
tags:
  - automation
  - ruby
  - enumeration
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:12.511Z'
verified: false
validated: true
submitted: true
---
# run-enumeration-ruby-script

## Command

```bash
ruby InstagramBrandEnumerationExploit.rb
```

## Description

Executes a custom Ruby script to automate sending requests to the resend-verify endpoint for bulk username enumeration from an emails.txt file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `emails.txt` | File with list of emails to test (one per line) | Yes |
| Script config | Target URL hardcoded in script | No (edit if needed) |

## Examples

### Basic Usage

Ensure emails.txt exists, then:

```bash
ruby InstagramBrandEnumerationExploit.rb
```

### Advanced Usage

Run in background or with logging:

```bash
ruby InstagramBrandEnumerationExploit.rb > output.log
```

## Expected Output

Console prints valid emails as discovered, e.g., "Valid: user@example.com". Processes ~1001 requests in 10 minutes.

## Related

- [[Related Procedure: Automated-Username-Enumeration-with-Ruby-Script]]
