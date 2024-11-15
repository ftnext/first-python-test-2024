準備
====================

| どちらかを選んでください。
| おすすめは選択肢1️⃣です。

選択肢1️⃣ ローカル開発環境
------------------------------

お手元のPCにPython環境が必要です。

本リポジトリをclone

:file:`start` ディレクトリで進めます

Python 3.10以上（Structural Pattern Matchingを使いたいため）

.. code-block:: shell

    $ python -m venv .venv --upgrade-deps
    $ source .venv/bin/activate
    $ python -m pip install -e '.[dev]'

| pytestとプロジェクトをインストールする
| （プロジェクト、かつ再配布できるようにすると便利です）

選択肢2️⃣ GitHub Codespaces
------------------------------

ブラウザとGitHubアカウントだけ必要

.. TODO Codespaceの場合

.. note:: 標準に寄せたので uv, Hatch お好きにどうぞ
