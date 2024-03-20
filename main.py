from moviepy.editor import VideoFileClip
import os

# Caminho para o vídeo de entrada
video_path = "./video_exmplo1.mp4"

# Carrega o vídeo usando VideoFileClip
video = VideoFileClip(video_path)

# Define a taxa de captura de frames (1 frame a cada 3 segundos)
frame_rate = 1 / 3

# Cria o diretório para salvar os frames, se não existir
output_directory = "./resultado"
os.makedirs(output_directory, exist_ok=True)

# Loop através do vídeo
for i, frame in enumerate(video.iter_frames(fps=video.fps)):
    if i % (video.fps * 3) == 0:  # Salva um frame a cada 3 segundos
        frame_output_path = os.path.join(output_directory, f"frame_{i}.jpg")
        video.save_frame(frame_output_path, t=i/video.fps)

# Fecha o vídeo
video.close()
