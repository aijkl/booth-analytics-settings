## booth-analytics-public
Booth通知サーバーの設定ファイル用リポジトリです。  
利用者の方でも設定ファイルを変更する事ができます。  
| Key | Description |
----|---- 
| id | 一意なID。 |
| sql | これは通常使われないオプションです。 |
| useAvatarRelevanceEvaluation | アバターであればTrue、それ以外はFalse <br> Trueの商品はアバターとして扱われ、商品名に「専用」「用」がある場合はその商品名がタイトルに含まれないと通知されません。<br> 例:「○○専用」というタイトルの場合は説明欄に「狐雪」があったとしてもタイトルに「狐雪」が必要。 |
| categories | そのアバターが含まれている可能性があるカテゴリー<br> ここに含まれないカテゴリーの商品は通知されません。 |
| excludeKeywords |　ここに定義されているキーワードが含まれれる商品は通知されません。 |
| titleKeywords | タイトルにのみマッチングするキーワードです。 |
| keywords | タイトル、キーワード、タグ、説明欄にマッチングします。<br> アバターの場合は必ず商品IDを含めてください。 |
| productNames | 商品名です、前述のuseAvatarRelevanceEvaluationに使用されます。|
| minPrice | これ以下の商品は通知されません、通常は0です。|
| minLike | これ以下の商品は通知されません、通常は0です。|
| channelId | *ここの入力は必要ありません。開発者が入力します。* |
