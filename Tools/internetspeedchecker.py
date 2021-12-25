import pyspeedtest
s = pyspeedtest.Speedtest()

print("Testing....\n")

downloadspeed = s.download() / 1048576
uploadspeed = s.upload()/ 1048576
pingResult = round(s.results.ping)

print(f"Download speed: {downloadspeed}")
print(f"Upload speed: {uploadspeed}")
print(f"Ping: {pingResult} ms")