let promotion = document.querySelectorAll(".boxPromotion");
let box = document.querySelectorAll(".box");

// 要求三
// 讀取json資料
fetch(
  "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
)
  .then(function (response) {
    return response.json();
  })
  .then(function (list) {
    let data = list["result"]["results"];
    // promotion's picture
    for (let i = 0; i < promotion.length; i++) {
      const PromotionPic = document.createElement("img");
      let view = data[i]["file"].split("https");
      PromotionPic.className = "proPic";
      PromotionPic.src = "https" + view[1];
      promotion[i].appendChild(PromotionPic);
      // promotion's content
      const PromotionCon = document.createElement("div");
      const textnode = document.createTextNode(data[i]["stitle"]);
      PromotionCon.className = "desPromotion";
      PromotionCon.appendChild(textnode);
      promotion[i].appendChild(PromotionCon);
    }
    // title's picture
    let Count = 0;
    for (let i = 0; i < box.length; i++) {
      const TitlePic = document.createElement("img");
      let file = data[Count + 2]["file"].split("https");
      TitlePic.className = "pic";
      TitlePic.src = "https" + file[1];
      box[Count].appendChild(TitlePic);
      // titles's content
      const TitleCon = document.createElement("div");
      const textnode = document.createTextNode(data[Count + 2]["stitle"]);
      TitleCon.className = "description";
      TitleCon.appendChild(textnode);
      box[Count].appendChild(TitleCon);
      Count++;
    }
  });
