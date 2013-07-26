var text = "bla bla bla sdfsdf bla Patate pIF bla PoF test test haha bla bla PoF ";
var myName = "PoF";
var hits = [];

var compare = function(chaine1, chaine2){
    return chaine1 === chaine2;
};

for (var i = 0; i<text.length; i++){
    if (myName[0] === text[i]){
        var myNameTemp = "";
        for (var j = i ; j < i+myName.length; j++){
            myNameTemp += text[j];
        }
        if (compare(myNameTemp,myName)){
           hits.push(myNameTemp);
        }
    }
}
if (hits.length === 0){
    console.log("Your name wasn't found!");
}
else {
    console.log(hits);
}
