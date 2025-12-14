---
data: >-
  curl -X POST https://beerify.shopifycloud.com/graphql -H "Content-Type:
  application/json" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64;
  rv:62.0) Gecko/20100101 Firefox/62.0" -d '{"query": "query
  location{location(code:\"OTT150, 8th
  Floor\"){taps{edges{node{percentRemaining, beer{brewery, ibu, style,
  tastingNotes, beerLogo, abv}}}}}}"}'
tags:
  - graphql
  - collection
type: command
executor: bash
platforms:
  - Linux
  - Web
id: dddef78c-0dac-4c9c-91f8-4cc2c297b175
created_at: '2025-12-14T17:25:59.598Z'
updated_at: '2025-12-14T17:25:59.598Z'
verified: false
validated: true
submitted: true
---
# graphql-query-beer-details

## Command

```bash
curl -X POST https://beerify.shopifycloud.com/graphql -H "Content-Type: application/json" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0" -d '{"query": "query location{location(code:\"OTT150, 8th Floor\"){taps{edges{node{percentRemaining, beer{brewery, ibu, style, tastingNotes, beerLogo, abv}}}}}}"}'
```

## Description

This command queries GraphQL for beer tap details at a specific location, revealing consumption data like percentages and tasting notes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-H "Content-Type: application/json"` | JSON header | Yes |
| `-d` | Payload with code | Yes |
| `code` | Escaped location code | Yes |
| `query` | Full GraphQL string | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://beerify.shopifycloud.com/graphql -H "Content-Type: application/json" -d '{"query": "query location{location(code:\"OTT150, 8th Floor\"){taps{edges{node{percentRemaining, beer{brewery, ibu, style, tastingNotes, beerLogo, abv}}}}}}"}'
```

### Advanced Usage

```bash
curl -X POST https://beerify.shopifycloud.com/graphql -H "Content-Type: application/json" -H "Accept: application/json" -d '{"query": "..."}'
```

## Expected Output

JSON with taps: {"data":{"location":{"taps":{"edges":[{"node":{"percentRemaining":89,"beer":{"brewery":"Beau's Brewing Co","ibu":30,"style":"American-style Brown Ale","tastingNotes":"...","beerLogo":"","abv":5.6}}}]}}}}.

## Related

- [[Related Procedure]]
