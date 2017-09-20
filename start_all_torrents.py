import transmissionrpc

tc = transmissionrpc.Client('localhost', port=9091)
print "Starting all torrents"
tc.start_all()

