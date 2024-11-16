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

FizzBuzzのテストコードを書いてみよう
========================================

| たっぷり練習しましょう。
| 「私テストコード書けるんじゃない！？」とぜひ思ってください

なお、完成版は :file:`goal` の下にあります

.. code-block:: python
    :caption: src/fizzbuzz/core.py

    def fizzbuzz(number: int) -> str:
        match number % 3, number % 5:
            case 0, 0: return "FizzBuzz"
            case 0, _: return "Fizz"
            case _, 0: return "Buzz"
            case _, _: return str(number)

ref: `Day2 Keynote：A Perfect match ―Mr. Brandt Bucher (PyCon JP 2021 カンファレンスレポート) <https://gihyo.jp/news/report/01/pyconjp2021/0002#sec1>`__

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

    `Assertion Rewriting <https://docs.pytest.org/en/stable/how-to/writing_plugins.html#assertion-rewriting>`__

おすすめの実行方法

* :command:`pytest -vv`

    * ``--verbose``
    * ``-v`` でも詳しくなるが、 ``-vv`` だと ``assert A == B`` の差分がとても分かりやすい

* :command:`pytest --ff`

    * ``--failed-first``: 最後に落ちたテストから実行

* ケースの指定 :command:`pytest tests/test_practice.py::test_環境構築の確認`
* 『`テスト駆動Python 第2版`_』を一読すると、もっと知れます

.. note:: 日本語で書いてる！

    t-wadaさんのエントリの中の `日本語テストメソッド <https://t-wada.hatenablog.jp/entry/design-for-testability#%E3%83%9D%E3%82%A4%E3%83%B3%E3%83%88-%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%83%86%E3%82%B9%E3%83%88%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89>`__ より

        日本語でコミュニケーションをとっているプロジェクトの場合、日本語でテストメソッド名を書いても良いのではないかという考え方

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

:actual value: テスト対象を実行した値
:expected value: 期待結果

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

.. note:: ``assert`` の一覧

    .. list-table:: ``assert`` の形式（参考：『テスト駆動Python 第2版』表2-1）

        * - 検証したいこと
          - 書き方
        * - ``actual`` と ``expected`` が等しい
          - ``assert actual == expected``
        * - ``actual`` の期待値は ``True``
          - ``assert actual``
        * - ``actual`` の期待値は ``False``
          - ``assert not actual``
    
    ``assert actual is False`` より ``assert not actual`` の方がエラーメッセージが分かりやすくなります

.. note:: クラスを使ってテストケースを構造化できる

    TDDパートを参照

.. note:: pytest-watch

    テストを書いて毎回 :command:`pytest` している。

    | ファイルに変更があったら自動でpytestが流れるようにするライブラリがある。
    | https://pypi.org/project/pytest-watch/

    :command:`ptw -- -vv --ff`

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

1つのテストメソッドは、1つのことを検証しよう

* 3のとき
* 6のとき
* 9のとき

それぞれ分けたい

.. note:: アサーションルーレット（アンチパターン）

    t-wadaさんのエントリの中の `[ポイント] アサーションルーレット（Assertion Roulette） <https://t-wada.hatenablog.jp/entry/design-for-testability#%E3%83%9D%E3%82%A4%E3%83%B3%E3%83%88-%E3%82%A2%E3%82%B5%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%AB%E3%83%BC%E3%83%AC%E3%83%83%E3%83%88Assertion-Roulette>`__ より

        このテストが失敗したときに、どのアサーションが失敗したのかがわかりにくいのです。

では、個別にテストの関数を書くのか？

.. code-block:: python
    :caption: アサーションルーレットをしないためにこうする？

    def test_3の倍数のときはFizzを返す_3の場合():
        assert fizzbuzz(3) == "Fizz"
    

    def test_3の倍数のときはFizzを返す_6の場合():
        assert fizzbuzz(6) == "Fizz"

**パラメタ化テスト**

