## booth-analytics-public
Booth通知サーバーの設定ファイル用リポジトリです。 <br> 
利用者の方でも設定ファイルを変更する事ができます。<br>
**cloudSettings.jsonを編集してください。<br>https://github.com/aijkl/booth-analytics-settings/blob/main/cloudSettings.json**<br>
| Key | Description |
----|---- 
| id | 一意なID。 |
| sql | これは通常使われないオプションです。 |
| useAvatarRelevanceEvaluation | アバターであればTrue、それ以外はFalse <br> Trueの商品はアバターとして扱われ、商品名に「専用」「用」がある場合はその商品名がタイトルに含まれないと通知されません。<br> 例:「○○専用」というタイトルの場合は説明欄に「狐雪」があったとしてもタイトルに「狐雪」が必要。 |
| categories | **商品が含まれているカテゴリー** <br> **ここに含まれないカテゴリーの商品は通知されません。** |
| excludeKeywords | ここに定義されているキーワードが含まれれる商品は通知されません。 |
| titleKeywords | タイトルにのみマッチングするキーワードです。 |
| keywords | タイトル、キーワード、タグ、説明欄にマッチングします。<br> **通常は商品IDのみ記述します。** |
| productNames | 商品名です、前述のuseAvatarRelevanceEvaluationに使用されます。<br> **例:「Koyuki」「狐雪」** |
| minPrice | これより小さい商品は通知されません、通常は0です。|
| minLike | これより小さい商品は通知されません、通常は0です。|
| channelId | *ここの入力は必要ありません。開発者が入力します。* |  

設定ファイルの更新の仕組みです。<br>
定期的に変更が取り込まれているのでプルリクが承認されてから数分で適応されます。<br>
![portalmaker-3](https://user-images.githubusercontent.com/51302983/129369641-0c17b441-72bd-4da6-92a8-b34b1e405265.png)

