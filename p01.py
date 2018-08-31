from hyper import HTTP20Connection

http2_client = HTTP20Connection("www.sohu.com:443")
http2_client.connect()

for i in range(1,1000):
	stream = http2_client.request('GET', "/get", body=None, headers=None)
	print("stream id  = {0}".format(stream))
	res = http2_client.get_response(stream)
http2_client.close()