t-wadaさんエントリ `[ポイント] パラメータ化テスト（Parameterized Test） <https://t-wada.hatenablog.jp/entry/design-for-testability#%E3%83%9D%E3%82%A4%E3%83%B3%E3%83%88-%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E5%8C%96%E3%83%86%E3%82%B9%E3%83%88Parameterized-Test>`__ より

    ほぼ同じテスト内容でデータだけを変えたテストメソッドを（列挙であれループであれ）書いているときに、テストメソッドにパラメータを渡せればいいのに、と感じることがあると思います。

| pytestにおいては、テストケースの関数を ``@pytest.mark.parametrize`` でデコレートする
| `@pytest.mark.parametrize: parametrizing test functions <https://docs.pytest.org/en/stable/how-to/parametrize.html#pytest-mark-parametrize-parametrizing-test-functions>`__

.. code-block:: python
    :caption: tests/test_core.py

    import pytest

    from fizzbuzz.core import fizzbuzz


    @pytest.mark.parametrize("number", [3, 6])
    def test_3の倍数のときはFizzを返す(number):
        assert fizzbuzz(number) == "Fizz"

| 最初から狙ってやるものではなく、「パラメタ化できそう」と気づいたら適用するもの
| 参考：「*テストケースがない時に dataProvider から書かない*」（`拙ブログ <https://nikkie-ftnext.hatenablog.com/entry/phpcon-2022-unit-testing-for-beginners-log#2-%E6%98%8E%E6%97%A5%E3%81%8B%E3%82%89%E3%83%86%E3%82%B9%E3%83%88%E3%82%92%E5%AE%9F%E8%B7%B5%E3%81%99%E3%82%8B%E3%81%9F%E3%82%81%E3%81%AE%E7%9F%A5%E8%AD%98%E3%82%92%E5%BE%97%E3%82%8B-%E3%82%88%E3%82%8A>`__）

.. note:: parametrizeは積める

    拙ブログ `💡2️⃣ デコレータを複数積める（自動で組合せてくれる！） <https://nikkie-ftnext.hatenablog.com/entry/pytest-parametrize-tips-decorate-class-and-stack-multiple#2%EF%B8%8F%E2%83%A3-%E3%83%87%E3%82%B3%E3%83%AC%E3%83%BC%E3%82%BF%E3%82%92%E8%A4%87%E6%95%B0%E7%A9%8D%E3%82%81%E3%82%8B%E8%87%AA%E5%8B%95%E3%81%A7%E7%B5%84%E5%90%88%E3%81%9B%E3%81%A6%E3%81%8F%E3%82%8C%E3%82%8B>`__

.. note:: parametrizeと日本語

    エスケープされてしまう

    `pytestのtest IDにパラメータ由来の日本語を使う方法 <https://qiita.com/gimKondo/items/d7a874a97af1ad93052a>`__

    | 設定値 ``disable_test_id_escaping_and_forfeit_all_rights_to_community_support``
    | ただしこれも限定的（``pytest.param`` のidは未サポート）

pytestのフィクスチャを使う
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| フィクスチャを知った後の方がモックが説明しやすいため、紹介したときの順番と前後します。
| **pytestの概念** です

例えば、fizzbuzzの出力をテストするとしたら？

.. code-block:: python
    :caption: printする関数のテスト？

    def print_fizzbuzz(upper_limit: int) -> None:
        for number in range(1, upper_limit + 1):
            print(fizzbuzz(number))

pytestは機能を提供している

capsys (`Accessing captured output from a test function (How to capture stdout/stderr output) <https://docs.pytest.org/en/stable/how-to/capture-stdout-stderr.html#accessing-captured-output-from-a-test-function>`__)

capsysはpytestのビルトインのフィクスチャの1つ

フィクスチャは **テストの関数の引数に書く**

.. code-block:: python
    :caption: tests/test_core.py

    def test_fizzbuzzの出力のテスト(capsys):
        # 後述

* Actで標準出力を伴う関数を呼び出す
* Assertにおいて、``capsys.readouterr()`` を呼び出す

    * 標準出力は ``capsys.readouterr().out`` （これが ``actual``）
    * 標準出力が期待値と一致するかを ``assert``

