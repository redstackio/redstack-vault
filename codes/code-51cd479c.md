---
id: 51cd479c-250f-4af0-abf9-fc9f85a87c0f
type: code
language: Bash
verified: false
created_at: '2023-04-06T03:55:51.871972+00:00'
updated_at: '2023-04-10T20:21:11.930408+00:00'
---

# Code Snippet 51cd479c

**Language**: Bash

```bash
#Check token validity
curl "https://api.mapbox.com/tokens/v2?access_token=YOUR_MAPBOX_ACCESS_TOKEN"

#Get list of all tokens associated with an account. (only works if the token is a Secret Token (sk), and has the appropiate scope)
curl "https://api.mapbox.com/tokens/v2/MAPBOX_USERNAME_HERE?access_token=YOUR_MAPBOX_ACCESS_TOKEN"
```
