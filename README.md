# edit-debian-squashfs
これは、Debianのsquashfsファイルを編集するためのスクリプトです。
# 使い方
このコマンドは基本的にスーパーユーザー権限で実行してください。

これとは別途にカスタマイズするためのファイルやインターネット環境、squashfsファイルが必要です。さらに最後は手動でsquashfsファイルを`sudo mksquashfs squashfs-root/ filesystem.squashfs`のように再構築する必要があります。
## 引数一覧
#### `-f` または `--filesystem`
この引数は必須です。squashfsファイルを指定してください。

`-f ../filesystem.squashfs`のような感じで使用してください。
#### `-a`または`--add`
この引数を使用することでファイルシステム内にファイルをコピー出来ます。

`-a /path/to/hoge /path/to/fuga`のような感じで使用してください。
#### `-r`または`--remove`
この引数を使用することでファイルシステム内のファイルを削除出来ます。

`-r /path/to/hoge`のような感じで使用してください。
#### `-p`または`--purge`
この引数を使用することでファイルシステム内のパッケージを削除出来ます。

`-p gnome`のような感じで使用してください。
#### `-i`または`--install`
この引数を使用することでファイルシステム内にパッケージをインストール出来ます。

`-i foo`のような感じで使用してください。
#### `-d`または`--debfile`
この引数を使用することでファイルシステム内にdebファイルをインストール出来ます。

`-d /path/to/foo.deb`のような感じで使用してください。
## サンプル
~~~
sudo python3 build.py \
	-f ~/Downloads/filesystem.squashfs\
	-a /usr/share/plymouth/themes/plymouth-theme /usr/share/plymouth/themes/\
	-i fcitx-mozc\
	-p firefox-esr\
~~~
