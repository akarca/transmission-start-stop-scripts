import transmissionrpc
tc = transmissionrpc.Client('localhost', port=9091)
torrents = tc.get_torrents()

print "Stopping %s torrents" % len(torrents)

for torrent in torrents:
    tc.stop(torrent.id)
