function adaptWord (string){
    return string.toLowerCase();
}

function adaptToList (word){
    return word.split("");
}   

function verifyPalinder(list){
    let start = 0;
    let end = (list.length - 1);
    while (start < end){
        if (list[start] != list[end]){
            return "it is not a palinder";
        }
        start++;
        end--;
    }
    return "it is a palinder";
}

let readyWord = adaptWord ("Ava") ;
let chosenList = adaptToList(readyWord);
let result = verifyPalinder(chosenList);
alert(result);

