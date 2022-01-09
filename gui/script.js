const square = document.querySelector('.square');
const circle = document.querySelector('.circle')
const text = document.querySelector('.text');

const main = document.querySelector('.main')
const mainWidth = window.innerWidth - 300
const mainHeight = window.innerHeight - 80

console.log(mainWidth, mainHeight)

circle.onmousemove = e => {
    const item = e.target
    item.style.cursor = 'move'
    if (e.buttons) {
        item.style.top = `${e.clientY - (item.clientHeight / 2)}px`
        item.style.left = `${e.clientX - (item.clientWidth / 2)}px`
    }
    const x = document.querySelector('.main .x')
    const y = document.querySelector('.main .y')
    x.innerHTML = `RIGHT: ${((((e.clientX - 300 - (mainWidth)/2))/(mainWidth/2)) * 7.11).toFixed(2)}`
    y.innerHTML = `DOWN: ${((((e.clientY - 80 - (mainHeight)/2))/(mainHeight/2)) * 7.11).toFixed(2)}`
}

square.onmousemove = e => {
    const item = e.target
    item.style.cursor = 'move'
    if (e.buttons) {
        item.style.top = `${e.clientY - (item.clientHeight / 2)}px`
        item.style.left = `${e.clientX - (item.clientWidth / 2)}px`
    }
    const x = document.querySelector('.main .x')
    const y = document.querySelector('.main .y')
    x.innerHTML = `RIGHT: ${((((e.clientX - 300 - (mainWidth)/2))/(mainWidth/2)) * 7.11).toFixed(2)}`
    y.innerHTML = `DOWN: ${((((e.clientY - 80 - (mainHeight)/2))/(mainHeight/2)) * 7.11).toFixed(2)}`
}

text.onmousemove = e => {
    const item = e.target
    item.style.cursor = 'move'
    if (e.buttons) {
        item.style.top = `${e.clientY - (item.clientHeight / 2)}px`
        item.style.left = `${e.clientX - (item.clientWidth / 2)}px`
    }
    const x = document.querySelector('.main .x')
    const y = document.querySelector('.main .y')
    x.innerHTML = `RIGHT: ${((((e.clientX - 300 - (mainWidth)/2))/(mainWidth/2)) * 7.11).toFixed(2)}`
    y.innerHTML = `DOWN: ${((((e.clientY - 80 - (mainHeight)/2))/(mainHeight/2)) * 7.11).toFixed(2)}`
}