.. note:: PyCon JP 2024より「あなたのアプリケーションをレガシーコードにしないための実践Pytest入門」

    | https://speakerdeck.com/mhrtech/pyconjp2024-pytest
    | pytestのフィクスチャ辞典

    （ただし、テスト駆動開発については、こちらの発表内容は誤解が見受けられるので注意（後述））

.. note:: pytestのtmp_pathフィクスチャ

    | 一時ディレクトリや一時ファイルを作ってくれる。
    | 標準出力ではなくFizzBuzzをファイルに書き込む場合は、tmp_pathフィクスチャを使ってテストできる

    `The tmp_path fixture (How to use temporary directories and files in tests) <https://docs.pytest.org/en/stable/how-to/tmp_path.html#the-tmp-path-fixture>`__

.. note:: capsysやtmp_pathは本当に必要ですか？（発表者の考え）

    テストにもいろいろ

    * 単体 unit
    * 結合 integration

    pytestは **幅広くテストをカバー** しているように思われる（単体も結合もどちらも書ける）

    | capsysフィクスチャを使えばテストを書けるが、私は ``print_fizzbuzz`` 関数のテストは書かなくてもよいと考える。
    | ただし、 **fizzbuzz関数は徹底的にテスト** してある前提で。
    | なぜなら、 ``print_fizzbuzz`` 関数は ``fizzbuzz`` 関数の出力を ``print`` するだけだから。

    「*テストする必要がないほど質素なコードにして、コードに恥をかかせる*」（拙ブログより「 `printはテストしないという考え方 <https://nikkie-ftnext.hatenablog.com/entry/pycon-apac-2023-practice-test-talk-extra-test-topics-commentary#print%E3%81%AF%E3%83%86%E3%82%B9%E3%83%88%E3%81%97%E3%81%AA%E3%81%84%E3%81%A8%E3%81%84%E3%81%86%E8%80%83%E3%81%88%E6%96%B9>`__ 」）

    | また、設計の観点から入出力と計算処理は分離したほうが、変更が容易になる（拙ブログ「` ソフトウェアを作りたかった私へ：入出力と計算を分ける <https://nikkie-ftnext.hatenablog.com/entry/sharply-distinguish-io-from-calculation>`__」）。
    | **計算処理を徹底的にテスト** し、入出力はテストする必要がないほど質素なコードにする。

    | 参考：単体・結合の分け方以外に
    | Googleによる `Test Sizes <https://testing.googleblog.com/2010/12/test-sizes.html>`__

モック
^^^^^^^^^^^^^^^^^^^^

モックとは、ニセモノ

たとえば、出力が変わる関数

.. literalinclude:: ../../goal/src/fizzbuzz/lottery.py
    :language: python

.. note:: モックの使い所

    * 時間のかかる処理のテストを書く
    * 外部と通信する処理のテストを書く

出力が変わると困るので、テストにおいては ``random.randint()`` をニセモノに置き換える

(1) pytestのmonkeypatchフィクスチャを使った例

.. code:: python

    def test_6の目が出たら超吉と返す(monkeypatch):
        randint_call_count = 0

        def randint_mock(a, b):
            assert (a, b) == (1, 6)
            nonlocal randint_call_count
            randint_call_count += 1
            return 6

        # randintをニセモノに差し替えて、このテストでは1〜6のうち絶対6が出るものとする
        monkeypatch.setattr(random, "randint", randint_mock)

        assert draw_lottery() == "超吉"
        assert randint_call_count == 1

* 絶対6を返すニセモノの関数 ``randint_mock`` を定義した
* このテストにおいては、monkeypatchを使って ``random.randint`` を ``randint_mock`` に置き換えた

`How to monkeypatch/mock modules and environments <https://docs.pytest.org/en/stable/how-to/monkeypatch.html>`__

* ``draw_lottery`` のテストは、6の目が出たときの出力の検証に絞れる
* 実装の中で ``random.randint()`` を呼び出しているかも合わせて検証

