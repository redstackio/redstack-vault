---
url: 'https://github.com/carrierwaveuploader/carrierwave'
tags:
  - file-upload
  - ssrf
type: tool
platforms:
  - Linux
  - Web
description: >-
  File uploader library used in GitLab for handling attachments, vulnerable to
  SSRF via remote URLs.
id: f09d599d-7646-4561-9222-3b6d08de12d8
created_at: '2025-12-11T03:47:39.462Z'
updated_at: '2025-12-11T03:47:39.462Z'
verified: false
validated: true
submitted: true
---
# CarrierWave

**Status**: Unverified

## Overview

CarrierWave is a Ruby library for file uploads, used in GitLab's Note model to handle remote attachments, which can be exploited for SSRF by specifying arbitrary URLs.

## Description

It processes file downloads from URLs without sufficient validation in certain contexts, enabling attacks like fetching internal resources during GitLab project imports.

## Features

- Remote file downloading: Allows specifying URLs for attachments.
- Integration with Rails: Used in web applications for upload handling.
- Storage options: Supports various backends like local or cloud storage.

## Installation

### Requirements

- Ruby 2.6.5 or compatible.
- Rails framework.

### Install Commands

```bash
gem install carrierwave
```

## Basic Usage

```bash
# In Ruby code
uploader = AvatarUploader.new
```

### Common Options

| Option | Description |
|--------|-------------|
| `remote_attachment_url` | URL to download file from |
| `store_dir` | Directory for stored files |

## Examples

### Example 1: Basic Usage

```ruby
note.remote_attachment_url = 'http://example.com/file'
note.save
```

### Example 2: Advanced Usage

```ruby
uploader.download! 'http://internal.service/metrics'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Remote File Copy]]

### Tactics

- [[Initial Access]]
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for unexpected URL fetches to internal IPs.
- Log CarrierWave download attempts in application logs.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/GitLab]]

## References

- https://github.com/carrierwaveuploader/carrierwave
