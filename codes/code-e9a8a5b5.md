---
id: e9a8a5b5-60f1-42df-b00f-78861aa97a85
type: code
language: Bash
verified: false
created_at: '2023-04-06T03:55:52.632604+00:00'
updated_at: '2023-04-06T03:55:52.647166+00:00'
---

# Code Snippet e9a8a5b5

**Language**: Bash

```bash
#Check token validity
curl "https://api.mapbox.com/tokens/v2?access_token=YOUR_MAPBOX_ACCESS_TOKEN"

#Get list of all tokens associated with an account. (only works if the token is a Secret Token (sk), and has the appropiate scope)
curl "https://api.mapbox.com/tokens/v2/MAPBOX_USERNAME_HERE?access_token=YOUR_MAPBOX_ACCESS_TOKEN"
```


