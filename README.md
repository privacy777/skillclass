
# skillclass

Download every skillshare class you want. (thanks to HeckerNoHecking's api)

## Important notice : current status
- Unfortunately, HeckerNohecking posted on replit that his api was not available publicly anymore, possibly implying legal actions from skillshare, or maybe just lack of time to maintain the project.
- This means that the project is currently NOT working, until I find another alternative.
- Thank you for the support, this was the first time my project actually got more or less 10 stars, and a contributor :)
## Features

- Download all your skillshare courses for free
- Multiple Links now supported !
- Auto file-folder creation
- Simple error handling : will pass if one link is invalid in the list
- File Names are encoded so you can download the videos without any errors
- Easy to use
- No manual clicks needed.


## Deployment

First install python 3+, then run this command before running the "main.py" script :

```bash
  python -m pip install -r requirements.txt
  python main.py
```


## FAQ

#### How does it work

Basically, HeckerNoHecking's allows us to get the JSON data with the titles and url of any skillshare courses. So this tool automates the download of each file, so you can watch all your courses for free !

## Roadmap

- More "flexibility" over the link

- Multi-threaded downloads (faster with a better internet)

- Code cleanup and maybe OOP but idk why, it's just for fun i guess.

## Authors & contibutors

- [@privacy777](https://github.com/privacy777)

- [@HeckerNoHecking](https://replit.com/@HeckerNoHecking) for his API

- [@59n](https://github.com/59n) for his contribution on the main code (auto Folder creation in path)
