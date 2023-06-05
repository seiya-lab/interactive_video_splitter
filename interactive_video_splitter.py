import os
import subprocess

# FFmpegのインストールが必要です。インストールされていない場合は、以下のコマンドを使用してインストールしてください。
# !pip install ffmpeg-python

def split_video(input_file, timestamps, user_ids):
    # ファイル名と拡張子を分割
    file_name, extension = os.path.splitext(input_file)
    
    # 分割後のファイル名を生成
    # ファイルの名前は、ユーザidと対応している
    folder_names = ["", "presentation", "question"]
    output_files = [os.path.join(folder, folder + "_" + user_ids[i] + extension) for i, folder in enumerate(folder_names)]
    output_files = [os.path.join(folder, folder + "_" + file_name + extension) for folder in folder_names]
    
    # FFmpegを使用して動画を分割
    for i in range(2):
        command = ['ffmpeg', '-i', input_file, '-ss', timestamps[i], '-to', timestamps[i+1], '-c', 'copy', output_files[i+1]]
        subprocess.run(command)
        print(f"Split {input_file} into {output_files[i+1]}")
    
    # 1つ目のファイルは元ファイルをそのまま使用
    output_files[0] = input_file
    
    print("Splitting completed successfully.")

def interactive_video_splitting(folder, user_ids):
    # 指定されたフォルダ内のすべてのMP4ファイルを取得
    # 隠しファイルを除く
    file_list = [file for file in os.listdir(folder) if file.endswith(".mp4")]
    file_list = [file for file in file_list if not file.startswith(".")]
    
    # フォルダのファイル数とユーザidの数が一致するか確認
    if len(file_list) != len(user_ids):
        print("The number of files in the specified folder does not match the number of user ids. file_list: ", len(file_list), " user_ids: ", len(user_ids))
        return
    
    #file_listを時系列の早い順に並び替え
    file_list.sort()
    
    # 動画は、以下のユーザidと対応している
    
    if not file_list:
        print("No MP4 files found in the specified folder.")
        return
    
    for file in file_list:
        file_path = os.path.join(folder, file)
        timestamps = []
        
        # 現在の動画ファイル名を表示
        print("Current file: ", file)
        
        # 区切りのタイムスタンプを入力
        for i in range(2):
            timestamp = input(f"Enter the timestamp (mm:ss) to split {file} (part {i+1}): ")
            timestamps.append(timestamp)
        
        # 3つに分割
        split_video(file_path, timestamps)
    
    print("All files processed successfully.")

# フォルダのパスを指定
folder_path = 'D:/syozemi2023/20230530'

# 動画の発表順のユーザidが格納されたリスト
user_ids = ["s202309", "s202313", "s202310", "s202306", "s202308", "s202311", "s202301"]

# フォルダが存在することを確認
if not os.path.isdir(folder_path):
    print("The specified folder does not exist.")
else:
    # 対話的な動画分割の実行
    interactive_video_splitting(folder_path, user_ids)