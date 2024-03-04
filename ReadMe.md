# Stable Diffusion WebUI Forgeの自動更新と起動

このPythonスクリプトは、Stable Diffusion WebUI Forgeの自動更新と起動を行います。

## 必要なソフトウェア

- Python 3.x
- Git

## インストール手順

1. このリポジトリをクローンするか、コードをダウンロードしてください。
2. 必要なソフトウェアをインストールしてください。
3. Python仮想環境をセットアップします（オプション）。

## 使用方法

1. スクリプトを実行します。
2. スクリプトは毎週月曜日に自動的に更新を行います。
3. 更新が完了すると、Stable Diffusion WebUI Forgeが起動します。

## 注意事項

- このスクリプトは、Windows環境でのみ動作します。
- スクリプトを実行する前に、必要なパスや環境変数を適切に設定してください。
- **このスクリプトは、Stable Diffusion WebUI Forgeが提供するワンクリックインストールパッケージを使用しているユーザーに限定されています。**

\# Stable Diffusion WebUI (A1111)のディレクトリの絶対パスを入力してください。

A1111_HOME = r"**\absolute\path\to\stable-diffusion-webui**"

\# Stable Diffusion WebUI Forge (lllyasviel)のディレクトリの絶対パスを入力してください。

WEB_UI_FORGE = r"**\absolute\path\to\Stable Diffusion WebUI Forge (lllyasviel)**"

\# Stable Diffusion WebUI Forge (lllyasviel)のwebuiフォルダの絶対パスを入力してください。

WEB_UI = r"**\absolute\path\to\Stable Diffusion WebUI Forge (lllyasviel)**\webui"

## Stable Diffusion WebUI (A1111)で使用されるディレクトリを指定済みです：

- --ckpt-dir: モデルのチェックポイントが格納されているディレクトリ
- --embeddings-dir: 埋め込みが格納されているディレクトリ
- --hypernetwork-dir: ハイパーネットワークが格納されているディレクトリ
- --lora-dir: Loraが格納されているディレクトリ

使用しない場合

`# === Normal ===`

`# COMMANDLINE_ARGS = [`

`#     "--theme", "dark"`

`# ]`

## ライセンス

このプロジェクトは MIT ライセンスのもとで公開されています。詳細については、[LICENSE](LICENSE) ファイルを参照してください。

---
### English version

# Automatic Update and Launch of Stable Diffusion WebUI Forge

This Python script automates the process of updating and launching Stable Diffusion WebUI Forge.

## Requirements

- Python 3.x
- Git

## Installation

1. Clone this repository or download the code.
2. Install the required software.
3. Set up a Python virtual environment (optional).

## Usage

1. Run the script.
2. The script automatically updates every Monday.
3. After the update is completed, Stable Diffusion WebUI Forge is launched.

## Notes

- This script works only on Windows environments.
- Before running the script, make sure to set up the necessary paths and environment variables properly.
- **This script is intended for users who are using the one-click installation package provided by Stable Diffusion WebUI Forge.**

\# Please input the absolute path of the directory where Stable Diffusion WebUI (A1111) is located.

A1111_HOME = r"**\absolute\path\to\stable-diffusion-webui**"

\# Please input the absolute path of the directory where Stable Diffusion WebUI Forge (lllyasviel) is located.

WEB_UI_FORGE = r"**\absolute\path\to\Stable Diffusion WebUI Forge (lllyasviel)**"

\# Please input the absolute path of the directory where the webui folder is located inside Stable Diffusion WebUI Forge (lllyasviel).

WEB_UI = r"**\absolute\path\to\Stable Diffusion WebUI Forge (lllyasviel)**\webui"

## Directory used by Stable Diffusion WebUI (A1111) already specified:

- --ckpt-dir: Directory where model checkpoints are stored.
- --embeddings-dir: Directory where embeddings are stored.
- --hypernetwork-dir: Directory where hypernetworks are stored.
- --lora-dir: Directory where Lora is stored.

If not used

`# === Normal ===`

`# COMMANDLINE_ARGS = [`

`#     "--theme", "dark"`

`# ]`

## License

This project is licensed under the MIT License. For more information, see the [LICENSE](LICENSE) file.
