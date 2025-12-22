---
url: 'https://docs.gitlab.com/ee/ci/'
tags:
  - ci-cd
  - gitlab
  - automation
type: tool
platforms:
  - Web
  - Linux
description: >-
  GitLab's built-in continuous integration and deployment system for automating
  builds, tests, and artifact generation.
id: 55bd17e7-3302-4199-81de-b3e1f4f4c981
created_at: '2025-12-13T23:52:43.633Z'
updated_at: '2025-12-13T23:52:43.633Z'
verified: false
validated: true
submitted: true
---
# GitLab-CI-CD

**Status**: Unverified

## Overview

GitLab CI/CD is an integrated tool for defining pipelines in .gitlab-ci.yml files, enabling automated job execution including artifact creation, which can be abused to host files with specific MIME types for attacks like XSS payload delivery.

## Description

It runs jobs in Docker or shell environments, produces artifacts downloadable via unique URLs, and supports MIME type inference based on file extension. In security testing, it's used to bypass upload restrictions by generating files dynamically.

## Features

- Feature 1: YAML-based pipeline definition for jobs and artifacts
- Feature 2: Automatic MIME type serving for artifacts (e.g., .js as application/javascript)
- Feature 3: Expiration and access controls for artifacts

## Installation

### Requirements

- GitLab account and project
- No local install needed; uses GitLab runners

### Install Commands

```bash
# No installation; configure via .gitlab-ci.yml in repo
```

## Basic Usage

```bash
gitlab-ci --help  # Not applicable; use GitLab UI
```

### Common Options

| Option | Description |
|--------|-------------|
| artifacts: paths | List files to artifact
| expire_in | Set artifact TTL

## Examples

### Example 1: Basic Usage

Create .gitlab-ci.yml as shown in procedures to generate JS artifact.

### Example 2: Advanced Usage

```yaml
job:
  script: echo 'payload' > file.js
  artifacts:
    paths: [file.js]
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor CI/CD logs for echo to JS files
- Scan artifact URLs for malicious content

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Git]]
- [[Docker]]

## References

- Official documentation: https://docs.gitlab.com/ee/ci/
