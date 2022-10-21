let pf = ["mouse","pc","teclado"]

let newPf = ["Silla","Pantalla","Camara"]

pf = [...pf,...newPf]

let tupla = [ 1,2,3,5,6,4,6,4]

tupla = tupla.filter(item => item>5)

console.log(tupla)

let newTupla =[]

for(let index = 0; index < tupla.length; index++) {
    const element = tupla[index];
    if(element > 5){
        newTupla=[...newTupla,element]
    }
}
console.log(newTupla)


const capitales = { "Peru": "Lima" , "chile": "Santiago" }

console.log(Object.values(capitales))


let personas = {}

const Perosna = {
    id: 12,
    name: "Peter",
    age: 20
}

personas[Perosna.id]=Perosna
console.log(personas)

const miFunction = (...args) => {
    console.log(args) 
}

miFunction(1,2,3,6,)

const  ventas = [
    {'fecha': '2022-10-19', 'cliente': 'Eduardo de Rivero', 'cantidad': 10}, 
    {'fecha': '2022-10-29', 'cliente': 'Julissa Perez', 'cantidad': 30}, 
    {'fecha': '2022-10-30', 'cliente': 'Franco Portugal', 'cantidad': 10}
]

let total = 0
ventas.forEach(element =>(
    total += element.cantidad 
))

const totalAcc = ventas.reduce((acc,venta)=>{
    return acc + venta.cantidad
}, 0)

console.log(total)
console.log(totalAcc)