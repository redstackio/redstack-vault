---
id: ac-shopify-xss-tax-override
tags:
  - xss
  - shopify
  - admin
  - tax-override
  - collection
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Malicious-Collection-for-Shopify-XSS]]'
  - '[[procedures/Assign-Malicious-Collection-to-Tax-Override]]'
  - '[[procedures/Trigger-XSS-via-Tax-Override-Deletion]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:52.848Z'
description: >-
  A cross-site scripting attack exploiting lack of sanitization in Shopify's
  myshopify.com Admin Tax Overrides feature, using a malicious collection name
  to execute JavaScript during deletion.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# XSS in Shopify Admin Tax Overrides via Unsanitized Collection Name

Multi-stage attack chain demonstrating a complete XSS workflow in Shopify's myshopify.com Admin site.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Malicious Collection] --> B[Assign to Tax Override]
    B --> C[Trigger XSS on Delete]
    C --> D[JavaScript Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser with developer tools (e.g., Chrome DevTools for payload testing)

### Target Environment

- Shopify myshopify.com Admin site
- Access to store settings (admin privileges required)
- Products or collections management enabled

### Initial Access Requirements

- Valid Shopify admin account credentials
- Network access to myshopify.com
- No prior compromise needed, but admin role is essential

## Detailed Attack Procedures

### Step 1: Create Malicious Collection
procedure: [[procedures/Create-Malicious-Collection-for-Shopify-XSS]]

**Objective**: Create a product collection with a name containing an XSS payload to inject malicious JavaScript.

**Instructions**: Log in to the Shopify admin dashboard. Navigate to Products > Collections > Create collection. In the title field, enter a payload like `<img src=x onerror=prompt(7)>`. Save the collection. This payload will be stored without sanitization.

**Expected Output**: A new collection appears in the list with the malicious name visible.

**Success Indicators**:
- Collection created successfully
- Malicious name displays without alteration in the admin UI

### Step 2: Assign Malicious Collection to Tax Override
procedure: [[procedures/Assign-Malicious-Collection-to-Tax-Override]]

**Objective**: Link the malicious collection to a 'Rest of World' tax override to set up the reflection point.

**Instructions**: Go to Settings > Taxes and duties. In the 'Tax overrides' section, select 'Add tax override for Rest of World'. Choose the collection with the payload from the dropdown. Configure any tax rate (e.g., 0%) and save the override.

**Expected Output**: The override is added, and the malicious collection name is visible in the override details (as shown in addtax.png screenshot).

**Success Indicators**:
- Override saved without errors
- Payload name reflected in the UI

### Step 3: Trigger XSS via Tax Override Deletion
procedure: [[procedures/Trigger-XSS-via-Tax-Override-Deletion]]

**Objective**: Execute the XSS payload by deleting the tax override, causing the unsanitized name to be processed.

**Instructions**: In the Taxes settings, locate the 'Rest of World' override. Click the recycle bin icon to 'Delete Entire Override'. Confirm the deletion. The payload executes due to lack of escaping in the delete confirmation.

**Expected Output**: A JavaScript prompt appears (e.g., alert with '7'), confirming execution (as shown in xss.png and delete.png screenshots).

**Success Indicators**:
- JavaScript alert/prompt triggers
- No server-side errors; payload runs in browser context

## Attack Chain Summary

### Key Achievements

1. Injected XSS payload via collection name without detection
2. Reflected payload in tax override UI
3. Achieved arbitrary JS execution in admin browser, enabling session theft or data exfil

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---

*Last updated: 2023-10-01T00:00:00Z*
