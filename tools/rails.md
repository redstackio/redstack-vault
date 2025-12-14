---
id: tool-rails
url: 'https://rubyonrails.org/'
tags:
  - framework
  - web
type: tool
verified: false
platforms:
  - Web
  - Ruby on Rails
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:25.693Z'
validated: true
submitted: true
---
# Rails

**Status**: Unverified

## Overview

Ruby on Rails is a web application framework for building the sample vulnerable app to demonstrate the XSS issue in its html-sanitizer integration.

## Description

Rails handles MVC patterns, routing, and views with ERB templating. It integrates gems like rails-html-sanitizer for secure output. In testing, it's used to create endpoints that misuse sanitization for exploit reproduction.

## Features

- Feature 1: Convention over configuration
- Feature 2: Generators for scaffolding
- Feature 3: Built-in asset pipeline

## Installation

### Requirements

- Ruby 3.1.2

### Install Commands

```bash
gem install rails
rails new myapp
```

## Basic Usage

```bash
rails server
```

### Common Options

| Option | Description |
|--------|-------------|
| generate | Create code |
| assets:precompile | Build assets |

## Examples

### Example 1: Basic Usage

```bash
rails generate controller Poc index
rails server
```

### Example 2: Advanced Usage

With Docker integration.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Ports: 3000
- Logs: rails.log

## Related Procedures

- [[procedures/Build-Sample-Vulnerable-Rails-Application-with-Docker]]

## Related Tools

- [[tools/Ruby]]

## References

- Rails guides
