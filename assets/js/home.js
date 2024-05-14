//get create todoList buttob
const createList = document.getElementById("add-button");
const popup = document.getElementById("popup");

createList.addEventListener("click",show);


function show(){
	if (popup.style.display == "none"){
		popup.style.display = "block";
	}else{
		popup.style.display = "none"
	}

}