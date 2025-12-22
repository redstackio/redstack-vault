---
data: puts URI.unescape(request.query_string)
tags:
  - ruby
  - exfiltration
type: command
executor: ruby
platforms:
  - Linux
id: 3a49edf6-530c-4fc0-8876-917026caeaf2
created_at: '2025-12-13T09:00:27.279Z'
updated_at: '2025-12-13T09:00:27.279Z'
verified: false
validated: true
submitted: true
---
# puts-uri-unescape

## Command

```ruby
puts URI.unescape(request.query_string)
```

## Description

In a Sinatra route, this prints the unescaped query string from an HTTP request, used to display multi-line exfiltrated data in XXE attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `puts` | Output to console | Yes |
| `URI.unescape` | Decodes URL-encoded string | Yes |
| `request.query_string` | Query parameters from HTTP request | Yes |

## Examples

### Basic Usage

```ruby
get '/pingback' do
  puts URI.unescape(request.query_string)
end
```

## Expected Output

Unescaped file contents or directory listings, e.g., the full contents of /etc/passwd.

## Related

- [[commands/ruby-server-rb]]
- [[procedures/Update-Payload-for-Multi-Line-Exfiltration]]
