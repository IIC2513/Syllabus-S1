
# Ayudantía Consumo APIs

* **Fecha**: 06 de septiembre del 2024
* **Ayudantes**: Andrés Venegas - Gabriel Quiroz (feat la gran Victoria Jiménez)

## Actividad

El fin de esta actividad es que utilizen `Axios` para generar solicitudes del tipo `GET` a una `API` pública, y que esta información la reflejen en una **aplicación** construída utilizando **React**.

Para esto, se les ha indicado a través de comentarios **qué** es lo que tienen que realizar, y en qué **lugar**. El único archivo con el que deben trabajar es:

```
<repo>/src/App.jsx
```

Será fundamental que interactúen con el **Hook** de *React*, `state`.

### Instalación

**IMPORTANTE**: Se asume que ya realizaron el [SetUp](https://www.youtube.com/watch?v=KtH8qZt9aUg) que se les compartió a inicio de semana.

1. No se les solicita que empiecen un proyecto desde cero, sino que **usen este repositorio como base**. Para esto, clonen el repositorio en sus computadores,

```
git clone <repo>
```

2. Luego, es necesario que se posicionen en la carpeta del proyecto,

```
cd <repo>
```

3. Para instalar las **dependencias**, es necesario que ejecuten,

```
yarn install
```

4. Y finalmente, para **correr** la aplicación, ejecuten,

```
yarn dev
```

Si todo lo anterior ocurrió de manera exitosa, deberían poder acceder a `localhost:5173` desde su browser y visualizar la aplicación.

### PokeApi

Deberán consultar a la **API** *PokeApi*, para lo que necesitarán los siguientes recursos:

* **API**: [pokeapi.co/api/v2](https://pokeapi.co/api/v2)
* **Docs**: [pokeapi.co/docs/v2](https://pokeapi.co/docs/v2)

*A modo de familiarizarse con esta API, les recomendamos que desde su browser consulten la siguiente URL y observen la respuesta:*

https://pokeapi.co/api/v2/pokemon/pikachu

## Adicional

### Vite

Este proyecto fue creado utilizando [Vite](https://vitejs.dev/), para lo que se ejecutó `yarn create vite`, y se escogieron las opciones `React` y `JavaScript + SWC`.

### Errores

Es posible que les surgan errores dada la versión de **Node** que están utilizando actualmente, como el siguiente,

> The engine "node" is incompatible with this module. Expected version "^18.0.0 || >=20.0.0". Got "14.20.0"

Si les solicita una versión `^18.0.0`, lo deberían poder resolver ejecutando `nvm use 18.15`, ya que es la versión con la que ustedes cuentan luego de haber realizado correctamente los pasos de la [Cápsula de SetUp](https://www.youtube.com/watch?v=KtH8qZt9aUg).
