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
    // 要求四
    let more = document.querySelector(".more");
    let body = document.querySelector("body");
    let titleCount = 2;
    // onclick funciton
    more_id.onclick = function () {
      for (let i = 0; i < 2; i++) {
        const text = document.createElement("div");
        const textnode = document.createTextNode("");
        text.className = "title";
        text.appendChild(textnode);
        body.insertBefore(text, more);
      }

      let title = document.querySelectorAll(".title");
      for (let i = 0; i < 4; i++) {
        let addBox = document.createElement("div");
        let boxnode = document.createTextNode("");
        addBox.className = "box";
        addBox.appendChild(boxnode);
        title[titleCount].appendChild(addBox);
      }
      titleCount++;

      for (let i = 0; i < 4; i++) {
        let addBox = document.createElement("div");
        let boxnode = document.createTextNode("");
        addBox.className = "box";
        addBox.appendChild(boxnode);
        title[titleCount].appendChild(addBox);
      }
      titleCount++;
      //隱藏按鈕鍵
      if (Count + 8 >= data.length - 2) {
        more.style.visibility = "hidden";
      }

      let box = document.querySelectorAll(".box");
      for (let i = 0; i < box.length; i++) {
        const Pic = document.createElement("img");
        let view = data[Count + 2]["file"].split("https");
        Pic.className = "pic";
        Pic.src = "https" + view[1];
        box[Count].appendChild(Pic);
        // load more
        const content = document.createElement("div");
        const textnode = document.createTextNode(data[Count + 2]["stitle"]);
        content.className = "description";
        content.appendChild(textnode);
        box[Count].appendChild(content);
        Count++;
      }
    };
  });
