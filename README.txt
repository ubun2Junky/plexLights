PlexLights

Is a simple script that will allow Tautulli to launch a script and automate your home theatre lights by sending commands to your Vera smart home controller.

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
		Description: Movie Play - Lights Off

	-  [Triggers]
		Playback Start (check)

	-  [Conditions]
