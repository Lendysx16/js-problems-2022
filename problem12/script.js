function problem12() {
    class point {
        constructor(x, y) {
            this.x = x;
            this.y = y;
        }

    }
    function angle(point1, point2) {
        return Math.atan((point2.y - point1.y) / (point2.x - point1.x));
    }
    function to_right_angle(point1, angle_with_x){
        if(point1.x <= 0){
            angle_with_x += 180;
        }
        else{
            if(point1.y < 0){
                angle_with_x += 360;
            }
        }
        return Math.abs(angle_with_x);
    }

    let x1 = parseFloat(prompt("Enter x1: "));
    let y1 = parseFloat(prompt("Enter y1: "));
    let x2 = parseFloat(prompt("Enter x2: "));
    let y2 = parseFloat(prompt("Enter y2: "));
    let a = new point(x1, y1);
    let b = new point(x2, y2);
    let result1 = angle(a, new point(0, 0)) * 180 / Math.PI;
    result1 = to_right_angle(a, result1);
    let result2 =angle(b, new point(0, 0)) * 180 / Math.PI;
    result2 = to_right_angle(b, result2);

    if(result1 > result2){
        console.log(`Angle between vector A(${a.x}, ${a.y}) and OX is bigger than angle between vector B(${b.x}, ${b.y}) and OX`);

    }
    else if(result1 === result2){
        console.log(`Angle between vector A(${a.x}, ${a.y}) and OX is equal to angle between vector B(${b.x}, ${b.y}) and OX`);
    }
    else{
        console.log(`Angle between vector B(${b.x}, ${b.y}) and OX is bigger than angle between vector A(${a.x}, ${a.y}) and OX`);

    }
    console.log(`Angle between vector A(${a.x}, ${a.y}) and OX is ${result1} degrees`);
    console.log(`Angle between vector B(${b.x}, ${b.y}) and OX is ${result2} degrees`);

}

problem12();
