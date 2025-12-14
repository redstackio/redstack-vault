---
data: >-
  https://vulnstore.myshopify.com/admin/oauth/authorize?scope=read_customers&client_id=cad94488c733b0f377a9a1d7952db802
tags:
  - oauth
  - shopify
type: command
output: >-
  Permission dialog appears; after install, no redirect due to malformed
  callback
executor: browser
platforms:
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:45.009Z'
id: 9c214a23-9793-408a-8a60-40a55b132329
verified: false
validated: true
submitted: true
---
# shopify-oauth-authorize

## Command

Visit the URL in a web browser: https://vulnstore.myshopify.com/admin/oauth/authorize?scope=read_customers&client_id=cad94488c733b0f377a9a1d7952db802

## Description

This command initiates the OAuth authorization flow for installing a Shopify app on a target store, using specified scope and client_id. It triggers the permission dialog and installation, but with a malformed callback, it fails to redirect post-install.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| scope | Permissions requested (e.g., read_customers) | Yes |
| client_id | App's unique identifier | Yes |
| store | Target store subdomain (e.g., vulnstore.myshopify.com) | Yes |

## Examples

### Basic Usage

Visit: https://vulnstore.myshopify.com/admin/oauth/authorize?scope=read_customers&client_id=cad94488c733b0f377a9a1d7952db802

### Advanced Usage

Add more scopes: https://vulnstore.myshopify.com/admin/oauth/authorize?scope=read_customers,write_products&client_id=cad94488c733b0f377a9a1d7952db802

## Expected Output

OAuth permission dialog listing scopes; upon clicking 'Install App', installation succeeds but browser does not redirect, potentially showing an error or blank page.

## Related

- [[Related Procedure: Install-Shopify-App-via-OAuth]]
