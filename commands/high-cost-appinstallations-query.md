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
              metafields(first: 2) {
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
  - depletion
type: command
output: null
executor: graphql
platforms:
  - Web
  - Shopify
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.304Z'
id: 3aa90966-63df-4708-ab3d-fc7147b577d1
verified: false
validated: true
submitted: true
---
# high-cost-appinstallations-query

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
            metafields(first: 2) {
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

This GraphQL query targets appInstallations with multiple redundant nested fields like accessScopes and metafields, incurring high query costs (70-100 points) to deplete the rate limit bucket in Shopify's API.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| first: 10 | Limits results to 10 but nested fields inflate cost | Yes |
| Nested fields | Redundant accessScopes and metafields increase complexity | Yes |

## Examples

### Basic Usage

Execute in GraphiQL app to deduct points.

```graphql
{ appInstallations(first: 10) { ... } }
```

### Advanced Usage

Repeat for depletion:

```graphql
# Same query, executed 10-15 times
```

## Expected Output

JSON response with app data and extensions { cost: ~80, throttleStatus: { current: low, maximum: 1000 } }, deducting points from bucket.

## Related

- [[commands/negative-cost-appinstallations-query]]
