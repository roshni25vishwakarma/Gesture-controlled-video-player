 from sys import modules


import vlc.modules
import vlc
 
# creating vlc media player object
media = vlc.MediaPlayer("1.mp4")
 
# start playing video
media.play()

import time, vlc
 
# method to play video
def video(source):
   vlc_instance = vlc.Instance()
     
    # creating a media player
    player = vlc_instance.media_player_new()
     
    # creating a media
    media = vlc_instance.media_new(source)
     
    # setting media to the player
    player.set_media(media)
     
    # play the video
    player.play()
     
    # wait time
    time.sleep(0.5)
     
    # getting the duration of the video
    duration = player.get_length()
     
    # printing the duration of the video
    print("Duration : " + str(duration))
     
    # call the video method
    video("your_video.mp4")

