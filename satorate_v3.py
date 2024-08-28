#コードに必要なライブラリのインストール
import numpy as np #Numpy: 数値計算や配列操作を実施するためのもの。
import matplotlib.pylab as plt #Matplotlib: データの可視化を実施するためのもの。
import matplotlib.font_manager as fm #Matplotlibでのフォント管理

plt.rcParams['font.family'] = 'MS Gothic'

# 初期値と増加率の定義
satou_rate = 1.53  # 2022年の佐藤姓の割合
satou_growth = 1.0083 #佐藤性の増加の割合

# 佐藤姓の割合を計算する関数の定義
def satou(year):
    return satou_rate * satou_growth ** (year - 2022) #演算子(*: 乗算)(**: べき乗)

x = np.arange(2022, 2550)
y = satou(x)

year_exceed_100 = x[y > 100]
if len(year_exceed_100) > 0:
    exceed_year = year_exceed_100[0]
    print(f"佐藤姓の割合が100%を超える年: {exceed_year}年")
else:
    exceed_year = None
    print("佐藤姓の割合が100%を超える年はこの中にありません")

#データグラフの記述
plt.plot(x, y, label="佐藤姓の割合")

if exceed_year:
    plt.axvline(exceed_year, color='red', linestyle='--', label=f'{exceed_year}年: 100%超え')
    plt.text(exceed_year + 2, 105, f'{exceed_year}年', color='red')

plt.xlabel("年")
plt.ylabel("佐藤姓の割合 (%)")
plt.title("佐藤姓の割合の推移")
plt.legend()
plt.grid(True)

plt.show()
