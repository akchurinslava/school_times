//npm init -y
//npm i express cors
//node .

const express = require('express'); //tells the code to use express.js framework, which is popu ...
const cors = require('cors'); //tells the code to use cors packet, enabling to send cors headers ...
const app = express(); //the app is created using express framework ...

app.use(cors());        // Avoid CORS errors in browsers
app.use(express.json()) // Populate req.body


const widgets = [
    { id: 1, name: "Cizzbor", price: 29.99 },
    { id: 2, name: "Woowo", price: 26.99 },
    { id: 3, name: "Crazlinger", price: 59.99 },
]

app.get('/widgets', (req, res) => {
    res.send(widgets)
})

app.get('/widgets/:id', (req, res) => {
    if (typeof widgets[req.params.id - 1] === 'undefined') {
        return res.status(404).send({ error: "Widget not found" })
    }
    res.send(widgets[req.params.id - 1])
})

app.post('/widgets', (req, res) => {
    if (!req.body.name || !req.body.price) {
        return res.status(400).send({ error: 'One or all params are missing' })
    }
    let newWidget = {
        id: widgets.length + 1,
        price: req.body.price,
        name: req.body.name
    }
    widgets.push(newWidget)
    res.status(201).location('localhost:8080/widgets/' + (widgets.length - 1)).send(
        newWidget
    )
})

app.listen(8080, () => {
    console.log(`API up at: http://localhost:8080`)
})