---
id: uuid-curl-get
data: 'curl "http://target-ip:port/solr/select?q=*:*&wt=json"'
tags:
  - http
  - query
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.313Z'
verified: false
validated: true
submitted: true
---
# curl-get-request

## Command

```bash
curl "http://target-ip:port/solr/select?q=*:*&wt=json"
```

## Description

Sends a GET request to query the Solr instance, retrieving JSON data to assess access and content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Solr endpoint with query params | Yes |
| q=*:* | Wildcard search | No |
| wt=json | JSON output format | No |

## Examples

### Basic Usage

```bash
curl "http://target:port/solr/select?q=*:*&wt=json"
```

### Advanced Usage

```bash
curl -v "http://target:port/solr/select?q=term&wt=xml"  # Verbose with XML
```

## Expected Output

{"response":{"numFound":100,"docs":[{"id":"doc1","title":"Military Unit Info"}]}}

## Related

- [[commands/curl-post-request]]
- [[procedures/Query-Exposed-Solr-Instance]]
