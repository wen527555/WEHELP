// 要求一
function calculate(min, max, step) {
  let sum = 0;
  while (min <= max) {
    sum += min;
    min += step;
  }
  console.log(sum);
}
calculate(1, 3, 1); // 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2); // 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2); // 你的程式要能夠計算 -1+1，最後印出 0

console.log("--------------");

// 要求二

function avg(data) {
  // 請用你的程式補完這個函式的區塊
  let sum = 0; //非manager員工薪資累加的結果
  let count = 0; //非manager員工總數
  employees = data["employees"];
  let l = employees.length;
  for (i = 0; i < l; i++) {
    if (employees[i]["manager"] == false) {
      sum += employees[i]["salary"];
      count += 1;
    }
    let result = sum / count;
    console.log(result);
  }
}
avg({
  employees: [
    {
      name: "John",
      salary: 30000,
      manager: false,
    },
    {
      name: "Bob",
      salary: 60000,
      manager: true,
    },
    {
      name: "Jenny",
      salary: 50000,
      manager: false,
    },
    {
      name: "Tony",
      salary: 40000,
      manager: false,
    },
  ],
}); // 呼叫 avg 函式

console.log("--------------");
//要求三
function func(a) {
  // 請用你的程式補完這個函式的區塊
  function multiply(b, c) {
    console.log(a + b * c);
  }
  return multiply;
}
func(2)(3, 4); // 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5); // 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9); // 你補完的函式能印出 -3+(2*9) 的結果 15
// 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

console.log("--------------");
//要求四
function maxProduct(nums) {
  // 請用你的程式補完這個函式的區塊
  let result = [];
  for (let i = 0; i < nums.length; i++) {
    for (j = i + 1; j < nums.length; j++) {
      result.push(nums[i] * nums[j]);
    }
  }
  let max = result[0];
  for (i = 1; i < result.length; i++) {
    if (result[i] > max) {
      max = result[i];
    }
  }
  console.log(max);
}
maxProduct([5, 20, 2, 6]); // 得到 120
maxProduct([10, -20, 0, 3]); // 得到 30
maxProduct([10, -20, 0, -3]); // 得到 60
maxProduct([-1, 2]); // 得到 -2
maxProduct([-1, 0, 2]); // 得到 0 或 -0
maxProduct([5, -1, -2, 0]); // 得到 2
maxProduct([-5, -2]); // 得到 10

console.log("--------------");
//要求五
function twoSum(nums, target) {
  // your code here
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] == target) {
        return [i, j];
      }
    }
  }
}
let result = twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9

console.log("--------------");
//要求六
function maxZeros(nums) {
  // 請用你的程式補完這個函式的區塊
  let max_zeros = 0;
  let count = 0;
  for (i = 0; i < nums.length; i++) {
    if (nums[i] == 0) {
      max_zeros++;
      if (max_zeros > count) {
        count++;
      }
    } else {
      max_zeros = 0;
    }
  }
  console.log(count);
}
maxZeros([0, 1, 0, 0]); // 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4
maxZeros([1, 1, 1, 1, 1]); // 得到 0
maxZeros([0, 0, 0, 1, 1]); // 得到 3
