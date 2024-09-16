let socket = io()
// 

let send_button = document.querySelector(".send_message")

let message_text = document.querySelector(".message_text")

function send_message(){
    let text = message_text.value
    message_text.value = ''
    socket.emit("message", text)
}

send_button.addEventListener('click', send_message)

function handle_message(message){
    let main_container = document.querySelector('.main_container') 
    let username = document.querySelector(".username_value").value
    if (username == message.user){
        let new_div = document.createElement('div')
        new_div.classList.add('message')
        new_div.classList.add('right_side')
        new_div.innerHTML = `
        <div class="user">
            <img class="user_image" src="/chat/images/user.png" alt="">
            <p class="username">${message.user}:</p>
        </div>
        <p class="text">${message.text}</p>`
        main_container.appendChild(new_div)
    }else{
        let new_div = document.createElement('div')
        new_div.classList.add('message')
        new_div.innerHTML = `
        <div class="user">
            <img class="user_image" src="/chat/images/user.png" alt="">
            <p class="username">${message.user}:</p>
        </div>
        <p class="text">${message.text}</p>`
        main_container.appendChild(new_div)
    }


    
}

socket.on("message", handle_message)