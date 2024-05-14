
const createList = document.getElementById("add-button");
const addTask = document.getElementById("addTask-button");

const popup = document.getElementById("popup");
const popupTask = document.getElementById("new-task-form");

const taskForm = document.getElementById("new-task-form");

//creation of a new list
const newListBtn = document.getElementById('new-list-btn');
const listName = document.getElementById("id_name"); //created using django forms


const noTasksContainer = document.getElementById('taskEmpty-container');



//display create list form
createList.addEventListener("click",function(){
	if (popup.style.display == "none"){
		popup.style.display = "block";
	}else{
		popup.style.display = "none"
	}
});



//display add task form
addTask.addEventListener("click",function(){

	if (popupTask.style.display == "none"){
		popupTask.style.display = "block";
		noTasksContainer.style.display = "none";


	}else{
		popupTask.style.display = "none"
	}	

});








