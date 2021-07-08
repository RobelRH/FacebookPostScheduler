import requests
import schedule

page_id = 102xxxxxxxxx867 # you will enter your page id here

# long_lived_user_token
long_lived_user_token = "" # enter your long lived user token here

# long_lived_access_token
long_lived_access_token = "" # enter your long lived access token here

def postTextFunction(post_title):
    # message = input("enter here to post into facebook")
    post_url = "https://graph.facebook.com/{}/feed".format(page_id)
    payload = {
        'message': post_title,
        'access_token': long_lived_access_token
    }
    r = requests.post(post_url, data=payload)
    return r.text


def postImgeFunction(image_location):
    image_url = "https://graph.facebook.com/{}/photos".format(page_id)
    # image_location = "https://www.datamation.com/wp-content/uploads/2021/04/Amazon-Web-Services-Logo-e1617809700657.png"
    img_payload = {
        "url": image_location,
        "access_token": long_lived_access_token
    }
    r = requests.post(image_url, data=img_payload)
    return r.text

def fullPostFunction(post_title, image_location):
    image_url = "https://graph.facebook.com/{}/photos".format(page_id)
    full_payload = {
        'message': post_title,
        'url': image_location,
        'access_token': long_lived_access_token
    }
    r = requests.post(image_url, data=full_payload)
    return r.text
