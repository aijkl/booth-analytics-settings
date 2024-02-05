## booth-analytics-public
Booth通知サーバーの設定ファイル用リポジトリです。 <br> 
利用者の方でも設定ファイルを変更する事ができます。<br>
**cloudSettings.jsonを編集してください。<br>https://github.com/aijkl/booth-analytics-settings/blob/main/cloudSettings.json**<br>
| Key | Description |
----|---- 
| <p align="center"> id </p> | <p align="center">　一意なID。通常アバター名を英字で記載します。 </p> |
| <p align="center"> sql</p> | <p align="center"> これは通常使われないオプションです。<br> 利用時は、各種キーワード指定は無視されます。 </p>  |
| <p align="center"> botId</p> | <p align="center"> **ここの入力は必要ありません。レポジストリーの管理者が入力します。** </p>  |
| <p align="center">useAvatarRelevanceEvaluation</p> | <p align="center"> アバターであればTrue、それ以外はFalse。 <br> Trueの商品はアバターとして扱われ、 <br> 商品名に「専用」「用」がある場合は <br> その商品名がタイトルに含まれないと通知されません。<br>  <br> 例: <br> 「○○専用」というタイトルの場合は説明欄に <br> 「狐雪」があったとしてもタイトルに「狐雪」が必要。</p>  |
| <p align="center">useModifyService</p> | <p align="center"> 通常はTrue。 <br> Trueの場合、後からキーワードが追加された場合に補足されます。</p>  |
| <p align="center"> categories </p>  | <p align="center">**商品が含まれているカテゴリー** <br> **ここに含まれないカテゴリーの商品は通知されません。** </p>  |
| <p align="center"> excludeKeywords </p>  | ここに定義されているキーワードが含まれれる商品は通知されません。 |
| <p align="center"> titleKeywords </p>  | <p align="center">タイトルにのみマッチングするキーワードです。</p> |
| <p align="center"> keywords </p>  | <p align="center">タイトル、キーワード、タグ、説明欄にマッチングします。<br> **通常は商品IDのみ記述します。** </p> |
| <p align="center"> productNames </p>  | <p align="center"> 商品名です、前述のuseAvatarRelevanceEvaluationに使用されます。 <br> 日本語と英語を通常記載します。<br> **例:「Koyuki」「狐雪」** </p> |
| <p align="center"> minPrice </p>  | <p align="center"> これに満たない価格の商品は通知されません、通常は0です。</p>  |
| <p align="center"> minLike </p>  | <p align="center"> これ満たない商品は通知されません、通常は0です。</p>  |
| <p align="center"> channelId </p>  | <p align="center"> **ここの入力は必要ありません。レポジストリーの管理者が入力します。** </p>  |  

設定ファイルの更新の仕組みです。<br>
定期的に変更が取り込まれているのでプルリクが承認されてから数分で適応されます。<br>
![portalmaker-3](https://user-images.githubusercontent.com/51302983/129369641-0c17b441-72bd-4da6-92a8-b34b1e405265.png)

