# VideoThat

## Automagically Generate a Music Video for Your Input Audio

This project was created as part of [DataHack 2019 Israel](https://www.datahack.org.il/).
*********
## Installation

##### clone VideoThat repository to your file system


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
#### Create Data-Base (db) of video clips
To start downoading all of the videoclips and create a data-base, open the terminal go to the repository location and write
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
![Our Goal](../master/assets/our_goal.jpg)

*********

That's Us

![That's Us!](../master/assets/thats_us.jpg)

Yael Daihes       [GitHub](https://github.com/yooli3)   [LinkedIn](https://www.linkedin.com/in/yael-daihes/)

Yaara Arkin       [GitHub](https://github.com/yaarasegre)   [LinkedIn](https://www.linkedin.com/in/yaara-arkin-86706013/)

Orian Sharoni     [GitHub](https://github.com/Sharonio)   [LinkedIn](https://www.linkedin.com/in/orian-sharoni/)

Roee Shenberg     [GitHub](https://github.com/shenberg)   [LinkedIn](https://www.linkedin.com/in/roeeshenberg/)

Dalya Gartzman    [GitHub](https://github.com/DalyaG)   [LinkedIn](https://www.linkedin.com/in/dalya-gar/)


*********
