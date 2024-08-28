import numpy as np

# 初期値と増加率の定義
satou_rate = 1.53  # 2022年の佐藤姓の割合
satou_growth = 1.0083 # 佐藤性の増加の割合

# 佐藤姓の割合を計算する関数の定義
def satou(year):
    return satou_rate * satou_growth ** (year - 2022)

# 2022年から2550年までの年を生成
x = np.arange(2022, 2550)

# 各年における佐藤姓の割合を計算
y = satou(x)

# 結果の割合が100%を超える年を特定
year_exceed_100 = x[y > 100]
if len(year_exceed_100) > 0:
    print(f"佐藤姓の割合が100%を超える年: {year_exceed_100[0]}年")
else:
    print("佐藤姓の割合が100%を超える年はありません")
