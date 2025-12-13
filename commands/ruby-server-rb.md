---
data: ruby server.rb
tags:
  - ruby
  - server
type: command
executor: bash
platforms:
  - Linux
id: 0d4574cc-6df7-4980-ba06-432c26c5b432
created_at: '2025-12-13T09:00:27.281Z'
updated_at: '2025-12-13T09:00:27.281Z'
verified: false
validated: true
submitted: true
---
# ruby-server-rb

## Command

```bash
ruby server.rb
```

## Description

Runs a Ruby script that starts a Sinatra web server hosting malicious files like robots.txt and sitemap.xml for XXE attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `ruby` | Ruby interpreter | Yes |
| `server.rb` | Script file | Yes |

## Examples

### Basic Usage

```bash
ruby server.rb
```

## Expected Output

Server startup logs, such as '== Sinatra (v3.0.0) has taken the stage on 4567 for development' and incoming request logs including exfiltrated data.

## Related

- [[commands/gem-install-sinatra]]
- [[procedures/Setup-Attacker-Server-for-XXE]]
