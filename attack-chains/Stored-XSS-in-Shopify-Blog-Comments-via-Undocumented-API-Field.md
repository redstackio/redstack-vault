---
tags:
  - xss
  - stored-xss
  - shopify
  - api
  - javascript
type: attack_chain
tools:
  - '[[tools/Web-Browser]]'
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Inject-Malicious-Payload-into-Shopify-Blog-Comment-via-API]]'
step_count: 5
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:32:29.355Z'
description: >-
  A multi-step attack exploiting a stored XSS vulnerability in Shopify's blog
  comments by injecting unsanitized HTML/JS through the undocumented 'body_html'
  field in the API, leading to arbitrary JavaScript execution in the storefront
  and admin panel.
skill_level: intermediate
impact_level: high
id: aeb75859-af49-402f-9c85-cf1f11885fd8
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored XSS in Shopify Blog Comments via Undocumented API Field

Multi-stage attack chain demonstrating exploitation of a stored XSS vulnerability in Shopify's blog comment system by bypassing web sanitization through the API's undocumented 'body_html' field, enabling arbitrary JavaScript execution when victims view the blog post or admins check comments.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Post Comment via Web] --> B[Extract Comment ID]
    B --> C[Setup Shopify App]
    C --> D[Update Comment via API]
    D --> E[Trigger XSS Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#f39c12
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Web-Browser]]
- [[tools/Browser-Developer-Tools]]

### Target Environment

- Shopify-hosted online store with blog enabled
- Access to Shopify admin for app creation (requires store owner permissions)
- Network access to the storefront and admin API

### Initial Access Requirements

- Ability to post comments on the blog (public access)
- Shopify partner account or store admin credentials to create apps with comment read/write scopes
- API access token for the app

## Detailed Attack Procedures

### Step 1: Post Initial Comment
procedure: [[procedures/Inject-Malicious-Payload-into-Shopify-Blog-Comment-via-API]]

**Objective**: Create a legitimate comment on a blog post to obtain a comment ID for later modification, noting that web-submitted content is sanitized.

**Instructions**: Navigate to a blog post on the target Shopify storefront and submit a benign comment via the web form.

**Expected Output**: Comment appears on the page, sanitized of any HTML/JS.

**Success Indicators**:
- Comment successfully posted and visible on the blog
- No errors in submission

### Step 2: Extract Comment ID
procedure: [[procedures/Inject-Malicious-Payload-into-Shopify-Blog-Comment-via-API]]

**Objective**: Inspect the page source to retrieve the unique ID of the posted comment for targeting in the API update.

**Instructions**: Use [[tools/Browser-Developer-Tools]] to inspect the HTML element of the comment, looking for an ID attribute like <div id="comment-2929551246">

**Expected Output**: Comment ID extracted, e.g., 2929551246.

**Success Indicators**:
- Valid numeric ID obtained from the DOM
- ID matches the posted comment

### Step 3: Setup Shopify App with Permissions
procedure: [[procedures/Inject-Malicious-Payload-into-Shopify-Blog-Comment-via-API]]

**Objective**: Create a custom Shopify app with read/write access to comments to enable API modifications.

**Instructions**: In the Shopify admin, create a new app, grant scopes for comments (read_comments, write_comments), install the app, and obtain an API access token.

**Expected Output**: App installed with valid API token for authentication.

**Success Indicators**:
- App creation successful without errors
- API token generated and testable

### Step 4: Update Comment via API
procedure: [[procedures/Inject-Malicious-Payload-into-Shopify-Blog-Comment-via-API]]

**Objective**: Send a PUT request to the comments API endpoint, injecting unsanitized HTML/JS into the undocumented 'body_html' field to bypass sanitization.

**Instructions**: Authenticate with the API token and execute [[commands/shopify-update-comment-api]] to modify the comment. Send the request twice if needed to ensure persistence.

```bash
curl -X PUT "https://your-shop.myshopify.com/admin/comments/<comment-id>.json" \
  -H "X-Shopify-Access-Token: your-api-token" \
  -H "Content-Type: application/json" \
  -d '{"comment": {"id": <comment-id>, "body": "blahblah", "body_html": "blah<img src=x onerror=alert(0);>"}}'
```

**Expected Output**: HTTP 200 response with updated comment details; no sanitization applied to body_html.

**Success Indicators**:
- Response confirms update ("comment" object returned)
- No validation errors on body_html

### Step 5: Trigger and Observe XSS Execution
procedure: [[procedures/Inject-Malicious-Payload-into-Shopify-Blog-Comment-via-API]]

**Objective**: Load the blog post or view comments in admin to execute the injected JavaScript, demonstrating arbitrary code execution.

**Instructions**: Visit the blog post URL in a browser or navigate to the comments section in Shopify admin.

**Expected Output**: Alert box or other JS effects trigger on page load.

**Success Indicators**:
- JavaScript executes (e.g., alert(0) pops up)
- Execution occurs in both storefront and admin contexts

## Attack Chain Summary

### Key Achievements

1. Bypassed web sanitization by leveraging the API's undocumented field
2. Achieved stored XSS affecting both end-users and admins
3. Demonstrated potential for session hijacking or data theft via JS

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
