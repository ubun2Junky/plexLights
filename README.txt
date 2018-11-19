PlexLights

Is a simple script that will allow Tautulli to launch a script and automate your home theatre lights by sending commands to your Vera smart home controller.

Quick Reference:

usage: plexLights.py [-h] [--loglvl 10] [--action ACTION] [--media MEDIA]
                     {vera,smartthings} controllerIP controllerPort daynightID
                     sceneID

Plex home theatre light controller script.

positional arguments:
  {vera,smartthings}    Select between vera or smartthings controller
  controllerIP          IP of the controller.
  controllerPort        Port the controller is connected to.
  daynightID            Object ID on controller
  sceneID               Scene ID on controller

optional arguments:
  -h, --help            show this help message and exit
  --loglvl 10, -l 10    log detail (10 info, 20 debug)
  --action ACTION, -a ACTION
                        Trigger action
  --media MEDIA, -m MEDIA
                        Media type 

Requirements:

You will need to have a Plex Media Server (of course), Tautulli installed and configured.  You will also need to assign static IP address for your Vera home controller and all Plex Media Player you need to reference.

Installation:

Place this script in the /config/jbops directory of your Tautulli application.

Configuration:

1.  Need to create three scenes on your Vera controller.  Take note of the scene ID when you complete setting up the scene.  You will need it later.  (Refer to vera documentation to setup up scenes on vera.)

	-  Movie Play:  This is the state in which you want your lights when the movie is playing.  I normally set my dimmers to off.

	-  Movie Pause:  This is the state in which you want your lights when the media has been paused.  I normally set my dimmers to 50%.

	-  Movie Stopped:  This is the state in which you want your lights when the media has been stopped.  I normally set my dimmers to 100%.

2.  Need to install "Day or Night" app in your Vera.  Once the app has been installed get device #.

3.  Need to get Vera controller IP and port information.  The default value for the port is 3480.

4.  Create triggers in Tautulli.

	-  Create new 'notification agent', Tautulli -> Settings -> Notification Agents -> 'Add new notification agent' -> Script

	-  [Configuration]
		Script Folder:  /config/jbops/plexLights
		Script File: ./plexLights.py
		Description: Living Room - Movie Lights Control
		SAVE

	-  [Triggers]
		Playback Start (check)
		Playback Stop (check)
		Playback Pause (check)
		Playback Resume (check)
		SAVE

	-  [Conditions]
		Condition 1:
		'IP Address' 'is' <IP address of your plex media player>

		Condition 2:
		'Media type' 'is' 'movie'  (options are movie and episode for tv shows)
		SAVE

	- [Arguments]
		Playback Start:
		vera <IP address of Vera> <veraPort> <DayNightID> <SceneID> -a {action} -m {media_type}

			<IP Address of vera>:  This is the static IP address of vera controller.

			<veraPort>:  By default the value is 3480, you can add a different value here if your port number is different.
			
			<DayNightID>:  This is the device ID that you got from the day or night app in your Vera controller.

			<sceneID>:  The scene id of the scene, in this case we will use the scene id for 'Movie Play'.  This will be a numberic value.

			{action} & {media_type}:  These values are provided by Tautulli.  These are for debugging purposes.

		SAVE

You should now see a orange bell, meaning the script is active.  You can try running a movie on your plex media player, view the logs in Tautulli and see if the script is getting triggered.  view logs -> Notification Logs.  The script should trigger when you play, pause, stop and resume your movie.

You can create different scenarios for different media types.  If you enjoy watching movies with no lights vs perhaps just dimming the lights when watching a tv series.




