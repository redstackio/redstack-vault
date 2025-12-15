---
data: RUBYGEMS_PROXY=true rackup
tags:
  - server-start
  - proxy
type: command
output: >-
  Puma starting in single mode... * Puma version: 5.2.2 (ruby 2.7.1-p83) ... *
  Listening on http://127.0.0.1:9292 * Listening on [::1]:9292
executor: bash
platforms:
  - Ruby
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.218Z'
id: d9599f5c-449d-4b30-95e9-ea9f96cd1b9c
verified: false
validated: true
submitted: true
---
# start-evil-gem-server

## Command

```bash
RUBYGEMS_PROXY=true rackup
```

## Description

Launches a Rack-based Puma server for the modified Geminabox application with RubyGems proxy enabled, serving the malicious payload on /api/v1/dependencies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| RUBYGEMS_PROXY=true | Enables proxy mode for RubyGems compatibility | Yes |
| rackup | Starts the Rack app | Yes |

## Examples

### Basic Usage

```bash
RUBYGEMS_PROXY=true rackup
```

### Advanced Usage

Run in background: `RUBYGEMS_PROXY=true rackup -D`.

## Expected Output

Server startup logs indicating listening on port 9292.

## Related

- [[commands/ruby-create-rce-payload]]
- [[procedures/Set-Up-Malicious-Gem-Server-to-Serve-Deserialization-Payload]]
