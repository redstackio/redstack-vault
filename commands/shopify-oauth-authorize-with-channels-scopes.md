---
data: >-
  curl
  "https://while42.myshopify.com/admin/oauth/authorize?client_id=fc49e813f5aad9c8d8f65117031a9684&scope=read_apps,write_apps,write_content,read_content,write_customers,read_customers,read_disputes,write_fulfillments,read_fulfillments,write_gift_cards,read_gift_cards,write_orders,read_orders,read_products,write_products,read_script_tags,write_script_tags,write_scripts,read_scripts,read_shipping,write_shipping,write_social_network_accounts,read_social_network_accounts,read_themes,write_themes,read_channels,write_channels&redirect_uri=http://while42.myshopify.com/&state=123&shop=while42"
tags:
  - shopify
  - oauth
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.723Z'
id: bac08e6d-faa0-439d-aa83-5b634a1d5bcf
verified: false
validated: true
submitted: true
---
# shopify-oauth-authorize-with-channels-scopes

## Command

```bash
curl "https://while42.myshopify.com/admin/oauth/authorize?client_id=fc49e813f5aad9c8d8f65117031a9684&scope=read_apps,write_apps,write_content,read_content,write_customers,read_customers,read_disputes,write_fulfillments,read_fulfillments,write_gift_cards,read_gift_cards,write_orders,read_orders,read_products,write_products,read_script_tags,write_script_tags,write_scripts,read_scripts,read_shipping,write_shipping,write_social_network_accounts,read_social_network_accounts,read_themes,write_themes,read_channels,write_channels&redirect_uri=http://while42.myshopify.com/&state=123&shop=while42"
```

## Description

Initiates Shopify OAuth authorization requesting excessive scopes including undocumented read_channels and write_channels to enable beta API access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| client_id | App client ID | Yes |
| scope | Comma-separated scopes including channels | Yes |
| redirect_uri | Callback URL | Yes |
| state | CSRF protection state | Yes |
| shop | Target shop domain | Yes |

## Examples

### Basic Usage

```bash
curl "https://shop.myshopify.com/admin/oauth/authorize?client_id=YOUR_ID&scope=read_channels,write_channels&redirect_uri=http://callback&state=123&shop=shop"
```

### Advanced Usage

Include full standard scopes as shown in the command.

## Expected Output

Redirect response with ?code=AUTH_CODE in the redirect_uri query.

## Related

- [[Related Procedure: Request-Undocumented-Shopify-OAuth-Scopes]]
