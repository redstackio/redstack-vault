---
data: 'https://vulnstore.myshopify.com/admin/apps'
tags:
  - dos
  - shopify
type: command
output: >-
  500 internal server error due to the presence of the app with malformed
  redirect_uri
executor: browser
platforms:
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:45.007Z'
id: 95cb198f-3e1b-4917-9deb-deeddce5d83e
verified: false
validated: true
submitted: true
---
# shopify-admin-apps-access

## Command

Visit the URL in a web browser: https://vulnstore.myshopify.com/admin/apps

## Description

This command accesses the Shopify admin's installed apps management page on a target store. When a malicious app with malformed redirect_uri is installed, it results in a 500 error, demonstrating the DoS effect.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| store | Target store subdomain (e.g., vulnstore.myshopify.com) | Yes |

## Examples

### Basic Usage

Visit: https://vulnstore.myshopify.com/admin/apps

### Advanced Usage

N/A - direct page access.

## Expected Output

HTTP 500 Internal Server Error; page fails to load, preventing viewing or managing installed apps.

## Related

- [[Related Procedure: Verify-DoS-on-Shopify-Admin-Apps-Page]]
