import pyrealsense2 as rs

BAG_OUTPUT = "Scan_Porta.bag"
NUM_FRAMES = 20  

pipeline = rs.pipeline()
config = rs.config()
config.enable_record_to_file(BAG_OUTPUT)
config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 6)  

spatial_magnitude = 2  
spatial_smooth_alpha = 0.3  
spatial_smooth_delta = 30  
spatial_holes_fill = 1  

filter_spatial = rs.spatial_filter()
filter_spatial.set_option(rs.option.filter_magnitude, spatial_magnitude)
filter_spatial.set_option(rs.option.filter_smooth_alpha, spatial_smooth_alpha)
filter_spatial.set_option(rs.option.filter_smooth_delta, spatial_smooth_delta)
filter_spatial.set_option(rs.option.holes_fill, spatial_holes_fill)

filter_temporal = rs.temporal_filter(smooth_alpha=0.6, smooth_delta=50, persistence_control=3) 

pipeline.start(config)
print(f"Gravando para {BAG_OUTPUT}, capturando {NUM_FRAMES} frames...")

for i in range(NUM_FRAMES):
    frames = pipeline.wait_for_frames()
    depth_frame = frames.get_depth_frame()
    if not depth_frame:
        continue
    depth_filtered = filter_spatial.process(depth_frame)
    depth_filtered = filter_temporal.process(depth_filtered)
    print(f"Frame {i+1} capturado e filtrado.")

pipeline.stop()
print("Gravação finalizada.")