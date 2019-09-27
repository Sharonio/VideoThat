# VideoThat

## Automagically Generate a Music Video for Your Input Audio

2nd place DataHack winner 🥈, September 2019

VideoThat will automagically generate the perfect video compilation that fits impeccably to the theme song of your choice. The algorithm’s default choice is to create a video clip from Taylor Swift’s videos to an Arctic Monkey song.

This project was created as part of [DataHack 2019 Israel](https://www.datahack.org.il/), read all about it in our [blog post](https://www.meimadix.com/posts/videothat.html) 👾

![The algorithm](../master/assets/anim.gif)
*********
## Installation

##### Fork VideoThat repository to your file system


#### System requirements
Ubuntu/debian
```shell
sudo apt install ffmpeg
```
macOS
```shell
brew install ffmpeg
```

Install requirements file
```shell
pip3 install -r requirements.txt
```

Install the newest version of youtube-dl
```shell
pip3 install --upgrade youtube-dl
```
*****
## Code pipeline

#### Create Data-Base (db) of video clips
To start downoading all of the videoclips and create a data-base, open the terminal go to the repository location and write

note: the following command will download ~1.5GB to your directory and can take a while
```shell
./download-db.sh
```

Detect all of the scene cuts from the db you just created
```shell
./scenedetect_all.sh
```
Run `create_scene_db.py` to create a `.pkl` df unified file of all the scenes from the db (this creates `scene_db.pkl` and `song_db.pkl`)
```shell
python3 create_scene_db.py
```
Run `choose_scenes.py` to run the algorithm which chooses taylor swift scenes from the db to match to a song (creates `chosen_scenes.pkl`)
```shell
python3 choose_scenes.py
```
Run `build_video.py` to create the video file from the chosen scenes
```shell
python3 build_video.py
```
#### The video `videoThat.mp4` has been successfully created and added to your directory 
*******
## Code structure

![Code structure](../master/assets/VideoThat_code_structure.jpg)

*********

That's Us

![That's Us!](../master/assets/thats_us.jpg)

Yael Daihes       [GitHub](https://github.com/yooli3)   [LinkedIn](https://www.linkedin.com/in/yael-daihes/)

Yaara Arkin       [GitHub](https://github.com/yaarasegre)   [LinkedIn](https://www.linkedin.com/in/yaara-arkin-86706013/)

Orian Sharoni     [GitHub](https://github.com/Sharonio)   [LinkedIn](https://www.linkedin.com/in/orian-sharoni/)

Roee Shenberg     [GitHub](https://github.com/shenberg)   [LinkedIn](https://www.linkedin.com/in/roeeshenberg/)

Dalya Gartzman    [GitHub](https://github.com/DalyaG)   [LinkedIn](https://www.linkedin.com/in/dalya-gar/)


*********
