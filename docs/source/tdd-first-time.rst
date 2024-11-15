テスト駆動開発の世界をのぞいてみよう
========================================

（IMO）TDDは、環境構築の確認でやったことをもっと徹底的にやる

* 環境構築できていれば ``assert False`` で落ちる
* ``assert True`` に変えればテストは全部通る

それにより、終始 **コントロールしている感覚**

テスト駆動開発
--------------------

Test Driven Development（テストが開発を駆動する）

| 提案はKent Beck。『`テスト駆動開発 <https://www.ohmsha.co.jp/book/9784274217883/>`__』
| t-wadaさん `【翻訳】テスト駆動開発の定義 <https://t-wada.hatenablog.jp/entry/canon-tdd-by-kent-beck#%E7%BF%BB%E8%A8%B3%E3%83%86%E3%82%B9%E3%83%88%E9%A7%86%E5%8B%95%E9%96%8B%E7%99%BA%E3%81%AE%E5%AE%9A%E7%BE%A9>`__

私の言葉で説明すると

1. テストシナリオのリストを書く
2. テストシナリオから **1つだけ** 選び、テストコードを書き、テストが失敗することを確認
3. プロダクトコードを変更し、すべてのテストコードを成功させる
4. テストコードやプロダクトコードをリファクタリング（必要だと思ったらやる）
5. テストリストが空になるまで2に戻って繰り返す

**サイクル** ♻️「テストリスト (2) -> Red (2) -> Green (3) -> Refactor (4)」

Red（先にテストコードを書いて落とす）：テストファースト

pytestでテストの書き方は皆さん体験したので、ここでは **テストを書く順番・開発を進める流れにご注目** ください

「動作するきれいなコード」

* まず動作させる（Red -> Green）
* 次に動作したままきれいなコードにする（Green -> Refactor）

| サイクルなので、テストリストを最初に全部テストコードにするわけでは **ない** です。
| 1つ選んでテストコードを書き、そのテストが通るように実装し、リファクタリングできるかを考えるというサイクルを何度も何度も（テストリストが空になるまで）回します

FizzBuzzを例にテスト駆動開発
----------------------------------------

FizzBuzzの仕様からテストリストを書き出す

.. code-block:: markdown
    :caption: テストリスト

    - [ ] 数をそのまま文字列に変換する
    - [ ] 3の倍数のときは数の代わりに「Fizz」に変換する
    - [ ] 5の倍数のときは数の代わりに「Buzz」に変換する
    - [ ] 15の倍数のときは数の代わりに「FizzBuzz」に変換する

| 「数をそのまま文字列に変換する」はそのままではテストコードに落とし込めない。
| 数を決める

.. code-block:: markdown
    :caption: テストリスト

    - [ ] 数をそのまま文字列に変換する
      - [ ] 1を渡すと文字列1を返す
    - [ ] 3の倍数のときは数の代わりに「Fizz」に変換する
    - [ ] 5の倍数のときは数の代わりに「Buzz」に変換する
    - [ ] 15の倍数のときは数の代わりに「FizzBuzz」に変換する

1を渡すと文字列1を返す

.. code-block:: python
    :caption: tests/test_core.py

    def test_1を渡すと文字列1を返す():
        assert fizzbuzz(1) == "1"

実装はまだしていない（呼べるように関数定義だけしておく）

.. code-block:: python
    :caption: src/fizzbuzz/core.py

    def fizzbuzz(n: int) -> str:
        raise NotImplementedError

🟥テストが落ちる (0/1)

仮実装
--------------------

``test_1を渡すと文字列1を返す`` だけを通すことを考える。

| テストリストが全部通ればFizzBuzzができた状態になる。
| いまは最初のテスト
| FizzBuzzを実装しようとするのではなく、1を渡すときだけ通すことを考える

.. code-block:: diff
    :caption: src/fizzbuzz/core.py

    def fizzbuzz(n: int) -> str:
    -    raise NotImplementedError
    +    return "1"

🟩テストが通る (1/1)

「茶番では？」

* テストを書き間違える可能性がある
* 文字列 `"1"` を返すように実装して、テストがRedのままであれば、テストを間違えていることに気づける
* 文字列 `"1"` を返すように実装して、テストがGreenならば「想定通り。実装もテストコードもコントロールして進めている」

テストコード・実装どちらかにRefactorの余地はあるか？ -> なさそう

『テスト駆動開発』第2章

    コードでまずベタ書きの値を使い、

三角測量
--------------------

FizzBuzzとしては常に文字列の1を返すのはよくない。
一般化したい

一般化するために、テストケースを追加する

.. code-block:: markdown
    :caption: テストリスト

    - [ ] 数をそのまま文字列に変換する
      - [x] 1を渡すと文字列1を返す
      - [ ] 2を渡すと文字列2を返す
    - [ ] 3の倍数のときは数の代わりに「Fizz」に変換する
    - [ ] 5の倍数のときは数の代わりに「Buzz」に変換する
    - [ ] 15の倍数のときは数の代わりに「FizzBuzz」に変換する

2を渡すと文字列2を返す

.. code-block:: python
    :caption: tests/test_core.py

    def test_2を渡すと文字列2を返す():
        assert fizzbuzz(2) == "2"

🟥テストが落ちる (1/2)

実装する。ここで一般化
（``n`` が ``1`` のときはと分岐するより、一般化したほうが実装を単純なまま＝きれいに保てる）

