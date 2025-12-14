---
data: |-
  #!/bin/bash
  creds=`cat ../creds`

  curl "$creds/admin/webhooks.json?since=1" \
    -H "Content-Type: application/json" 

  printf "\n"
tags:
  - shopify
  - api
  - webhook
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:11.017Z'
id: 65175521-e2e9-4622-9a53-130fa2c365b4
verified: false
validated: true
submitted: true
---
# list-shopify-webhooks

## Command

```bash
#!/bin/bash
creds=`cat ../creds`

curl "$creds/admin/webhooks.json?since=1" \
  -H "Content-Type: application/json" 

printf "\n"
```

## Description

This bash script queries the Shopify API to list webhooks created since a specified timestamp, using credentials from a file. It demonstrates how webhooks become hidden after permission revocation by returning an empty array.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| creds | Path to credentials file (shop.myshopify.com:api_key:password) | Yes |
| since | Timestamp filter (e.g., 1 for recent) | Yes |

## Examples

### Basic Usage

```bash
#!/bin/bash
creds=`cat ../creds`

curl "$creds/admin/webhooks.json?since=1" \
  -H "Content-Type: application/json"
```

### Advanced Usage

```bash
# With output formatting
#!/bin/bash
creds=`cat ../creds`

curl "$creds/admin/webhooks.json?since=1" \
  -H "Content-Type: application/json" | jq '.["webhooks"]'
```

## Expected Output

After permission revocation: {"webhooks":[]}, an empty array hiding existing webhooks.

## Related

- [[commands/create-shopify-webhook]]
- [[procedures/Verify-Hidden-Webhook-in-Listing]]
