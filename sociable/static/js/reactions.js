function like(num){

document.getElementById(`likebtn${num}`).style='font-weight:bold;background:grey;'
document.getElementById(`likebtn${num}`).disabled=true;

console.log(num)
}