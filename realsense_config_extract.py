import pyrealsense2 as rs

# Create a pipeline and config
pipeline = rs.pipeline()
config = rs.config()

# Tell config to use the bag file
config.enable_device_from_file(r"/home/dmytro-overlord/VSCode_Workspace/p1.bag") 

# Start streaming from file
profile = pipeline.start(config)

# Get stream profiles
for stream in profile.get_streams():
    intrinsics = stream.as_video_stream_profile().get_intrinsics()
    print(f"Stream type: {stream.stream_type()}, Width: {intrinsics.width}, Height: {intrinsics.height}")
    print(f"Intrinsics: {intrinsics}")

# You can also get extrinsics between streams if needed

"""
**Depth Stream**
- Resolution: 1280x720
- Principal Point (p): [632.716, 367.241]
- Focal Length (f): [905.397, 905.397]
- Distortion Model: Brown Conrady
- Distortion Coefficients: [0, 0, 0, 0, 0]

**Infrared Stream (Left & Right)**
- Resolution: 1280x720
- Principal Point (p): [632.716, 367.241]
- Focal Length (f): [905.397, 905.397]
- Distortion Model: Brown Conrady
- Distortion Coefficients: [0, 0, 0, 0, 0]

**Color Stream**
- Resolution: 1280x720
- Principal Point (p): [634.238, 361.73]
- Focal Length (f): [916.872, 914.933]
- Distortion Model: Inverse Brown Conrady
- Distortion Coefficients: [0, 0, 0, 0, 0]
"""