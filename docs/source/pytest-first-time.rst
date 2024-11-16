入門 テストコード
========================================

テストコードが書けると何がいいのか
----------------------------------------

* 良いコード（変更しやすい、言語の機能を引き出している）に **近づけていく**
* 今の全霊をかけたコードだが、よりよい書き方を知ったら書き換えたい

| 変更するたびに、壊していないか不安
| 壊す＝振る舞いを変えてしまう

3つのアプローチ

* 祈る 🙏🙏「どうか変わっていませんように」🙏🙏

    * 不安だけど確認はしない

* 手で動作確認 ✋

    * 対話モードでimportして動作確認
    * 確認するので安心できるが、関数の数が増えると現実的でない

* コードを書いて動作確認 🤖（自動テスト）

    * 「手で動作確認」の自動化
    * プログラムで使う部品のコードは、プログラムを書いて動作確認（ちょうぜつ本）
    * 自動化しているので繰り返し確認できる

| 自動テストにより、変更して振る舞いを変えていないかという不安は **退屈** に変わる
| 「自動テストが1つも失敗していないから振る舞いは変わってない！」（*回帰テスト*）

| このテストは開発者のためのもの（開発中に自信を持てる）
| 品質保証のためのテストは別に必要です

IMO：テストコード書かないなんて、 *もったいない* ですよ

``assert`` 文
--------------------

:前提: :file:`start` ディレクトリにいます

対話モード

.. code-block:: pycon

    >>> assert True
    >>> assert False
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AssertionError

.. code-block:: pycon
    :caption: ``True`` と評価される式と ``assert``

    >>> 1 == 1
    True
    >>> assert 1 == 1

.. code-block:: pycon
    :caption: ``False`` と評価される式と ``assert``

    >>> 1 == 2
    False
    >>> assert 1 == 2
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AssertionError

書いてみて練習しよう（別の数字、別の型）

.. note:: assert文のドキュメント

    言語リファレンス `7.3. assert 文 <https://docs.python.org/ja/3/reference/simple_stmts.html#the-assert-statement>`__

.. note:: 表明なるもの

    「``assert`` って（pytestのテストコード以外で）どこで使うの？」と思った方へ

    .. raw:: html

        <iframe class="speakerdeck-iframe" style="border: 0px; background: rgba(0, 0, 0, 0.1) padding-box; margin: 0px; padding: 0px; border-radius: 6px; box-shadow: rgba(0, 0, 0, 0.2) 0px 5px 40px; width: 100%; height: auto; aspect-ratio: 560 / 420;" frameborder="0" src="https://speakerdeck.com/player/68b40ca9983a48dc9efec540ab98f88d?slide=69" title="PHP7 で堅牢なコードを書く - 例外処理、表明プログラミング、契約による設計 / PHP Conference 2016" allowfullscreen="true" data-ratio="1.3333333333333333"></iframe>

ディレクトリ構成
--------------------

pytestは

* ファイルを置く
* ``assert`` を使って関数を書く（後述）

現在

.. code-block::

    start/
    ├── src/
    │   └── fizzbuzz/
    │       ├── __init__.py
    │       └── core.py
    ├── tests/
    │   ├── __init__.py
    │   └── test_practice.py
    └── pyproject.toml

このように育ちます（イメージです）

.. code-block::

    start/
    ├── src/
    │   └── fizzbuzz/
    │       ├── __init__.py
    │       └── core.py
    ├── tests/
    │   ├── __init__.py
    │   ├── test_core.py
    │   └── test_fizzbuzz.py
    └── pyproject.toml

| 影響 `unittestで始めるユニットテスト入門 (PyCon JP 2019) <https://pycon.jp/2019/schedule/?sessionId=213>`__
| https://docs.google.com/presentation/d/1F0fkcbuuQBCbVDLD2v8YQlMOqEMnF_PpI2AAR5nwhfI/edit#slide=id.g628217d75a_0_0

.. note:: キーワード src-layout

    :file:`src` ディレクトリを作るやり方。OSSのライブラリではこちらが主流

    `src レイアウト対フラットレイアウト <https://packaging.python.org/ja/latest/discussions/src-layout-vs-flat-layout/>`__

テストを実行
--------------------

テストが1つ用意されています。

.. literalinclude:: ../../start/tests/test_practice.py
    :language: python

このテストを実行してみましょう。

:command:`pytest`

.. code-block:: shell

    (.venv) $ pytest
    ================================== test session starts ==================================
    platform darwin -- Python 3.12.6, pytest-8.3.3, pluggy-1.5.0
    rootdir: /.../first-python-test-2024/start
    configfile: pyproject.toml
    collected 1 item                                                                        

    tests/test_practice.py F                                                          [100%]

    ======================================= FAILURES ========================================
    _____________________________________ test_環境構築の確認 ______________________________________

        def test_環境構築の確認():
    >       assert False
    E       assert False

    tests/test_practice.py:2: AssertionError
    ================================ short test summary info ================================
    FAILED tests/test_practice.py::test_環境構築の確認 - assert False
    =================================== 1 failed in 0.02s ===================================

用語紹介

:pass: テストが通る（すべてのテストが成功。pytestでは . が並ぶ）
:fail: テストが落ちる（1つでもテストが失敗。F（やE）が1つ以上ある）

何をしたのか
--------------------

* :command:`pytest` と実行したら ``test_環境構築の確認`` が落ちた
* ``assert False`` と書いているので、落ちるのは当然
* なぜこんなことをした？

``assert False`` で落ちることを確認したかった

* 環境構築に失敗したら他のところで落ちる
* 環境構築できているから ``assert False`` で落ちる

``assert True`` に書き換えたら？ -> 通る！🙌

.. code-block:: shell

    (.venv) $ pytest
    ================================== test session starts ==================================
    platform darwin -- Python 3.12.6, pytest-8.3.3, pluggy-1.5.0
    rootdir: /.../first-python-test-2024/start
    configfile: pyproject.toml
    collected 1 item                                                                        

    tests/test_practice.py .                                                          [100%]

    =================================== 1 passed in 0.01s ===================================

| 準備ができました！
| :file:`tests/test_practice.py` は環境構築の確認のためのものなので消して構いません

.. note:: ``assert False`` で始める儀式

    拙ブログより `assert Falseで始める儀式 <https://nikkie-ftnext.hatenablog.com/entry/stapy-88-yattom-san-talk-pytest#assert-False%E3%81%A7%E5%A7%8B%E3%82%81%E3%82%8B%E5%84%80%E5%BC%8F>`__

    最初はpytestの導入でつまづくこともあったので、新しいプロジェクトでこの儀式をしてました
