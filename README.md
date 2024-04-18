# Human_Reflection_Time_Measurement
大学の授業である人間情報工学にて与えられた「人間の反応速度に関する法則(フィッツの法則)が適切かどうか計測する」という課題で用いる装置とソフトウェアを開発しました。

専用の装置などは大学側から与えられず、参考資料として過去の実験例の画像と簡単な仕組みを与えられたのみであり、それを元に各実験グループにて最適な装置を開発する必要がありました。

私の所属するグループではソフトとハードの両方の開発経験をもつ人材がいなかったため、練習も兼ねて私が制作することになりました。
## 装置の仕組み
以下に示した図がフィリッツが行った実験装置の概要です。

<img width="376" alt="スクリーンショット 2024-04-18 12 27 38" src="https://github.com/TANIGUCHIREI/Human_Reflection_Time_Measurement/assets/120480219/d9398030-21b5-4503-8118-2daaa9e9083d">

授業にて、リッチなOSを持つソフトウェアでは反応速度を計測するのに計測遅延が生じるからあまり適切ではない、と言われたため(そこまで要求されるかは不明ですが)、GPIOを持つラズパイではなくArduinoを計測側で利用し、その計測結果をpythonサーバにシリアル通信にて送信しcsvに自動書き込みを行うという仕組みを作成しました。

↓装置部分の拡大図

<img src="https://github.com/TANIGUCHIREI/Human_Reflection_Time_Measurement/assets/120480219/348d17fe-c4c3-43f4-807d-1aa4ec69d677" width="50%">

以下は動作のデモンストレーションを行った動画です。

https://github.com/TANIGUCHIREI/Human_Reflection_Time_Measurement/assets/120480219/892fffa4-9810-4abe-b884-97a6a6eecdae






実際に被験者が実験を行っている様子です↓

https://github.com/TANIGUCHIREI/Human_Reflection_Time_Measurement/assets/120480219/825b09ef-2c52-41f6-a856-4a7a5d8e68ce

