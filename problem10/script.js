function problem10() {
    let num = prompt("Enter a number in a binary format: ");
    let base = 1;
    let result = 0;
    for (let i = num.length - 1; i >= 0; --i) {
        let digit = parseInt(num[i]);
        if (digit > 1) {
            throw new Error("Input is not a binary number");
        }
        result += digit * base;
        base <<= 1;
    }
    console.log(`The decimal value of binary expression "${num}" is ${result}`);
    if(result % 15 === 0) {
        console.log(`The number ${result} is divisible by 15`);
    }
    else{
        console.log(`The number ${result} is not divisible by 15`);
    }
}


try {
    problem10();
} catch (e) {
    console.log(e.message);
}
