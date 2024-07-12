# ZZZDialog
A project that extracts ZenlessZoneZero text corpus.

本项目抽取绝区零的文本对话语料。

**Current Status**: Waiting for a way to restore dialogues containing role, content 

## Supported Feature

- [x] Extract Interknot posts and comments (抽取绳网的博客与评论)
- [x] Extract partners simple info (抽取角色信息)
- [ ] Extract dialogs 

## Examples

- Interknot posts and comments (in CHS)

```json
{
  "id": "1007",
  "poster": "CHAR",
  "title": "[委托]幽灵列车真的存在！",
  "text": "我看见  亲眼看见  真的是列车员  在那里   然后又不在了！!\n等等，等等等等…我重新组织一下语言，打字的手还在抖…\n就在刚才，我和朋友聚餐回来，这个点街上几乎没有人了。拐进锦鲤面馆对面那条小路的时候路灯突然暗了，我以为是灯坏了就没在意。继续往前走了没几步，身后坏掉的路灯突然又亮了起来，回头一看灯下站着一个大活人！\n一开始我没反应过来，看到他手上攥着的破车票时我才想起来。这家伙的脸我有印象，是上个月新闻报道里殉职的列车驾驶员！\n我头也不回一口气跑回了家，从阳台上望去那个路灯下的人也不见了。不会是我聚餐喝多产生幻觉了吧，可我喝的是乌龙茶啊…",
  "script": null,
  "comments": [
    {
      "role": "下辈子我要当只猫",
      "content": "哦那个列车失事的新闻我记得，据说是一列末班车后的空车，只有驾驶员在车上。因为突发的空洞没来得及撤离，就和车厢一起永远困在克里特空洞里了。"
    },
    {
      "role": "有那味儿了",
      "content": "我还听说过一个幽灵列车Plus版本，说至今列车还在空洞里行驶，只不过乘客都是在空洞里遭遇事故的人们。\n列车员会出现在午夜的街道上，如果接受他的邀请登上幽灵列车，就能见到死去的亲人…"
    },
    {
      "role": "RON",
      "content": "补充一个PlusProMax版本，如果看到幽灵列车员不要慌张，对他说出特定的暗语，他就会把手里的车票递给你哦。"
    },
    {
      "role": "想在空洞开食堂",
      "content": "明明只是个怪谈灌水帖，被你们越编越详细。\n这下我开始担心有人真的会傻呵呵地去六分街通宵蹲守了。"
    }
  ],
  "player_reply": [
    "特定的暗语是什么？",
    "3楼别卖关子了。"
  ]
}
```

- Partner simple info (in JA)

```json
{
  "Partner_Name_1021": "猫宮又奈",
  "Avatar_Female_Size01_Tsubaki": "猫又",
  "Partner_OutlookDesc_1021": "新エリー都・市民認証ファイルの記録：\nホロウ調査員-猫又。エーテル適性は優秀、都内の既知ホロウ（共生ホロウを含む）にて調査採掘等の基本業務に従事することを許可。\n\n備考：シリオンは人間に比べ、ホロウの環境に適応する能力が高い。ただしシリオンは新陳代謝も人類より活発なため、ひとたび侵蝕を受ければ人類より速く異化されてしまう。同様の理由で、ホロウの環境から離脱後に侵蝕症状が解消されていくのも速い。",
  "Partner_Gender_02": "女性",
  "Partner_Race_01": "邪兎屋",
  "Partner_Stature_02": "148",
  "Partner_Birthday_02": "7月30日",
  "Partner_ProfileDesc_1021": "猫宮又奈、普段は自らを「猫又」と呼んでいます。\nネコのシリオンである彼女はネコ科動物の特性を持ち合わせており、\n狩猟態勢に入ると凄まじい俊敏さを発揮するほか、\n外の世界に対して過剰ともいえる好奇心を持ちます。\n大抵は、ちょっとした出来心で無害ないたずらをする程度ですが、彼女が「獲物」を狙うとき、\nネコ科動物生来の恐るべき行動力と集中力を目の当たりにするでしょう。\n今一番興味があるのは「他人の財布」とのことです。\nアドバイス：猫又と一緒にいる時は、財布から目を離さないことを。\n\n猫又はかつて新エリー都の古参ギャング「赤牙組」に属しており、幼い頃から\nそのボス「シルバーヘッド」ミゲルには、まるで娘同然に可愛がられていました。\nしかし後に赤牙組との間に理念の相違が生まれ、\n組織を離れた彼女は一人放浪することになりました。\nやがてニコたちと共にいくつかの事件を経た後、邪兎屋への加入を決意し、\n邪兎屋の従業員第三号となって今に至ります。",
  "Partner_Impression_f_1021": "ネコちゃん！猫が嫌いな人なんていないよね！\nはぁ、猫又のしっぽをモフりたい…だって2本もあるんだよ！\n幸せも2倍なんだから！",
  "Partner_Impression_m_1021": "落ち着いて。新エリー都のそこらにいるような、\n無邪気でかわいい猫たちとは違うんだから…\n彼女の相手をするとき最も重要なのは、自分の財布を死守することだ。",
  "PartnerBg_CampGentleHouse": "GENTLE HOUSE ",
  "Avatar_Female_Size01_Tsubaki_En": "Nekomata",
  "nickname": "Nekomiya"
}
```

## Steps

- Git clone [Dim's ZenlessData](https://github.com/Dimbreath/ZenlessData)
- Git clone this project and cd to this repo
- Run the extraction codes by specifying Dim's zenless data path and language option
- Go to data folder to see full results.

```cmd
python extract_interknot_post_comment.py --repo=path/to/ZenlessData --lang=
```

Note: 

- Language option: As for lang option, see Zenless/TextMap filenames. For example, there are CHT, KO, JA, EN, etc. (By default, "" is CHS)
- The files in data folder in this repo may not be complete. You need to run the command yourself to get full contents.

## FAQs

1. Interested in some game corpus?

- [GenshinDialog](https://github.com/mrzjy/GenshinDialog)
- [StarrailDialog](https://github.com/mrzjy/StarrailDialogue)
- [ZZZDialog](https://github.com/mrzjy/ZZZDialog)
- [HonkaiImpact3rdDialog](https://github.com/mrzjy/HonkaiImpact3rdDialog)
- [ArknightsDialog](https://github.com/mrzjy/ArknightsDialog)
- [WutheringDialog](https://github.com/mrzjy/WutheringDialog)
- [hoyo_public_wiki_parser](https://github.com/mrzjy/hoyo_public_wiki_parser): Parse Hoyoverse public wiki data
