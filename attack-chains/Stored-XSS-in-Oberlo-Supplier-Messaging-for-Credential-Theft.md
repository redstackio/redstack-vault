---
tags:
  - xss
  - stored-xss
  - oberlo
  - shopify
  - credential-theft
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Stored-XSS-in-Oberlo-Supplier-Messaging]]'
step_count: 6
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:52:24.216Z'
description: >-
  A multi-step attack exploiting a stored XSS vulnerability in the Oberlo
  supplier messaging feature to inject malicious JavaScript payloads that
  execute when messages are viewed, enabling credential theft and session
  hijacking.
skill_level: intermediate
impact_level: high
id: a940f277-0c1f-40a9-9811-bd8045c38905
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
---

# Stored XSS in Oberlo Supplier Messaging for Credential Theft

Multi-stage attack chain demonstrating a complete attack workflow exploiting a stored XSS vulnerability in the Oberlo application's supplier messaging feature.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Navigate to Suppliers Page] --> B[Select Product]
    B --> C[Access Messaging Interface]
    C --> D[Inject Malicious Payload]
    D --> E[Send Message]
    E --> F[View Inbox to Trigger XSS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome with developer tools for payload testing)

### Target Environment

- Oberlo application (https://app.oberlo.com)
- Valid user account with access to suppliers page
- Web platform

### Initial Access Requirements

- Authenticated session in Oberlo
- No special privileges required beyond standard user access
- Direct network access to the Oberlo web application

## Detailed Attack Procedures

### Step 1: Navigate to the Suppliers Page
procedure: [[procedures/Exploit-Stored-XSS-in-Oberlo-Supplier-Messaging]]

**Objective**: Gain access to the suppliers section to begin the messaging workflow.

**Instructions**: Open a web browser and log in to the Oberlo application if not already authenticated. Directly access the suppliers page by navigating to the URL.

**Expected Output**: Suppliers page loads, displaying a list of suppliers and products.

**Success Indicators**:
- Page loads successfully at https://app.oberlo.com/suppliers
- Supplier list is visible

### Step 2: Select a Product
procedure: [[procedures/Exploit-Stored-XSS-in-Oberlo-Supplier-Messaging]]

**Objective**: Redirect to a specific product page to access associated supplier messaging options.

**Instructions**: From the suppliers page, click on any available product to view its details. This action redirects to the product-specific page.

**Expected Output**: Redirected to a product page URL like https://app.oberlo.com/suppliers/8/products/488813.

**Success Indicators**:
- Product page loads with supplier details
- URL includes supplier and product identifiers

### Step 3: Locate the Message Icon
procedure: [[procedures/Exploit-Stored-XSS-in-Oberlo-Supplier-Messaging]]

**Objective**: Identify the entry point for initiating a message to the supplier.

**Instructions**: On the product page, scan the UI for the message icon positioned next to the supplier name.

**Expected Output**: Message icon is visible in the interface near the supplier information.

**Success Indicators**:
- Icon is present and clickable
- Hovering over the icon shows messaging tooltip if applicable

### Step 4: Open the Messaging Interface
procedure: [[procedures/Exploit-Stored-XSS-in-Oberlo-Supplier-Messaging]]

**Objective**: Access the form for composing a supplier message.

**Instructions**: Click the message icon to launch the messaging form.

**Expected Output**: A form opens with fields for reason, subject, and message body.

**Success Indicators**:
- Form fields are editable
- Submit button is available

### Step 5: Inject Malicious Payload and Send
procedure: [[procedures/Exploit-Stored-XSS-in-Oberlo-Supplier-Messaging]]

**Objective**: Insert the XSS payload into the unsanitized message body and submit the message for storage.

**Instructions**: In the message body field, enter the payload `'><img src=x onerror=prompt(document.cookie)>`. Fill in the reason and subject fields with benign text (e.g., "Inquiry" and "Product Question"), then click the send button.

**Expected Output**: Message is sent successfully without errors, stored in the backend.

**Success Indicators**:
- Confirmation of message sent
- No validation errors on payload injection

### Step 6: View Inbox to Trigger XSS
procedure: [[procedures/Exploit-Stored-XSS-in-Oberlo-Supplier-Messaging]]

**Objective**: Retrieve and display the stored message to execute the injected JavaScript.

**Instructions**: Navigate to the inbox or messages section to view the sent message.

**Expected Output**: The payload executes, displaying a prompt with the document.cookie value.

**Success Indicators**:
- JavaScript alert/prompt appears with session cookies
- Potential for further exploitation like credential theft

## Attack Chain Summary

### Key Achievements

1. Successful injection of stored XSS payload in supplier messaging
2. Execution of malicious JavaScript upon message viewing
3. Potential for session hijacking, data theft, or impersonation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---

*Last updated: 2023-10-01T00:00:00Z*
