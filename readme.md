以下は、上記のコードの概要と使用方法を記述したREADME.mdファイルの例です。このファイルをプロジェクトのルートディレクトリに配置することで、他の開発者やユーザに対してコードの説明や実行方法を提供できます。

```
# Interactive Video Splitting

このPythonスクリプトは、指定されたフォルダ内の動画ファイルを対話的に分割するためのツールです。動画ファイルをユーザIDごとに3つに分割し、それぞれのファイルを適切なフォルダに格納します。

## 必要なもの

- Python 3.x
- FFmpeg

## インストール

FFmpegのインストール:

```shell
pip install ffmpeg-python
```

## 使用方法

1. プロジェクトのルートディレクトリに移動します。

2. `main.py`スクリプトを開き、以下の行で指定された箇所を編集します。

    ```python
    # フォルダのパスを指定
    folder_path = 'D:/syozemi2023/20230530'

    # 動画の発表順のユーザIDが格納されたリスト
    user_ids = ["s202309", "s202313", "s202310", "s202306", "s202308", "s202311", "s202301"]
    ```

3. ターミナルまたはコマンドプロンプトを開き、プロジェクトのルートディレクトリに移動します。

4. 以下のコマンドを実行します。

    ```shell
    python main.py
    ```

5. 指定されたフォルダ内の動画ファイルを順に処理します。各動画ファイルに対して、ユーザIDと分割タイムスタンプを入力します。

6. 分割された動画ファイルは、指定したフォルダと同じ階層に生成された「presentation」と「question」という名前のフォルダに格納されます。

7. ログには各処理のステータスやファイルパスが表示されます。

## 注意事項

- FFmpegが正しくインストールされていることを確認してください。
- このスクリプトは動作確認が行われていないため、使用時には十分なテストとエラーハンドリングが必要です。