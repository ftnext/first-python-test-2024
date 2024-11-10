# ref: https://speakerdeck.com/mhrtech/pyconjp2024-pytest?slide=27
from introduction.fileio import cat_to_dog


def test_cat_to_dog(tmp_path):
    input_path = tmp_path / "input.txt"
    output_path = tmp_path / "output.txt"
    input_path.write_text("吾輩は猫である。名前はまだない。")

    cat_to_dog(input_path, output_path)

    assert output_path.read_text() == "吾輩は犬である。名前はまだない。"
