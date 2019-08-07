#py -3.6 -m pip install pyrealsense2

#py -3.6 filename.py
import pyrealsense2 as rs

try:
  pipeline=rs.pipeline()
  pipeline.start()
  print("started")
  totalDist=0
  frames=pipeline.wait_for_frames()
  depth=frames.get_depth_frame()
  coverage = [0]*64
  distList=""
  for y in range(480):
    for x in range(640):
        dist = depth.get_distance(x, y)
        distList+=str(dist)+"  "
        if(dist!=0):
          totalDist+=dist
    distList+="\n"
  print(distList)

except Exception as e:
  print(e)
  pass