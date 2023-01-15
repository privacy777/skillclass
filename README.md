
# skillclass

Download every skillshare class you want. (thanks to HeckerNoHecking's api)


## Features

- Download all your skillshare courses for free
- File Names are encoded so you can download them without any errors
- Easy to use
- No manual clicks needed.


## Deployment

First install python 3+, then run this command before running the "main.py" script :

CF : Make a "Dowloaded" folder (without the quotes) in the same path/folder your main.py script is, this is where all the downloaded videos will be.

```bash
  python -m pip install -r requirements.txt
  python main.py
```


## FAQ

#### How does it work

Basically, HeckerNoHecking's allows us to get the JSON data with the titles and url of any skillshare courses. So this tool automates the download of each file, so you can watch all your courses for free !

#### Can i delete the "Downloaded" folder

No, not at the moment, unless u "mod" it to your convenience, i made this little project and i will update it soon. DO not hesitate to notify me on the thread on what i could do, or commit changes to the code and upload them to me. thanks !



## Roadmap

- More "flexibility" over the link

- Multi-threaded downloads (faster with a better internet)

- Code cleanup and maybe OOP but idk why, it's just for fun i guess.

## Authors

- [@privacy777](https://github.com/privacy777)

- [@HeckerNoHecking](https://replit.com/@HeckerNoHecking) for his API
