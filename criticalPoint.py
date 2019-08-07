#py -3.6 -m pip install pyrealsense2
#py -3.6 filename.py
#can either just run file or run init_Camera()
# #10% is cutoff

import pyrealsense2 as rs
import time
  
def readCamera(pipeline):
  try:
    testTime=time.time()
    prevTime=0
    while(True):
      prevTime=testTime
      testTime=time.time()
      diff=testTime-prevTime
      print(diff)
      #time.sleep(0.18)
      criticalCount=0 #ammount of points in a dangerous distance
      leftCount=0 #ammount of critical points on left side
      rightCount=0 #ammount of critical points on right side
      bottomCutoff=0.1 #critical distance range to ignore erroneous measurements
      topCutoff=1.1 #critical distance range
      frames=pipeline.wait_for_frames()
      depth=frames.get_depth_frame()
      for y in range(480):
          for x in range(640):
              dist = depth.get_distance(x, y)
              
              if(dist>bottomCutoff and dist<topCutoff):
                criticalCount+=1
                if(x<320):
                  leftCount+=1
                else:
                  rightCount+=1
      criticalPercent=100*criticalCount/(480*640)
      leftPercent=100*leftCount/(480*640)
      rightPercent=100*rightCount/(480*640)
      if(criticalPercent>15 or leftPercent>10 or rightPercent>10): #critical cutoff is set to 15
        if(leftPercent>rightPercent):
          print("left")
        else:
          print("right")
      else:
        print("okay")
      
      print("Total count: "+str(criticalPercent)+"   Left count: "+str(leftPercent)+"   Right count: "+str(rightPercent)+"\n")
  except Exception as e:
    print(e)
    pass

def init_Camera():
  try:
    pipeline=rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
    pipeline.start(config)
    print("started")
    readCamera(pipeline)
  except Exception as e:
    print(e)
    pass

try:
  pipeline=rs.pipeline()
  config = rs.config()
  config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
  pipeline.start(config)
  print("started")
  readCamera(pipeline)
except Exception as e:
  print(e)
  pass