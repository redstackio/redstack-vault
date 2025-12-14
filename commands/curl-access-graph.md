---
id: cmd-curl-graph-access
data: 'curl -b cookies.txt ''https://████/graph.php?p=7'' -o response.html'
tags:
  - http-get
  - endpoint-access
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:05.812Z'
verified: false
validated: true
submitted: true
---
# curl-access-graph

## Command

```bash
curl -b cookies.txt 'https://████/graph.php?p=7' -o response.html
```

## Description

Accesses the ZendTo graph.php endpoint with authentication to test normal functionality.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-b cookies.txt` | Uses session cookies | Yes |
| `-o response.html` | Saves output to file | Yes |
| `p=7` | Benign parameter for graph load | Yes |

## Examples

### Basic Usage

```bash
curl -b cookies.txt 'https://████/graph.php?p=7' -o response.html
```

### Advanced Usage

```bash
curl -b cookies.txt 'https://████/graph.php?p=7' -o response.html -v
```

## Expected Output

RRD graph content saved to response.html without errors.

## Related

- [[Related Procedure: Access-ZendTo-Graph-Endpoint]]
