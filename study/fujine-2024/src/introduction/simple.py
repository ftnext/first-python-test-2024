def calculate_bmi(*, height_m: float, weight_kg: float) -> float:
    """身長[m]と体重[kg]からBMIを計算する

    ref: https://speakerdeck.com/mhrtech/pyconjp2024-pytest?slide=13
    """
    if (height_m <= 0) or (weight_kg <= 0):
        raise ValueError("Height and weight must be greater than 0.")

    return weight_kg / (height_m**2)
