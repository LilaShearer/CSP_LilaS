let pictures = ["https://capitolreefcountry.com/wp-content/uploads/2024/08/Goblin-Valley-ET1200.jpg", "https://capitolreefcountry.com/wp-content/uploads/2024/08/Goblin_Valley_Utah1200.jpg", "https://capitolreefcountry.com/wp-content/uploads/2024/08/GoblinValleyStatePark-Utah-BigMountainLodge1200.jpg", "https://capitolreefcountry.com/wp-content/uploads/2024/05/51334705102_6949a9f9f9_k.jpg"]


let number = 0
let counter = 0
let ishidden = ["block","none"]
function imagechange(){
    if (number < pictures.length){
        document.getElementById("changeimage").src=pictures[number]
        number+=1
    }
    else{
        number = 0
        document.getElementById("changeimage").src=pictures[number]
    }
}

function reveal(){
    if (counter < ishidden.length){
        document.getElementById("secretthings").style.display = ishidden[counter]
        counter+=1
    }
    else{
        counter = 0
        document.getElementById("secretthings").style.display = ishidden[counter]
    }    
}
