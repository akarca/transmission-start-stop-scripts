# transmission-start-stop-scripts
Transmission-daemon Start and Stop Scripts

I'm using my raspberrypi as a media server. This scripts help me to schedule torrenting.

Example crontab entry to start all torrents at 2 am:

0 2 * * * python /home/osmc/transmission-start-stop-scripts/start_all_torrents.py

And stop all torrents at 8 am:

0 8 * * * python /home/osmc/transmission-start-stop-scripts/stop_all_torrents.py
