for (var i=1 ; i< 21; i++){
    console.log(i%3 === 0 && i%5 ===0 ? 'FizzBuzz' :
               i%3 === 0 ? 'Fizz' :
               i%5 ===0 ? 'Buzz' :
               i);
}
