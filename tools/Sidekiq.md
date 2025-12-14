---
url: 'https://sidekiq.org/'
tags:
  - background-job
  - ruby
  - gitlab
type: tool
platforms:
  - Linux
description: >-
  Ruby background job processor used in GitLab for asynchronous tasks like
  import unpacking; its delay creates the race window in this attack.
id: f07c8f14-808a-4ed2-8412-cda9dfa3c48a
created_at: '2025-12-14T17:24:19.264Z'
updated_at: '2025-12-14T17:24:19.264Z'
verified: false
validated: true
submitted: true
---
# Sidekiq

**Status**: Unverified

## Overview

Sidekiq is a background job processing library for Ruby applications, commonly used in GitLab to handle asynchronous tasks such as unpacking import archives and restoring repositories. In security contexts, its processing delay after file uploads enables race conditions for file overwrites.

## Description

Sidekiq uses Redis to queue and process jobs reliably. In GitLab, after an import file upload, it enqueues a job to extract the tar.gz and apply repo data. Without immediate execution, shared files are vulnerable to concurrent modifications. Attackers exploit this by timing uploads to hijack jobs.

## Features

- Feature 1: Redis-backed queuing for high throughput.
- Feature 2: Retry mechanisms for failed jobs.
- Feature 3: Web UI for monitoring queues and workers.

## Installation

### Requirements

- Ruby 2.5+ and Bundler.
- Redis server 4.0+.

### Install Commands

```bash
# Add to Gemfile
# gem 'sidekiq'

bundle install
```

## Basic Usage

```bash
bundle exec sidekiq
```

### Common Options

| Option | Description |
|--------|-------------|
| `-e production` | Set Rails environment |
| `-C config/sidekiq.yml` | Load config file |
| `-q default` | Process specific queue |

## Examples

### Example 1: Basic Usage

```bash
bundle exec sidekiq -e development
```

### Example 2: Advanced Usage

```bash
bundle exec sidekiq -C config/sidekiq.yml -q imports,1
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Python]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor Redis connections for unusual job enqueues.
- Log worker processes and queue backlogs during high-load periods.
- Alert on jobs processing files with mismatched timestamps.

## Related Procedures



## Related Tools

- [[Redis]]
- [[Resque]]

## References

- Official documentation: https://sidekiq.org/
- GitLab integration: https://docs.gitlab.com/ee/administration/sidekiq.html
