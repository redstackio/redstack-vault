---
id: cmd-uuid-1
data: >-
  RAILS_ENV=production RACK_ENV=production SECRET_KEY_BASE=foo
  RAILS_SERVE_STATIC_FILES=enabled RAILS_MAX_THREADS=2
  RAILS_LOG_TO_STDOUT=enabled rails s
tags:
  - server
  - rails
type: command
output: 'Server startup logs, listening on http://localhost:3000'
executor: bash
platforms:
  - Ruby on Rails
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.502Z'
verified: false
validated: true
submitted: true
---
# Start Rails Server in Production Mode

## Command

```bash
RAILS_ENV=production RACK_ENV=production SECRET_KEY_BASE=foo RAILS_SERVE_STATIC_FILES=enabled RAILS_MAX_THREADS=2 RAILS_LOG_TO_STDOUT=enabled rails s
```

## Description

Starts the Puma server for a Rails app in production mode, simulating a deployed environment with limited threads to exacerbate resource exhaustion during DoS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| RAILS_ENV=production | Sets Rails to production config | Yes |
| RACK_ENV=production | Sets Rack environment | Yes |
| SECRET_KEY_BASE=foo | Dummy secret key | Yes |
| RAILS_SERVE_STATIC_FILES=enabled | Enables static serving | Yes |
| RAILS_MAX_THREADS=2 | Limits to 2 threads | Yes |
| RAILS_LOG_TO_STDOUT=enabled | Logs to console | Yes |
| rails s | Starts server on port 3000 | Yes |

## Examples

### Basic Usage

```bash
RAILS_ENV=production rails s
```

### Advanced Usage

```bash
RAILS_ENV=production RACK_ENV=production SECRET_KEY_BASE=foo RAILS_MAX_THREADS=2 rails s
```

## Expected Output

Puma logs: "Listening on tcp://127.0.0.1:3000", no errors.

## Related

- [[commands/send-repeated-malformed-requests]]
