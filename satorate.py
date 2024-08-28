# 初期値と増加率の定義
satou_rate = 1.53  # 2022年の佐藤姓の割合
satou_growth = 1.0083 #佐藤性の増加の割合
sato_result = 2025 # 佐藤性の割合を計算する年

# 佐藤姓の割合を計算する関数の定義
def satou(year):
    return satou_rate * satou_growth ** (year - 2022)

# 指定した年数 (sato_result) の佐藤姓の割合を計算
result = satou(sato_result)
print(f"{sato_result}年の佐藤姓の割合: {result}%")

