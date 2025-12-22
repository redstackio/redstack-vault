---
id: tool-letter-opener
url: 'https://github.com/ryanb/letter_opener'
tags:
  - email-testing
  - rails
  - xss
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:20.762Z'
validated: true
submitted: true
---
# Letter-Opener

**Status**: Unverified

## Overview

Letter Opener is a Ruby on Rails gem that intercepts outgoing emails in development environments and displays them in the browser, ideal for testing XSS in email templates without sending real messages.

## Description

Integrated into GDK for GitLab, it captures emails like MR notifications and renders them at `/rails/letter_opener/`. Crucial for verifying unsanitized HTML/JS in bodies, such as branch names triggering alerts.

## Features

- Feature 1: Browser-based email viewing.
- Feature 2: HTML rendering to test client-side execution.
- Feature 3: No actual SMTP sending in dev.

## Installation

### Requirements

- Rails app (included in GDK).

### Install Commands

```bash
# In Gemfile
gem 'letter_opener'
bundle install
```

## Basic Usage

```bash
# Access after triggering email
# http://localhost:3000/rails/letter_opener
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Config via initializer |

## Examples

### Example 1: Basic Usage

```bash
# Trigger email in app, then visit endpoint
```

### Example 2: Advanced Usage

Customize in `config/initializers/letter_opener.rb` for paths.

## Expected Output

List of emails; clicking shows rendered HTML with potential JS execution.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]] JavaScript

### Tactics

- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- `/rails/letter_opener` endpoint access.
- Dev-only gem in production (alert).

## Related Procedures


## Related Tools

- [[tools/GDK-GitLab-Development-Kit]]

## References

- GitHub: https://github.com/ryanb/letter_opener
- Rails integration docs
