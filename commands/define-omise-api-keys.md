---
data: >-
  <?php require_once dirname(__FILE__).'/vendor/autoload.php';
  define('OMISE_PUBLIC_KEY', 'pkey_test_54ot96fkr3i2op60cng');
  define('OMISE_SECRET_KEY', 'skey_test_54ot96fkr3i2op60cng');
  define('OMISE_API_VERSION', '2017-11-02');
tags:
  - api-configuration
  - omise
type: command
output: null
executor: php
platforms:
  - Web
  - PHP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.362Z'
id: ff354d33-cb2a-4cfa-99cd-49819b3da599
verified: false
validated: true
submitted: true
---
# define-omise-api-keys

## Command

```php
<?php
require_once dirname(__FILE__).'/vendor/autoload.php';
define('OMISE_PUBLIC_KEY', 'pkey_test_54ot96fkr3i2op60cng');
define('OMISE_SECRET_KEY', 'skey_test_54ot96fkr3i2op60cng');
define('OMISE_API_VERSION', '2017-11-02');
```

## Description

This PHP code snippet sets up constants for integrating the Omise PHP library by defining public and secret API keys along with the API version. It is typically used in example code to demonstrate library initialization but can expose sensitive keys if committed to public repositories without redaction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `OMISE_PUBLIC_KEY` | Placeholder public key for client-side token creation (e.g., 'pkey_test_54ot96fkr3i2op60cng') | Yes |
| `OMISE_SECRET_KEY` | Placeholder secret key for server-side operations like charges and balance retrieval (e.g., 'skey_test_54ot96fkr3i2op60cng') | Yes |
| `OMISE_API_VERSION` | Specifies the Omise API version for compatibility (e.g., '2017-11-02') | Yes |

## Examples

### Basic Usage

```php
<?php
require_once dirname(__FILE__).'/vendor/autoload.php';
define('OMISE_PUBLIC_KEY', 'pkey_test_54ot96fkr3i2op60cng');
define('OMISE_SECRET_KEY', 'skey_test_54ot96fkr3i2op60cng');
define('OMISE_API_VERSION', '2017-11-02');
// Now use Omise\Charge::create([...]);
```

### Advanced Usage

Incorporate into a full script after installation via Composer:

```php
<?php
require_once dirname(__FILE__).'/vendor/autoload.php';
define('OMISE_PUBLIC_KEY', 'pkey_test_54ot96fkr3i2op60cng');
define('OMISE_SECRET_KEY', 'skey_test_54ot96fkr3i2op60cng');
define('OMISE_API_VERSION', '2017-11-02');

// Example: Retrieve account balance
$balance = OmiseBalance::retrieve();
print_r($balance);
```

## Expected Output

Defines the constants silently with no console output. When used in Omise functions, successful API calls return JSON responses (e.g., account balance details); placeholders result in authentication errors.

## Related

- [[Related Procedure: Discover-Exposed-API-Keys-in-GitHub-Repository]]
