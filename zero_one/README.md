# others
ex

# 解析手法  
xmlに記述されているbase64のコードを2進数に変換し、同じ2進数の繰り返し部分を探しながら、
パラメータ箇所を探っていく。  
base64をそのままテキストに変換しない理由は単純で簡単に復号化出来ないから。
復号対策なのか不要で無意味な0が大量に挿入されているので、2進数で探っていく必要がある。

# 手順
1. xmlからbase64データ取得
2. 改行全て解消
3. pythonコードで2進数に変換
4. 同じ繰り返しを探していく 

　　
  

一文字あたり2進数表記で8桁なので，8桁区切りで同じ繰り返し箇所を探していく

横に72文字で整形

# 解析手助けサイト

[バイナリから文字列へのコンバータ](https://www.rapidtables.org/ja/convert/number/binary-to-string.html)

[Base64 Encode and Decode - Online](https://www.base64encode.org/)

[2進数バイナリ文字列変換 日本語変換 Online - DenCode](https://dencode.com/ja/string/bin)
