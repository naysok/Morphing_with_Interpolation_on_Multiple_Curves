# Morphing_with_Interpolation_on_Multiple_Curves  


複数の曲線の間を補間して、モーフィングするスクリプト。  

ジオメトリ処理や描画系の世話が面倒なので、Rhino 及び Grasshopper の関数を、Python から呼ぶことで描画に。  

![photo](out.gif)  

[https://vimeo.com/319324504](https://vimeo.com/319324504)  


---  

---  


# Update  


### 191229  

Rhino5 と Rhino6 で rs.Comanad(query) で、Rhino を動かしている Rhino 側の仕様が変わっている（多分）ので、書き直した。  
  
```Python
query = "-ViewCaptureToFile "+ \
    " W=1080 H=1080 S=1 L=_No D=_No R=_No A=_No T=_No " + \
    export_name + \
    " _Enter " + \
    " _SelAll _Delete"
    
rs.Command(query)
```

-ViewCaptureToFile の実行時、Rhino5 では、ファイル名を渡してから、オプションの設定だったと記憶しているが（記憶してるというかそういう風にコードに書いてある）、Rhino6 では、これだと動かない。  
ファイル名を渡した瞬間に実行されるので、オプションの設定が効かない。順番の入れ替えを試してみると、上のコードのように、オプションを先に、その後ファイル名の指定でうまくいった。  




### 190610  

軽量化、エラー発生防止も兼ねて、がっつリ書き直した  


- メソッドに分割  


- 補完カーブが、綺麗なドメイン（0 (to 1 ...) to N）を持っていたので、PointAt() でできた。  
  - 点と線の交差を取得していた。まったく同じ点があると、そこが例外になっていたので、適当にキャッチしていたのでエラー頻発。  
  
  ```Python
  pt = rg.Curve.PointAt(crv, param_slice[l])
  ```  




- ghpc の排除  
  ```Python
  import ghpythonlib.components as ghpc
  ```

- Python のネストで処理するようにした。  



~~文字のところで、2枚同じ画像が生成されているで、カクつく。  
n-1 から n で m 個に分割（最初と最後も含む）、n から n+1 で m 個に分割（最初と最後も含む）、で、分割したものを、append() で回収しているので、重複があると思われる。  
for ループを、一個手前で止めればいいので、修正は多分簡単。~~  


---