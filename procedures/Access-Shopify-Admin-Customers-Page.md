---
tags:
  - shopify
  - admin
  - customers
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.540Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 31526815-9ae0-4e4a-80ba-12d5b543f822
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Access Shopify Admin Customers Page

## Summary

This procedure navigates to the customers management section in the Shopify admin panel, serving as the entry point for accessing customer data and communications in preparation for exploiting stored vulnerabilities like XSS.

## Description

In the context of a stored XSS attack on Shopify's admin, this step establishes access to the customers feature. It requires a staff account and targets the admin panel at a URL like https://store.myshopify.com/admin/customers. The procedure assumes prior login and focuses on reaching the list of customers where targeted profiles can be selected. Expected outcomes include visibility into customer records, enabling subsequent steps in the attack chain.

## Requirements

1. Valid staff credentials with 'Customers' permission enabled
2. Direct network access to the Shopify admin panel (no VPN or proxy restrictions)
3. Modern web browser (e.g., Chrome, Firefox) for navigation

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls (RBAC) to limit staff permissions
- Monitor admin panel logins for anomalous IP addresses or times
- Use web application firewalls (WAF) to detect unusual navigation patterns

## Objectives

1. Gain visibility into customer list for targeting
2. Confirm access to admin features without errors
3. Set up for deeper profile inspection

## Instructions

### Step 1: Log In and Navigate

**Context**: Authenticate and reach the customers endpoint to load the management interface.

Log in to the Shopify admin panel at https://store.myshopify.com/admin using staff credentials. From the dashboard, select 'Customers' from the left sidebar or directly enter the URL https://store.myshopify.com/admin/customers in the browser address bar.

> This loads the customers page, displaying a searchable list of all customer accounts.

### Step 2: Verify Access

**Context**: Ensure the page is fully loaded and permissions are active.

Scan the page for the customer list table. If permissions are insufficient, an error will appear; otherwise, proceed to search or browse for the target customer.

> Successful load confirms access; look for elements like search bar and pagination.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[admin]]
- [[customers]]
