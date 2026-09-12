let map;
let geoLayer;

const countriesList = [];

let targetCountry = "";
let score = 0;


/*
========================================
Inicializar mapa
========================================
*/

document.addEventListener(
    "DOMContentLoaded",
    initializeMap
);


async function initializeMap() {

    map = L.map("map").setView(
        [20, 0],
        2
    );

    L.tileLayer(
        "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
        {
            maxZoom: 19
        }
    ).addTo(map);


    try {

        const response = await fetch(
            "https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json"
        );

        const data = await response.json();

        createCountryLayer(data);

        await startGame();

    } catch (error) {

        console.error(error);

        showMessage(
            "No fue posible cargar el mapa.",
            "error"
        );
    }
}


/*
========================================
Crear países
========================================
*/

function createCountryLayer(data) {

    geoLayer = L.geoJSON(
        data,
        {

            style: {
                color: "#333",
                weight: 1,
                fillColor: "#66aaff",
                fillOpacity: 0.4
            },

            onEachFeature: function (
                feature,
                layer
            ) {

                const name =
                    feature.properties.name;

                countriesList.push(name);


                layer.on(
                    "mouseover",
                    function () {

                        layer.setStyle({
                            fillColor: "#ffcc00"
                        });

                    }
                );


                layer.on(
                    "mouseout",
                    function () {

                        geoLayer.resetStyle(
                            layer
                        );

                    }
                );


                layer.on(
                    "click",
                    function () {

                        checkCountry(name);

                    }
                );
            }
        }
    ).addTo(map);
}


/*
========================================
Comenzar partida
========================================
*/

async function startGame() {

    const response = await fetch(
        "/game/api/start",
        {

            method: "POST",

            headers: {
                "Content-Type":
                    "application/json"
            },

            body: JSON.stringify({
                countries: countriesList
            })
        }
    );


    const data = await response.json();


    if (!response.ok) {

        showMessage(
            data.error,
            "error"
        );

        return;
    }


    targetCountry = data.target;
    score = data.score;

    updateInterface();
}


/*
========================================
Nueva ronda
========================================
*/

async function startRound() {

    const response = await fetch(
        "/game/api/round",
        {

            method: "POST",

            headers: {
                "Content-Type":
                    "application/json"
            },

            body: JSON.stringify({
                countries: countriesList
            })
        }
    );


    const data =
        await response.json();


    if (!response.ok) {

        showMessage(
            data.error,
            "error"
        );

        return;
    }


    targetCountry = data.target;

    updateInterface();
}


/*
========================================
Comprobar respuesta
========================================
*/

async function checkCountry(clickedName) {

    const response = await fetch(
        "/game/api/answer",
        {

            method: "POST",

            headers: {
                "Content-Type":
                    "application/json"
            },

            body: JSON.stringify({
                country: clickedName
            })
        }
    );


    const data =
        await response.json();


    if (!response.ok) {

        showMessage(
            data.error,
            "error"
        );

        return;
    }


    score = data.score;


    if (data.correct) {

        showMessage(
            `✓ Correcto: ${data.clicked}`,
            "success"
        );

    } else {

        showMessage(
            `✗ Era ${data.target}. Seleccionaste ${data.clicked}.`,
            "error"
        );

    }


    updateInterface();

    /*
    Esperamos ligeramente para que
    el usuario pueda leer el resultado.
    */

    setTimeout(
        startRound,
        900
    );
}


/*
========================================
Interfaz
========================================
*/

function updateInterface() {

    document
        .getElementById(
            "targetCountry"
        )
        .textContent =
        targetCountry;


    document
        .getElementById(
            "score"
        )
        .textContent =
        score;
}


function showMessage(
    message,
    type
) {

    const element =
        document.getElementById(
            "message"
        );


    element.textContent =
        message;


    element.className =
        `message ${type}`;
}