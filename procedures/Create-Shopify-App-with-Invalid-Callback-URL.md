---
tags:
  - shopify
  - app-creation
  - input-validation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:45.022Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: a28a4a8a-2ce0-450e-84c7-f1a77bcacc78
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Shopify-App-with-Invalid-Callback-URL

## Summary

This procedure creates a new Shopify app using the Partner Dashboard with a deliberately malformed Application Callback URL, exploiting lack of input validation to prepare for a denial of service attack.

## Description

In the Shopify ecosystem, apps are created via the Partner Dashboard at https://app.shopify.com/services/partners/api_clients/new. The Application Callback URL (redirect_uri) is not properly validated for standard URI schemes, allowing custom or invalid schemes like 'shit:google.com'. This sets up the app for later installation that will fail post-OAuth redirects, leading to application state issues. Prerequisites include a valid Shopify Partner account. The procedure is web-based and requires manual form submission.

## Requirements

1. Active Shopify Partner account with app creation permissions
2. Web browser with access to https://app.shopify.com
3. Basic knowledge of Shopify app development workflow

## Defense

Defensive measures and detection strategies:

- Implement strict URI scheme validation (e.g., only allow http/https) during app creation
- Monitor for unusual callback URLs in app registrations via partner dashboard logs
- Rate-limit or review app installations from new partners

## Objectives

1. Register a malicious app with invalid redirect_uri
2. Obtain client_id for subsequent OAuth installation
3. Prepare for DoS impact on target store

## Instructions

### Step 1: Navigate to App Creation

**Context**: Access the Shopify Partner Dashboard to start creating a new app.

**Instructions**: Log in to your Shopify Partner account and go to https://app.shopify.com/services/partners/api_clients/new. Fill in basic app details such as name and description.

### Step 2: Set Malformed Callback URL

**Context**: Introduce the invalid input in the redirect_uri field to bypass validation.

**Instructions**: In the Application Callback URL field, enter 'shit:google.com'. Optionally, set other URLs if required, but focus on the callback.

### Step 3: Save and Register App

**Context**: Submit the form to create the app and retrieve the client_id.

**Instructions**: Review details and submit the creation form. Upon success, note the generated client_id (e.g., cad94488c733b0f377a9a1d7952db802) from the app details page.

> Expected output: App created confirmation; client_id displayed for use in OAuth.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- app-creation
- input-validation
