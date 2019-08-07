import pyrealsense2 as rs

try:
  pipeline=rs.pipeline()
  pipeline.start()
  print("started")
  count=40
  while(count>=0):
    totalDist=0
    frames=pipeline.wait_for_frames()
    depth=frames.get_depth_frame()
    coverage = [0]*64
    for y in range(480):
        for x in range(640):
            dist = depth.get_distance(x, y)
            if(dist!=0):
              totalDist+=dist
            '''
            if 0 < dist and dist < 1:
                coverage[x//10] += 1 '''
    print(100*totalDist/(480*600))
    count=count-1

except Exception as e:
  print(e)
  pass