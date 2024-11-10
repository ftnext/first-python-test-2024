import re
from pathlib import Path


def cat_to_dog(input_path: Path, output_path: Path) -> None:
    """input_pathのテキストに含まれる"猫"を"犬"に置換してoutput_pathに書き込む

    ref: https://speakerdeck.com/mhrtech/pyconjp2024-pytest?slide=26
    """
    input_text = input_path.read_text()
    output_text = re.sub("猫", "犬", input_text)
    output_path.write_text(output_text)
