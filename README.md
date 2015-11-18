# directory_syncer

Summary: With this webapp, I can update my Raspberry Pi with big files from the mothership

Features:

* Sync run: RSync job to synchronize a directory on the mothership server with the raspberry. RSync should work with SSH Keys so no passwords need to be entered
* Start a sync run from crontab / celery?
* Start a sync run from webapp
* Start a sync run from Raspi GPIO Button
* Notify external source (Raspi RGB LED):
  * Is a sync run going on? Pulsating light
  * Has there been an error in the last sync run? Red light¨
  * Has the last sync run successfully downloaded some files? Green light &amp; run external command (Kodi Refresh?)
* Webapp during sync: Shows progress and ETA
* Webapp after sync: Shows results of last sync run, list of downloaded files
