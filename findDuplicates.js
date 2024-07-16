function findDuplicates(arr) {
    let elementCount = new Map();
    let duplicates = new Set();

    for (let item of arr) {
        if (elementCount.has(item)) {
            duplicates.add(item);
        } else {
            elementCount.set(item, 1);
        }
    }

    return Array.from(duplicates);
}

// Example usage
let array = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 9, 3];
let duplicateElements = findDuplicates(array);
console.log(duplicateElements); 
