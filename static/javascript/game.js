function updateBoard({board,player,gameOver,winnningLine})
{
    board.forEach((x, i) => {
        button = document.getElementById(i)
        button.innerHTML = x
        switch(x)
        {
            case 'X':
                button.className = 'X'
                break
            case 'O':
                button.className = 'O'
                break
            
            default:
                button.className = ''
        }

    });

    if (!gameOver){
        return
    }

    if(winnningLine == [])
    {
        return
    }

    console.log(winnningLine)


}

async function playMove(id){
    response = await fetch('',{method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({index:id})})
    return await response.json()
}

async function buttonPress(id){
    response = await playMove(id)
    updateBoard(response)

}

