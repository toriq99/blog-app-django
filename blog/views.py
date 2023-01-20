from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from datetime import date

post_data = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Ariq",
        "date": date(2022, 1, 10),
        "title": "Mountain Hiking",
        "excerpt": "This is my first trip to this mountain, the view is so good!, i hope you can enjoy the views too!",
        "content": """       
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores quibusdam in, totam error nesciunt consequuntur ad sit necessitatibus, fugit perferendis enim, sapiente vero rerum odio qui. Nostrum ullam accusantium quidem.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores quibusdam in, totam error nesciunt consequuntur ad sit necessitatibus, fugit perferendis enim, sapiente vero rerum odio qui. Nostrum ullam accusantium quidem.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores quibusdam in, totam error nesciunt consequuntur ad sit necessitatibus, fugit perferendis enim, sapiente vero rerum odio qui. Nostrum ullam accusantium quidem.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores quibusdam in, totam error nesciunt consequuntur ad sit necessitatibus, fugit perferendis enim, sapiente vero rerum odio qui. Nostrum ullam accusantium quidem.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores quibusdam in, totam error nesciunt consequuntur ad sit necessitatibus, fugit perferendis enim, sapiente vero rerum odio qui. Nostrum ullam accusantium quidem.
        """
    },
    { 
        "slug": "learn-django",
        "image": "django.png",
        "author": "Ariq",
        "date": date(2022, 2, 13),
        "title": "Learn Django",
        "excerpt": "My first step learning django!",
        "content": """       
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores quibusdam in, totam error nesciunt consequuntur ad sit necessitatibus, fugit perferendis enim, sapiente vero rerum odio qui. Nostrum ullam accusantium quidem.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores quibusdam in, totam error nesciunt consequuntur ad sit necessitatibus, fugit perferendis enim, sapiente vero rerum odio qui. Nostrum ullam accusantium quidem.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores quibusdam in, totam error nesciunt consequuntur ad sit necessitatibus, fugit perferendis enim, sapiente vero rerum odio qui. Nostrum ullam accusantium quidem.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores quibusdam in, totam error nesciunt consequuntur ad sit necessitatibus, fugit perferendis enim, sapiente vero rerum odio qui. Nostrum ullam accusantium quidem.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores quibusdam in, totam error nesciunt consequuntur ad sit necessitatibus, fugit perferendis enim, sapiente vero rerum odio qui. Nostrum ullam accusantium quidem.
        """
    },
    {
        "slug": "at-the-zoo",
        "image": "zoo.jpg",
        "author": "Ariq",
        "date": date(2022, 1, 14),
        "title": "Holiday at Zoo",
        "excerpt": "Zoo is fun, i hope you can enjoy the views too!",
        "content": """       
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores quibusdam in, totam error nesciunt consequuntur ad sit necessitatibus, fugit perferendis enim, sapiente vero rerum odio qui. Nostrum ullam accusantium quidem.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores quibusdam in, totam error nesciunt consequuntur ad sit necessitatibus, fugit perferendis enim, sapiente vero rerum odio qui. Nostrum ullam accusantium quidem.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores quibusdam in, totam error nesciunt consequuntur ad sit necessitatibus, fugit perferendis enim, sapiente vero rerum odio qui. Nostrum ullam accusantium quidem.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores quibusdam in, totam error nesciunt consequuntur ad sit necessitatibus, fugit perferendis enim, sapiente vero rerum odio qui. Nostrum ullam accusantium quidem.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores quibusdam in, totam error nesciunt consequuntur ad sit necessitatibus, fugit perferendis enim, sapiente vero rerum odio qui. Nostrum ullam accusantium quidem.
        """
    },
    {
        "slug": "riding-motocycle",
        "image": "riding.jpg",
        "author": "Ariq",
        "date": date(2022, 3, 24),
        "title": "Riding Motocycle",
        "excerpt": "One of my hobbies, its very fun!",
        "content": """       
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores quibusdam in, totam error nesciunt consequuntur ad sit necessitatibus, fugit perferendis enim, sapiente vero rerum odio qui. Nostrum ullam accusantium quidem.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores quibusdam in, totam error nesciunt consequuntur ad sit necessitatibus, fugit perferendis enim, sapiente vero rerum odio qui. Nostrum ullam accusantium quidem.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores quibusdam in, totam error nesciunt consequuntur ad sit necessitatibus, fugit perferendis enim, sapiente vero rerum odio qui. Nostrum ullam accusantium quidem.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores quibusdam in, totam error nesciunt consequuntur ad sit necessitatibus, fugit perferendis enim, sapiente vero rerum odio qui. Nostrum ullam accusantium quidem.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores quibusdam in, totam error nesciunt consequuntur ad sit necessitatibus, fugit perferendis enim, sapiente vero rerum odio qui. Nostrum ullam accusantium quidem.
        """
    }
]

def get_date(post_data):
    return post_data['date']

# Create your views here.

def index(request):
    sorted_post = sorted(post_data, key=get_date)
    latest_post = sorted_post[-3:]
    return render(request, 'blog/index.html',{
        "post": latest_post,
    })

def posts(request):
    return render(request, 'blog/all-posts.html')

def posts_details(request, slug):
    return render(request, 'blog/posts-details.html')