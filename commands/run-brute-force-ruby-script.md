---
id: uuid-9
data: ruby InstagramBrandLoginBruteForce.rb
tags:
  - brute-force
  - ruby
  - automation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:12.507Z'
verified: false
validated: true
submitted: true
---
# run-brute-force-ruby-script

## Command

```bash
ruby InstagramBrandLoginBruteForce.rb
```

## Description

Runs a custom Ruby script to perform brute-force login attempts on the target endpoint using a password list and specified email.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `passlist.txt` | File with passwords to try (one per line) | Yes |
| Line 7 in script | Target email to use for attempts | Yes (edit script) |

## Examples

### Basic Usage

With passlist.txt ready and email set:

```bash
ruby InstagramBrandLoginBruteForce.rb
```

### Advanced Usage

Multi-thread if modified:

```bash
ruby InstagramBrandLoginBruteForce.rb --threads 4
```
(Note: Base script is single-threaded.)

## Expected Output

Logs each attempt, e.g., "Trying password123... Failed". On success: "Login successful with passwordXYZ". ~1020 attempts in 10 minutes.

## Related

- [[Related Procedure: Automated-Brute-Force-Login-with-Ruby-Script]]
