#py -3.6 -m pip install pyrealsense2

#py -3.6 filename.py
import pyrealsense2 as rs

try:
  pipeline=rs.pipeline()
  pipeline.start()
  print("started")
  bottomCutoff=0.1 #critical distance range to ignore erroneous measurements
  topCutoff=1.05 #critical distance range
  for i in range(100):
        criticalCount=0 #ammount of points in a dangerous distance
        leftCount=0 #ammount of critical points on left side
        rightCount=0 #ammount of critical points on right side
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

        print("Total count: "+str(100*criticalCount/(480*640)))
        print("Left count: "+str(100*leftCount/(480*640)))
        print("Right count: "+str(100*rightCount/(480*640))+"\n")

except Exception as e:
  print(e)
  pass