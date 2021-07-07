# Facebook Post Scheduler

This is Facebook Post Scheduler Application made with Python and Facebooks's Graph API.

I use Tkinter to create the GUI

## Requirements
Before running this project you need to get user token and access token from facebook.

visit https://developers.facebook.com/ to get user token and access token.

## Code Explanation
There are 2 classes in this project
1. facebook_automate.py - contains multiple function to post into facebook
2. main.py - this is the main page where you can add your images, posts and scheduler your post.


### facebook_automate.py
This one below is where you put you page id.
to get your Page ID go to Facebook.com, click on one of your pages which you used to generate your user token and access token.
```python
page_id = 102xxxxxxxxxx867
```

Facebooks gives you short lived tokens at first, so you have to generate tokens which are long lived in order to do that you need to visit https://developers.facebook.com/docs/facebook-login/access-tokens/refreshing
```python
long_lived_user_token = ""
long_lived_access_token = ""
```
If you want to post only texts(with out any image), you can use this function
```python
def postTextFunction(post_title):
    # message = input("enter here to post into facebook")
    post_url = "https://graph.facebook.com/{}/feed".format(page_id)
    payload = {
        'message': post_title,
        'access_token': long_lived_access_token
    }
    r = requests.post(post_url, data=payload)
    return r.text
   ```
   
 If you want to post only images(with out texts), you can use this function
 ```python
 def postImgeFunction(image_location):
    image_url = "https://graph.facebook.com/{}/photos".format(page_id)
    img_payload = {
        "url": image_location,
        "access_token": long_lived_access_token
    }
    r = requests.post(image_url, data=img_payload)
    return r.text
```

If you want to post both image with capition, you can use this function
```python
def fullPostFunction(post_title, image_location):
    image_url = "https://graph.facebook.com/{}/photos".format(page_id)
    full_payload = {
        'message': post_title,
        'url': image_location,
        'access_token': long_lived_access_token
    }
    r = requests.post(image_url, data=full_payload)
    return r.text
```
