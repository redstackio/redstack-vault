---
id: proc-vimeo-add-to-cart-2
tags:
  - web-interaction
  - parameter-extraction
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:51.813Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Add-Non-Free-Track-to-Cart-and-Extract-Track-ID

## Summary

This procedure involves selecting a paid track in Vimeo's music store and adding it to the cart via UI interaction, which triggers a POST request containing the track_id for later exploitation.

## Description

The attack scenario targets the /cart/music endpoint during the add-to-cart process for non-free tracks. By interacting with the UI, a POST request is sent with parameters including action=add, license_id=2, license_name=Personal, price=1.99, track_id, track_title, uid, and token. This step reveals the track_id without completing payment. Expected outcome is temporary cart addition and request capture. Target is Vimeo's web app; requires authenticated session.

## Requirements

1. Authenticated session from prior login.
2. Browser with network inspection tools enabled (e.g., DevTools).
3. Access to a non-free track listing.

## Defense

Defensive measures and detection strategies:

- Validate all cart actions server-side with purchase status checks.
- Log and monitor POST requests to /cart/music for anomalous patterns.
- Implement client-side obfuscation of sensitive parameters like track_id.

## Objectives

1. Trigger the add-to-cart request for a paid track.
2. Capture the request to obtain track_id.
3. Avoid completing the checkout process.

## Instructions

### Step 1: Select Non-Free Track

**Context**: Identify and interact with a paid track to initiate the cart addition.

In the music store, locate a track with a price (e.g., $1.99) and click the Add to Cart icon.

> This sends a POST to https://vimeo.com/cart/music with form data including track_id (e.g., 110947), price=1.99, license_id=2.

### Step 2: Monitor Network Request

**Context**: Use DevTools to observe the request during the UI action.

Open browser DevTools (F12), go to the Network tab, and filter for POST requests. Reproduce the add-to-cart click to capture the request.

> Request body shows parameters; note the track_id for extraction in the next procedure.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web-interaction
- parameter-extraction
