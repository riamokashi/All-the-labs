//
//
// console.log("Running Click Events Script");
//
// const box1 = document.querySelector("#box1");
// const box2 = document.querySelector("#box2");
// const box3 = document.querySelector("#box3");
//
// const changeOtherBoxColors = () => {
//   box1.style.backgroundColor = "red"
//   box2.style.backgroundColor = "red";
//   box3.style.backgroundColor = "red";
// }
//
// box1.addEventListener("click", changeOtherBoxColors)
//
// const changeToOrange = () => {
//   box1.style.backgroundColor = "orange";
//   box2.style.backgroundColor = "orange";
//   box3.style.backgroundColor = "orange"
// }
//
// box3.addEventListener("click", changeToOrange)
//
// const changeToPink = () => {
//   box1.style.backgroundColor = "pink"
//   box2.style.backgroundColor = "pink"
//   box3.style.backgroundColor = "pink"
// }
//
// box2.addEventListener("click", changeToPink)

const changeAllBoxColors = (color) => {
  box1.style.backgroundColor = color;
  box2.style.backgroundColor = color;
  box3.style.backgroundColor = color;
}
 box1.addEventListener("click", () => [
   changeAllBoxColors("red")
 ]);

 box2.addEventListener("click", () => [
   changeAllBoxColors("pink")
 ]);




 box3.addEventListener("click", () => [
   changeAllBoxColors("orange")
 ]);

const box4 = document.querySelector("#box4");
const box5 = document.querySelector("#box5")

box4.addEventListener("click", () => {
  box4.classList.toggle("active");
  box5.classList.toggle("active");
})
//
// const changeYellowBox = (color) => {
//   box4.style.backgroundColor = color
// }
//
// box4.addEventListener("click", () => [
//   changeYellowBox("blue")
//   if box4 = "blue", changeYellowBox("black");
// ]);
