let userName= document.getElementById("name");
let email= document.getElementById("email");
let password= document.getElementById("password");
let form= document.querySelector("form");


function validateInput(){
	if(userName.value.trim()===""){
		onError(userName,"User name can't be empty");
}

else{
	onSuccess(userName);
	}
	
}
document.querySelector("button")
.addEventListener("click",(event)=>{
	event.preventDefault();
	validateInput();
});

function onSuccess(input){
	let parent=userName.parentElement;
		let messageEle=parent.querySelector("small");
		messageEle.style.visibility="hidden";
		messageEle.innerText="";
		parent.classList.remove("error");
		parent.classList.add("success");

}
function onError(input,message){
	    let parent=userName.parentElement;
		let messageEle=parent.querySelector("small");
		messageEle.style.visibility="visible";
		messageEle.innerText=message;
		parent.classList.add("error");
		parent.classList.remove("success");

}
