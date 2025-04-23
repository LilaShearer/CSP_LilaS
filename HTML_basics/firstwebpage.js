let pictures = ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQShT58xVMh-AeHVdIHolsRC9wdYO46zu7Pow&s", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_uAkLBYKa-WZbuOhPc7714_L6BqzpE_nLIA&s", "https://t4.ftcdn.net/jpg/01/28/80/67/360_F_128806753_9SVq7J4mhyU7pJPSH17vJmGoqcP6nSln.jpg"]

let number = 0

function picturechange(){
    if (number < pictures.length){
        document.getElementById("quill").src=pictures[number]
        number+=1
    }
    else{
        number = 0
        document.getElementById("quill").src=pictures[number]
    }
}

function reveal(){
    
}