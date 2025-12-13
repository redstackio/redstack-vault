---
data: |-
  #!/usr/bin/env ruby
  require 'webrick'
  server = WEBrick::HTTPServer.new(:Port => 8080)
  server.mount_proc '/' do |req, res|
    res.body = 'hello world'
  end
  server.mount_proc '/flag' do |req, res|
    res.body = 'flag is 123456'
  end
  server.start
tags:
  - ruby
  - webrick
  - server
type: command
executor: ruby
platforms:
  - Web
id: 2173c524-786c-4e67-82a2-d45c5974ff86
created_at: '2025-12-13T09:01:22.208Z'
updated_at: '2025-12-13T09:01:22.208Z'
verified: false
validated: true
submitted: true
---
# WEBrick Server Setup

## Command

```ruby
#!/usr/bin/env ruby
require 'webrick'
server = WEBrick::HTTPServer.new(:Port => 8080)
server.mount_proc '/' do |req, res|
  res.body = 'hello world'
end
server.mount_proc '/flag' do |req, res|
  res.body = 'flag is 123456'
end
server.start
```

## Description

Runs a WEBrick HTTP server with two endpoints: '/' and '/flag', used to set up the backend for demonstrating vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `:Port` | Port to listen on (e.g., 8080) | Yes |
| `mount_proc` | Defines endpoint handlers | Yes |

## Examples

### Basic Usage

```ruby
#!/usr/bin/env ruby
require 'webrick'
server = WEBrick::HTTPServer.new(:Port => 8080)
server.mount_proc '/' do |req, res|
  res.body = 'hello world'
end
server.start
```

### Advanced Usage

Add more endpoints as needed.

## Expected Output

Starts an HTTP server listening on port 8080, responding to requests.

## Related

- [[procedures/Set-Up-Vulnerable-WEBrick-Server]]
- [[tools/WEBrick]]
