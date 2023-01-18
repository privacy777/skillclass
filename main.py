import requests,json,wget,os
from slugify import * #slugify is here for safe, file name formats, either way it could crash. this way it's just formatting it so that the wget doesn't crash

path = os.getcwd() #getting the directory name for file download, either way it's in default forlder

def skillcourse(url):
    """Takes an URL link and download all the course videos in the Downloaded folder (needed, don't delete) using heckernohecking's API

    Args:
        url (str): your course link, with only the courses' digits at the end or it won't work (i will fix it dw)
    """
    try:
        
        if not os.path.exists(f'{path}/Downloaded'): # Make download folder if it doesn't exist
            os.mkdir(f'{path}/Downloaded')

        with requests.get(f'https://skillshare-api--heckernohecking.repl.co/{url}') as r: #requesting the API, with is used so that it closes after the requests automatically.

            data = r.text #data is basically the answer of the page, we'll use this data at out advantage

        json_data = json.loads(data) #since data is in JSON format, we'll load it to pick the elements we need

        vidsnumber = data.count('title') #for each "title" of videos in the course, it's 1 more video to download after each one. we'll use this later on

        name = json_data['class'] #the name of the course is the name of the course

        print(f'>>> Downloading {name}...') #we print the name of the course

        os.mkdir(f'{path}/Downloaded/{slugify(name)}') #we create a folder for the course, with the name of the course, encoded so no crash


        for i in range(vidsnumber): #for the numbers of videos

            url = json_data["lessons"][i]['url'] #the video's url is it's url (in order, from first to last)

            title = json_data["lessons"][i]['title']#the video's title is it's title (in order, from first to last)

            print(title,'\n') 

            wget.download(url, out=f'{path}/Downloaded/{slugify(name)}/{slugify(title)}.mp4') #we download the video, in the current users's path, in the downloaded folder with it's title encoded so no crash

            print('\n') #line skipping

            i += 1 #we checked one vid, so i increases to check the next one, and so on until there's no video left
    except:
        print('\n>>> Error, Invalid URL. Passing')
        pass



if __name__=="__main__":
    
    links = [] # this is where our links will be stored (multi link options only)
    
    os.system("cls") #Clearing the screen
    
    print("""
          
          
.▄▄ · ▄ •▄ ▪  ▄▄▌  ▄▄▌   ▄▄· ▄▄▌   ▄▄▄· .▄▄ · .▄▄ · 
▐█ ▀. █▌▄▌▪██ ██•  ██•  ▐█ ▌▪██•  ▐█ ▀█ ▐█ ▀. ▐█ ▀. 
▄▀▀▀█▄▐▀▀▄·▐█·██▪  ██▪  ██ ▄▄██▪  ▄█▀▀█ ▄▀▀▀█▄▄▀▀▀█▄
▐█▄▪▐█▐█.█▌▐█▌▐█▌▐▌▐█▌▐▌▐███▌▐█▌▐▌▐█ ▪▐▌▐█▄▪▐█▐█▄▪▐█
 ▀▀▀▀ ·▀  ▀▀▀▀.▀▀▀ .▀▀▀ ·▀▀▀ .▀▀▀  ▀  ▀  ▀▀▀▀  ▀▀▀▀ 

          
          """)
    
    
    choice = input('>>> Multi-link or Single link mode ? 0 or 1 \n>>>  ')
    
    if choice == "0":
        
        try:
            
            with open('links.txt','r') as f: #we open our links.txt file
                for lines in f: 
                    links.append(lines.strip('\n'))  #we then put the links into a list, while removing the '\n' unicode of the end of the link.
            
            
            while len(links) > 0: #While looping until our list is empty
                url = links[0] #we take the first element of the list
                
                skillcourse(url.rsplit('/', 1)[-1]) 
                links.pop(0) #we delete it
        except:
            print('\n>>>Error : links.txt is missing.')
            
            with open('links.txt','w+'): #creating links.txt text file
                print('\n>> links.txt created / in folder, paste links in it.')
            pass
        
    elif choice == "1":
        
        url = input('>>> Class Link (ONLY NUMBER AT THE END OF URL) \n>>>  ').rsplit('/', 1)[-1] #basically only taking the last number arg of the url, the course link which is essential

        skillcourse(url)
    else:
        pass

    print('\n>>>Done')
