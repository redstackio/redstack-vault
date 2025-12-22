---
url: 'https://marketplace.stripe.com/apps/custom-links'
tags:
  - stripe-app
  - link-creation
  - xss-testing
type: tool
verified: false
platforms:
  - Web
id: e53993e1-a8df-4957-a64a-53cdf3328d2d
created_at: '2025-12-13T23:56:03.563Z'
updated_at: '2025-12-13T23:56:03.563Z'
validated: true
submitted: true
---
# Custom-Links-App

**Status**: Unverified

## Overview

The Custom Links app is a Stripe marketplace integration that allows users to add customizable hyperlinks to products in the dashboard, useful for testing URL validation in security assessments like XSS.

## Description

This third-party app extends Stripe's products functionality by enabling the creation and management of custom links attached to items. In offensive security, it's leveraged to inject malicious URIs such as javascript: schemes, probing for stored XSS. It requires Stripe account installation and integrates via the dashboard UI, with no CLI or advanced config needed.

## Features

- Feature 1: Simple UI for adding/editing links in products
- Feature 2: Supports arbitrary URL input without scheme restrictions
- Feature 3: Links are stored and visible to organization members

## Installation

### Requirements

- Stripe account with app install permissions
- Access to https://dashboard.stripe.com

### Install Commands

No CLI; browser-based:

Visit https://marketplace.stripe.com/apps/custom-links and click 'Install'.

## Basic Usage

Access via Stripe products section to create links.

### Common Options

| Option | Description |
|--------|-------------|
| URL Field | Input for link destination (e.g., javascript: payload) |
| Save | Persist the custom link |

## Examples

### Example 1: Basic Usage

In products, add a link with URL 'https://example.com'.

### Example 2: Advanced Usage

Add malicious payload: URL 'javascript://%0aalert(1)'.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor Stripe logs for app installations
- Scan product links for non-standard schemes

## Related Procedures


## Related Tools

- [[tools/Browser-Developer-Console]]

## References

- Stripe Marketplace: https://marketplace.stripe.com/apps/custom-links
