# Post Scheduler For Facebook Pages

This is Facebook Post Scheduler Application made with Python and Facebooks's Graph API.

I use Tkinter to create the GUI

## Run Project
If you meet the requirements below, you can open the main.py file and enjoy.

## Requirements
Before running this project you need to get user token and access token from facebook.

visit https://developers.facebook.com/ to get user token and access token.

## Code Explanation
There are 2 classes in this project
1. facebook_automate.py - contains multiple function to post into facebook
2. main.py - this is the main page where you can add your images, posts and schedule your post.


### facebook_automate.py
This one below is where you put you page id.
to get your Page ID go to Facebook.com, click on one of your pages which you used to generate your user token and access token.
```python
page_id = 102xxxxxxxxxx867
```

Facebooks will give you short lived tokens at first, so you have to generate tokens which are long lived in order to do that you need to visit https://developers.facebook.com/docs/facebook-login/access-tokens/refreshing

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

### main.py
This is our main class.

![preview](https://user-images.githubusercontent.com/65722317/124776064-d1c5b800-df47-11eb-9655-baedfb6466be.png)

You can enter title, image or both title and image
You can choose specific date and time, and it will be posted on the time you selected.

As you can see on the screen shot above, i entered some text and image url, i also set the date and time to be posted, now it is counting to minutes to post it into Facebook.

This is after it gets posted into Facebook.
![posted](https://user-images.githubusercontent.com/65722317/124783445-bf4e7d00-df4d-11eb-94c2-6a3b3aa0075a.PNG)


After importing necessary libraries to work with, we will specify the required width and height of the main frame

```python
root = tk.Tk()
root.geometry("800x560")
root.title("Facebook Post Scheduler")
```

In main.py i use 2 frames
1. for the scheduler
2. for preview

Scheduler Frame(frame1)

This is our first frame which is in the left side.

```python
frame1 = Frame(root, width=268, height=560, bg="#ffffff", borderwidth=2, relief="groove")
frame1.grid(row=0, column=0, padx=0, pady=0)

post_label = Label(frame1,text="Enter your post title",font=('cambria',12,'bold'), bg="#ffffff", fg="#25265E")
post_label.place(x=10,y=10)

post_title = scrolledtext.ScrolledText(frame1, font=('cambria',12), wrap=tk.WORD, width=25, height=4)
post_title.place(x=10,y=35)

image_url_label = Label(frame1,text="Enter image url",font=('cambria',12,'bold'), bg="#ffffff", fg="#25265E")
image_url_label.place(x=10,y=120)

image_url = Entry(frame1,width=26, font=('cambria',12), borderwidth=1, relief=SUNKEN)
image_url.place(x=10,y=145)

# Combobox creation
time_label = Label(frame1,text="Select date and time",font=('cambria',12,'bold'), bg="#ffffff", fg="#25265E")
time_label.place(x=10, y=180)

cal = Calendar(root, selectmode='day', year=thisyear, month=thismonth, date=thisday, background ="#25265E", headersbackground="#ffffff", normalbackground ="#F5F8FF", bordercolor="green")
cal.place(x=10, y=210)

h = tk.StringVar()
hour = ttk.Combobox(frame1, font=('cambria',12), width = 2, textvariable = h)

m = tk.StringVar()
minute = ttk.Combobox(frame1, font=('cambria',12), width = 2, textvariable = m)

ap = tk.StringVar()
ampm = ttk.Combobox(frame1, font=('cambria',12), width = 3, textvariable = ap)

# Adding combobox drop down list
hour['values'] = (0,1,2,3,4,5,6,7,8,9,10,11,12)
hour.place(x=10, y=410)

minute['values'] = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,
                    31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59)
minute.place(x=60, y=410)

ampm['values'] = ('AM', 'PM')
ampm.place(x=120, y=410)

hour.set(thistime.strftime("%I"))
minute.set(thistime.minute)
ampm.set(thistime.strftime("%p"))

preview = Button(frame1,text="preview",font=('cambria',12,'bold'), width=26, highlightthickness=2, highlightcolor="#4884F6",  highlightbackground="#4884F6", borderwidth=2, relief="groove",  bg="#F5F8FF", fg="#0C5BF3", command=preview)
preview.place(x=10,y=450)

post = Button(frame1,text="schedule and post", font=('cambria',12,'bold',), width=26,  background="#1877F2", fg="#ffffff",  command=schedulepost)
post.place(x=10,y=490)

scheduled_time = Label(frame1,text="",font=('cambria',12,'bold'))
scheduled_time.place(x=10, y=525)
```

Preview Function
we call this function if we want to preview what we filed in our Scheduler Frame(to be previewed in the Preview Frame(frame2)). 
we must set date, time and title or image in order to preview our post

```python
def preview():
    if (len(post_title.get('1.0', tk.END)) == 1 and len(image_url.get()) == 0):
        messagebox.showwarning("warning", "Please insert title or image")
        return
    if (cal.selection_get() == None):
        messagebox.showwarning("warning", "Please select date")
        return
    else:
        if(len(post_title.get('1.0', tk.END)) > 1):
            inserted_title.place(x=90,y=52)
            inserted_title.config(text = post_title.get('1.0', tk.END))
        if(len(image_url.get()) > 0):
            inserted_url.place(x=90,y=90)
            URL = image_url.get()
            u = urlopen(URL)
            raw_data = u.read()
            u.close()

            im = Image.open(BytesIO(raw_data))
            im.thumbnail((300, 400))
            photo = ImageTk.PhotoImage(im)

            inserted_url.configure(image=photo)
            inserted_url.image = photo
        return
```

Schedule Post Function

This function is used to calculate time left, it will substract the selected date and time from the current date and time, and pass the total seconds into another function called countdown()

```python
def schedulepost():
    # date time
    timenow = datetime.time(thishour, thisminute, thissecond)

    timeset = datetime.time(int(hour.get()), int(minute.get()), 0)
    timeset = timeset.strftime('%H:%M:%S')
    timesetconverted = timeconvert(timeset, ampm.get())
    timesetconverted = datetime.datetime.strptime(timesetconverted, "%H:%M:%S").time()

    datenow = datetime.date(thisyear, thismonth, thisday)
    dateset = datetime.date(cal.selection_get().year, cal.selection_get().month, cal.selection_get().day)

    datetimenow = datetime.datetime.combine(datenow, timenow)
    datetimeset = datetime.datetime.combine(dateset, timesetconverted)
    tobeposted = datetimeset - datetimenow
    tt = tobeposted.total_seconds()
    countdown(int(tt))
```

countdown() function

This function receives seconds from the calculated seconds above and start counting till it hits 0. after that it will call the function postit() in order be posted to facebook.

```python
def countdown(count):
    # change text in label        
    mins, secs = divmod(count, 60) 
    hours, mins = divmod(mins, 60)
    days, hours = divmod(hours, 24)
    timer = '00:00:00:00'
    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count-1)
        timer = '{:02d} days, {:02d}:{:02d}:{:02d}'.format(days, hours, mins, secs) 
    if(timer == '00:00:00:00'):
        scheduled_time.config(text= "posted")
        postit()
    else:
        scheduled_time.config(text= "after " + timer)
```

postit() function

when this function called it will post our image and title to facebook.

```python
def postit():
    if (len(post_title.get('1.0', tk.END)) == 1 and len(image_url.get()) == 0):
        messagebox.showwarning("warning", "Please insert title or image")
        return
    if (cal.selection_get() == None):
        messagebox.showwarning("warning", "Please select date")
        return
    else:
        if(len(post_title.get('1.0', tk.END)) > 1 and len(image_url.get()) == 0):
            fb.postTextFunction(post_title.get('1.0', tk.END))
        elif(len(post_title.get('1.0', tk.END)) == 1 and len(image_url.get()) != 0):
            fb.postImgeFunction(image_url.get())
        else:
            fb.fullPostFunction(post_title.get('1.0', tk.END), image_url.get())
```

Even the time in the interface you see is 12 hours format, behind it is converted to 24 hours format, becuase i don't want to get lost using AM and PM so i created a small function which acceptes time in 12 hours format and convert it to 24 Hours format.

```python
def timeconvert(str1, ap):
    if(ap == "AM" and str1[:2] == "12"):
        return "00" + str1[2:]
    elif ap == "AM":
        return str1[:]
    elif ap == "PM" and str1[:2] == "12":
        return str1[:]
    else:
        return str(int(str1[:2]) + 12) + str1[2:8]
```

Preview Frame(frame2)

This is our second frame where we preview our posts before it gets posted.

```python
frame2 = Frame(root, width=530, height=560, bg="#F2F2F2", border="10")
frame2.grid(row=0, column=1, padx=0, pady=0)

inserted_title = Label(frame2,text="your title will appear here",font=('cambria',12,'bold'), background="#F2F2F2")
# inserted_title.place(x=90,y=52)

URL = "https://t4.ftcdn.net/jpg/02/07/87/79/360_F_207877921_BtG6ZKAVvtLyc5GWpBNEIlIxsffTtWkv.jpg"
u = urlopen(URL)
raw_data = u.read()
u.close()

im = Image.open(BytesIO(raw_data))
im.thumbnail((300, 400))
photo = ImageTk.PhotoImage(im)

inserted_url = Label(frame2, image = photo, borderwidth=0, width=300, height=400, background="snow")
inserted_url.place(x=90,y=90)
```
