---
data: |-
  import omise
  omise.api_secret = 'skey_test_5sqdfyjv0rtqzs9f2x2'

  customer = omise.Customer.create(
   description='John Doe',
   email='john.doe@example.com'
  )
tags:
  - api-call
  - credential-exposure
type: command
output: |-
  DEBUG:omise.request:Authorization: skey_test_5sqdfyjv0rtqzs9f2x2
  {'object': 'customer', 'id': 'cust_test_...', 'description': 'John Doe', ...}
executor: python
platforms:
  - Python
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.766Z'
id: 518066de-80ee-4fa0-8486-58fcd11fb5c3
verified: false
validated: true
submitted: true
---
# create-omise-customer-with-api-secret

## Command

```python
import omise
omise.api_secret = 'skey_test_5sqdfyjv0rtqzs9f2x2'

customer = omise.Customer.create(
 description='John Doe',
 email='john.doe@example.com'
)
```

## Description

This Python command sets the Omise API secret key and creates a test customer, which triggers debug logging that exposes the full API key in the console when logging is set to DEBUG level. Use this in a controlled environment to demonstrate credential logging vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| omise.api_secret | The secret API key for authentication (format: skey_test_...) | Yes |
| description | Description of the customer | Yes |
| email | Email address for the customer | Yes |

## Examples

### Basic Usage

```python
import omise
omise.api_secret = 'skey_test_5sqdfyjv0rtqzs9f2x2'
customer = omise.Customer.create(description='John Doe', email='john.doe@example.com')
print(customer)
```

### Advanced Usage

```python
import omise
import logging
logging.basicConfig(level=logging.DEBUG)
omise.api_secret = 'skey_test_5sqdfyjv0rtqzs9f2x2'
customer = omise.Customer.create(description='John Doe', email='john.doe@example.com', metadata={'source': 'test'})
print(customer)
```

## Expected Output

Console log output including 'DEBUG:omise.request:Authorization: skey_test_5sqdfyjv0rtqzs9f2x2' along with the customer creation response object containing id, livemode, etc.

## Related

- [[Related Procedure: Execute-Omise-Python-Script-with-Debug-Logging-to-Expose-API-Key]]
