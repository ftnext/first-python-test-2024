準備
====================

https://github.com/ftnext/first-python-test-2024 を開きます

| どちらかを選んでください。
| おすすめは選択肢1️⃣です。

選択肢1️⃣ ローカル開発環境
------------------------------

お手元のPCにPython環境が必要です。

本リポジトリをclone（またはZIPダウンロード）

.. image:: _static/local.png

:file:`start` ディレクトリで進めます

Python 3.10以上（`Structural Pattern Matching <https://docs.python.org/ja/3.13/whatsnew/3.10.html#pep-634-structural-pattern-matching>`__ を使いたいため）

.. code-block:: shell

    $ python -m venv .venv --upgrade-deps
    $ source .venv/bin/activate
    $ python -m pip install -e '.[dev]'

| pytestとプロジェクトをインストールする
| （プロジェクト、かつ再配布できるようにすると便利です）

選択肢2️⃣ GitHub Codespaces
------------------------------

ブラウザとGitHubアカウントだけ必要

.. image:: _static/codespaces.png

Codespacesは使い捨ての環境なので、仮想環境は不要です。

:file:`start` ディレクトリに移動して

.. code-block:: shell

    $ python -m pip install -e '.[dev]'

.. note:: Structural Pattern Matchingの日本語記事

    * `Python 3.10の新機能：構造化パターンマッチング <https://gihyo.jp/article/2022/07/monthly-python-2207>`__
    * `Pythonの構造的パターンマッチングのさらに便利なパターン紹介 <https://gihyo.jp/article/2024/01/monthly-python-2401>`__

.. note:: 標準に寄せたので uv お好きにどうぞ

    :file:`start` ディレクトリにて

    .. code-block:: shell

        $ uv pip install -e '.[dev]'
        $ uv run pytest