.. note:: nonlocal

    Python チュートリアル `9.2. Python のスコープと名前空間 <https://docs.python.org/ja/3/tutorial/classes.html#python-scopes-and-namespaces>`__

(2) ``unittest.mock.patch`` を使った例

.. code-block:: python

    @patch("random.randint", return_value=5)
    def test_6以外の目が出たら凶と返す(mock_randint):
        assert draw_lottery() == "凶"
        mock_randint.assert_called_once_with(1, 6)

* ``unittest.mock.patch`` を使って ``random.randint`` を ``mock_randint`` に置き換えた

    * ``mock_randint`` は ``unittest.mock.MagicMock``

        * `マジックメソッド <https://docs.python.org/ja/3/glossary.html#term-magic-method>`__ を実装している
        * ``__call__()`` もある

    * ``mock_randint()`` と呼び出されたときの返り値を設定
    
        * ``return_value=5`` （呼び出されたら常に5）

* ``MagicMock`` は呼び出され方を記録している

自作の関数を ``monkeypatch.setattr()`` したのと同様のことを少ないコードで実現できている

ref: `patch デコレータ（unittest.mock --- 入門） <https://docs.python.org/ja/3/library/unittest.mock-examples.html#patch-decorators>`__

.. note:: 特殊メソッド ``__call__()``

    https://docs.python.org/ja/3/reference/datamodel.html#class-instances
    
        任意のクラスのインスタンスは、クラスで ``__call__()`` メソッドを定義することで呼び出し可能になります。

.. note:: PyCon JP 2020より「unittest.mockを使って単体テストを書こう 〜より効率的で安定したテストに〜 」

    https://pycon.jp/2020/timetable/?id=203572

.. note:: Test Doubles

    http://xunitpatterns.com/Test%20Double.html

    * 広義のモック
    * テストにおける代役（代役にもいろいろある）

        * スタブ：（HTTP通信などが）実際に動かないようにする代役
        * 狭義のモック：呼び出す処理を実際に動かないようにする + モックを期待通り使っているかassert

    拙ブログ `PHPUnitのドキュメントを機にxUnit Test Patternsのサイトを確認し、Test Double・Stub・Mockを整理 〜広義のモックと狭義のモック〜 <https://nikkie-ftnext.hatenablog.com/entry/phpunit-docs-test-doubles-refer-xunit-test-patterns>`__

.. note:: pytestのフィクスチャの使いこなし

    (1)のケースのリファクタリング

    .. code-block:: python

        @pytest.fixture
        def always_6_randint(monkeypatch):
            randint_call_count = 0

            def randint_mock(a, b):
                assert (a, b) == (1, 6)
                nonlocal randint_call_count
                randint_call_count += 1
                return 6

            monkeypatch.setattr(random, "randint", randint_mock)

            yield

            assert randint_call_count == 1


        def test_6の目が出たら超吉と返す_リファクタ版(always_6_randint):
            assert draw_lottery() == "超吉"

    * monkeypatchを使った自作のフィクスチャを定義
    * 「6の目が出たら超吉と返す」は自作のフィクスチャを指定して実装

        * 「6の目が出たら超吉と返す」ではmonkeypatchを指定していないが、自作のフィクスチャが指定しているので、これでmonkeypatchを含めて動く

    自分で書いたフィクスチャによって、Arrangeをスッキリさせられる

    :command:`pytest --setup-show` でフィクスチャのsetup順が確認できる

小まとめ
--------------------

「（本ワークショップで）体験する概念」の1と2をカバーしました

* テスティングフレームワークpytestを使って、テストコードを書いた
* ここで書いたのは開発者のためのテスト

2点目の参考：拙ブログ `誰のためのテスト？ <https://nikkie-ftnext.hatenablog.com/entry/gihyo-jp-twada-tdd-lecture-articles-lecture-part#%E8%AA%B0%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E3%83%86%E3%82%B9%E3%83%88>`__
