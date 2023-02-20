<a name="readme-top"></a>
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/tyesh/roberta_final_project">
    <img src="https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Analisis de Sentimientoes para tweets mediante el modelo roBERTa</h3>

  <p align="center">
    An ecommerce app made with Node.js and React.js
    <br />
    <a href="https://github.com/tyesh/roberta_final_project"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/tyesh/roberta_final_project/issues">Reportar Bug</a>
    ·
    <a href="https://github.com/tyesh/roberta_final_project/issues">Solicitar funcionalidad/a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#acerca-del-proyecto">Acerca del protecto</a>
      <ul>
        <li><a href="#creado-con">Creado con</a></li>
      </ul>
    </li>
    <li>
      <a href="#empezando">Empezando</a>
      <ul>
        <li><a href="#Prerequisitos">Prerequisitos</a></li>
        <li><a href="#instalación">Instalación</a></li>
      </ul>
    </li>
    <li><a href="#usos">Usos</a></li>
    <li><a href="#licencia">Licencia</a></li>
    <li><a href="#contacto">Contacto</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## Acerca del proyecto
Este proyecto está diseñado a implementar en python el modelo de análisis de sentimientos roBERTA. Este modelo fue desarrollado por el equpo de Meta AI y fue entreneado con una gran cantidad de tweets.

<p align="right">(<a href="#readme-top">Volver al inicio</a>)</p>

### Creado con

Esta es la lista de los lenguajes y frameworks utilizados en este proyecto

* Python
* Tensorflow
* Meta AI roBERTa

<p align="right">(<a href="#readme-top">Volver al inicio</a>)</p>

<!-- GETTING STARTED -->
## Empezando
Para poder utilizar la aplicación solo es necesario clonar en un repositorio local e installar todas las dependencias con pip.

### Prerequisitos

Para poder utilizar correctamente el modelo, es necesario contar con una targeta grafica, de ser posible ser comparible con la tecnología CUDA de nVIdia, para poder instalar tensorflow.

Contar con la instalación de tensorflow también es necesario para poder ejecutar el proyecto.

También es necesario contar con las claves de una aplicación de Twitter para poder utlizar el extractor de tweets.

<p align="right">(<a href="#readme-top">Volver al inicio</a>)</p>

### Instalación

Para poder instalar las depencias, solo es necesario ejecutar el instalar de paquetes pip
* pip
  ```sh
  pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116
   ```
   ```sh
  pip install tensorflow
   ```
   
   ```sh
  pip install tweepy
   ```
   
   ```sh
  pip install scipy
   ```
   
   ```sh
  pip install openpyxl 
   ```
   
   ```sh
  pip install matplotlib 
   ```
   
    ```sh
  pip install sklearn 
   ```   
   
   ```sh
  pip install transformers 
   ```
   
   

<p align="right">(<a href="#readme-top">Volver al inicio</a>)</p>

<!-- USAGE EXAMPLES -->
## Usos

Para poder utilzizar el estractor y predictor de tweets solo es necesario correr el archivo 

Para correr el colector de tweets
   ```sh
   python tweepy_processor.py
   ```

Para correr la predicción y la matriz de confusión
   ```sh
   python excel_processor.py
   ```
   
Ejemplo https://www.loom.com/share/b92ddd1a009f4e598fa1c324e5487257

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distribuido bajo licencia MIT. 

<p align="right">(<a href="#readme-top">Volver al inicio</a>)</p>

<!-- Contacto -->
## Contacto

Email - carlos.velazquez91@gmail.com

<p align="right">(<a href="#readme-top">Volver al inicio</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/tyesh/roberta_final_project.svg?style=for-the-badge
[contributors-url]: https://github.com/tyesh/roberta_final_project/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/tyesh/roberta_final_project.svg?style=for-the-badge
[forks-url]: https://github.com/tyesh/roberta_final_project/network/members
[stars-shield]: https://img.shields.io/github/stars/tyesh/roberta_final_project.svg?style=for-the-badge
[stars-url]: https://github.com/tyesh/roberta_final_project/stargazers
[issues-shield]: https://img.shields.io/github/issues/tyesh/roberta_final_project.svg?style=for-the-badge
[issues-url]: https://github.com/tyesh/roberta_final_project/issues
[license-shield]: https://img.shields.io/github/license/tyesh/roberta_final_project.svg?style=for-the-badge
[license-url]: https://github.com/tyesh/roberta_final_project/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/carlos-velazquez-94760694/
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[Node.js]: https://img.shields.io/badge/Node.JS-2c3e50?style=for-the-badge&logo=nodedotjs&logoColor=white+
[Node-url]: https://nodejs.org/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[MongoDB]: https://img.shields.io/badge/MongoDB-27ae60?style=for-the-badge&logo=mongodb&logoColor=white
[MongoDB-url]: https://www.mongodb.com/
