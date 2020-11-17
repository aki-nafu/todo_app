# 元となるイメージを指定
FROM python:3
# バッファにデータを保持しない設定(1でなくても任意の文字でいい)
ENV PYTHONUNBUFFERED 1
# コンテナの中にディレクトリを作成
RUN mkdir /app
# 作業ディレクトリを指定
WORKDIR /app
# pipでインストールするパッケージをまとめたファイルを /appディレクトリにコピー
COPY requirements.txt /app/
RUN pip install -r requirements.txt
# ローカルのDockerfileを設置したディレクトリ内のファイルをコンテナの/appディレクトリへコピー
COPY . /app/