.. code-block:: diff
    :caption: src/fizzbuzz/core.py

    def fizzbuzz(n: int) -> str:
    -    return "1"
    +    return str(n)

🟩テストが通る (2/2)

『テスト駆動開発』第3章より

    コードを一般化できるのは、2つ以上の実例があるときだけ

Refactor：実装の変数をrename。 ``n`` より ``number`` の方が読みやすい

（パラメタ化テストは、私はいったん置いておく）

明白な実装
--------------------

| 3の倍数のときは数の代わりに「Fizz」に変換する
| 3でテストコードを書く

.. code-block:: markdown
    :caption: テストリスト

    - [x] 数をそのまま文字列に変換する
      - [x] 1を渡すと文字列1を返す
      - [x] 2を渡すと文字列2を返す
    - [ ] 3の倍数のときは数の代わりに「Fizz」に変換する
      - [ ] 3を渡すと文字列Fizzを返す
    - [ ] 5の倍数のときは数の代わりに「Buzz」に変換する
    - [ ] 15の倍数のときは数の代わりに「FizzBuzz」に変換する

.. code-block:: python
    :caption: tests/test_core.py

    def test_3を渡すと文字列Fizzを返す():
        assert fizzbuzz(3) == "Fizz"

🟥テストが落ちる (2/3)

| テストにも実装にも自信を持ち始めたので、三角測量せずに直接実装（**明白な実装**）。
| TDDはやっているときの自信度合いに応じて進む歩幅を変えられる
| 参考：拙ブログ `おーい、t-wadaさん、ペアプロしようぜ！TDD Boot Camp 2020 Online #1 基調講演/ライブコーディング 視聴ログ🦁 <https://nikkie-ftnext.hatenablog.com/entry/tddbc-2020-online-archive-twada-keynote-live-coding-log>`__

.. code-block:: python
    :caption: src/fizzbuzz/core.py

    def fizzbuzz(number: int) -> str:
        if number % 3 == 0:
            return "Fizz"
        return str(number)

🟩テストが通る (3/3)

Refactorの余地はなさそう

『テスト駆動開発』第2章

    すぐに頭の中の実装をコードに落とす。

テストリスト -> Red -> Green -> Refactor を回す
------------------------------------------------------------

5の倍数

.. code-block:: markdown
    :caption: テストリスト

    - [x] 数をそのまま文字列に変換する
      - [x] 1を渡すと文字列1を返す
      - [x] 2を渡すと文字列2を返す
    - [x] 3の倍数のときは数の代わりに「Fizz」に変換する
      -  [x] 3を渡すと文字列Fizzを返す
    - [ ] 5の倍数のときは数の代わりに「Buzz」に変換する
      -  [ ] 5を渡すと文字列Buzzを返す
    - [ ] 15の倍数のときは数の代わりに「FizzBuzz」に変換する

.. code-block:: python
    :caption: tests/test_core.py

    def test_5を渡すと文字列Buzzを返す():
        assert fizzbuzz(5) == "Buzz"

🟥テストが落ちる (3/4)

.. code-block:: diff
    :caption: src/fizzbuzz/core.py

    def fizzbuzz(number: int) -> str:
        if number % 3 == 0:
            return "Fizz"
        +if number % 5 == 0:
        +    return "Buzz"
        return str(number)

🟩テストが通る (4/4)

Refactorの余地はなさそう

15の倍数

.. code-block:: markdown
    :caption: テストリスト

    - [x] 数をそのまま文字列に変換する
      - [x] 1を渡すと文字列1を返す
      - [x] 2を渡すと文字列2を返す
    - [x] 3の倍数のときは数の代わりに「Fizz」に変換する
      -  [x] 3を渡すと文字列Fizzを返す
    - [x] 5の倍数のときは数の代わりに「Buzz」に変換する
      -  [x] 5を渡すと文字列Buzzを返す
    - [ ] 15の倍数のときは数の代わりに「FizzBuzz」に変換する
      -  [ ] 15を渡すと文字列FizzBuzzを返す

.. code-block:: python
    :caption: tests/test_core.py

    def test_15を渡すと文字列FizzBuzzを返す():
        assert fizzbuzz(15) == "FizzBuzz"

🟥テストが落ちる (4/5)

.. code-block:: diff
    :caption: src/fizzbuzz/core.py

    def fizzbuzz(number: int) -> str:
        +if number % 15 == 0:
        +    return "FizzBuzz"
        if number % 3 == 0:
            return "Fizz"
        if number % 5 == 0:
            return "Buzz"
        return str(number)

🟩テストが通る (5/5)

Refactor：最初に見たStructural Pattern Matchingに書き換えてみてもよいかも

テストリストが全部実装できた。FizzBuzz完成！

.. note:: 動作する仕様書にできる

    TDDBC（後述）

    * クラスを使って構造化する例
    * 三角測量に使った例は消してしまう

pytestの機能も使える
------------------------------

TODO 実際の例から持ってくる？

モック
パラメタ化
フィクスチャ

この先の学習リソース
------------------------------

pytestではないが、pytestに置き換えて進めていけるはず

* TDDBC https://www.youtube.com/watch?v=Q-FJ3XmFlT8&t=1145s
* 『`ちょうぜつソフトウェア設計入門 <https://gihyo.jp/book/2022/978-4-297-13234-7>`__』（ちょうぜつ本）第6章

Next: 達人のテスト駆動開発は実は単位が小さい
==================================================

まとめ & TODO
