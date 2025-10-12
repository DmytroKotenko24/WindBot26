import pyrealsense2 as rs

BAG_OUTPUT = "saida_camera.bag"
NUM_FRAMES = 20  # número de frames a capturar

pipeline = rs.pipeline()
config = rs.config()
config.enable_record_to_file(BAG_OUTPUT)
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)  # ajuste conforme necessário

pipeline.start(config)
print(f"Gravando para {BAG_OUTPUT}, capturando {NUM_FRAMES} frames...")

for i in range(NUM_FRAMES):
    pipeline.wait_for_frames()
    print(f"Frame {i+1} capturado.")

pipeline.stop()
print("Gravação finalizada.")