function problem7(){
    function premute(data, i, length){
        if(i === length){
            console.log(data.join(''));
        }
        else{
            for(let j = i; j < length; j++){
                [data[i], data[j]] = [data[j], data[i]];
                premute(data, i + 1, length);
                [data[i], data[j]] = [data[j], data[i]];
            }
        }
    }
    let num = prompt("Enter a number");
    let data = [];
    num = parseInt(num);
    for(let i = 1; i <= num; i++){
        data.push(i);
    }
    premute(data, 0, num);

}


problem7();
