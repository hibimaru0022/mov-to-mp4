import os
from moviepy.editor import VideoFileClip


def convert_mov_to_mp4(input_file, output_file):
    try:
        video_clip = VideoFileClip(input_file)
        video_clip.write_videofile(output_file, codec='libx264')
        print(f"Conversion complete: {output_file}")
    except Exception as e:
        print(f"Error during conversion: {e}")


input_directory = 'input_movie_folder'  # 変換したいファイルがあるディレクトリのパス
output_directory = 'output_movie_folder'  # 変換後変換後のファイルを保存保存するディレクトリのパス

# all directory change to mp4 file
for file_name in os.listdir(input_directory):
    if file_name.endswith('mov'):
        input_path = os.path.join(input_directory, file_name)
        output_path = os.path.join(
            output_directory, file_name.replace('mov', 'mp4'))
        convert_mov_to_mp4(input_path, output_path)
