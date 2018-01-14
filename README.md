# googleSuggestViewer
クエリに対するgoogleのサジェストワードの頻度と関連を可視化するツール

環境はwindows10,python3.6で実行を確認しています。

[graphviz](https://graphviz.gitlab.io/_pages/Download/Download_windows.html)
からインストーラでインストールするかzipを落として中のbinにパスを通して再起動

pythonが動く環境下で
pip install graphviz
とたたく。

その後
python getSuggestAndMakeNode.py query output
(例: python getSuggestAndMakeNode.py "灼眼のシャナ" "syana")

とたたくとsyana.pngが生成される。
わーい可視化された。
