---
tags:
  - setup
  - wordpress
  - woocommerce
  - customer-creation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-13T23:52:34.338Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 95a68ff5-cd7e-4220-babf-0543dc4f3ed4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Set-Up-WordPress-WooCommerce-Environment-and-Create-Customer

## Summary

This procedure establishes a vulnerable WordPress environment with the WooCommerce plugin and creates a registered customer account, serving as the foundation for injecting persistent XSS payloads in customer address fields.

## Description

In a testing or attack scenario targeting WooCommerce version 3.5.7 on WordPress, this procedure involves installing the necessary components and registering a customer user. The environment simulates a typical e-commerce site where customer registration is enabled. Prerequisites include a local or remote web server capable of running PHP and MySQL. Once set up, the customer account provides the necessary permissions to edit addresses without admin privileges, setting the stage for payload persistence in the database.

## Requirements

1. Access to a server or local machine (e.g., XAMPP/LAMP) for WordPress installation.
2. Download of WordPress core and WooCommerce plugin (version 3.5.7).
3. MySQL database configured for WordPress.
4. Enabled customer registration in WooCommerce settings.

## Defense

Defensive measures and detection strategies:

- Regularly update WooCommerce and WordPress to patch known XSS vulnerabilities.
- Enable customer registration moderation or CAPTCHA to limit account creation.
- Monitor database for anomalous address field entries containing script tags.

## Objectives

1. Deploy a functional WooCommerce-enabled WordPress site.
2. Create a legitimate customer account for subsequent exploitation.
3. Verify environment readiness for address editing.

## Instructions

### Step 1: Install WordPress and WooCommerce

**Context**: Set up the base platform with the vulnerable plugin version.

Download and install WordPress, then activate WooCommerce 3.5.7 via the admin dashboard under Plugins > Add New.

> Configure WooCommerce settings to enable customer registration (WooCommerce > Settings > Accounts & Privacy > Allow customers to create an account).

### Step 2: Create Customer Account

**Context**: Register a new user with customer role to gain access to account features.

Navigate to the site's registration page (e.g., /my-account/) and fill in details to create an account, or use the WordPress admin to add a user with 'customer' role.

> Expected: Confirmation email or dashboard access; note the user ID (e.g., 4) for later reference.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[wordpress]]
- [[woocommerce]]
