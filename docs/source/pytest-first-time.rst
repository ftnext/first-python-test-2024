テストコード
========================================

テストコードが書けると何がいいのか
----------------------------------------

不安は **退屈** に変わる

https://ftnext.github.io/2023-slides/pyconapac/practice-test-code.html#/6

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

.. note:: 表明なるもの

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

キーワード src-layout

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

:pass: テストが通る（すべてのテストが成功）
:fail: テストが落ちる（1つでもテストが失敗）

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

FizzBuzzのテストコードを書いてみよう
========================================

| たっぷり練習しましょう。
| 「私テストコード書けるんじゃない！？」とぜひ思ってください

.. code-block:: python
    :caption: src/fizzbuzz/core.py

    def fizzbuzz(number: int) -> str:
        match number % 3, number % 5:
            case 0, 0: return "FizzBuzz"
            case 0, _: return "Fizz"
            case _, 0: return "Buzz"
            case _, _: return str(number)

https://gihyo.jp/news/report/01/pyconjp2021/0002#sec1

| :file:`tests/test_core.py` を書いてみよう。
| 「3の倍数のときはFizzを返す」

まずはテストの関数を書く

.. code-block:: python
    :caption: tests/test_core.py

    def test_3の倍数のときはFizzを返す():
        # 後述

* 3の倍数を渡して ``fizzbuzz`` 関数を呼び出す

    * 3の倍数としてなにか1つ値を選ぶ（例 ``3``）

* 返り値は ``Fizz`` になるはず

呼び出すところまで書いてみる

.. code-block:: python
    :caption: tests/test_core.py

    from fizzbuzz.core import fizzbuzz

    def test_3の倍数のときはFizzを返す():
        _ = fizzbuzz(3)

「返り値は ``Fizz`` になるはず」、``assert`` の出番！

.. code-block:: python
    :caption: tests/test_core.py

    from fizzbuzz.core import fizzbuzz

    def test_3の倍数のときはFizzを返す():
        assert fizzbuzz(3) == "Fizz"

テストが書けました！！

テストを実行すると、（``fizzbuzz`` 関数は完成しているので）通ります。

``fizzbuzz`` 関数を壊すと、テストは落ちます（壊したことに気づける！）

.. note:: pytestはassert文を拡張（だから出力が変わっている）

おすすめの実行方法

* :command:`pytest -vv`
* :command:`pytest --ff`
* ケースの指定 ``pytest tests/test_practice.py::test_環境構築の確認``

.. note:: 日本語テストメソッド

    https://t-wada.hatenablog.jp/entry/design-for-testability#%E3%83%9D%E3%82%A4%E3%83%B3%E3%83%88-%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%83%86%E3%82%B9%E3%83%88%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89

3A
--------------------

| あえて回りくどく書いてみる
| 「テスト対象を実行した値は、期待結果と一致する」

.. code-block:: python
    :caption: tests/test_core.py

    def test_3の倍数のときはFizzを返す():
        number = 3
        actual = fizzbuzz(number)

        expected = "Fizz"
        assert actual == expected

:actual: テスト対象を実行した値
:expected: 期待結果

3A、すなわち3つのA

https://xp123.com/articles/3a-arrange-act-assert/

* Arrange 準備
* Act 実行
* Assert 検証

.. code-block:: python
    :caption: tests/test_core.py

    def test_3の倍数のときはFizzを返す():
        # Arrange: テストの準備（データの用意など）
        number = 3

        # Act: テスト対象の関数を実行
        actual = fizzbuzz(number)

        # Assert: 実行結果が期待値と等しいかを検証
        expected = "Fizz"
        assert actual == expected

先のテスト（``assert fizzbuzz(3) == "Fizz"``）は

1. Arrange と Act を書いた（``fizzbuzz(3)``）
2. Assert を書いた

.. note:: テストはAssertから書く

    個人的にはどこから書いてもよいと思っている。
    Assertから書くと「Actが必要だ」「Arrangeが必要だ」と詰まらずに書きやすい印象があるので、初めての方は試してみてもいいかも

なにか1つ、テストを書いてみましょう

* 5の倍数のとき
* 15の倍数のとき
* 3の倍数でも5の倍数でもないとき

.. note:: assertの一覧

    TODO actualを使った表を書こう

.. note:: クラスを使ってテストケースを構造化できる

.. note:: pytest-watch

pytestはテストコードを書くのをサポートする
--------------------------------------------------

テストの概念

* パラメタ化テスト
* モック

pytestの機能

* pytestのフィクスチャ

パラメタ化テスト
^^^^^^^^^^^^^^^^^^^^

🙅‍♂️「3の倍数のテストで、複数の値を実行しちゃえ」

.. code-block:: python
    :caption: よくない例

    def test_3の倍数のときはFizzを返す():
        assert fizzbuzz(3) == "Fizz"
        assert fizzbuzz(6) == "Fizz"
        assert fizzbuzz(9) == "Fizz"

.. note:: アサーションルーレット（アンチパターン）

    https://t-wada.hatenablog.jp/entry/design-for-testability#%E3%83%9D%E3%82%A4%E3%83%B3%E3%83%88-%E3%82%A2%E3%82%B5%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%AB%E3%83%BC%E3%83%AC%E3%83%83%E3%83%88Assertion-Roulette

では、個別にテストの関数を書くのか？

.. code-block:: python
    :caption: アサーションルーレットをしないためにこうする？

    def test_3の倍数のときはFizzを返す_3の場合():
        assert fizzbuzz(3) == "Fizz"
    

    def test_3の倍数のときはFizzを返す_6の場合():
        assert fizzbuzz(6) == "Fizz"

**パラメタ化テスト**

https://t-wada.hatenablog.jp/entry/design-for-testability#%E3%83%9D%E3%82%A4%E3%83%B3%E3%83%88-%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E5%8C%96%E3%83%86%E3%82%B9%E3%83%88Parameterized-Test

    ほぼ同じテスト内容でデータだけを変えたテストメソッドを（列挙であれループであれ）書いているときに、テストメソッドにパラメータを渡せればいいのに、と感じることがあると思います。

pytestにおいては、テストケースの関数を ``@pytest.mark.parametrize`` でデコレートする

.. code-block:: python
    :caption: tests/test_core.py

    import pytest

    from fizzbuzz.core import fizzbuzz


    @pytest.mark.parametrize("number", [3, 6])
    def test_3の倍数のときはFizzを返す(number):
        assert fizzbuzz(number) == "Fizz"

モック
^^^^^^^^^^^^^^^^^^^^

pytestのフィクスチャを使う
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

小まとめ
--------------------

「（本ワークショップで）体験する概念」の1と2をカバーしました

* テスティングフレームワークpytestを使って、テストコードを書いた
* ここで書いたのは開発者のためのテスト（品質保証のためのテストではない）
