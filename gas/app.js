function doPost(req){
  data = JSON.parse(req.postData.getDataAsString())

  const ss = SpreadsheetApp.getActive()

  // リセット
  const sheet = ss.getSheetByName("リアクション");
  sheet.clear();
  const metaSheet = ss.getSheetByName("メタ");
  metaSheet.clear();

  const records = data.reactions.map(reaction=>{
    return [reaction.emoji, reaction.user.name, reaction.user.id]
  })
  records.unshift(['emoji','name','id']) // ヘッダー
  sheet.getRange(1, 1, records.length, 3).setValues(records);
  metaSheet.getRange(1,1).setValue(data.content)

  return ContentService.createTextOutput(JSON.stringify({ message: "success!" }));
}